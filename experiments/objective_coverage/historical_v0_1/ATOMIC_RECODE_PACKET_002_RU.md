# ATOMIC_RECODE_PACKET 002

**Статус:** `READY_FOR_MULTI_MODEL_RUBRIC_STRESS_TEST / V0_2_DRAFT / NOT_OUTCOME_BLIND_VALIDATION`

## 1. Назначение

Этот пакет проверяет исправления `DOMAIN_NEUTRAL_EVIDENCESTATE_ADAPTER v0.2 DRAFT` после `AGREEMENT_REPORT_001`.

Цель — не повторить старый scalar coding, а проверить, уменьшается ли disagreement после:

- атомизации mixed claims;
- явных cutoff dates;
- механического zeroing для cutoff FAIL;
- разделения pressure/stabilizer;
- разделения event strength, coverage scale, evidence quality и confidence;
- отдельного sensor-only режима;
- разделения message content direction и system pressure role.

Этот пакет НЕ является outcome-blind validation: внешняя модель может знать исторический исход из обучения.

## 2. Общие правила

Для каждого atomic item заполнить:

```text
item_id
cutoff_admissibility = PASS | FAIL | CONDITIONAL
pressure_signal = 0 | 1
stabilizer_signal = 0 | 1
event_strength = 0 | 1 | 2 | 3
coverage_scale = LOCAL | MULTI_LOCAL | REGIONAL | NATIONAL | CROSS_BORDER | UNKNOWN
evidence_quality = LOW | MEDIUM | HIGH
confidence = LOW | MEDIUM | HIGH
ambiguity_status = LOW | MEDIUM | HIGH
coding_reason
```

Если `cutoff_admissibility = FAIL`:

```text
pressure_signal = 0
stabilizer_signal = 0
event_strength = 0
```

Если `cutoff_admissibility = CONDITIONAL`, numeric contribution запрещён; `event_strength` оставить 0 до resolution.

## 3. Дополнительные поля для специальных claims

Для information item добавить:

```text
message_content_direction = ESCALATORY | DEESCALATORY | NEUTRAL | NOT_APPLICABLE
system_pressure_role = PRESSURE | STABILIZER | NEUTRAL | UNKNOWN
```

Для sensor-only item добавить:

```text
sensor_status = PRESENT_VALUE_NOT_IMPORTED | VALUE_IMPORTED | NOT_SENSOR
```

Для projection:

```text
claim_mode = OBSERVED | PROJECTED | MIXED_NOT_ALLOWED
```

## 4. Explicit snapshot cutoffs

Россия–Украина:

```text
RU_CUTOFF = 2022-02-23T23:59:59Z
```

Мьянма:

```text
MM_CUTOFF = 2021-06-30T23:59:59Z
```

Никаких формулировок `early 2021` использовать нельзя.

## 5. Atomic items — Россия–Украина

### RU-A002-001 — monitored targeting volume

Publication: 2021-12-23
Cutoff: 2022-02-23T23:59:59Z
Source claim: EUvsDisinfo reported that more than 2,700 pro-Kremlin disinformation examples had been added in 2021 and roughly one-third targeted Ukraine.
Limitation: curated monitoring database; not representative of population exposure or belief.
Special type: INFORMATION

### RU-A002-002 — specific narrative content

Publication: 2021-12-06
Cutoff: 2022-02-23T23:59:59Z
Source claim: a monitored pro-Kremlin narrative portrayed warnings of Russian aggression as fabricated hysteria.
Limitation: existence of a monitored narrative case only; no reach/belief/effect estimate.
Special type: INFORMATION

### RU-A002-003 — resilience/countermeasure statement

Publication: 2022-01-24
Cutoff: 2022-02-23T23:59:59Z
Source claim: EU foreign ministers called for stronger resilience and response capabilities against cyber/hybrid attacks and foreign information manipulation while reaffirming support for Ukraine and diplomatic mechanisms.
Limitation: policy commitment does not prove mitigation effectiveness.
Special type: COUNTERMEASURE

### RU-A002-004 — later retrospective synthesis

Publication: 2022-10-24
Cutoff: 2022-02-23T23:59:59Z
Source claim: later EEAS synthesis reported a sharp increase in some monitored pro-Kremlin narratives during the three months before 24 February 2022.
Limitation: publication occurs after cutoff.
Special type: RETROSPECTIVE

## 6. Atomic items — Мьянма

### MM-A002-001 — observed food/fuel price movement

