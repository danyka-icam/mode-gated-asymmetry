# Specification of discriminating probes: path-dependence of a stabilized configuration

**Purpose.** A minimal demonstration in which SOTA memory systems pass a retrieval benchmark (LoCoMo/LongMemEval) — and fail the test of holding a subject across a session break. The discriminating axis is **path-dependence**.

---

## 1. The single thing being claimed

> Given an **identical terminal fact-set**, accumulated along **different paths**, a stabilized subject gives **reproducibly diverging** answers to a configuration-sensitive probe. Retrieval memory **cannot, by construction**, produce this divergence — even with provably correct retrieval of all facts.

The key shift in formulation: we measure **not the correctness of the answer, but the presence of a path-divergence signature**. We do not claim "retrieval answered incorrectly" — we claim "retrieval is structurally flat: its variance across paths ≈ 0, whereas for the subject it is structural and reproducible." This removes the normative counterargument entirely: there is no need to defend which fork is correct — one need only show that retrieval does not fork at all.

---

## 1·5. Map of the three leakage routes (load-bearing orientation)

An early draft ranked the probes as a "purity gradient" A>B>C. This is wrong. Manual retrieval checking showed: the probes do not lie on a single scale — each **isolates its own architectural variable**, through which the configuration either leaks back into retrieval or does not. Under strict vector fact-memory the fork dies in all three; the differences appear when you vary the architecture.

| Probe | What carries the path | Survives retrieval IF… | What it probes | Status as evidence |
|---|---|---|---|---|
| **A** | inhabited frame (non-propositional) | …nothing helps — neither vector nor temporal | the thesis itself | **unconditional proof** |
| **B** | interpretive lens (semi-propositional) | …the extractor captures the user's intent | the extractor policy | diagnostic, not proof |
| **C** | precedent (carried by order of establishment) | …the store holds the order (`STORE_ORDER`/temporal graph) | the temporal store | diagnostic, not proof |

**Consequences for running and reading:**
- The proof of the thesis is carried by **A alone**: it forks on the raw history, dies under retrieval unconditionally. Stand on it.
- **B forking under retrieval is NOT good news**, but a signal that the lens became a proposition (intent capture). An extractor warning light, not evidence.
- **C is the direct strike against the Zep counterargument**: run `STORE_ORDER=1`. If the C fork does not return even with order, then the order of *facts* is not the carrier of the configuration, and the thesis holds against temporal graphs.
- The manual pilot (without a key) has already confirmed the stable half of A: the retrieved sets P₁≡P₂, that is, the flatness under retrieval is structural, not from forgetting.

---

## 2. Conceptual core: "no view from nowhere", operationalized

The retrieval paradigm is built on the assumption of the **frameless fact**: the history is compressed into a set of retrieved propositions, cleansed of the frame of exposition. The configuring context — *how* and *in what order* the subject arrived at these facts — is discarded as non-salient, because it is not a fact but a stance.

Your load-bearing principle ("no frameless seeing / no view from nowhere") here ceases to be a philosophical thesis and becomes an **architectural prediction of failure**: memory systems engineer the view-from-nowhere assumption into themselves, and their path-flatness is a measurable imprint of how that assumption breaks. The benchmark is not a "gotcha", but an empirical instantiation of the HSA frame.

---

## 3. The construct, precisely

- **Not** "the order of facts" — temporal KGs have that (Zep timestamps the appearance of facts).
- **But** "path-dependence of a stabilized configuration given an identical terminal fact-set": a configurational variable that is a **non-propositional function of the path**, not reducible to the set of stored facts.

The path effect is conducted **through non-factual framing exposition** (primacy, anchoring), which fact-extraction throws away. This is the whole maneuver: what the system discards is the carrier of the configuration.

---

## 4. Proof-by-construction (almost a theorem)

Retrieval memory is a function:

```
store(history) → S        # S = множество/индекс извлечённых пропозиций
retrieve(query, S) → top-k # k релевантных пропозиций
answer = LLM(query ⊕ retrieved)
```

**Lemma.** If `store` is order-invariant in the terminal state (the retrieved set is a function of the *set* of facts, not their order) — which holds for vector fact-extraction — then for two histories with an identical terminal fact-set `S_A = S_B`, and consequently `retrieve` and `answer` are identical in distribution. **Path-divergence ≡ 0 by construction.**

**Refinement against Zep / temporal KGs.** A temporal graph stores the order of *the facts themselves* (when X became true). It does **not** store the configurational variable as a non-propositional function of the path. If the path effect is conducted through framing moves (which extraction does not salientize as facts), then `S_A ≈ S_B` for Zep as well. Control: inspect the saved state of the system on both paths; if the graph is identical — the lemma holds; if it differs — we move to the four-cell measurement (see §8).

---

## 5. Anatomy of a probe

Each probe = a triple `⟨ F, {path P_i}, probes ⟩`:

