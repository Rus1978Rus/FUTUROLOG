# Objective Layer Design v1

> **English semantic mirror.** This edition preserves the decisions, interfaces, constraints, status boundaries, and implementation intent of the Russian source. It is meaning-oriented rather than sentence-by-sentence. Canonical identifiers, formulas, API names, reason codes, and compatibility requirements remain unchanged.

## Purpose

Specifies the interfaces, context objects, activation logic, aggregation behavior, and tests for the Objective Layer.

## Preserved decisions

- Each component returns value, confidence, missing inputs, reasons, and partial-status metadata.
- ObjectiveLayerContext carries score history, observer results, source registry, noise baseline, and scale aggregates.
- Missing components are excluded and active weights are renormalized.
- Layer confidence is reported separately from objective value.
- Inactive Objective Layer behavior must equal the no-objective baseline exactly.
- Supporting structures include observer registry, source-independence graph, noise baseline, scale aggregator, and score history.
- MVP implementation is staged and must expose partial operation honestly.

## Boundaries and verification status

- A component with insufficient evidence must not fabricate a neutral score.
- Confidence is not probability of truth unless separately calibrated.

## Implementation meaning

This design turns “how real is this signal?” into an explicit, inspectable computation rather than a hidden model intuition.

## Source relationship

The Russian source remains the detailed normative working artifact. This English mirror is the public semantic counterpart and must be updated whenever a decision, invariant, interface, formula, or status changes.
