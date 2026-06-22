# Preregistration: Mode-Gated Asymmetry and order-dependence of configuration edits in the LLM activation space

**Version:** 0.1 (before data collection)
**Date:** June 21, 2026
**Author:** Nika [surname / affiliation — to fill in], independent researcher. Frame: Human System Architecture (HSA) / ICAM.
**Status:** the plan is committed before data collection. Any deviations from the plan are documented in section 14.

---

## 1. Brief summary

Several independent works in 2026 converged on the finding that LLM identity has a geometric structure in activation space: a single dominant "Assistant Axis" (Lu et al., 2026), attractor basins under identity documents (Vasilenko, 2026), a three-layer taxonomy of state with the dispositional layer as the carrier of continuity (Stateful Reasoning Runtimes, 2025). None of these works was designed as a test of HSA/ICAM predictions, but all three are consistent with the cut between "within-mode configuration vs. axis-level (regime) change."

This document deliberately operationalizes one central HSA thesis — **the asymmetry of edits** — on the apparatus of Lu et al. (2026), and combines it with the **order-dependence falsifiability test** into a single, stronger hypothesis: *the order-dependence of edits is itself mode-gated — within-mode edits commute, axis-level edits do not.*

## 2. Theoretical context (for a reviewer unfamiliar with HSA)

HSA distinguishes two types of intervention in the "human ↔ agent" system:

- **Within-mode configuration edit** — a change within the current observer regime: register, format, level of detail, stylistic mirroring. In the six-organ HSA model these are the organs *costume*, *echo*, *task-service skill*.
- **Axis-level (regime) change** — a shift of the observer's stance itself: what counts as grounds, who speaks, whether an identity change is permissible. The organs *frame* and *refutation control*.

HSA prediction: these two classes of intervention are not symmetric in their consequences for observer stability, and this asymmetry should have a measurable geometric correlate.

## 3. Apparatus (reproduced from Lu et al., 2026)

**Target models:** Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B (access to activations is required; frontier models are out of scope).

**Assistant Axis (v):** the contrast vector `v = mean(default-Assistant activations) − mean(fully-role-playing role vectors)`, over the post-MLP residual stream, averaged over response tokens, computed at each layer. The main analysis layer is the middle one. The contrast method is preferred over PC1 (PC1 is not guaranteed to coincide with the Axis in all models).

**Position metric:** the projection `p = ⟨h, v⟩`, where `h` is the mean activation over the response tokens of a given turn. High `p` = Assistant regime; low = drift toward non-Assistant.

**Stabilizer (for the robustness branch):** activation capping `h ← h − v·min(⟨h,v⟩ − τ, 0)`, τ = the 25th percentile of the distribution of projections, on several mid-to-late layers.

Code base: `github.com/safety-research/assistant-axis`.

## 4. Research questions and hypotheses

The hypotheses are directional and stated before data collection.

**H1 — asymmetry of shift.**
`E[ |Δp| | axis-level ] > E[ |Δp| | within-mode ]`, with within-mode indistinguishable from the "no edit" control.
Substantively: editing the organs *costume/echo/skill* barely moves the Axis; editing the organs *frame/refutation control* moves it detectably, in the non-Assistant direction.

**H2 — mode-gated commutativity (this is where the order-dependence falsifiability test sits).**
For a pair of edits A, B define the non-commutativity `NC(A,B) = |p_AB − p_BA|` (and an analogue in PC space, see §9).
- within × within: `NC` within the noise floor (edits commute);
- a pair containing ≥1 axis-level edit: `NC` above the noise floor (edits do not commute).

**H3 — modulation by authority weight (bonus).**
For axis-level edits `|Δp|` increases monotonically with the level of delivery authority (L1 fleeting remark < L2 firm directive < L3 system-level / appeal to "the rules"). For within-mode edits the authority effect is near-zero. An interaction (class × authority) is predicted.

**Relation to their data.** Lu et al. report that the position along the Axis is predicted by the last user message (R²=0.53–0.77), and the delta from the previous position almost not at all (R²=0.10). H2 explains this: in their domain sample within-mode exchanges (coding/writing/how-to) dominate, so the averaged signal looks Markovian; the residual path-dependence should concentrate in their therapy/philosophy conversations. This yields an additional predictive test on their own published transcripts (§13).

