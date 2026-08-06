# Entropy-RG v3 Domain-Neutral Migration Release

> English semantic mirror of the consolidated Russian migration document.

## Release intent

Transform the inherited Entropy-RG scoring engine from a marketplace-specific implementation into a domain-neutral foundation suitable for FUTUROLOG domain adapters.

## Main changes

- replace `seller` and `listing` ontology with `actor` and `event`;
- introduce canonical scoring names and a versioned legacy mapping;
- expose dual legacy/canonical output during migration;
- version system, formula, mapping, and scoring metadata;
- preserve compatibility through declared aliases and migration rules;
- establish the M1.4 no-objective baseline;
- prepare, but do not silently activate, the M3 Objective Layer.

## Validation requirements

Release readiness requires aligned code, tests, data migrations, storage schemas, API responses, documentation, security/sealing payloads, and rollback behaviour.

## Compatibility boundary

Deprecated aliases are temporary and require declared removal versions. Silent field removal or semantic reassignment is prohibited.

## Calibration boundary

Domain-neutral implementation does not imply domain-neutral calibration. Each production domain requires representative data, evaluation criteria, thresholds, and prospective validation.

## Status

This repository currently contains architecture and migration specifications. Runtime implementation and release readiness must be verified in the actual source-code repository.