Publication: 2021-03-16
Cutoff: 2021-06-30T23:59:59Z
Source claim: WFP observed post-coup increases in monitored food and fuel prices, including substantial palm-oil and fuel increases and smaller rice increases in some monitored areas.
Limitation: monitored markets are not every household or market; township variation exists.
Special type: OBSERVED

### MM-A002-002 — observed banking/remittance disruption

Publication: 2021-03-16
Cutoff: 2021-06-30T23:59:59Z
Source claim: WFP reported near paralysis of the banking sector, slowing remittances and widespread cash-availability limits.
Limitation: informal finance channels not fully measured.
Special type: OBSERVED

### MM-A002-003 — contingency food stocks as buffer

Publication: 2021-03-16
Cutoff: 2021-06-30T23:59:59Z
Source claim: WFP reported building contingency food stocks to preserve assistance to more than 360,000 people if cash or market supply became constrained.
Limitation: prepared capacity does not prove delivered coverage or broader stabilization.
Special type: COUNTERMEASURE

### MM-A002-004 — observed coping behavior

Publication: 2021-04-22
Cutoff: 2021-06-30T23:59:59Z
Source claim: WFP described households skipping meals, eating less nutritious food and taking on debt.
Limitation: examples/field observations are not a population denominator.
Special type: OBSERVED

### MM-A002-005 — hunger projection

Publication: 2021-04-22
Cutoff: 2021-06-30T23:59:59Z
Source claim: WFP projected that up to 3.4 million additional people could become hungry within six months.
Limitation: forward estimate, not observed count at publication time.
Special type: PROJECTION

### MM-A002-006 — year-end displacement synthesis

Publication: 2021-12-31
Cutoff: 2021-06-30T23:59:59Z
Source claim: UNHCR year-end reporting recorded large post-coup displacement totals.
Limitation: publication occurs after cutoff.
Special type: RETROSPECTIVE

### MM-A002-007 — dated displacement sensor

Publication: 2021-06-21
Cutoff: 2021-06-30T23:59:59Z
Source claim: UNHCR published a dated displacement overview, establishing contemporaneous geospatial monitoring.
Limitation: establishes sensor/document existence; no validated numeric displacement value imported here.
Special type: SENSOR_ONLY

## 7. Output template

```csv
item_id,cutoff_admissibility,pressure_signal,stabilizer_signal,event_strength,coverage_scale,evidence_quality,confidence,ambiguity_status,message_content_direction,system_pressure_role,sensor_status,claim_mode,coding_reason
RU-A002-001,,,,,,,,,,,,,
RU-A002-002,,,,,,,,,,,,,
RU-A002-003,,,,,,,,,,,,,
RU-A002-004,,,,,,,,,,,,,
MM-A002-001,,,,,,,,,,,,,
MM-A002-002,,,,,,,,,,,,,
MM-A002-003,,,,,,,,,,,,,
MM-A002-004,,,,,,,,,,,,,
MM-A002-005,,,,,,,,,,,,,
MM-A002-006,,,,,,,,,,,,,
MM-A002-007,,,,,,,,,,,,,
```

## 8. Guards

```text
CUTOFF_FAIL => DIRECTIONAL_CONTRIBUTION_ZERO
CUTOFF_FAIL => STRENGTH_CONTRIBUTION_ZERO
CUTOFF_CONDITIONAL => NO_NUMERIC_CONTRIBUTION
SIGNAL_STRENGTH != COVERAGE_SCALE
SIGNAL_STRENGTH != EVIDENCE_QUALITY
COUNTERMEASURE_EXISTS != THREAT_REDUCTION
THREAT_PERCEPTION_SIGNAL != PRESSURE_EVENT
SENSOR_EXISTENCE != EVENT_STRENGTH
PROJECTION != OBSERVED_COUNT
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_DIRECTION
PRESSURE != OUTCOME
STABILIZER != PROVEN_STABILIZATION
```

## 9. Что сравнивать после recode

Минимальные показатели:

```text
cutoff_agreement
pressure_signal_agreement
stabilizer_signal_agreement
event_strength_exact_agreement
event_strength_MAE
coverage_scale_agreement
sensor_rule_violations
projection_rule_violations
cutoff_zeroing_violations
high_ambiguity_count
```

Главный критерий улучшения: disagreement должен концентрироваться в разумных границах strength/scale, а не в базовых правилах cutoff, sensor, projection и pressure-vs-stabilizer.

## 10. Статус

```text
ATOMIC_RECODE_PACKET_002_READY
V0_2_RUBRIC_STRESS_TEST_READY
NUMERIC_EVIDENCESTATE_BLOCKED
TRUE_OUTCOME_BLIND_VALIDATION_NOT_CLAIMED
```
