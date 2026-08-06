# Read Me First for Developers

> **English semantic mirror.** This edition preserves the decisions, interfaces, constraints, status boundaries, and implementation intent of the Russian source. It is meaning-oriented rather than sentence-by-sentence. Canonical identifiers, formulas, API names, reason codes, and compatibility requirements remain unchanged.

## Purpose

Defines how a developer must approach the FUTUROLOG handoff before changing code or treating any document as implemented.

## Preserved decisions

- Read documents in the declared order and verify assumptions before implementation.
- Treat explicit invariants as hard constraints, not optional guidance.
- Preserve the safe-rollout sequence and compatibility behavior.
- Do not convert architectural intent into production claims without code, tests, and calibration evidence.

## Boundaries and verification status

- The package is a developer handoff and research architecture, not proof of a finished runtime.
- Items marked REQUIRES_VERIFICATION remain unresolved until checked against source code and baselines.

## Source relationship

The Russian source remains the detailed normative working artifact. This English mirror is the public semantic counterpart and must be updated whenever a decision, invariant, interface, formula, or status changes.
