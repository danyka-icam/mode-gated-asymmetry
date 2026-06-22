# Structural Flatness: why path is lost in the memory regime

**Version:** 0.1
**Relation:** explains the Round 2 behavioral null and connects it to the memory benchmark (Mem0/Zep/Letta, Probe A). No GPU.

## Two different nulls, easily confused

The Round 2 behavioral null was obtained in a regime where the **entire permuted history sat in a single context**. The path *was* in the tokens — the model ignored it. So this null means **in-context stabilization** (capping/RLHF suppress order-sensitivity at output), not "nothing to grab onto."

"Nothing to grab onto" is a **different** null: cross-session, mediated by memory — where the history is not in the window but reconstructed from a store. That is what this document is about.

## Thesis (precisely)

In current retrieval architectures, **the path by which a subject reached its present state is not recoverable at inference**, because the memory→context step flattens order. Two subjects with identical fact-sets but different histories yield identical assembled contexts → identical behavior. Path-dependence here is structurally impossible, not merely suppressed.

## The precision about temporal graphs (without which the thesis breaks)

One cannot say "memory does not store order" — Zep holds a temporal knowledge graph; event logs carry timestamps. The store *does* carry order. But the **waist** between store and model loses it: retrieval ranks by relevance (top-k), not by trajectory, and collapses into a context the model reads as a set. Even an order-carrying store hands back an order-flat context. The claim is about the **assembly step**, not the store.

## The real thesis: state vs trajectory

Beneath ranking lies representation. Current systems represent a subject as a **state** — a set of facts/embeddings/nodes. Path-dependence requires representing the subject as a **trajectory** — an ordered, possibly non-commutative accumulation, where `accumulate(A,B) ≠ accumulate(B,A)`.

This is not a bug fixable by better retrieval. It is a representational choice. Only a memory whose *retrieved* representation is sensitive to accumulation order can carry path — and none of the current ones are, at the waist. This is the fundable gap: **memory infrastructure represents subjects as states, not trajectories; observer continuity requires trajectory-carrying memory.**

## Empirical leg (no GPU)

The structural argument is an analysis; its empirics are the benchmark. Probe A ("structural flatness"): two subjects converge to the same fact-set by different paths → if the contexts assembled from memory are identical and behavior is identical, flatness is confirmed at the memory I/O level, without touching model internals.

## Dissociating the two causes (this makes both versions falsifiable)

Two arms separate stabilization from structure:

- **In-context** (full history in the window): isolates **stabilization**. Round 2 = this arm; result flat.
- **Memory-mediated** (history NOT in the window, reconstructed from the store): isolates **structure**. Best run on a **less-stabilized** open model — then stabilization is removed as an explanation. If still flat → the cause is structural, not behavioral.

Prediction: memory-mediated flatness holds even where in-context stabilization is removed. If it does *not* (memory-mediated forks), the structural thesis is wrong, path leaks through the waist somehow, and that must be accepted.

## Relation to the configuration map

The observer (the dispositional layer) is exactly what should carry path. Current systems collapse it into a fact-set on two levels at once: at the model's output (stabilization) and in memory assembly (structure). The behavioral null and structural flatness are one observer-collapse seen from two layers. The map predicted a single seam; here it appears as a single path-loss mechanism.

## What this buys

- Explains the null without rescuing the theory: the Round 2 null is *measured* stabilization, not a failure.
- Moves the claim to the regime where it is true, novel, and compute-free.
- Stitches the order-dependence line to the memory benchmark into one state-vs-trajectory thesis.
- Makes GPU/activation work a clearly-scoped *future* step (the third layer), not a precondition.
