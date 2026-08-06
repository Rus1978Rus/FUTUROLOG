# FUTUROLOG — IMPLEMENTATION ORDER

## Phase 0 — Establish baseline

1. Identify the authoritative source repository and default branch.
2. Record current tests, fixtures, schemas, and public interfaces.
3. Run the existing test suite without modifications.
4. Capture failures and environment assumptions.
5. Do not declare a clean baseline unless the suite actually passes.

## Phase 1 — M1 domain-neutral migration

Apply in order:

1. `patches_M1/M1.1_migration_plan_v3_0.md`
2. `patches_M1/M1.2_domain_rename_patch.md`
3. `patches_M1/M1.3_scoring_rename_patch.md`
4. `patches_M1/M1.4_dual_output_patch.md`
5. `patches_M1/M1.5_documentation_release.md`

Exit condition: domain-specific trading vocabulary is removed or isolated behind adapters,
while compatibility expectations are documented and tested.

## Phase 2 — Scoring contract

1. Implement the canonical scoring mapping.
2. Distinguish primary risk from objective support.
3. Preserve explicit missing-data and uncertainty states.
4. Add schema and contract tests.

## Phase 3 — M3 objective layer

Apply in order:

1. temporal persistence;
2. observer agreement;
3. source redundancy;
4. noise separation;
5. scale stability;
6. objective-layer activation;
7. objective-layer operational integration.

## Phase 4 — Integration and calibration

1. Build deterministic fixtures.
2. Test monotonicity and boundary conditions.
3. Test correlated-source failure cases.
4. Calibrate thresholds on domain-specific datasets.
5. Document where calibration does not transfer between domains.

## Phase 5 — Release gate

A release must not be described as validated unless:

- the code exists;
- relevant tests pass;
- calibration data are documented;
- limitations are explicit;
- output explanations are reproducible;
- the objective score is not misrepresented as truth probability.
