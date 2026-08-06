# CRITICAL INVARIANTS

## 1. Trust adjustment is subtracted once

```text
universal_raw = sum(weights × component_scores) + confluence_bonus
universal_risk = universal_raw - gamma × trust_adjustment
final_score = universal_raw × (alpha + (1 - alpha) × objective_risk_or_1) - gamma × trust_adjustment
```

Never use `universal_risk` as the multiplier in the final formula.

## 2. No-objective regression must equal M1.4 baseline

If Objective Layer is disabled or inactive:

```text
objective_risk_or_1 = 1.0
final_score = universal_risk
```

## 3. Objective activation rule

```text
objective_layer_active = true
iff:
    active_component_count >= 3
    AND scale_stability is active
    AND objective_layer_enabled = true
```

## 4. Active component definition

```text
result is not None AND confidence >= 0.3
```

## 5. Objective weights

```text
scale_stability       0.25
temporal_persistence  0.20
source_redundancy     0.20
observer_agreement    0.20
noise_separation      0.15
```

Weights are normalized over active components only.

## 6. Objective modules are stateless

No I/O, no DB calls, no API calls, no imports from `app.scoring`.

## 7. Calibration status

Until M5:

```text
calibration_status = "uncalibrated"
```

`final_score` is not a probability.

## 8. Safe rollout

```text
objective_layer_enabled=false by default
```
