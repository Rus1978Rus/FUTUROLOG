# Canonical Scoring Mapping v1

> **English semantic mirror.** This edition preserves the decisions, interfaces, constraints, status boundaries, and implementation intent of the Russian source. It is meaning-oriented rather than sentence-by-sentence. Canonical identifiers, formulas, API names, reason codes, and compatibility requirements remain unchanged.

## Purpose

Maps legacy Entropy-RG components into the FUTUROLOG universal and objective scoring layers.

## Preserved decisions

- Universal components include local action risk, profile deviation, flow asymmetry, graph risk, trust penalty, sequential anomaly, and RG persistence.
- Objective components include scale stability, temporal persistence, source redundancy, observer agreement, and noise separation.
- Legacy keys and canonical FUTUROLOG keys are connected through an explicit mapping layer.
- Objective risk is computed only from active components with normalized active weights.
- The final formula combines universal risk, objective contribution, trust adjustment, and bounded confluence behavior.

## Boundaries and verification status

- Weights are design defaults until calibrated.
- A mapping is not evidence that two concepts are empirically equivalent.

## Implementation meaning

This document is the semantic bridge between the inherited scoring engine and the future domain-neutral platform. Implementations must preserve key provenance and expose both legacy and canonical outputs during migration.

## Source relationship

The Russian source remains the detailed normative working artifact. This English mirror is the public semantic counterpart and must be updated whenever a decision, invariant, interface, formula, or status changes.
