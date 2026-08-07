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
- **E-Continuity** contributes recoverability discipline and a useful archive-audit tool for historical evaluation corpora.
- **CONVEYOR** remains a development/review process, not a runtime brain component.
- **MSL/MIP** is an optional structural-text adapter and source of pinned-data / visible-degradation rules.

## Overlap boundaries

`WORLD/EVIDENCE_TRACE != SYSTEM_EXECUTION_TRACE`: Notarius owns evidence provenance; ACDM-style audit owns what FUTUROLOG did with the evidence.

`NUMERIC_HYSTERESIS != STATE_HOLD`: Motor-style deadband handles threshold jitter; ACDM-style hold handles temporal de-escalation stability.

Vakhter, MSL/MIP, and Notarius must not be collapsed into one text subsystem: sanitation, structural interpretation, and provenance are separate responsibilities.

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

Outside runtime: Foundation Layer provides protective principles, CONVEYOR governs change/review, QuditEngine contributes reproducibility discipline, and E-Continuity governs long-term corpus recoverability.

Key invariant for the next layer:

`HIGH_MEASURED_SCORE + LOW_COVERAGE != HIGH_EFFECTIVE_CONFIDENCE`.
