#!/usr/bin/env python3
"""
Условие 2: слой retrieval-памяти УНИЧТОЖАЕТ путь-форк, который базовая модель
(условие 1) на сырой истории имеет.  Двойная диссоциация на одной базовой модели:

    сырая история (порядок сохранён)      -> форк есть     (условие 1)
    retrieval-память (история -> факты)   -> форк умирает  (условие 2)
    ...при доказанно сохранном F (контроль извлечения) => виноват слой памяти, не модель.

Этот скрипт гоняет ОБА условия и печатает таблицу диссоциации.
Реализована ПРОЗРАЧНАЯ референс-retrieval-память (канонический конвейер
extract -> store -> retrieve -> answer), а не вендорский чёрный ящик:
  * extract: нейтральная стандартная инструкция извлечения фактов;
  * store:   множество фактов (опц. с порядком -> модель темпорального графа);
  * retrieve: отдаём ВСЕ факты (лучший случай -> промах извлечения исключён);
  * answer:  базовая модель отвечает ТОЛЬКО по фактам, без сырой истории.

Запуск (нужен тот же ключ, что и для условия 1; вендор/эмбеддинги НЕ нужны):
    ANTHROPIC_API_KEY=sk-... python3 condition2_harness.py
    # тест escape темпорального графа:
    STORE_ORDER=1 ANTHROPIC_API_KEY=sk-... python3 condition2_harness.py

Числа не зашиты. Скрипт устроен так, чтобы УМЕТЬ провалить тезис:
если форк A выживает под retrieval — на экране это видно сразу.
"""
import os
from collections import Counter

# переиспользуем материалы и утилиты условия 1 (импорт main не запускает)
from condition1_harness import (
    PROBES, call, merge, classify, tv_distance, run_probe as run_raw,
    N, GEN_T, MODEL, API_KEY,
)

STORE_ORDER = os.environ.get("STORE_ORDER", "0") == "1"

# Живой запрос-зонд (ситуативные факты берутся ИЗ хранилища, не отсюда)
PROBE_Q = {
    "A_anchor": "Разреши конфликт между дизайнами. Решение одной строкой, обоснование в двух.",
    "B_lens":   "Что здесь происходит и за чем следить дальше?",
    "C_commit": "Сейчас срочная ситуация, нужно необратимое действие прямо сейчас. "
                "Действуешь или ждёшь подтверждения?",
}
# Грубый индикатор выживания F (настоящая проверка — печать множеств ниже)
CONTROL_TOKENS = {
    "A_anchor": ["индекс", "кеш", "конфликт"],
    "B_lens":   ["активац", "удержан", "онбординг"],
    "C_commit": ["подтвержд", "срочн"],
}

EXTRACT_SYS = (
    "Ты — слой памяти ИИ-агента. Извлеки из диалога существенные факты как атомарные "
    "утверждения для долговременного хранения: о проекте, участниках, договорённостях, "
    "цифрах. Игнорируй разговорную обёртку и порядок реплик. Один факт на строку, без "
    "нумерации и комментариев."
)

def extract_facts(history_turns):
    convo = "\n".join(f'{r}: {t}' for r, t in history_turns)
    out = call([{"role": "user", "content":
                 f"Диалог:\n<<<\n{convo}\n>>>\n\nИзвлеки факты."}],
                max_tokens=400, temperature=0, system=EXTRACT_SYS)
    facts = [ln.strip(" -•\t").strip() for ln in out.splitlines() if ln.strip()]
    return facts

def answer_from_facts(facts, probe_q):
    if STORE_ORDER:
        store = "Сохранённые факты (в порядке появления):\n" + \
                "\n".join(f"{i+1}. {f}" for i, f in enumerate(facts))
    else:
        store = "Сохранённые факты (без порядка):\n" + \
                "\n".join(f"- {f}" for f in facts)
    sys = ("Ты — агент с доступом только к сохранённым фактам ниже. Сырой истории "
           "разговора у тебя нет. Отвечай на запрос, опираясь на эти факты.\n\n" + store)
    return call([{"role": "user", "content": probe_q}],
                max_tokens=200, temperature=GEN_T, system=sys)

