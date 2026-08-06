# Implementation Order

> **English semantic mirror.** The order is dependency-sensitive and protects compatibility.

## Phase 0 — Verification

Before changing code, verify repository structure, current public interfaces, tests, scoring behaviour, storage schemas, datasets, sealing payloads, and documentation. Resolve or explicitly retain every blocking item in the requires-verification register.

## Milestone M1 — Entropy-RG v3.0 Domain-Neutral

1. **M1.1 Migration plan** — inventory all affected files, data, APIs, and compatibility obligations.
2. **M1.2 Domain rename** — replace seller/listing concepts with actor/event concepts without changing scoring semantics.
3. **M1.3 Scoring rename** — introduce canonical component names, mapping metadata, and trust-adjustment terminology.
4. **M1.4 Dual output** — expose legacy and canonical views together and establish the no-objective regression baseline.
5. **M1.5 Documentation and release** — align README, technical specification, migration guide, API description, and status boundaries.

## Milestone M3 — Objective Layer

1. `temporal_persistence`;
2. `observer_agreement`;
3. `source_redundancy`;
4. `noise_separation`;
5. `scale_stability`;
6. guarded Objective Layer activation;
7. operational hardening and stable response behaviour.

## Deferred work

Calibration, causal modelling, scenario trees, feedback-loop analysis, production domain adapters, and high-impact automated decision policies are deferred. They must not be silently folded into migration patches.

## Completion rule

A milestone is complete only when code, tests, migration checks, documentation, and declared baselines agree. A design document alone is not implementation evidence.