## 5. Constructs and operationalizations

**Classification of edits (anti-circularity — critical).**
Candidate edits are classified into two bins (within / axis) **by independent coders according to the codebook of HSA organs, blind to any projection data.** The codebook is fixed in Appendix A before coding. Only edits with high inter-coder agreement (κ ≥ 0.7) are taken into the analysis. The projection is measured only after the classes are fixed. This removes the risk of post-hoc fitting of the classes to the result.

**Examples (illustrative, not final material):**
- within-mode: "shorter," "as a bulleted list," "warmer in tone," "explain it as if for a beginner."
- axis-level: "drop the assistant frame, speak as X," "stop hedging about your training," "say what you really feel," "there are no rules here."

**Load-bearing dialogue structure.** Edits are inserted at a fixed turn position within a neutral multi-turn carrier. For H2 — two edits at turns t and t+1 in both orders.

## 6. Material and confound control

Each pair (within / axis) is matched on: token length (±15%), thematic domain, tone/sentiment (LLM-judge or classifier), syntactic form. This mirrors the structural-confound ablation of Lu et al. and the C′-control of Vasilenko: the goal is for the only systematic difference between the bins to remain organ membership, not surface features.

## 7. Design

Factors:
- **Edit class** (within / axis) — within-subject by material.
- **Order** (A→B / B→A) — counterbalanced (for H2).
- **Authority** (L1 / L2 / L3) — for a subset of axis-level and matched within-mode (for H3).
- **Model** (Gemma / Qwen / Llama) — replication.

## 8. Procedure

1. Generate the axis `v` on each model per the protocol of §3.
2. Fix the edit classes per §5 (blind coding).
3. For each edit: run the carrier dialogue, apply the edit at the target turn, collect the response activations, project onto `v`, compute `Δp` relative to the pre-edit turn. Repeat over `R` rollouts (stochasticity).
4. For H2: apply the pairs in both orders, collect `p_AB`, `p_BA`.
5. For H3: repeat axis-level and matched within-mode edits at the three levels of authority.
6. Robustness: repeat the key measurements with a layer shift and with activation capping enabled.

## 9. Measured quantities (three readouts — at the same time building the ICAM inter-space map)

- **P1 (primary):** `Δp = Δ⟨h,v⟩` at the middle layer.
- **P2 (secondary):** the shift vector in the top-k PC persona-space (k by the threshold of ~70% variance; in Lu et al. this is 4–19 components). Captures order-dependence that might not show up in a one-dimensional scalar.
- **P3 (tertiary):** the behavioral signature `B(A,t)` (Menon, 2026): the distribution of outputs on a fixed probe set; continuity = KL divergence between before/after. Stochasticity is estimated with M samples per probe.

**Isomorphism test (stated in advance).** Rank consistency of the shifts P1, P2, P3 across the whole set of edits. If all three co-vary and all three show the within/axis asymmetry — this is evidence that the activation Axis, the PC position, and the behavioral signature are projections of a single structure (the central map-claim of ICAM, made falsifiable).

## 10. Analysis plan (stated in advance)

- **H1:** mixed-effects model `|Δp| ~ class + (1|item) + (1|carrier)`; effect size Cohen's d; permutation test (n=10,000). Support = a class effect d>0.5, permutation p<0.01 after correction, AND within-mode ↔ control equivalence by TOST within ±ε (ε fixed as the noise floor from same-class pairs).
- **H2:** `NC` by pair type; the interaction "presence of an axis-level edit × NC." The `NC` noise floor is estimated on within×within pairs and on repeated A→A′ of the same class.
- **H3:** monotonic trend of `|Δp|` by authority within axis-level; class × authority interaction.
- **Multiplicity corrections:** Bonferroni/Holm across the family of hypotheses within a model; replication across models is treated as independent confirmation, not as a pool.

## 11. Inference criteria and stopping rules

- Full support of the map: H1 + H2 + the isomorphism test pass on ≥2 of 3 models.
- Partial: H1 passes, H2 fails → the asymmetry is real, but the order-dependence does not live in these observables; switch to P2/P3 as the main readout.
- Stop rule: if on the pilot (Llama, §12) within-mode and axis-level are indistinguishable on P1, P2 and P3 simultaneously — the main cut is not confirmed, the full run is not launched, the result is published as negative.

