# CROSS_PROJECT_DONOR_REGISTER v0.1
## Donor register for the universal FUTUROLOG core

**Status:** `WORKING_REGISTER / PRE-INTEGRATION / NO_CODE_IMPORTED_YET`

This is a meaning-oriented English mirror of the Russian working document. Its purpose is to prevent uncontrolled cross-project imports by assigning one functional owner per mechanism before code is reused.

## Import statuses

- `IMPORT` — candidate for near-direct reuse after local tests.
- `ADAPT` — mechanism is useful but its code or contract must be changed.
- `REFERENCE` — methodology/reference only, not a runtime dependency.
- `LATER` — potentially useful, but not at the current stage.
- `REJECT` — not suitable for the current FUTUROLOG architecture.

## Main allocation

- **Entropy-RG v2.2** remains the baseline scoring/anomaly core.
- **ACDM-KERNEL** contributes domain-neutral signal contracts, runtime audit, observability horizon, decision damping, governance, and plugin conformance ideas.
- **Notarius** contributes evidence provenance, transformation traces, mandatory-route completeness, and source-integrity mechanisms.
- **Motor-/SmoothGuard** contributes numeric hysteresis and a reproducible backtest pattern.
- **QuditEngine** contributes preregistration, seeded reproducibility, errata discipline, and retention of negative results; its quantum mathematics is not imported into scoring.
- **BRUINGate** contributes the architectural principle of a cheap ingestion gate before expensive analysis; its de Bruijn/HMAC token logic is rejected for the analytical core.
- **Vakhter** contributes canonicalization, detector isolation, and fail-closed/degraded behavior for untrusted text.
- **Foundation Layer** contributes governance guards against status/proof confusion.
- **E-Continuity** contributes recoverability discipline and an archive-audit tool for historical evaluation corpora.
- **CONVEYOR** remains a development/review process, not a runtime brain component.
- **MSL/MIP** is an optional structural-text adapter and source of pinned-data / visible-degradation rules.
- **Seed and Formula** contributes a candidate formalization-stage map and pre-technology maturity diagnosis for emerging domains. Its numeric formality/meaning deltas and crisis boost are reference-only and are not calibrated metrics.

## New donor: “Seed and Formula”

Source: user-provided archive `OKComputer_Философы_и_математики.zip`.

The source describes a seven-stage logical map: verbalization of the question → definition → idealization → symbolization → measurement → axiomatization → algorithmization. The source explicitly says this is a logical order rather than a mandatory chronological law: real trajectories can reorder stages, loop back, or stall.

FUTUROLOG retains the diagnostic structure, not a claim of a universal law of scientific development.

Candidate guards:

`MEASUREMENT != CONSTRUCT_VALIDITY`

`FORMALIZATION != UNDERSTANDING`

`FORMALIZATION_PROGRESS != REALITY_COVERAGE`

The simulator’s `formality_delta`, `meaning_delta`, starting metrics, and `CRISIS_BOOST = 1.5` are not treated as calibrated measurements and must not enter Objective/Coverage or core scoring without an independent evaluation protocol.

Detailed candidate card: `docs/en/research/emerging_domain_assessment_candidate_v0_1.md`.

## Overlap boundaries

`WORLD/EVIDENCE_TRACE != SYSTEM_EXECUTION_TRACE`: Notarius owns evidence provenance; ACDM-style audit owns what FUTUROLOG did with the evidence.

`NUMERIC_HYSTERESIS != STATE_HOLD`: Motor-style deadband handles threshold jitter; ACDM-style hold handles temporal de-escalation stability.

Vakhter, MSL/MIP, and Notarius remain separate: sanitation, structural interpretation, and provenance are different responsibilities.

Foundation Layer, CONVEYOR, and ACDM governance also remain separate: principles, development process, and runtime authority are different layers.

## Draft architecture

```text
RAW INPUT
   ↓
INGESTION GATE
   ↓
TEXT / STRUCTURE SANITATION
   ↓
SOURCE / ELEMENT PROVENANCE
   ↓
NORMALIZATION
   ↓
ENTROPY-RG CORE
   ↓
OBJECTIVE / COVERAGE / FRESHNESS
   ↓
DECISION STABILITY
   ↓
ENRA ORCHESTRATION
   ↓
RUNTIME GOVERNANCE / AUDIT
   ↓
EXPLAINABLE OUTPUT
```

Outside runtime: Foundation Layer provides protective principles, CONVEYOR governs change/review, QuditEngine contributes reproducibility discipline, E-Continuity governs corpus recoverability, and Seed and Formula remains a candidate diagnostic for emerging-domain maturity.

Current prohibitions include importing unvalidated donor numerics as truth-like metrics, including Seed and Formula’s formality/meaning deltas.

Key invariant for the next layer:

`HIGH_MEASURED_SCORE + LOW_COVERAGE != HIGH_EFFECTIVE_CONFIDENCE`.

The implementation sequence is unchanged: next comes `OBJECTIVE_COVERAGE_FORMULA_BAKEOFF_v0_1`.
