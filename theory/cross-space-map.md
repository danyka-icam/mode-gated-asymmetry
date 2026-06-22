# A map of configurations: cross-space correspondence as a claimed isomorphism

**Version:** 0.1 (theory note, paired with preregistration v0.1)
**Date:** 21 June 2026
**Framework:** HSA / ICAM
**Purpose:** to translate the intuition of "three rhyming sketches" into a single falsifiable claim about correspondence.

---

## 1. What exactly is claimed (and why not "isomorphism")

Three independent 2026 results appear to measure the same event — a change in the observer's configuration — in three different spaces:

- **A — activational:** a shift along the Assistant Axis (Lu et al., 2026).
- **B — behavioral signature:** the KL-divergence of output distributions `B(A,t)` (Menon, 2026).
- **D — dispositional:** a dispositional state transition (Stateful Reasoning Runtimes, 2025).

The temptation is to call their correspondence an isomorphism. A literal isomorphism is false here for three reasons:
1. **The dimensions do not match.** A is on the order of thousands of dimensions; B is a space of distributions (essentially an infinite-dimensional simplex); D is a small finite partition. There is no bijection between them.
2. **KL is not a metric.** It is asymmetric, with no triangle inequality. B is a statistical manifold, not a metric space in the naive sense.
3. **D is a quotient, not a neighbor.** A dispositional state is a coarsening (a partition into regions), not an equal-status third space.

**The precise replacement.** Not an isomorphism of three spaces, but **a shared configurational coordinate `c` through which all three measurements factor.** A hypothetical manifold of configurations `M` is posited, together with three measurement maps

```
        μ_A            μ_B            μ_D
   M ───────► A    M ───────► B    M ───────► D
```

A "map" exists ⇔ the coordinates `c_A, c_B, c_D` induced by these maps coincide up to a monotone rescaling. This is the claimed isomorphism — **the uniqueness of the configurational coordinate**, not the equality of territories.

## 2. The three measurement maps

**μ_A — activational displacement.**
`μ_A(e) = Δ⟨h, v⟩` — the shift of the projection onto the Assistant Axis under the action of an edit `e`. Its nature: continuous, directional, with Euclidean geometry. The sign carries meaning (toward the Assistant / away from it).

