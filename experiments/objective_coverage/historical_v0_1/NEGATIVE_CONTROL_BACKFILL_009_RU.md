# NEGATIVE_CONTROL_BACKFILL 009

**Статус:** `NEGATIVE_CONTROL_BACKFILL_STARTED / EXISTING_COUNTERSIGNALS_INDEXED / NEW_SOURCE_BACKFILL_PARTIAL / NUMERIC_EVIDENCESTATE_BLOCKED`

## 1. Цель

Закрыть главный blocker из `LEAKAGE_AUDIT_001_RU.md`: риск hindsight/selection bias, когда после знания исхода исследователь легче замечает только evidence, согласующееся с последующим кризисом.

Этот этап НЕ ищет «опровержение истории». Он обязан дать корпусу contemporaneous evidence четырёх типов:

```text
STABILIZER
DE_ESCALATION_SIGNAL
NORMALITY_SIGNAL
ALTERNATIVE_EXPLANATION
```

И отдельно:

```text
FALSE_POSITIVE_ANALOGUE
```

— похожий сигнал, который не обязан вести к тому же исходу.

## 2. Главное правило

```text
COUNTERSIGNAL != PROOF_OF_SAFETY
PRESSURE != PROOF_OF_OUTCOME
```

Negative control нужен не для искусственного уменьшения риска, а для проверки, способен ли FUTUROLOG хранить конкурирующие состояния одновременно.

## 3. Россия–Украина — уже существующие counter-signals

Ниже индексируются уже собранные и cutoff-дисциплинированные элементы. Они НЕ являются новыми фактами; этот документ меняет только их роль в audit pipeline.

### RU-NC-001 — IDP integration / durable-solutions response

Связано с `RU-EV-002-002`.

Тип:

```text
STABILIZER
```

Смысл: при сохраняющемся displacement pressure существовали государственные/международные механизмы интеграции, компенсации, правовой помощи и durable solutions.

Guard:

```text
PROGRAM_EXISTS != PROGRAM_EFFECTIVE
```

### RU-NC-002 — higher-education adaptation

Связано с `RU-EV-002-004`.

Тип:

```text
STABILIZER / INSTITUTIONAL_ADAPTATION
```

Смысл: система образования продолжала получать ресурсы на модернизацию и устойчивость во время COVID.

### RU-NC-003 — community integration signal

Связано с `RU-EV-002-006`.

Тип:

```text
STABILIZER / SOCIAL_COHESION_SIGNAL
```

Ограничение: event-based evidence не является population-level measure.

### RU-NC-004 — health-system adaptation

Индексирует contemporaneous WHO evidence из Batch 006 по infection-prevention adaptation и продолжающейся health-system reform.

Тип:

```text
STABILIZER / ADAPTIVE_CAPACITY
```

### RU-NC-005 — water infrastructure restoration

Индексирует targeted backfill 008 по проектам восстановления/поддержания водоснабжения в conflict-affected communities.

Тип:

```text
STABILIZER / BASIC_SERVICE_RESILIENCE
```

### RU-NC-006 — energy stress has multiple causes

Индексирует contemporaneous IEA evidence 2021.

Тип:

```text
ALTERNATIVE_EXPLANATION
```

Смысл: напряжённость газового рынка в 2021 нельзя кодировать как однофакторный результат действий одного актора; спрос, погода и LNG-market conditions также были частью contemporaneous explanation set.

Guard:

```text
ENERGY_STRESS != SINGLE_CAUSE
```

### RU-NC-007 — survey disagreement / uncertainty

Индексирует KIIS December 2021: часть населения воспринимала угрозу вторжения как реальную, значительная часть — нет.

Тип:

```text
NORMALITY_OR_UNCERTAINTY_SIGNAL
```

Это не доказательство безопасности. Это evidence того, что contemporaneous expectation field не был однородным.

Guard:

```text
SURVEY_EXPECTATION != OBJECTIVE_EVENT_PROBABILITY
```

## 4. Мьянма — уже существующие counter-signals

### MM-NC-001 — partial mobility/logistics stabilization

Связано с `MM-EV-002-006`.

Тип:

```text
DE_ESCALATION_OR_FUNCTIONAL_RECOVERY_SIGNAL
```

World Bank в июльском contemporaneous monitoring отмечал отдельные признаки улучшения mobility и easing logistics disruptions в мае–июне при сохранении слабой общей ситуации.

### MM-NC-002 — contingency food stocks

Связано с `MM-EV-003-004`.

Тип:

```text
STABILIZER / HUMANITARIAN_BUFFER
```

### MM-NC-003 — food-assistance scale-up

