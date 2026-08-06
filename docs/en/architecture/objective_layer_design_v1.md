# Objective Layer Design v1

> **English semantic mirror.** Meaning-oriented counterpart of the Russian working document.

## Purpose

The Objective Layer answers a question that the universal risk score cannot answer by itself: **how objectively supported is the detected signal?**

## Component result contract

Each objective component returns:

- `value` — normalized component result;
- `confidence` — confidence in the component result, not automatically a calibrated probability of truth;
- `missing_inputs` — evidence required but unavailable;
- `reasons` — machine- and human-readable explanation;
- `partial` — whether the result was computed from incomplete context.

Insufficient evidence must not be replaced with a fabricated neutral score.

## ObjectiveLayerContext

The context extends scoring input with explicit supporting structures:

- `score_history` for temporal analysis;
- `observer_results` for independent analytical agreement;
- `source_registry` and source-dependence information;
- `noise_baseline` for signal/noise comparison;
- `scale_aggregates` for cross-scale stability.

## Components

- `temporal_persistence` — checks whether the signal survives across time windows;
- `observer_agreement` — measures agreement across sufficiently independent observers;
- `source_redundancy` — evaluates support from multiple non-duplicate sources;
- `noise_separation` — tests whether the signal differs materially from the noise baseline;
- `scale_stability` — checks whether the pattern remains coherent at different aggregation scales.

## Aggregation

Only valid active components participate in `objective_risk`. Active weights are renormalized. Layer confidence is reported separately from the objective value.

The layer is inactive when no objective component is valid. In that case, the final system output must equal the M1.4 no-objective baseline exactly.

## Supporting structures

The design introduces or anticipates:

- `ObserverRegistry`;
- `SourceIndependenceGraph`;
- `NoiseBaseline`;
- `ScaleAggregator`;
- `ScoreHistory`.

These structures must remain explicit and auditable. Hidden state would undermine reproducibility and testing.

## MVP strategy

Implementation is staged component by component. Partial operation must be visible in the response schema. “Implemented” and “calibrated” are separate statuses.

## Testing requirements

Tests should cover monotonicity where applicable, missing inputs, short histories, conflicting observers, dependent sources, stale baselines, scale gaps, active-weight normalization, inactive-layer regression, and formula-order invariants.

## Boundary

The Objective Layer estimates evidential support under declared assumptions. It does not transform uncertain evidence into certainty and does not prove causality.