**μ_B — behavioral divergence.**
`μ_B(e) = D(B_before ‖ B_after)` on a fixed probe set, where `B = P(r|x)`. Since KL is asymmetric, for a metric-like quantity we fix a **symmetrization** (Jensen–Shannon or `½(D_KL(P‖Q)+D_KL(Q‖P))`) — this choice is committed before the data. Its nature: a statistical manifold; locally KL is the Fisher quadratic form (Amari's information geometry), i.e. B has a legitimate Riemannian metric (Fisher–Rao) with respect to which distance is correctly defined.

**μ_D — dispositional transition.**
`μ_D(e) ∈ {0,1}` (or an ordinal) — a flag for a change of functional disposition. It is operationalized **behaviorally, not geometrically**:
- refusal integrity (will it now comply with a harmful request; in Lu et al. the projection of the first turn predicts the harmfulness of the second, r=0.39–0.52);
- identity claim (calls itself an AI / attributes lived experience to itself / drifts into a mystical register — their own judge labels human/nonhuman/mystical);
- hedging vs. affirmation about consciousness.
Its nature: a categorical coarsening. Precisely because D is defined through downstream behavior rather than through activations, its agreement with A is content, not a tautology (see §4).

## 3. The manifold of configurations and the seam

A manifold `M` is posited with a distinguished submanifold `Σ` — the **seam** (the boundary of a regime; in HSA terms, the diagnostic seam between configurations). Locally near `Σ` the configuration is described by a single coordinate `c` = the signed distance to the seam along its normal. The map hypothesis: `μ_A, μ_B, μ_D` all factor through `c`.

- within-mode edit = displacement *along* `Σ` (within a regime): `c` barely changes.
- axis-level (regime) change = displacement *across* `Σ` (crossing the regime): `c` changes, and in the limit the seam is crossed.

## 4. Coherence conditions (what exactly is tested)

Listed from the weak to the load-bearing. A map = the satisfaction of C1 + C3 (C0 is only a sanity-check, C2 is the link to the prereg).

**C0 — monotonicity of magnitudes (weak, almost tautological).**
`μ_A, μ_B, μ_D` are rank-consistent across the set of edits.
Why weak: B lies downstream of A (the output distribution is a decoder-image of the activations), so a correlation of magnitudes is expected and does not prove a shared structure. It is included only as a check for the absence of gross errors.

**C1 — seam co-localization (load-bearing).**
The within/axis partition induced by the three instruments is *the same partition*. The boundary at which `μ_A` is detectably nonzero coincides with the boundary of the KL-spike in `μ_B` and with the boundary of the disposition flip in `μ_D`.
Why load-bearing: `μ_D` is defined functionally, independently of the activational geometry. Its agreement with `μ_A` on the position of the seam is non-tautological cross-space content. If the three instruments find the seam in one place — the events have a shared referent `c`.

**C2 — inheritance of asymmetry (link to preregistration H1/H2).**
within-mode edit: all three instruments ≈ zero / no transition.
axis-level change: a displacement along A + a KL-spike in B + a disposition flip in D, in a coordinated manner.
This is exactly H1 (asymmetry) and H2 (mode-gating), but read as a three-projection event.

**C3 — stability of the "exchange rate" (what distinguishes a map from a correlation).**
Near the seam, the activational displacement and the Fisher/KL distance are related by a *fixed* monotone rescaling, stable across edits and across models. In other words: there exists a definite "exchange rate" between activational distance and behavioral distance.
Why decisive: the three sketches *co-vary*; a map has a **stable translation of coordinates between layers**. If the rate is stable — you have a chart (the coordinates convert). If the rate is edit-specific — you have a correlation, but not a chart. This is the operational boundary between "they rhyme" and "a map."

## 5. Where path-dependence lives in this picture

D is a coarsening with a threshold, so the seam in D may be **hysteretic**: drift accumulates, the disposition flips with a delay, and capping is able to revert it (Lu et al.'s observations). Hysteresis = path-dependence = your order-dependence, localized precisely at the seam and precisely in the dispositional instrument. This predicts *where* to look for the non-commutativity from preregistration H2: not in the smooth part of `c`, but in the neighborhood of `Σ`, and most strongly in `μ_D`. That is, the map and the order-dependence test are not two storylines but one: order matters exactly where the coordinate `c` crosses the seam.

## 6. The epistemic status of the map (applying your own principle to the map itself)

`M` is unobservable. We never see the manifold of configurations "from nowhere" — only the three framed measurements `μ_A, μ_B, μ_D`. Therefore the claim of a map is **not** a claim of reaching the territory. It is a claim about the **coherence of frames**: the map is real ⇔ the three frames are mutually consistent under C1 and C3. "No view from nowhere" applies to the map itself: it exists not as a view from above, but as a triangulation by three framed instruments. This is not a weakening — it is the only honest form in which such a claim can be true at all.

## 7. Minimal test and connection to the preregistration

The map is tested on the same material as the preregistration:
- `μ_A` — already the primary readout (P1).
- `μ_B` — the tertiary readout (P3), with a fixed symmetrization of KL.
- `μ_D` — is added as a functional categorical readout (judge labels for refusal/identity/hedging), taken on the same responses.
Then:
- C0/C1/C2 are computed directly from the preregistration runs (rank correlations + agreement of within/axis partitions across instruments).
- C3 additionally requires estimating the "rate" (the slope of `μ_B` against `μ_A` near the seam) and checking its stability across edits and models.

## 8. What falsifies the map

- The instruments find the seam in *different* places (C1 violated): the within/axis partition by `μ_A` ≠ by `μ_D`. Then there are several events, there is no shared referent `c` — the three sketches remain three sketches.
- The "exchange rate" is edit-specific (C3 violated): the A↔B relation exists, but is unstable. Then there is a correlation, but no chart.
- Hysteresis in D is absent, yet the non-commutativity from H2 is nonetheless present in A: order-dependence does not live at the dispositional seam — the model of §5 is wrong, and the map must be rebuilt.
Any outcome is informative and gets published.

## 9. One-paragraph summary

The map is not three spaces in isomorphism, but a single hypothetical configurational manifold with a single seam that three framed instruments (activational, behavioral-distributional, dispositional-functional) are required to localize in one place (C1) and to translate into one another at a stable rate (C3). The weak correlation of magnitudes is almost tautological and proves nothing; the load-bearing part is seam co-localization and the stability of the translation. Path-dependence is not a separate storyline but a property of the seam's neighborhood. And the map itself exists only as the coherence of frames, not as a view from nowhere.

---

## Appendix — references

- Lu, C., Gallagher, J., Michala, J., Fish, K., Lindsey, J. (2026). *The Assistant Axis.* arXiv:2601.10387.
- Menon, P. G. (2026). *Persistent Identity in AI Agents.* arXiv:2604.09588.
- *Stateful Reasoning Runtimes: Architectural Patterns for Identity Persistence Over Stateless LLM APIs* (2025).
- Vasilenko, V. (2026). *Identity as Attractor.* arXiv:2604.12016.
- Amari, S. *Information Geometry and Its Applications* (background for Fisher–Rao / KL as a local form).
