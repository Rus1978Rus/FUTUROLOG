# FUTUROLOG — CRITICAL INVARIANTS

These invariants must survive implementation, refactoring, calibration, and domain adaptation.

## 1. Risk is not objective support

The primary score and objective-support score answer different questions and must remain separate.

- Primary risk: how concerning or anomalous is the observed pattern?
- Objective support: how strongly is that pattern supported by persistence, agreement, redundancy, noise separation, and scale stability?

A high risk score with low objective support must remain possible and visible.

## 2. Objective support is not truth probability

The objective score must not be marketed or interpreted as the probability that a claim is true.
It is a structured support measure under an explicit model and evidence set.

## 3. Missing evidence is not negative evidence

Unknown, unavailable, or unmeasured values must not silently become zero.
Missingness needs an explicit representation and policy.

## 4. Repetition is not independence

Multiple copies of one source must not be counted as multiple independent confirmations.
Source dependence and common-origin amplification must be modelled or conservatively bounded.

## 5. Persistence is not causality

A signal that persists over time may still be spurious, manipulated, or downstream of another process.
Temporal persistence cannot be used as proof of causal structure.

## 6. Agreement is not correctness

Observers may agree because they share the same source, model, incentive, or bias.
Observer agreement requires dependence checks.

## 7. Noise filtering must be auditable

The system must explain which observations were down-weighted or excluded and why.
Noise separation must not become an opaque mechanism for discarding inconvenient evidence.

## 8. Domain neutrality requires adapters

A common core does not eliminate domain-specific semantics, calibration, thresholds, and data-quality rules.
Domain-specific assumptions must be isolated in explicit adapters or configurations.

## 9. Compatibility changes require tests

Renaming fields, changing score semantics, or introducing dual outputs requires migration tests and documented compatibility behaviour.

## 10. Documentation is not implementation

No document, patch specification, architecture diagram, or status label proves that runtime behaviour exists.
Only code plus relevant verification evidence can support an implementation claim.

## 11. Human decision authority remains explicit

FUTUROLOG is a decision-support system. It must not silently convert analytical scores into irreversible actions without an explicitly designed governance layer.

## 12. Uncertainty must remain visible

Outputs must preserve confidence limitations, missing inputs, model assumptions, and unresolved contradictions.
