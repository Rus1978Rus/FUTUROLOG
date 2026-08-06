# FUTUROLOG HANDOFF PACK — READ ME FIRST

## 1. Purpose

This archive is a developer handoff package for the FUTUROLOG project.

It is not a finished product and it is not a guarantee that all patches are implemented.
The package consolidates architecture documents, migration patches, verification registers,
and implementation guidance into one transfer bundle.

## 2. What the project is

FUTUROLOG is intended as a domain-neutral analytical system that separates:

- a primary risk or anomaly score;
- an objective-support score describing how well the signal is independently supported.

The system is designed for noisy, heterogeneous, multi-source environments.
It must not be described as an oracle or as a system that can predict the future with certainty.

## 3. Start order

Read the files in this order:

1. `implementation_order.md`
2. `../specification/critical_invariants.md`
3. `../index/source_document_index.md`
4. `../architecture/futurolog_architecture_v1.1.md`
5. `../architecture/objective_layer_design_v1.md`
6. `../architecture/canonical_scoring_mapping_v1.md`
7. `../validation/requires_verification_register.md`
8. `../research/open_questions_register.md`
9. `../validation/test_baseline_policy.md`

Then review the M1 and M3 patch sets.

## 4. Important status rule

Documented intent is not proof of implementation.
A patch file is a specification until code, tests, and integration evidence demonstrate otherwise.

Use these distinctions consistently:

- `DOCUMENTED`
- `PLANNED`
- `PARTIALLY_IMPLEMENTED`
- `IMPLEMENTED`
- `VERIFIED`

Do not collapse them into one status.

## 5. Package contents

The package contains current and legacy architecture documents, Objective Layer design, canonical scoring mapping, domain-neutral migration material, M1 and M3 patch sets, verification registers, a test baseline policy, and original reference material.

## 6. Developer instruction

Before changing code:

1. establish the current repository baseline;
2. map each specification to actual modules and tests;
3. preserve the critical invariants;
4. implement one bounded patch at a time;
5. verify behaviour against explicit fixtures;
6. record unresolved assumptions instead of silently resolving them.

## 7. Boundary

This handoff package is suitable for implementation planning and technical review. It is not evidence of production readiness, scientific validation, commercial fitness, or predictive accuracy.
