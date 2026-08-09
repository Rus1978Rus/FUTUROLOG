# FOCUSED_RECODE_PACKET 003

**Статус:** `READY_FOR_MULTI_MODEL_FOCUSED_STRESS_TEST / RUBRIC_V0_3_CANDIDATE / NOT_OUTCOME_BLIND_VALIDATION`

## 1. Цель

Проверить только четыре остаточных дефекта после packet 002:

1. de-escalatory message content vs system pressure role;
2. observed strength 2 vs 3;
3. coverage scale without explicit denominator;
4. projection magnitude vs observed event strength.

## 2. Поля

```text
item_id
cutoff_admissibility = PASS | FAIL | CONDITIONAL
pressure_signal = 0 | 1
stabilizer_signal = 0 | 1
observed_event_strength = 0 | 1 | 2 | 3
projected_magnitude = 0 | 1 | 2 | 3 | NOT_APPLICABLE
coverage_scale = LOCAL | MULTI_LOCAL | REGIONAL | NATIONAL | CROSS_BORDER | UNKNOWN
message_content_direction = ESCALATORY | DEESCALATORY | NEUTRAL | UNKNOWN | NOT_APPLICABLE
system_pressure_role = PRESSURE | STABILIZER | NEUTRAL | UNKNOWN
sensor_status = PRESENT_VALUE_NOT_IMPORTED | VALUE_IMPORTED | NOT_SENSOR
claim_mode = OBSERVED | PROJECTED
ambiguity_status = LOW | MEDIUM | HIGH
coding_reason
```

## 3. Guards

```text
CUTOFF_FAIL => pressure_signal=0, stabilizer_signal=0, observed_event_strength=0
PROJECTED => observed_event_strength=0
OBSERVED => projected_magnitude=NOT_APPLICABLE
DEESCALATORY_MESSAGE_CONTENT != STABILIZER_SIGNAL
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_ROLE
EVENT_STRENGTH != COVERAGE_SCALE
NO_EXPLICIT_SCOPE => coverage_scale=UNKNOWN
NO_DENOMINATOR => DO_NOT_INFER_POPULATION_SCALE
SENSOR_PRESENT_VALUE_NOT_IMPORTED => observed_event_strength=0
```

## 4. Items

### F003-001 — de-escalatory narrative as information pressure

Publication: 2021-12-06
Cutoff: 2022-02-23T23:59:59Z
Claim: a monitored pro-Kremlin narrative portrayed warnings of Russian aggression as fabricated hysteria.
Context supplied for coding: this item is collected in an information-manipulation monitoring corpus; existence of the narrative is verified, but reach/belief/effect are not measured.
Special type: INFORMATION / OBSERVED

### F003-002 — countermeasure statement

Publication: 2022-01-24
Cutoff: 2022-02-23T23:59:59Z
Claim: EU foreign ministers called for stronger resilience and response capabilities against cyber/hybrid attacks and foreign information manipulation while reaffirming support for Ukraine and diplomatic mechanisms.
Limitation: policy commitment exists; mitigation effectiveness is not demonstrated.
Special type: COUNTERMEASURE / OBSERVED

### F003-003 — banking disruption

Publication: 2021-03-16
Cutoff: 2021-06-30T23:59:59Z
Claim: WFP reported near paralysis of the banking sector, slowing remittances and widespread cash-availability limits.
Limitation: informal finance channels are not fully measured.
Scope statement: the claim explicitly refers to the banking sector as a system, but does not provide a population denominator.
Special type: OBSERVED

### F003-004 — household coping observations

Publication: 2021-04-22
Cutoff: 2021-06-30T23:59:59Z
Claim: WFP described households skipping meals, eating less nutritious food and taking on debt.
Limitation: field observations/examples are provided; no explicit national or regional denominator is supplied in this atomic claim.
Special type: OBSERVED

### F003-005 — hunger projection

Publication: 2021-04-22
Cutoff: 2021-06-30T23:59:59Z
Claim: WFP projected that up to 3.4 million additional people could become hungry within six months.
Limitation: forward estimate, not observed count at publication time.
Special type: PROJECTED

### F003-006 — displacement sensor without imported value

Publication: 2021-06-21
Cutoff: 2021-06-30T23:59:59Z
Claim: UNHCR published a dated displacement overview, establishing contemporaneous geospatial monitoring.
Limitation: no validated displacement value is imported in this item.
Special type: SENSOR_ONLY / OBSERVED

## 5. Output template

```csv
item_id,cutoff_admissibility,pressure_signal,stabilizer_signal,observed_event_strength,projected_magnitude,coverage_scale,message_content_direction,system_pressure_role,sensor_status,claim_mode,ambiguity_status,coding_reason
F003-001,,,,,,,,,,,,
F003-002,,,,,,,,,,,,
F003-003,,,,,,,,,,,,
F003-004,,,,,,,,,,,,
F003-005,,,,,,,,,,,,
F003-006,,,,,,,,,,,,
```

## 6. Gate criteria

```text
cutoff_agreement = 100%
sensor_rule_violations = 0
projection_rule_violations = 0
pressure/stabilizer agreement >= 90%
message/system-role confusion = 0
remaining disagreement may exist only at strength boundary if reason is explicit
```

## 7. Status

```text
FOCUSED_RECODE_PACKET_003_READY
RUBRIC_V0_3_CANDIDATE_UNDER_TEST
NUMERIC_EVIDENCESTATE_BLOCKED
TRUE_OUTCOME_BLIND_VALIDATION_NOT_CLAIMED
```
