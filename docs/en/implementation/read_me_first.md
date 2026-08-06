# Read Me First for Developers

> **English semantic mirror.** This is the required entry point before implementing any FUTUROLOG or Entropy-RG migration document.

## Status

The repository is a research architecture and developer handoff. It contains proposed patches, interfaces, invariants, registers, and migration guidance. It does not by itself prove that the described runtime exists or that the scoring model is calibrated.

## Primary rule

Verify the actual source repository, schemas, tests, API behaviour, and stored data before applying any patch. Patch text is a design artifact until reconciled with the real codebase.

## Required reading order

1. Critical invariants.
2. Requires-verification register.
3. Test baseline policy.
4. Implementation order.
5. Current architecture v1.1.
6. Canonical scoring mapping.
7. Objective Layer design.
8. Milestone patches in numerical order.

## Prohibited shortcuts

- Do not declare a component implemented because a code excerpt exists in a document.
- Do not treat default weights as calibrated.
- Do not remove compatibility aliases without the declared migration boundary.
- Do not activate the Objective Layer by passing an empty context.
- Do not apply trust adjustment more than once.
- Do not erase failed predictions or corrections from the audit history.

## Safe rollout

Use a branch, preserve the no-objective baseline, apply one milestone at a time, run regression and component tests, expose partial operation honestly, and maintain rollback capability.
