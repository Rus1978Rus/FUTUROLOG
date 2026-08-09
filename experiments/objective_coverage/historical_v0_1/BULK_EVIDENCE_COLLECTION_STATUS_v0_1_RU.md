# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `COVERAGE_TOPOLOGY_MATRIX_001_COMPLETE / NEGATIVE_CONTROL_BACKFILL_009_PARTIAL / SECOND_CODING_CHECK_READY / NOT_READY_FOR_NUMERIC_EVIDENCESTATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` завершены широкие intake-пакеты Batch 001–007 для двух пилотных кейсов и выполнен `FORMAL_GAP_AUDIT_v0_1_RU.md`.

Затем выполнены:

- targeted backfill 008 для Россия–Украина и Мьянмы;
- `PRE_EVIDENCESTATE_DRY_RUN_001_RU.md`;
- `LEAKAGE_AUDIT_001_RU.md`;
- начало `NEGATIVE_CONTROL_BACKFILL_009_RU.md` с переиндексацией уже существующих stabilizers/counter-signals;
- `COVERAGE_TOPOLOGY_MATRIX_001_RU.md`;
- machine-readable `coverage_topology_matrix_001.csv`.

## Coverage topology — главный результат

Теперь корпус хранит не только факт наличия evidence, но и структуру наблюдаемости.

Для каждого крупного сегмента зафиксировано качественное состояние:

```text
STRONG
MODERATE
WEAK
SENSOR_ONLY
RETROSPECTIVE_ONLY
GAP
DEGRADED_BY_ACCESS
```

Это не score состояния страны. Это описание того, насколько хорошо FUTUROLOG способен видеть соответствующую часть реальности.

Ключевые guards:

```text
OBSERVABILITY != PREVALENCE
COLLECTABILITY != PREVALENCE
SAME_SCHEMA != SAME_OBSERVABILITY
SAME_COVERAGE_PERCENT != SAME_COVERAGE_TOPOLOGY
CROSS_CASE_SCORE_DIFFERENCE != TRUE_STATE_DIFFERENCE
```

## Россия–Украина — topology summary

Сильнее наблюдаются:

- formal institutions;
- military/security public signals;
- macro/energy/resource evidence;
- polling/institutional expectations;
- health/education formal systems;
- public information-manipulation narratives;
- international assistance/sanctions.

Слабее наблюдаются:

- household normality;
- food/fuel affordability at household level;
- closed messengers/private groups;
- small informal groups;
- local intergroup relations;
- real prevalence and behavioral effect of narratives.

## Мьянма — topology summary

Сильнее наблюдаются:

- humanitarian consequences;
- local food/fuel prices;
- displacement sensors;
- professional-group mobilization;
- macro/banking/logistics disruptions;
- internet-access degradation;
- visible conflict events.

Слабее наблюдаются:

- remote/inaccessible regions;
- informal economy;
- content-level information operations/rumours;
- exact scale/command of small armed groups;
- household normality;
- direct water-security coverage;
- processes hidden after internet/media repression.

## Cross-case comparability

Одинаковая frozen schema применяется к обоим кейсам, но topology сильно различается.

Поэтому будущий numeric EvidenceState обязан хранить `coverage topology annotation`, а не один агрегированный coverage percent.

## Negative controls — состояние

`NEGATIVE_CONTROL_BACKFILL_009` остаётся частично незавершённым.

Уже переиндексированы существующие:

- stabilizers;
- de-escalation / functional-recovery signals;
- normality / uncertainty signals;
- alternative explanations;
- fragmentation signals, не позволяющие автоматически объявить coalition/unified command.

Но ещё требуются дополнительные targeted false-positive analogues и systematic counter-signal search.

```text
BALANCED_RECORD_COUNT != BALANCED_REALITY
COUNTERSIGNAL != PROOF_OF_SAFETY
PRESSURE != PROOF_OF_OUTCOME
```

## Gate после topology matrix

```text
LEAKAGE_AUDIT: PASS_WITH_RESIDUAL_SELECTION_RISK
NEGATIVE_CONTROL_EXISTING_INDEX: PASS
SYSTEMATIC_NEGATIVE_CONTROL_BACKFILL: PARTIAL
COVERAGE_TOPOLOGY_MATRIX: PASS
BLIND_SPOTS_EXPLICIT: PASS
CROSS_CASE_OBSERVABILITY_ASYMMETRY: PASS
READY_FOR_SECOND_CODING_CHECK: YES
READY_FOR_NUMERIC_EVIDENCESTATE: NO
```

## Следующий разрешённый этап

```text
SECOND_CODING_CHECK
→ NEGATIVE_CONTROL_TARGETED_SOURCE_BACKFILL (если disagreement/gap требует)
→ NUMERIC_EVIDENCESTATE_GATE_REVIEW
```

`SECOND_CODING_CHECK` должен повторно закодировать подмножество evidence/snapshots без просмотра первой кодировки и измерить устойчивость интерпретации.

Числовой EvidenceState остаётся заблокирован.

## Статус

```text
BATCH_001_TO_007_COMPLETE
FORMAL_GAP_AUDIT_COMPLETE
TARGETED_BACKFILL_008_PARTIAL_PASS
PRE_EVIDENCESTATE_DRY_RUN_001_COMPLETE
LEAKAGE_AUDIT_001_COMPLETE
NEGATIVE_CONTROL_BACKFILL_009_PARTIAL
COVERAGE_TOPOLOGY_MATRIX_001_COMPLETE
SECOND_CODING_CHECK_READY
NUMERIC_EVIDENCESTATE_BLOCKED
SCHEMA_FREEZE_PRESERVED
FORECAST_VALIDATION_NOT_CLAIMED
NOT_VALIDATED
```
