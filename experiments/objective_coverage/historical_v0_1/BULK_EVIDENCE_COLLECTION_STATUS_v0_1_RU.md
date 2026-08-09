# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `MULTI_MODEL_AGREEMENT_REPORT_COMPLETE / ADAPTER_v0_2_REVISED_DRAFT / ATOMIC_RECODE_PACKET_002_READY / NOT_READY_FOR_NUMERIC_EVIDENCESTATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` завершены широкие intake-пакеты Batch 001–007, formal gap audit, targeted backfill, non-numeric dry run, leakage audit, negative-control work, coverage topology, first/second coding checks и numeric gate review 001.

Дополнительно завершены:

- multi-model external coding pilot (Copilot, Grok, Claude) по `BLIND_SECOND_CODER_PACKET_001_RU.md`;
- `AGREEMENT_REPORT_001_RU.md`;
- targeted negative-control backfill 010;
- patch `DOMAIN_NEUTRAL_EVIDENCESTATE_ADAPTER_v0_2_DRAFT_RU.md` по найденным disagreement;
- новый `ATOMIC_RECODE_PACKET_002_RU.md`.

## Что показал multi-model audit

Agreement оказался переменным: часть items кодируется устойчиво, но dual-use evidence, retrospective evidence, sensor-only и mixed observed+projection claims создавали систематические расхождения.

Ключевой вывод:

```text
CODER_DISAGREEMENT != CODER_ERROR_BY_DEFAULT
DISAGREEMENT_CLUSTER => RUBRIC_REVIEW
```

Главные дефекты старой формы coding:

1. один scalar `direction` смешивал pressure и stabilizer;
2. cutoff FAIL не механически обнулял contribution;
3. strength смешивал силу события, масштаб покрытия и качество evidence;
4. sensor existence можно было ошибочно кодировать как strength;
5. observed facts и projections иногда жили в одной row;
6. информационный message content можно было перепутать с system pressure role;
7. расплывчатые cutoff labels создавали различия трактовки.

## Patch v0.2

`DOMAIN_NEUTRAL_EVIDENCESTATE_ADAPTER_v0_2_DRAFT_RU.md` теперь содержит:

```text
MIXED_CLAIM => ATOMIZE_BEFORE_CODING
CUTOFF_FAIL => pressure_signal = 0
CUTOFF_FAIL => stabilizer_signal = 0
CUTOFF_FAIL => event_strength = 0
CUTOFF_CONDITIONAL => NO_NUMERIC_CONTRIBUTION
SIGNAL_STRENGTH != COVERAGE_SCALE
SIGNAL_STRENGTH != EVIDENCE_QUALITY
SENSOR_EXISTENCE != EVENT_STRENGTH
PROJECTION != OBSERVED_COUNT
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_DIRECTION
```

Вместо одного signed direction введены отдельные `pressure_signal` и `stabilizer_signal`.

Отдельно хранятся:

```text
event_strength
coverage_scale
evidence_quality
confidence
```

## Atomic recode packet 002

Создан `ATOMIC_RECODE_PACKET_002_RU.md` с точными snapshot cutoffs:

```text
Russia–Ukraine cutoff = 2022-02-23T23:59:59Z
Myanmar cutoff = 2021-06-30T23:59:59Z
```

Mixed claims разделены: observed coping behavior и hunger projection теперь разные atomic rows; sensor-only и retrospective rows имеют отдельные правила.

Пакет предназначен для нового multi-model rubric stress test. Он НЕ заявляется как outcome-blind validation.

## Numeric gate

Числовой EvidenceState остаётся заблокирован.

Причины:

```text
ADAPTER_v0_2_NOT_ACTIVE
ATOMIC_RECODE_NOT_YET_COMPLETED
CHANNEL_AGGREGATION_NOT_CALIBRATED
NEGATIVE_CONTROL_FALSE_POSITIVE_ANALOGUES_INCOMPLETE
TRUE_OUTCOME_BLIND_VALIDATION_NOT_PROVEN
OBSERVED_NOISE_BLOCKED
```

## Следующий разрешённый порядок

```text
ATOMIC_RECODE_PACKET_002 -> MULTI_MODEL_RECODE
→ AGREEMENT_REPORT_002
→ ADAPTER_v0_2_REVIEW
→ FALSE_POSITIVE_ANALOGUES_BACKFILL
→ NUMERIC_EVIDENCESTATE_GATE_REVIEW_002
```

Если recode покажет, что базовые правила cutoff/sensor/projection/pressure-vs-stabilizer стали устойчивыми между моделями, v0.2 можно переводить в `ACTIVE_CANDIDATE`, но не в `VALIDATED`.

## Текущий статус

```text
BATCH_001_TO_007_COMPLETE
FORMAL_GAP_AUDIT_COMPLETE
PRE_EVIDENCESTATE_DRY_RUN_001_COMPLETE
LEAKAGE_AUDIT_001_COMPLETE
COVERAGE_TOPOLOGY_MATRIX_001_COMPLETE
FIRST_CODING_LEDGER_001_FROZEN
MULTI_MODEL_CODING_PILOT_001_COMPLETE
AGREEMENT_REPORT_001_COMPLETE
NEGATIVE_CONTROL_TARGETED_BACKFILL_010_STARTED
DOMAIN_NEUTRAL_ADAPTER_v0_2_REVISED_DRAFT
ATOMIC_RECODE_PACKET_002_READY
NUMERIC_GATE_REVIEW_001_DENIED
NUMERIC_EVIDENCESTATE_BLOCKED
HISTORICAL_SCHEMA_FREEZE_PRESERVED
FORECAST_VALIDATION_NOT_CLAIMED
NOT_VALIDATED
