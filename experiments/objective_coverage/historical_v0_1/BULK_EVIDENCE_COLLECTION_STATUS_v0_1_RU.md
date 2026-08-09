# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `BULK_COLLECTION_PAUSED_FOR_TARGETED_BACKFILL / BATCH_007_COMPLETE / FORMAL_GAP_AUDIT_COMPLETE / NOT_READY_FOR_NUMERIC_EVIDENCESTATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` завершены широкие intake-пакеты Batch 001–007 для двух пилотных кейсов:

- `russia_ukraine/`;
- `myanmar_post_coup_civil_war/`.

После Batch 007 выполнен отдельный `FORMAL_GAP_AUDIT_v0_1_RU.md`.

Главный вывод: широкое накопление данных уже дало достаточную карту покрытия. Продолжать просто добавлять новые широкие batch сейчас неэффективно. Следующий этап — только `TARGETED_BACKFILL_008` по блокирующим пробелам.

## Россия–Украина — blocking gaps

1. regional household inequality / affordability;
2. language / identity / culture / collective memory с несколькими независимыми source families;
3. religion / religious institutions / intergroup relations;
4. household food / water / fuel access;
5. complete topology-of-coverage map;
6. negative controls и дополнительные stabilizers.

## Мьянма — blocking gaps

1. numeric displacement snapshots из уже найденных contemporaneous UNHCR sensors;
2. diaspora / donations / external-support provenance для non-state actors;
3. content-level contemporaneous information-operation evidence;
4. direct water-access / flood-impact records beyond structural baseline;
5. более точная временная карта small-group formation / coalescence / fragmentation;
6. negative controls и дополнительные stabilizers.

## Gate после formal gap audit

```text
MULTIPLE_SOURCE_FAMILIES: PARTIAL_PASS
PRESSURE_AND_STABILIZERS: PARTIAL_PASS
RETROSPECTIVE_CUTOFF_GUARD: PASS
TOPOLOGY_GAPS_IDENTIFIED: PASS
MISSING_DOMAINS_EXPLICIT: PASS
SAME_FROZEN_SCHEMA: PASS
READY_FOR_NUMERIC_EVIDENCESTATE: NO
READY_FOR_NON_NUMERIC_PRE_EVIDENCESTATE_DRY_RUN: ALMOST
```

## Обязательные guards

```text
OBSERVABILITY != PREVALENCE
VISIBLE_EXCEPTION != BASE_RATE
DOMAIN_PRESENT != DOMAIN_WELL_COVERED
SOURCE_COUNT != INDEPENDENT_CONFIRMATION
SENSOR_PRESENT != MEASUREMENT_IMPORTED
RETROSPECTIVE_KNOWLEDGE != CUTOFF_KNOWLEDGE
SAME_SCHEMA != SAME_OBSERVABILITY
CROSS_CASE_SCORE_DIFFERENCE != TRUE_STATE_DIFFERENCE
```

## Следующий разрешённый этап

`TARGETED_BACKFILL_008`.

После него выполняется повторный formal gap audit. Если critical `EVIDENCE_GAP` по обязательным слоям закрыты, разрешается `PRE_EVIDENCESTATE_DRY_RUN` — нечисловой прогон состояния доказательств без прогноза и без числовой калибровки.

Числовой EvidenceState остаётся заблокирован до отдельного calibration/evaluation gate.

## Статус

```text
BATCH_001_TO_007_COMPLETE
FORMAL_GAP_AUDIT_COMPLETE
TARGETED_BACKFILL_REQUIRED
NUMERIC_EVIDENCESTATE_BLOCKED
NON_NUMERIC_DRY_RUN_NEAR_READY
SCHEMA_FREEZE_PRESERVED
NOT_VALIDATED
```
