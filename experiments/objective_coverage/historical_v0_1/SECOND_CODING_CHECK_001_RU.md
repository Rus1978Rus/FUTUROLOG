# SECOND_CODING_CHECK 001

**Статус:** `REPEAT_CODING_COMPLETE / TRUE_INDEPENDENT_CODER_NOT_YET_AVAILABLE / CROSS_CASE_ADAPTER_MISMATCH_FOUND / NUMERIC_EVIDENCESTATE_BLOCKED`

## 1. Цель

Проверить, насколько кодирование evidence зависит от интерпретатора, до первого числового EvidenceState.

Frozen adapter v0.1 требует как минимум подмножество snapshot закодировать второй попыткой независимо от первого результата. Также он прямо предупреждает:

```text
CODER_AGREEMENT != WORLD_TRUTH
```

и высокий disagreement означает слабость adapter/rubric.

## 2. Важное ограничение этого прогона

Этот прогон выполнен тем же AI-ассистентом, который участвовал в построении корпуса. Поэтому он НЕ является настоящим независимым second coder.

Правильная классификация:

```text
REPEAT_CODING / CONSISTENCY_CHECK
!=
INDEPENDENT_CODER_VALIDATION
```

Нельзя объявлять agreement независимым только потому, что кодирование выполнено повторно.

## 3. Что можно проверить честно сейчас

Для выбранного подмножества можно повторно кодировать, глядя только на сами evidence claims и frozen rubric:

```text
cutoff_admissibility
direction = +1 | 0 | -1
strength = 1 | 2 | 3
ambiguity_status
```

Но нельзя честно вычислить межкодировочное agreement по `class_severity`, потому что в intake-файлах нет отдельного сохранённого первого `coded_value`/`coding_reason` для каждого item.

Следовательно:

```text
NO_STORED_FIRST_CODE
→ NO_TRUE_PAIRWISE_AGREEMENT_METRIC
```

## 4. Выборка для repeat coding

Выбраны элементы с разными ролями, а не только pressure:

### Россия–Украина

- `RU-EV-007-001` — curated disinformation targeting signal;
- `RU-EV-007-003` — specific narrative case;
- `RU-EV-007-005` — information-security policy response / stabilizer;
- `RU-EV-007-006` — retrospective synthesis, quarantined.

### Мьянма

- `MM-EV-003-001` — food/fuel price pressure;
- `MM-EV-003-003` — banking/remittance/cash constraints;
- `MM-EV-003-004` — contingency food assistance / stabilizer;
- `MM-EV-003-005` — hunger projection + field observations;
- `MM-EV-003-007` — year-end displacement total with cutoff caution;
- `MM-EV-003-008` — displacement sensor without imported numeric value.

## 5. Repeat coding result

| item | cutoff admissibility | repeat direction | repeat strength | ambiguity | note |
|---|---|---:|---:|---|---|
| RU-EV-007-001 | admissible after 2021-12-23 | +1 | 2 | MEDIUM | strong evidence of monitored targeting inside a curated dataset; not population prevalence |
| RU-EV-007-003 | admissible after 2021-12-06 | +1 | 1 | MEDIUM | proves narrative existence, not reach/effect |
| RU-EV-007-005 | admissible after 2022-01-24 | -1 | 1 | MEDIUM | institutional countermeasure exists; effectiveness unknown |
| RU-EV-007-006 | retrospective-only for pre-invasion snapshots | 0 | 0/EXCLUDED | LOW | cannot participate in pre-24.02.2022 state |
| MM-EV-003-001 | admissible after 2021-03-16 | +1 | 2 | LOW-MEDIUM | observed price pressure across monitored markets; not household prevalence |
| MM-EV-003-003 | admissible after 2021-03-16 | +1 | 2 | MEDIUM | strong functional-access pressure, incomplete informal-finance picture |
| MM-EV-003-004 | admissible after 2021-03-16 | -1 | 1 | MEDIUM | buffer capacity, not proof of needs being met |
| MM-EV-003-005 | admissible after 2021-04-22 | +1 | 2 | HIGH | mixes projection with field observations; projection cannot be coded as observed prevalence |
| MM-EV-003-007 | admissible only at year-end | 0 | 0/EXCLUDED for early cutoffs | LOW | valid year-end synthesis, invalid early-2021 input |
| MM-EV-003-008 | admissible after 2021-06-21 as sensor | 0 | 0/UNKNOWN_NUMERIC | LOW | establishes sensor existence only |

## 6. Consistency findings

### PASS

Повторное кодирование сохраняет ключевые distinctions корпуса:

```text
PRESSURE != OUTCOME
STABILIZER != PROVEN_STABILIZATION
NARRATIVE_EXISTS != POPULATION_BELIEF
PROJECTION != OBSERVED_COUNT
SENSOR_EXISTS != NUMERIC_VALUE_VALIDATED
RETROSPECTIVE_KNOWLEDGE != CUTOFF_KNOWLEDGE
```

