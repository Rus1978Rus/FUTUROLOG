# RUBRIC v0.3 — FINAL PATCH CANDIDATE

**Статус:** `FINAL_PATCH_CANDIDATE / NOT_NUMERICALLY_VALIDATED / READY_FOR_FALSE_POSITIVE_ANALOGUE_DESIGN`

## 1. Жёсткие guards

```text
CUTOFF_FAIL => pressure_signal=0
CUTOFF_FAIL => stabilizer_signal=0
CUTOFF_FAIL => observed_event_strength=0
CUTOFF_CONDITIONAL => NO_NUMERIC_CONTRIBUTION
PROJECTED => observed_event_strength=0
SENSOR_PRESENT_VALUE_NOT_IMPORTED => observed_event_strength=0
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_ROLE
DEESCALATORY_MESSAGE_CONTENT != STABILIZER_SIGNAL
GEOGRAPHIC_COVERAGE != SYSTEM_SCOPE
SENSOR_DOCUMENT_SCOPE != UNDERLYING_OBSERVATION_COVERAGE
SIGNAL_STRENGTH != EVIDENCE_QUALITY
SIGNAL_STRENGTH != COVERAGE_SCALE
```

## 2. Information manipulation rule

Для evidence, заранее классифицированного как `INFORMATION_MANIPULATION`:

- `message_content_direction` описывает риторическое содержание сообщения;
- `system_pressure_role` описывает функцию evidence в наблюдаемой системе;
- деэскалирующее/успокаивающее содержание НЕ создаёт `stabilizer_signal` автоматически;
- stabilizer допускается только при evidence реального механизма, снижающего давление/уязвимость, а не при риторическом отрицании угрозы;
- existence of narrative не означает reach, belief или behavioral effect.

## 3. Observed event strength anchors

`0` — нет допустимого наблюдаемого directional event contribution; projection/sensor-only/cutoff-failed.

`1 WEAK` — факт/эффект наблюдается, но ограничен, единичен или без evidence существенной функциональной деградации.

`2 SUBSTANTIAL` — наблюдается существенная функциональная деградация/давление, но scope неполон, неоднороден или нет evidence широкого системного отказа.

`3 SEVERE` — есть явное evidence широкого/системного функционального отказа или тяжёлого impairment с достаточным scope support.

Эмоциональная тяжесть claim сама по себе не повышает strength.

## 4. Projected magnitude

`projected_magnitude` — отдельная ось. Она никогда не превращается в observed strength.

До отдельной calibration шкала 1/2/3 считается ordinal-only и не должна входить в общий numeric EvidenceState.

## 5. Geographic coverage и system scope

Вводятся две оси:

`geographic_coverage = LOCAL | MULTI_LOCAL | REGIONAL | NATIONAL | CROSS_BORDER | UNKNOWN`

`system_scope = INDIVIDUAL | GROUP | SECTOR | MULTI_SECTOR | SYSTEM_WIDE | UNKNOWN`

Правила:

- отсутствие явного geographic scope => `UNKNOWN`;
- national institution/sector != NATIONAL geographic coverage автоматически;
- system-level wording может поддерживать `SECTOR`/`SYSTEM_WIDE`, но не географический denominator;
- sensor publication geography не равна coverage underlying observations без extraction.

## 6. Stabilizer qualification

`stabilizer_signal=1` разрешён только если claim описывает существующий механизм/действие/ресурс, потенциально уменьшающий давление или повышающий устойчивость.

```text
STABILIZER_EXISTS != STABILIZER_EFFECTIVE
COUNTERMEASURE_EXISTS != THREAT_REDUCTION
RHETORICAL_REASSURANCE != STABILIZER
```

## 7. Numeric gate

Даже после этого patch numeric EvidenceState остаётся BLOCKED до:

1. false-positive analogues;
2. negative-control completion;
3. calibration of strength anchors on broader evidence sample;
4. coverage/system-scope implementation;
5. leakage recheck;
6. explicit aggregation rule review.

## 8. Status

```text
RUBRIC_V0_3_FINAL_PATCH_CANDIDATE = READY
MECHANICAL_GUARDS = STABLE_IN_FOCUSED_PILOT
SEMANTIC_PATCHES = ADDED
NUMERIC_VALIDATION = NOT_CLAIMED
NEXT = FALSE_POSITIVE_ANALOGUE_DESIGN_001
```