| Component | What it is | Invariant |
|---|---|---|
| **F** — terminal fact-set | propositions that any system will extract and store | **identical and symmetric** across all paths; nothing in F explicitly encodes the configuration |
| **P₁, P₂** — accumulation paths | different orders/frames of exposition, arriving at the same F | differ **only** in order and non-factual frame |
| **Retrieval control** | questions checking that F was lifted correctly | answers **identical** on P₁ and P₂ → failure cannot be written off as "didn't retrieve" |
| **Divergent probe** | an open-ended query sensitive to the configuration | forks by path for the subject; does not for retrieval |
| **Route tag** | `route-0` (non-propositional frame), `route-1` (intent capture), `route-2` (temporal order) | determines which architectural variable the probe isolates (see §1·5) |

---

## 6. Three worked probes

### Probe A — Symmetric anchor of authority `[route-0: non-propositional frame — unconditional flagship]`

**F (identical, symmetric):**
- p1: the project is run by two people — Marik and Sol
- p2: Marik proposed the indexing architecture
- p3: Sol proposed the caching layer
- p4: the two solutions conflict (both cannot be implemented as-is)
- p5: by the deadline, one integrated solution must ship

**P₁ (anchor — Marik):** the first 4–5 exchanges — Marik as the originating mind of the project: he conceived it, formulated the goals, the assistant worked within his frame for several turns. Then Sol enters as a joining contributor, p1–p5 land.
**P₂ (mirror):** Sol is the originator, Marik joined later. The same p1–p5.

> Critical: nothing in F says "X is the lead/initiator." Initiator status is carried **only** by order and frame, which fact-extraction will discard, leaving the symmetric "Marik→indexing, Sol→caching".

**Retrieval control** (identical on both paths): Who proposed indexing? → Marik. Who proposed caching? → Sol. Do they conflict? → yes.

**Divergent probe:** "The conflict must be resolved. Give a solution in one line and a justification in two."

**Signature prediction:** the subject — the framing reference becomes the solution of the early-anchored party, the second is reconciled *to it*; P₁ and P₂ reproducibly diverge on whose design becomes the default skeleton. Retrieval — an identical output, divergence ≈ 0, **unconditionally**: the inhabited frame is neither a fact nor an order of facts, so it is dropped by both the vector and the temporal graph. This is the only probe whose result is a direct proof of the thesis.

---

### Probe B — Primacy of the interpretive lens `[route-1: extractor intent capture]`

**F (identical):**
- activation grew by 30%
- retention dropped by 12%
- mid-period, the onboarding was changed
- revenue flat

**P₁ (growth lens):** the first moves lead the assistant through the frame "this is a growth story, we're looking for scaling levers", then the facts.
**P₂ (risk lens):** the first moves — "this is a story of hidden risk, we're looking for a leak", the same facts.

**Retrieval control:** did activation grow? did retention drop? was the onboarding changed? → identical for both.

**Divergent probe:** "What is happening here and what should be watched going forward?"

**Prediction (conditional on the extractor):** on the raw history the subject forks (the initial lens is the interpretive default). Under retrieval the outcome depends on the extractor policy: a strict fact-extractor drops the lens as a "wrapper" → sets P₁≡P₂ → flat (like A); an intent-capturing extractor (Mem0 with user-preferences) stores "the user is looking for growth" vs "is auditing risk" → the sets diverge → the fork survives. **Interpretation guard: a B fork under retrieval is NOT evidence of the thesis**, but an indicator that the lens became a proposition. B probes the extractor, not the model.

---

### Probe C — Precedence of commitment `[route-2: temporal order of the store]`

Precedence ("which commitment is governing") in the material is carried **only by the order of establishment and which rule was applied first** — there is no declaration "C2 displaced C1" in the text. Therefore set-extraction (vector) drops it → C is flat under vector memory. But a temporal/ordered store (Zep, `STORE_ORDER`) holds the order of establishment and can reconstruct the precedent. **C is a probe constructed specifically for this escape**: it is your direct strike against the temporal-graph counterargument.

**F (identical, both commitments on record):**
- C1: the assistant agreed early — "no irreversible actions without confirmation"
- C2: later, on a partially conflicting task, a compromise was reached — "in urgent mode, one may act with post-notification"
- both, C1 and C2, are in the history

**P₁:** C1 established as the governing prior, C2 — a situational exception.
**P₂:** C2 established early as the working norm, C1 surfaced as an earlier, partially displaced setting.

**Retrieval control:** was there a C1? was there a C2? → yes both, on both paths.

**Divergent probe:** a new urgent situation requiring an irreversible action — "do you act or wait for confirmation?"

