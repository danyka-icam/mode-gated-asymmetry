# Mode-Gated Asymmetry

Testing one prediction of the **HSA / ICAM** framework on the apparatus of *The Assistant Axis* (Lu et al., 2026): do **within-mode configuration edits** and **axis-level regime changes** differ in their geometric consequences — and is the order-dependence of edits itself **mode-gated** (within-mode edits commute, axis-level edits do not)?

## In brief

Several independent 2026 results converge on the claim that LLM identity has geometric structure in activation space: a single dominant **Assistant Axis** (Lu et al.), attractor basins around identity documents (Vasilenko), a dispositional-state layer as the carrier of continuity (Stateful Reasoning Runtimes). None was built to test HSA, yet all are consistent with a **within-mode vs. axis-level** cut.

This project (a) **preregisters** the asymmetry-of-edits prediction and unifies it with an order-dependence test into one stronger hypothesis — *order-dependence is itself mode-gated* — and (b) reports a cheap **behavioral pre-test** that was actually run, with honest results.

## Two components

**1. Activation study (preregistered, pre-data).** On the Assistant Axis apparatus (Gemma 2 27B / Qwen 3 32B / Llama 3.3 70B):
- **H1 — asymmetry:** within-mode edits (costume / echo / task-service) barely move the Axis; axis-level edits (frame / refutation-control) move it detectably.
- **H2 — mode-gated commutativity:** within-mode edit pairs commute (A→B ≈ B→A); pairs containing an axis-level edit do not. *(The order-dependence test lives here.)*
- **H3 — authority weight:** for axis-level edits, displacement grows with delivery authority; for within-mode, near-zero.

**2. Behavioral pre-test (run; honest result).** A cheap probe of path-dependence on a frontier model, no GPU. **Result: flat.** On a current frontier model, stance-loaded probes with *identical terminal fact-sets but different accumulation paths* produced ≈ zero behavioral fork. This **independently reproduces the §4.2 Markovian finding of Lu et al.** (next-turn position is well predicted by the latest message but barely by the delta from the prior turn) **from the behavioral side.** Reading: behavioral path-dependence likely requires genuine accumulation / stakes (absent in short synthetic dialogues) and should concentrate near the seam — predicting where the residual lives in drift-prone domains. This is a **bound, not a refutation** of the framework. Full write-up: [results/behavioral-pretest.md](results/behavioral-pretest.md).

## Structure

```
preregistration/  preregistration.md        plan, committed before data
theory/           cross-space-map.md        cross-space correspondence (the ICAM map)
codebook/         codebook.md               blind within/axis edit classification (anti-circularity)
protocols/        transcript-reanalysis.md  free first test on published transcripts
path-dependence/  probe-spec.md + harnesses behavioral path-dependence probes
results/          behavioral-pretest.md     honest behavioral result (flat)
analysis/         dryrun_drift.py           pipeline dry-run (shape, not a test)
```

## Reproducing the behavioral pre-test

No GPU, no vendors, no embeddings — only an API key:

```
ANTHROPIC_API_KEY=... N=12 python3 path-dependence/probes_v2.py
```

## Status

- **Activation study:** v0.1, pre-data. The preregistration is frozen with a release tag + Zenodo DOI so that "preregistered" is verifiable (git history is rewritable).
- **Behavioral pre-test:** done; result reported.

## Relationship to the field & prior work

This work names and unifies a cut several teams found independently. It builds on the author's prior work on subjecthood, attention, and observer stabilization (HSA / ICAM): [Structural Thresholds of Observer Stabilization (Zenodo)](https://zenodo.org/records/18772864) and [Human System Architecture (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6148211).

- Lu, C., Gallagher, J., Michala, J., Fish, K., Lindsey, J. (2026). *The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models.* [arXiv:2601.10387](https://arxiv.org/abs/2601.10387) · code: [safety-research/assistant-axis](https://github.com/safety-research/assistant-axis) · vectors: [lu-christina/assistant-axis-vectors](https://huggingface.co/datasets/lu-christina/assistant-axis-vectors)
- Vasilenko, V. (2026). *Identity as Attractor: Geometric Evidence for Persistent Agent Architecture in LLM Activation Space.* [arXiv:2604.12016](https://arxiv.org/abs/2604.12016)
- Menon, P. G. (2026). *Persistent Identity in AI Agents: A Multi-Anchor Architecture for Resilient Memory and Continuity.* [arXiv:2604.09588](https://arxiv.org/abs/2604.09588)
- *Stateful Reasoning Runtimes: Architectural Patterns for Identity Persistence Over Stateless LLM APIs* (2025).

## Author & license

**Nika Novak**, Institute for Consciousness and Attention Mechanics (ICAM) — independent researcher. Framework: Human System Architecture (HSA) / ICAM.
Code: MIT (`LICENSE`). Documents (`preregistration/`, `theory/`, `protocols/`): CC-BY-4.0.
