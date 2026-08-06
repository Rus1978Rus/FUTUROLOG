# Critical Invariants

> **English semantic mirror.** These constraints are non-negotiable unless changed through an explicit versioned decision.

## 1. Trust adjustment is subtracted once

The trust-related deduction must enter the final formula exactly once. It must not be duplicated inside component scores and then subtracted again at integration.

## 2. No-objective regression equals the M1.4 baseline

When the Objective Layer has no active valid components, final behaviour must be exactly equivalent to the M1.4 no-objective baseline.

## 3. Objective activation is evidence-based

The Objective Layer is active only when at least one objective component has a valid result. The presence of an empty context object does not activate the layer.

## 4. Active component definition

An active component has sufficient inputs, a valid normalized value, and no blocking error. Missing or invalid components are excluded rather than assigned fabricated neutral values.

## 5. Active weights are normalized

Objective weights are renormalized over active components. A missing component must not silently dilute the total.

## 6. Objective modules are stateless

Component outputs must be functions of explicit input and context. Registries, histories, baselines, and graphs are passed or referenced explicitly so results remain reproducible and testable.

## 7. Calibration status is explicit

Implemented, tested, calibrated, validated, and production-ready are different statuses. None may be inferred from another.

## 8. Safe rollout

Migration proceeds through guarded milestones with compatibility output, regression baselines, component-level tests, partial-status reporting, and rollback capability.