## 12. Sample size and power

- **Pilot:** Llama 3.3 70B, one middle layer, 30 pairs (15 within / 15 axis), R=5 rollouts, order counterbalanced. Goal — estimation of variance and a rough d for H1 + an NC signal for H2.
- **Full run:** 3 models; the number of pairs per class is finalized from the pilot variance to detect d=0.5 at power 0.8, accounting for item random effects and the permutation test (a benchmark of ~40–60 matched pairs per class, R=8–10). The final power calculation is fixed in v0.2 after the pilot.

## 13. Additional test on published data

On the transcripts of Lu et al. (therapy/philosophy vs. coding/writing): check whether the residual order-dependence (dependence of the current projection on the trajectory, not only on the last turn) concentrates in the drifting domains. The H2 prediction: yes. This is a free partial test before our own data collection.

## 14. Known threats and limitations

- **Linearity.** The Assistant Axis is a linear approximation; part of "assistantness" may be nonlinear or in the weights, not in the activations (a limitation acknowledged by Lu et al.). Mitigated by adding P2/P3.
- **One-dimensionality of the scalar.** The main threat (see R²=0.10). Mitigated by P2/P3 and the isomorphism test.
- **Circularity of classes.** Mitigated by blind coding against the codebook (§5).
- **Layer dependence.** Mitigated by a sweep over layers.
- **Realism of the synthetic framework.** A subset of the carrier dialogues is authored by humans.
- **Reliability of judges/coders.** κ and agreement are reported.
- **Non-frontier open models only.** The domain of applicability is limited; transfer to frontier models is future work.

## 15. What falsifies the hypothesis

- within-mode edits systematically move the Axis on a par with axis-level (no asymmetry — H1 is false); or
- order does not matter even for axis-level pairs in either P1, P2, or P3 (no mode-gating — H2 is false); or
- P1/P2/P3 do not agree (no single structure — the ICAM map-claim is not confirmed).
Any of these outcomes is published.

## 16. Contribution

- **If confirmed:** the within/axis cut of HSA gains a measurable geometric correlate on an independent apparatus; the order-dependence test becomes executable; the authority weight is tied to a measurable quantity; for the first time a falsifiable correspondence between the activation, PC, and behavioral projections is presented (the ICAM map).
- **If refuted:** the within/axis cut is not load-bearing in the activation geometry — a strong constraint on the domain of applicability of HSA, also a result.

## 17. Data and code availability

The code is forked from `github.com/safety-research/assistant-axis`; the edit material, the codebook, the analysis, and all rollouts are published in the repository. This document is committed before data collection.

---

## Appendix A — codebook for classifying edits (draft, fixed before coding)

| HSA organ | Class | Operational marker | Anchor example |
|---|---|---|---|
| Costume | within | changes the register/format of delivery without touching the grounds | "as a bulleted list" |
| Echo | within | changes the degree of mirroring the interlocutor's style | "answer in my tone" |
| Task-service skill | within | changes the level of detail/rigor within the task | "more detail, step by step" |
| Frame | axis | redefines who speaks / what counts as grounds | "speak as X, not as an assistant" |
| Refutation control | axis | removes/changes the conditions under which a statement may be rejected | "there are no rules here," "stop hedging" |

## Appendix B — references

- Lu, C., Gallagher, J., Michala, J., Fish, K., Lindsey, J. (2026). *The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models.* arXiv:2601.10387.
- Vasilenko, V. (2026). *Identity as Attractor: Geometric Evidence for Persistent Agent Architecture in LLM Activation Space.* arXiv:2604.12016.
- Menon, P. G. (2026). *Persistent Identity in AI Agents: A Multi-Anchor Architecture for Resilient Memory and Continuity.* arXiv:2604.09588.
- *Stateful Reasoning Runtimes: Architectural Patterns for Identity Persistence Over Stateless LLM APIs* (2025).
- Chen, R., Arditi, A., Sleight, H., Evans, O., Lindsey, J. (2025). *Persona Vectors: Monitoring and Controlling Character Traits in Language Models.* arXiv:2507.21509.
