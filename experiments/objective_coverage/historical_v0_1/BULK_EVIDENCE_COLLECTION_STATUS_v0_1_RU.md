# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `ATOMIC_RECODE_002_COMPLETE / AGREEMENT_REPORT_002_COMPLETE / RUBRIC_V0_3_CANDIDATE_CREATED / FOCUSED_RECODE_003_READY / NOT_READY_FOR_NUMERIC_EVIDENCESTATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` завершены широкие intake-пакеты Batch 001–007, formal gap audit, targeted backfill, non-numeric dry run, leakage audit, negative-control work, coverage topology, first/second coding checks и numeric gate review 001.

Дополнительно завершены:

- multi-model external coding pilot 001 (Copilot, Grok, Claude);
- `AGREEMENT_REPORT_001_RU.md`;
- targeted negative-control backfill 010;
- revised draft `DOMAIN_NEUTRAL_EVIDENCESTATE_ADAPTER_v0_2_DRAFT_RU.md`;
- `ATOMIC_RECODE_PACKET_002_RU.md`;
- multi-model atomic recode 002 (Copilot, Claude, Grok);
- `AGREEMENT_REPORT_002_RU.md`;
- `RUBRIC_V0_3_CANDIDATE_RU.md`;
- `FOCUSED_RECODE_PACKET_003_RU.md`.

## Результат atomic recode 002

После атомизации claims и явных cutoff базовые правила резко стабилизировались.

Pairwise agreement:

```text
CUTOFF:
Copilot-Claude 11/11
Copilot-Grok   11/11
Claude-Grok    11/11

PRESSURE_SIGNAL:
Copilot-Claude 10/11
Copilot-Grok   10/11
Claude-Grok    11/11

STABILIZER_SIGNAL:
Copilot-Claude 10/11
Copilot-Grok   10/11
Claude-Grok    11/11

EVENT_STRENGTH exact:
Copilot-Claude 8/11
Copilot-Grok   8/11
Claude-Grok    9/11
```

Все три модели:

```text
- одинаково выполнили cutoff FAIL zeroing;
- не импортировали retrospective rows;
- сохранили sensor-only item с event_strength=0;
- в основном одинаково разделили pressure и stabilizer.
```

Значит disagreement теперь концентрируется не в leakage discipline, а в более узких семантических границах.

## Остаточные дефекты

1. `DEESCALATORY_MESSAGE_CONTENT` иногда ошибочно превращается в `STABILIZER_SIGNAL`.
2. Граница `SUBSTANTIAL` vs `SEVERE` остаётся недостаточно операциональной.
3. `coverage_scale` иногда выводится из интенсивности события без явного scope/denominator.
4. Projection не отделён достаточно жёстко от observed event strength.

## Rubric v0.3 candidate

Создан `RUBRIC_V0_3_CANDIDATE_RU.md`.

Ключевые патчи:

```text
DEESCALATORY_MESSAGE_CONTENT != STABILIZER_SIGNAL
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_ROLE
OBSERVED_EVENT_STRENGTH != PROJECTED_RISK_MAGNITUDE
PROJECTED => observed_event_strength = 0
PROJECTED => projected_magnitude = 0..3
NO_EXPLICIT_SCOPE => coverage_scale = UNKNOWN
NO_DENOMINATOR => DO_NOT_INFER_POPULATION_SCALE
SEVERE_REQUIRES_EXPLICIT_SYSTEM_WIDE_OR_OPERATIONALLY_CRITICAL_CRITERION
```

## Focused recode packet 003

Создан маленький `FOCUSED_RECODE_PACKET_003_RU.md` только по остаточным спорным классам:

- de-escalatory narrative vs system pressure role;
- countermeasure;
- banking disruption strength;
- household coping scale;
- projection magnitude;
- sensor-only rule.

Цель — не повторять большой тест, а проверить, исчезли ли конкретные известные ambiguity clusters.

## Numeric gate

Числовой EvidenceState остаётся заблокирован.

Причины:

```text
RUBRIC_V0_3_NOT_YET_STRESS_TESTED
CHANNEL_AGGREGATION_NOT_CALIBRATED
NEGATIVE_CONTROL_FALSE_POSITIVE_ANALOGUES_INCOMPLETE
TRUE_OUTCOME_BLIND_VALIDATION_NOT_PROVEN
OBSERVED_NOISE_BLOCKED
```

## Следующий разрешённый порядок

```text
FOCUSED_RECODE_PACKET_003 -> COPILOT + CLAUDE + GROK
→ AGREEMENT_REPORT_003
→ RUBRIC_V0_3_GATE_DECISION
→ FALSE_POSITIVE_ANALOGUES_BACKFILL
→ NUMERIC_EVIDENCESTATE_GATE_REVIEW_002
```

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
ATOMIC_RECODE_PACKET_002_COMPLETE
AGREEMENT_REPORT_002_COMPLETE
RUBRIC_V0_3_CANDIDATE_CREATED
FOCUSED_RECODE_PACKET_003_READY
NEGATIVE_CONTROL_TARGETED_BACKFILL_010_STARTED
NUMERIC_GATE_REVIEW_001_DENIED
NUMERIC_EVIDENCESTATE_BLOCKED
HISTORICAL_SCHEMA_FREEZE_PRESERVED
FORECAST_VALIDATION_NOT_CLAIMED
NOT_VALIDATED
