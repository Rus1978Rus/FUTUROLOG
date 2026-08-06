# Implementation Order

> **English semantic mirror.** This edition preserves the decisions, interfaces, constraints, status boundaries, and implementation intent of the Russian source. It is meaning-oriented rather than sentence-by-sentence. Canonical identifiers, formulas, API names, reason codes, and compatibility requirements remain unchanged.

## Purpose

Defines the dependency-aware order for migrating Entropy-RG into the domain-neutral FUTUROLOG scoring foundation.

## Preserved decisions

- Phase 0 verifies the actual codebase, tests, schemas, and current behavior.
- Milestone M1 establishes domain-neutral naming, canonical scoring names, dual output, and release documentation.
- Milestone M3 introduces the Objective Layer only after the M1 baseline is stable.
- Deferred milestones must not be smuggled into earlier patches.

## Boundaries and verification status

- Ordering is normative because later formulas assume earlier compatibility work.
- A milestone is not complete merely because a design document exists.

## Source relationship

The Russian source remains the detailed normative working artifact. This English mirror is the public semantic counterpart and must be updated whenever a decision, invariant, interface, formula, or status changes.
