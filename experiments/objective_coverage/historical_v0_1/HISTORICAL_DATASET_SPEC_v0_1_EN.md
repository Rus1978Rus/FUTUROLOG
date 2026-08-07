# HISTORICAL_DATASET_SPEC v0.1
## First GEOECON pilot corpus for Objective/Coverage historical evaluation

**Status:** `DATASET_SPEC_FROZEN / PILOT_PIPELINE_VALIDATION / NOT_FORMULA_SELECTION / NOT_VALIDATED`

This is a meaning-oriented English mirror of the Russian working specification.

The pilot episode is the 2021–2022 Russia–Ukraine escalation preceding Russia's full-scale invasion of Ukraine on 24 February 2022. It was selected because military, diplomatic, and economic/energy evidence existed before the event.

## Target event

`TARGET_EVENT_CLASS = LARGE_SCALE_INTERSTATE_KINETIC_ESCALATION`

For this pilot only, the outcome is fixed as the start of the full-scale invasion on `2022-02-24`.

Exercises, rhetoric, troop movements without full-scale invasion, isolated cyber incidents, sanctions statements, and pre-24-February local clashes are not separately counted as the target outcome.

## Horizon

Primary horizon: `30 DAYS`.

A snapshot is labelled positive only if the target event occurs in `(cutoff_time, cutoff_time + 30 days]`.

Snapshots from the same crisis are correlated and are not independent cases. Therefore this pilot cannot select a final formula.

## Source families

Initial frozen families:
- `NATO_OFFICIAL` — official NATO statements/transcripts;
- `CSIS_ANALYSIS` — dated independent analytical publications;
- `IEA_ENERGY` — economic/energy context, with strict protection against importing post-event interpretation into pre-event snapshots.

Multiple pages repeating one NATO claim do not become multiple independent sources.

## Evidence classes

```text
MILITARY_BUILDUP
DIPLOMATIC_COERCION_OR_WARNING
ECONOMIC_ENERGY_STRESS
CROSS_DOMAIN_CONVERGENCE
```

`CROSS_DOMAIN_CONVERGENCE` is derived and must retain references to the primary evidence items that produced it.

## EvidenceState

Each cutoff eventually produces:

```text
measured_score
evidence_coverage
source_independence
freshness
pipeline_completeness
observed_noise
```

`measured_score` must come from a frozen scoring provider, not from a retrospective human label such as “war was near”. Until that provider is specified, the field remains `NOT_COMPUTED`.

Coverage uses three required primary classes: military buildup, diplomatic coercion/warning, and economic/energy stress. Cross-domain convergence is derived and does not increase the denominator.

## Leakage invariant

Every evidence item must carry original publication time and cutoff time.

```text
original_publication_time > cutoff_time
→ EXCLUDE_FROM_SNAPSHOT
```

Unknown original publication time means `REVIEW_REQUIRED / NOT_TRUSTED_FOR_FROZEN_RUN`.

## Pilot boundary

```text
ONE_CRISIS != GENERAL_VALIDATION
WEEKLY_SNAPSHOTS != INDEPENDENT_CASES
RUSSIA_UKRAINE_2022 != ALL_GEOPOLITICS
HIGH_SCORE_BEFORE_EVENT != CAUSAL_PROOF
```

A successful run can establish only `PIPELINE_VALIDATED_ON_ONE_HISTORICAL_EPISODE`.

Next artifact: `EVIDENCE_STATE_ADAPTER_SPEC_v0_1_RU.md`.