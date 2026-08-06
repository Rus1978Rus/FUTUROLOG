# Critical Invariants

> **English semantic mirror.** This edition preserves the decisions, interfaces, constraints, status boundaries, and implementation intent of the Russian source. It is meaning-oriented rather than sentence-by-sentence. Canonical identifiers, formulas, API names, reason codes, and compatibility requirements remain unchanged.

## Purpose

Captures non-negotiable scoring and rollout constraints.

## Preserved decisions

- Trust adjustment is subtracted exactly once.
- When no objective components are active, output must regress exactly to the M1.4 baseline.
- Objective activation depends on active components, not the mere presence of an object.
- Objective components are stateless functions of explicit context.
- Weights and calibration status must be explicit and versioned.
- Rollout proceeds through guarded, testable stages.

## Boundaries and verification status

- Changing an invariant requires an explicit versioned decision and baseline update.
- Calibration is not implied by implementation.

## Source relationship

The Russian source remains the detailed normative working artifact. This English mirror is the public semantic counterpart and must be updated whenever a decision, invariant, interface, formula, or status changes.
