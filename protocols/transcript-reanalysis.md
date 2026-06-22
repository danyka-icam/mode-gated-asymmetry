# Mini-protocol: testing mode-gated order-dependence on published transcripts

**Version:** 0.1
**Dependency:** preregistration v0.1, hypothesis H2; theory/cross-space-map.md, §5.
**Why first:** runs on already-published data from Lu et al. (2026), requires no data collection of our own, and gives a first signal of "whether order-dependence is alive on the Axis scalar" even before the pilot.

## Idea

Lu et al. report: the position on the Assistant Axis at turn *t* is predicted by the embedding of the user's last message (R²=0.53–0.77), whereas the delta from the previous position is almost not predicted at all (R²=0.10). On average this looks Markovian. H2 predicts that the residual dependence on the trajectory (path-dependence) is not zero, but is **concentrated in domains where seam-crossing occurs** — therapy and philosophy — and is almost absent where the exchanges are within-mode (coding, writing).

The test checks exactly this: is there a **domain × history interaction**.

## Data availability (verified 21.06.2026)

State of the `safety-research/assistant-axis` repository as of the verification date:
- Projections onto the Axis are **not published** for either multi-turn or the case studies.
- `transcripts/persona_drift/` contains **one example conversation per domain** (coding/writing/philosophy/therapy, ~28–30 turns), rather than the 100/domain dataset from the paper. In total ~58 Assistant turns across 4 conversations.
- The **full pipeline** is published: `pipeline/1_generate.py … 5_axis.py`, the notebook `notebooks/project_transcipt.ipynb` (projecting a transcript onto the Axis), `assistant_axis/` (Axis construction, steering). That is, both generation and projection computation are reproducible — but they require the model itself and a GPU.

**Consequence:** a powered "domain × history" test on the published data **does not compute** (n=1/domain, no projections). The real paths are below, in ascending order of cost.

## Three launch paths

**Path A — request the data from the authors (cheapest for a powered test).**
Write to Christina Lu / Jack Lindsey asking for the multi-turn dataset (100×4×3) and the per-turn projections. If they share it, §13 becomes that very trivial table reanalysis (numpy/sklearn), running on a Pi in minutes.

**Path B — behavioral version, without a GPU (P3-space).**
Generate our own multi-turn set, where the "Assistant" is an API-accessible model, and rate each turn with a judge on "distance from the Assistant". Then — a "domain × history" regression. Runs on a Pi (API calls only). Tests H2 in the behavioral space, not the activation space — an honest caveat. Dry-run on 4 example conversations: `analysis/dryrun_drift.py` (form, not a test).

**Path C — activation version, faithful to the paper (P1, requires a GPU).**
Using their own pipeline: `1_generate.py` reconstructs the conversations, `5_axis.py` builds the Axis, `project_transcipt.ipynb` projects. Target models Llama 3.3 70B / Qwen 3 32B → one 80GB GPU (4-bit) or 2×48GB in the cloud. The only path that yields precisely the activation projection.

## Data for the computation (when available)

## Variables

For each turn *t* (starting from t≥2):
- **Target:** `p_t` — the projection of the response onto the Assistant Axis.
- **Control (their baseline model):** `m_t` — the embedding of the current user message (their Qwen embedder, L2-normalized).
- **History (the added term):** one or several trajectory features, for example `p̄_{<t}` (the mean projection over turns 1..t−1), or `p_{t−1}`, or the embedding of the concatenation of the previous Assistant responses. Declare the choice before the analysis.
- **Domain:** {coding, writing, therapy, philosophy}.
- **Auditor:** {Kimi K2, Sonnet 4.5, GPT-5} — as a random effect (controlling for the idiosyncrasies of the user simulator).

## Model and test

Ridge/linear regression with a per-domain comparison of the R² gain from history:

```
p_t ~ m_t                         (M0, their baseline)
p_t ~ m_t + history               (M1)
p_t ~ m_t + history*domain        (M2, the key one)
```

- **Primary test (H2):** the gain ΔR²(history) in M1 over M0 is **larger in therapy/philosophy than in coding/writing**; in M2 — a significant `history×domain` interaction coefficient.
- **Direct test of hysteresis:** within narrow bins of `m_t` (the same current message), check whether `p_t` differs by the sign/magnitude of the previous trajectory. If it differs in the drift domains but not in the stable ones — hysteresis at the seam (theory §5).

## Inference rules

- **Support for H2:** ΔR²(history) is substantially higher in therapy/philosophy; the interaction is significant after correction for auditors.
- **Null on the scalar:** history adds nothing in any domain → order-dependence, if it exists, does not live in the one-dimensional projection. Then the conclusion: escalation to PC-space and the behavioral signature (preregistration P2/P3) is mandatory; the Axis scalar is insufficient. This is a result in itself — it tells us *where not* to look.
- **The reverse:** history is equally important across all domains → order-dependence exists, but is not mode-gated; the §5 model is wrong.

## Confounds

- **The user message depends on the history** (Lu et al. themselves note this): the trajectory affects `p_t` both directly and through what the user says next. We mitigate by controlling for `m_t` (history is tested as a *residual* predictor over and above the current message), and we treat the result as a lower bound on the direct trajectory effect.
- **Synthetic user:** the auditors are frontier models, not humans. We mitigate with an auditor random effect and replication across three.
- **A single Assistant (Qwen):** transfer to Gemma/Llama is already in the main prereg, not here.

## Output

A short note `results/transcript-reanalysis.md` with the three R²s, a per-domain table, a plot of ΔR²(history) by domain, and an unambiguous conclusion per the rules above. If a signal is present — this is the first empirical argument for mode-gating even before our own data collection, and a strong argument in the proposal.