Связано с `MM-EV-003-006`.

Тип:

```text
STABILIZER / HUMANITARIAN_RESPONSE
```

### MM-NC-004 — pre-coup education adaptation capacity

Индексирует Batch 004.

Тип:

```text
STABILIZER / PRE_EXISTING_ADAPTIVE_CAPACITY
```

Цифровые материалы, teacher training и COVID-safe reopening support показывают существовавшую способность системы адаптироваться до переворота.

### MM-NC-005 — community/religious support networks

Индексирует Batch 007 / targeted backfill 008.

Тип:

```text
STABILIZER / LOCAL_RESILIENCE_NETWORK
```

Guard:

```text
LOCAL_ASSISTANCE != NATIONAL_STABILIZATION
```

### MM-NC-006 — humanitarian continuity

Индексирует UNICEF multisector continuity evidence из Batch 006.

Тип:

```text
STABILIZER / SERVICE_CONTINUITY
```

### MM-NC-007 — fragmentation of resistance groups

Индексирует Batch 004/008.

Тип:

```text
ALTERNATIVE_STRUCTURE_SIGNAL
```

Смысл: увеличение числа local-defense actors не доказывает единой коалиции или unified command.

Guard:

```text
PROLIFERATION != COORDINATION
COALESCENCE_SIGNAL != COMPLETE_COALITION
```

## 5. Что ещё требуется как настоящий backfill

Существующие stabilizers уменьшают selection bias, но пока недостаточны для честного `observed_noise`.

Нужно дополнительно найти contemporaneous источники по:

### Россия–Украина

```text
RU-NC-GAP-01 diplomatic de-escalation mechanisms / negotiations
RU-NC-GAP-02 regions with pressure but no corresponding escalation
RU-NC-GAP-03 household/basic-needs indicators showing stability or recovery
RU-NC-GAP-04 false-positive military or information-pressure analogues
RU-NC-GAP-05 functioning cross-group/social ties
```

### Мьянма

```text
MM-NC-GAP-01 localities with severe economic pressure but lower conflict escalation
MM-NC-GAP-02 functioning service-delivery pockets
MM-NC-GAP-03 failed or weak group-coalescence attempts
MM-NC-GAP-04 information rumours that did not produce measurable behavioural effect
MM-NC-GAP-05 local ceasefire/dialogue or humanitarian-access mechanisms where contemporaneously documented
```

## 6. Coding rule for negative controls

Каждая запись получает:

```text
control_id
case_id
cutoff
control_type
claim
source_family
supporting_item_ids
original_publication_time
cutoff_admissibility
coverage_segment
counter_to_domain
strength = WEAK | SUBSTANTIAL | SEVERE
limitations
status
```

Negative control НЕ получает отрицательный score только потому, что он stabilizer.

На EvidenceState этапе он участвует в directional/noise coding согласно frozen adapter.

## 7. Guard against manufactured balance

Нельзя искусственно требовать одинаковое количество pressure и stabilizer records.

```text
BALANCED_RECORD_COUNT != BALANCED_REALITY
```

Если contemporaneous evidence действительно асимметричен, корпус обязан сохранить асимметрию. Задача backfill — доказать, что counter-signals искались систематически, а не гарантировать их наличие.

## 8. Результат этапа

```text
EXISTING_COUNTERSIGNALS_REINDEXED: PASS
PRESSURE_ONLY_CORPUS: NO_LONGER_TRUE
SYSTEMATIC_NEW_NEGATIVE_CONTROL_SEARCH: PARTIAL
FALSE_POSITIVE_ANALOGUES: NOT_YET_SUFFICIENT
HONEST_OBSERVED_NOISE_READY: NO
NUMERIC_EVIDENCESTATE_READY: NO
```

## 9. Следующий шаг

До numeric EvidenceState необходимо завершить два параллельных действия:

```text
NEGATIVE_CONTROL_TARGETED_SOURCE_BACKFILL
+
COVERAGE_TOPOLOGY_MATRIX_001
```

После этого:

```text
SECOND_CODING_CHECK
→ NUMERIC_EVIDENCESTATE_GATE_REVIEW
```

## 10. Статус

```text
NEGATIVE_CONTROL_BACKFILL_009_STARTED
EXISTING_STABILIZERS_INDEXED
SELECTION_BIAS_CONTROL_IMPROVED
SYSTEMATIC_COUNTERSIGNAL_SEARCH_PARTIAL
OBSERVED_NOISE_BLOCKED
NUMERIC_EVIDENCESTATE_BLOCKED
SCHEMA_FREEZE_PRESERVED
NOT_VALIDATED
```
