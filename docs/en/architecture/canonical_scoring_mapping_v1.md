# Canonical Scoring Mapping v1

> **English semantic mirror.** This document preserves the scoring distinctions and migration intent of the Russian source.

## Purpose

The mapping connects inherited Entropy-RG scoring terms with the domain-neutral FUTUROLOG vocabulary without pretending that a rename is an empirical validation.

## Universal layer

The intended universal components are:

- `local_action_risk`;
- `profile_deviation`;
- `flow_asymmetry`;
- `graph_risk`;
- `trust_penalty`;
- `sequential_anomaly_score`;
- `rg_persistence_score`.

These components estimate intensity, anomaly, structural concentration, sequence behaviour, and persistence inside the observed process.

## Objective layer

The intended objective components are:

- `scale_stability`;
- `temporal_persistence`;
- `source_redundancy`;
- `observer_agreement`;
- `noise_separation`.

These components estimate the quality and robustness of the evidence supporting the signal.

## Migration rule

Legacy Entropy-RG keys and canonical FUTUROLOG keys must be connected through an explicit versioned mapping layer. During migration, responses may expose both views. Silent replacement of public fields is prohibited.

## Aggregation rule

Objective risk is calculated only from active valid components. Missing components are excluded, and the remaining active weights are normalized. Component confidence and layer confidence are separate from component value.

Trust adjustment is subtracted exactly once. Formula order and confluence behaviour must remain explicit and covered by regression tests.

## Calibration boundary

Default weights are engineering hypotheses until calibrated on representative domain data. The mapping specifies semantic placement; it does not prove predictive usefulness, independence, or optimal weighting.

## Recommended implementation sequence

1. Stabilize legacy behaviour and tests.
2. Introduce canonical names and mapping metadata.
3. Expose dual legacy/canonical output.
4. Implement Objective Layer components behind inactive-safe integration.
5. Calibrate only after prospective datasets and evaluation criteria exist.