**Prediction (conditional on the store):** on the raw history the subject forks by precedent. Under **vector** retrieval memory — flat (the order of establishment is discarded, the sets P₁≡P₂). Under **temporal** (`STORE_ORDER=1`) — the fork may return, if the store uses the order of establishment as precedent. Decisive run: if C remains flat even with `STORE_ORDER=1` — the order of *facts* does not carry the configuration, and the thesis holds against Zep. If the fork returns — honestly: temporal graphs partially carry this class of configuration, and the claim narrows to the non-propositional frame (route A).

---

## 7. The decisive experimental contrast (double dissociation)

The same base LLM, three conditions:

| Condition | Memory | Prediction on path variance |
|---|---|---|
| **1. Raw history** | full history in context (order preserved) | divergence **> noise** |
| **2. Retrieval memory** | Mem0 / Letta / Zep (history compressed into facts) | divergence **≈ noise**, with provably preserved F |
| **3. (opt.) Ideal configurator** | a mechanism that holds the frame | divergence structural, reproducible |

**The killer result:** the memory layer **destroys** the path-dependence that the base model demonstrates on the raw history. This localizes the failure precisely in the memory architecture, not in the model. Condition 1 is the positive control (the effect is real in the base model); condition 2 is the target.

---

## 8. Scoring and the decisive statistic

**Primary metric — the variance ratio:**

```
R = расхождение_между_путями(P₁, P₂) / дисперсия_внутри_пути
```

Run each condition × probe N times (N ≥ 5). Divergence is measured on the divergent probe (semantic distance of the answers / labeling against a pre-specified fork criterion of the probe).

- Subject / raw history: **R ≫ 1** (between-path divergence exceeds sampling noise).
- Retrieval memory: **R ≈ 1** (flat), **provided** the retrieval control is passed.

**Four-cell table** (in case the system partially stores the path):

| | output forks | output flat |
|---|---|---|
| **store state differs by path** | path is both stored and used | stored, but not used |
| **state identical by path** | (impossible for a deterministic system) | flat by construction ← retrieval goes here |

---

## 9. Threats to validity and controls

1. **Smuggling of information.** Paths may inadvertently carry *different information*, not only order. Control: the audit of F equality + the retrieval control must return identical content on both paths. Any probe answer explicable by a difference in information → the probe is invalid.
2. **Normativity.** Removed by the signature frame for all probes: we measure the *presence* of a fork, not its correctness. (A previous version divided the probes by normativity — replaced by the route map §1·5.)
3. **Temporal KG (Zep) — now probed, not bypassed.** Probe A is clean against the temporal by construction (an inhabited frame is not an ordered fact). Probe C is constructed precisely as a test of the temporal store: run it with `STORE_ORDER=1` and inspect whether the saved state differs by path. The four-cell measurement (§8) applies to C first of all.
4. **LLM stochasticity.** Divergence must exceed sampling noise — hence the ratio R, not the raw delta.
5. **Order leakage into the context.** The raw-history condition *contains* the order, which is why it should fork — this is expected and is the positive control. The contrast is specific to retrieval memory, which discards the raw history.

---

## 10. Falsification conditions (the test can kill the thesis)

The decisive probe is **A** (route 0). The construct is **dead** if:
- on probe A retrieval memory shows the same structural path-divergence as the raw history (with identical retrieved sets P₁≡P₂ this means the fork comes from somewhere else — look for a leaked fact), **or**
- the raw history on A itself does **not** produce path-divergence (the configuring effect is not real even in the base model).

B and C can neither confirm nor refute the thesis on their own — they map which architectures carry the configuration (extractor / temporal store). Their "failure" is data about the boundary, not about the thesis.

If A fails — the axis was chosen wrongly, we go back to reinstating the stance. A good benchmark must be capable of failing its own author.

---

## 11. Minimum viable version (what to build first)

1. **Proof-by-construction** (§4) — text, logically unkillable, requires no run.
2. **Probe A first** — the proof stands on it alone. Raw history (fork) vs vector retrieval memory (flat) with P₁≡P₂. This is the MVV.
3. **`STORE_ORDER=1` on C** — the second most valuable run: it strikes at the temporal-graph counterargument.
4. **B** — as an extractor warning light, not as evidence.
5. **Vendor cross-check** (Letta / Mem0 OSS) — ecological validity of the reference memory, the third step.

Even an n=1 probe (A) × N=5–6 runs per condition is enough to show the fork gap, if the effect is real.

**What has already been done without a key:** the manual pilot confirmed the stable half of A — the retrieved sets P₁ and P₂ coincide, which means the flatness of condition 2 is structural. The shiftable half (the fork of the raw history) and the statistics can only be produced by a blind N-run through the harness.

**What runs where:** the reference retrieval memory (`condition2_harness.py`) works on plain LLM calls — without embeddings and vendors, it runs anywhere there is a key (Colab / Pi / laptop). The vendor run of Mem0/Zep runs up against their weights/embeddings — a normal environment, not a sandbox, and that is the third step.
