# TEST BASELINE POLICY

## Required baselines

### M1.4 no-objective baseline

Used when Objective Layer is inactive or disabled.

Expected:

```text
final_score == universal_risk
objective_layer_active == false
```

Marker:

```python
@pytest.mark.baseline_no_objective
```

### M3.6.1 full-objective baseline

Used when Objective Layer is enabled and active.

Required ENV:

```bash
ENTROPY_RG_OBJECTIVE_LAYER_ENABLED=true
ENTROPY_RG_ALPHA=0.5
```

Marker:

```python
@pytest.mark.baseline_full_objective
```

## Baseline update rule

Create a new baseline only when math changes: formula, weights, calibration, alpha/gamma policy, or component semantics.

Do not create a new baseline for docs-only updates or refactoring with no score change.
