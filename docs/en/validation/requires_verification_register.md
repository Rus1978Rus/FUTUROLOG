# Requires Verification Register

> **English semantic mirror.** The detailed Russian register remains the item-level working source. This mirror preserves its governance meaning and closure requirements.

## Purpose

The register prevents assumptions, proposed interfaces, inferred file paths, formula interpretations, and copied code fragments from silently becoming verified facts.

## Entry classes

Verification items may concern:

- existence and current location of source files;
- current function names, signatures, schemas, and public API fields;
- numeric behaviour and formula order;
- default weights, thresholds, alpha, gamma, and calibration state;
- database and dataset migration impact;
- compatibility aliases and planned removal versions;
- security, HMAC, sealing, and audit payload behaviour;
- test coverage and baseline availability;
- independence of sources or observers;
- validity of domain assumptions;
- documentation claims about implementation or readiness.

## Closure requirements

An item is closed only when the repository records:

1. the evidence inspected;
2. the exact conclusion;
3. the reviewer or responsible actor;
4. the date and relevant version or commit;
5. any resulting patch, test, or documentation change.

Absence of an observed contradiction is not verification. A plausible code excerpt in a patch document is not proof that the real source tree contains that code.

## Status discipline

Recommended statuses are:

- `OPEN`;
- `BLOCKING`;
- `IN_REVIEW`;
- `VERIFIED`;
- `REJECTED_ASSUMPTION`;
- `DEFERRED_WITH_RATIONALE`.

Bulk closure without item-level evidence is prohibited.
