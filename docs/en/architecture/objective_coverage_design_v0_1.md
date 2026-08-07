# OBJECTIVE_COVERAGE_DESIGN v0.1
## Objective / Coverage redesign for the universal FUTUROLOG core

**Status:** `DESIGN_DRAFT / PRE-IMPLEMENTATION / NOT_VALIDATED`

This English document is a meaning-oriented mirror of the Russian working design. The redesign prevents a high result from being treated as reliable when it is based on only a small visible fraction of the required evidence.

## Core invariant

```text
HIGH_MEASURED_SCORE + LOW_COVERAGE
!=
HIGH_EFFECTIVE_CONFIDENCE
```

## Required separate outputs

```text
measured_score
evidence_coverage
source_independence
freshness
pipeline_completeness
observed_noise
effective_confidence
```

- `measured_score` — what the available measurements actually show.
- `evidence_coverage` — how much of the required evidence picture is visible.
- `source_independence` — how independent the confirmations really are.
- `freshness` — how current the evidence is for the task.
- `pipeline_completeness` — whether the signal completed its mandatory processing route.
- `observed_noise` — measured instability/noise in the observed input.
- `effective_confidence` — confidence in the current analytical conclusion after accounting for observation limits.

## Missing-data policy

The following behavior is forbidden:

```text
missing component
→ remove it
→ renormalize remaining weights
→ report the result as if coverage were complete
```

`NO_DATA != NEGATIVE_EVIDENCE` and `NO_DATA != NO_RISK`.

## Candidate aggregation families

No final formula is selected in v0.1. At least three families must be compared on identical fixtures:

1. linear aggregation with explicit coverage;
2. weighted geometric mean;
3. hybrid/min-cap aggregation where critically weak coverage, freshness, or pipeline completeness limits maximum effective confidence.

## Donor imports at design level

ACDM-KERNEL contributes observability-horizon and explicit degradation ideas; Notarius contributes provenance and mandatory-route completeness; Vakhter contributes component isolation and the rule that analysis failure must not silently become CLEAN; Foundation Layer contributes proof/status guards; MSL/MIP contributes pinned-data and visible-degradation discipline; QuditEngine and CONVEYOR contribute preregistration and reproducible comparative evaluation.

## Draft API shape

```json
{
  "measured_score": 0.78,
  "evidence_coverage": 0.46,
  "source_independence": 0.61,
  "freshness": 0.88,
  "pipeline_completeness": 0.92,
  "observed_noise": 0.24,
  "effective_confidence": 0.41,
  "status": "DEGRADED_EVIDENCE"
}
```

Numbers above illustrate the contract only; they are not calibrated thresholds.

## Required boundary tests

The comparative prototype must cover: one perfect component out of five; many copies of one source; mixed freshness; a missing mandatory pipeline step; component failure; full coverage with high noise; and a strong signal with low coverage.

FUTUROLOG must also distinguish `SIGNAL_STRENGTH` from `EVIDENCE_CONFIDENCE`. A high signal with low confidence is a legitimate early-warning state.

## Semantic boundary

```text
CONFIDENCE_IN_ANALYSIS
!=
PROBABILITY_OF_FUTURE_EVENT
```

`effective_confidence` is not automatically a calibrated probability that a future event will occur.

Next step: `OBJECTIVE_COVERAGE_FORMULA_BAKEOFF_v0_1`.