`pressure_or_stabilizer` labels выбранных WORKING items в целом согласуются с повторным direction coding.

### PARTIAL / REVIEW_REQUIRED

Наиболее интерпретационно чувствительные элементы:

1. информационные narratives — легко завысить strength, если спутать existence/monitoring intensity с population effect;
2. policy/humanitarian stabilizers — легко завысить counter-strength, если спутать program existence с effectiveness;
3. forecast/projection evidence — легко превратить прогноз источника в наблюдавшийся факт;
4. mixed claims — один item может сочетать факт, прогноз и интерпретацию, что требует decomposition.

## 7. Критическая находка: adapter v0.1 не симметричен двум кейсам

Frozen `EVIDENCE_STATE_ADAPTER_SPEC v0.1` задаёт три primary evidence classes:

```text
MILITARY_BUILDUP
DIPLOMATIC_COERCION_OR_WARNING
ECONOMIC_ENERGY_STRESS
```

Это естественно для Россия–Украина, но не является нейтральной общей схемой для Мьянмы. Мьянманский корпус содержит критические классы вроде:

```text
COUP_AND_REPRESSION
SOCIAL_GROUP_MOBILIZATION
STATE_SERVICE_BREAKDOWN
DISPLACEMENT
LOCAL_ARMED_GROUP_FORMATION
FOOD_FINANCIAL_ACCESS_STRESS
OBSERVATION_DEGRADATION
```

которые v0.1 primary denominator не представляет напрямую.

Следовательно:

```text
SAME_HISTORICAL_SCHEMA
!=
SAME_EVIDENCESTATE_ADAPTER_FIT
```

и:

```text
RUSSIA_SPECIFIC_PRIMARY_CLASSES
→ INVALID_CROSS_CASE_NUMERIC_COMPARISON
```

Это не требует менять уже замороженную historical evidence schema. Но числовой adapter для cross-case pilot должен получить новую явно версионированную спецификацию (`v0.2` или отдельный domain-neutral adapter), а не тихое изменение v0.1.

## 8. Вторая критическая находка: first-code provenance недостаточен для agreement metric

Frozen adapter требует хранить:

```text
coded_value
coding_reason
supporting_item_ids
coder_version
```

В текущих intake CSV есть claim metadata, quality/confidence и limitations, но нет отдельного первого ordinal-code ledger для выбранных items.

Поэтому нельзя честно посчитать:

- exact agreement;
- weighted agreement;
- disagreement rate по severity;
- coder confusion matrix.

Нужно сначала создать immutable `FIRST_CODING_LEDGER_001`, затем независимый coder получает только source packet + rubric, но не первый ledger.

## 9. Решение по second-coding gate

```text
REPEAT_CODING_CONSISTENCY: PASS_WITH_LIMITATIONS
TRUE_INDEPENDENT_SECOND_CODING: NOT_DONE
FIRST_CODE_LEDGER_AVAILABLE: NO
CROSS_CASE_ADAPTER_FIT: FAIL
HISTORICAL_SCHEMA_CHANGE_REQUIRED: NO
ADAPTER_REVISION_REQUIRED_BEFORE_CROSS_CASE_NUMERIC_RUN: YES
READY_FOR_NUMERIC_EVIDENCESTATE: NO
```

## 10. Следующий порядок

```text
FIRST_CODING_LEDGER_001
→ DOMAIN_NEUTRAL_EVIDENCESTATE_ADAPTER_v0_2_DRAFT
→ BLIND_SECOND_CODER_PACKET_001
→ TRUE_SECOND_CODING
→ AGREEMENT_REPORT_001
→ NUMERIC_EVIDENCESTATE_GATE_REVIEW
```

Negative-control targeted source backfill может продолжаться параллельно, но не должен блокировать исправление adapter-fit.

## 11. Новые guards

```text
REPEAT_CODING != INDEPENDENT_CODING
CONSISTENCY != VALIDATION
NO_STORED_FIRST_CODE != MEASURABLE_AGREEMENT
SAME_SCHEMA != SAME_ADAPTER_FIT
DOMAIN_SPECIFIC_DENOMINATOR != CROSS_DOMAIN_COMPARABILITY
```

## 12. Статус

```text
SECOND_CODING_CHECK_001_COMPLETE
PASS_WITH_LIMITATIONS
TRUE_INDEPENDENT_CODER_NOT_YET_AVAILABLE
FIRST_CODE_LEDGER_REQUIRED
CROSS_CASE_ADAPTER_MISMATCH_FOUND
NUMERIC_EVIDENCESTATE_BLOCKED
HISTORICAL_SCHEMA_FREEZE_PRESERVED
NOT_VALIDATED
```