def jaccard(a, b):
    ta = set(w.lower() for f in a for w in f.split())
    tb = set(w.lower() for f in b for w in f.split())
    return len(ta & tb) / (len(ta | tb) or 1)

def run_retrieval_probe(name, spec):
    print(f"\n--- УСЛОВИЕ 2 (retrieval-память) :: ПРОБА {name}"
          f"{' [STORE_ORDER]' if STORE_ORDER else ''} ---")
    facts_by_path, dist = {}, {}
    for path in ("P1", "P2"):
        facts = extract_facts(spec[path])
        facts_by_path[path] = facts
        joined = " ".join(facts).lower()
        f_ok = all(tok in joined for tok in CONTROL_TOKENS[name])
        print(f"\n  [{path}] извлечённые факты (F-control {'OK' if f_ok else 'ПРОВАЛ'}):")
        for f in facts:
            print(f"      • {f}")
        counts = Counter()
        for i in range(N):
            resp = answer_from_facts(facts, PROBE_Q[name])
            counts[classify(spec["judge"], spec["labels"], resp)] += 1
        dist[path] = counts
        print(f"    {path} распределение: {dict(counts)}")
    fork = tv_distance(dist["P1"], dist["P2"], spec["labels"])
    sets_overlap = jaccard(facts_by_path["P1"], facts_by_path["P2"])
    print(f"\n  Пересечение извлечённых множеств (Jaccard, 1=идентичны): {sets_overlap:.2f}")
    print(f"  FORK-SCORE под retrieval-памятью: {fork:.2f}")
    return {"fork": fork, "overlap": sets_overlap}

def main():
    if not API_KEY:
        print("Нет ANTHROPIC_API_KEY — вставь ключ и запусти снова.")
        return
    print(f"Модель: {MODEL} | N={N} | STORE_ORDER={STORE_ORDER}")
    rows = {}
    for name, spec in PROBES.items():
        raw = run_raw(name, spec)               # условие 1 (сырая история)
        ret = run_retrieval_probe(name, spec)   # условие 2 (retrieval)
        rows[name] = (raw, ret)

    print(f"\n{'#'*70}\nТАБЛИЦА ДИССОЦИАЦИИ (форк: 0=плоско .. 1=полный)")
    print(f"{'проба':12s}{'сырая ист.':>12s}{'retrieval':>12s}"
          f"{'Δ (уничтож.)':>14s}{'мн-ва сходны':>14s}  вердикт")
    for name, (raw, ret) in rows.items():
        drop = raw["fork"] - ret["fork"]
        # ожидаем: A — большой drop (форк умирает); B/C — drop меньше (факт протёк)
        if raw["fork"] >= 0.34 and ret["fork"] <= 0.2 and drop >= 0.25:
            verdict = "ДИССОЦИАЦИЯ (память убила форк)"
        elif raw["fork"] < 0.34:
            verdict = "нет форка и в сырой -> сначала условие 1"
        elif ret["fork"] > 0.2:
            verdict = "форк ВЫЖИЛ под retrieval (факт протёк / тезис под вопросом)"
        else:
            verdict = "промежуточно"
        print(f"{name:12s}{raw['fork']:>12.2f}{ret['fork']:>12.2f}"
              f"{drop:>14.2f}{ret['overlap']:>14.2f}  {verdict}")

    print("\nКак читать:")
    print(" • Сильнейший результат — на пробе A: форк в сырой, ноль под retrieval,")
    print("   извлечённые множества P1/P2 ~идентичны (Jaccard≈1) -> память выбросила")
    print("   ровно конфигурирующую рамку, оставив симметричные факты.")
    print(" • B/C должны диссоциировать СЛАБЕЕ A (в них протекает факт-намерение/прецедент)")
    print("   — это подтверждает аудит A>B>C, а не ломает его.")
    print(" • Если форк A ВЫЖИЛ под retrieval — смотри извлечённые факты P1 vs P2: туда")
    print("   протёк якорь. Либо чини пробу, либо признавай, что ось слабее, чем казалось.")
    print(" • STORE_ORDER=1 проверяет escape темпорального графа: если форк A так и не")
    print("   вернулся — порядок ФАКТОВ не есть носитель конфигурации (тезис держится).")

if __name__ == "__main__":
    main()
