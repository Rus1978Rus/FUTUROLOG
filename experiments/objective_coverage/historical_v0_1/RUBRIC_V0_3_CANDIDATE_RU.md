# RUBRIC v0.3 CANDIDATE

**Статус:** `CANDIDATE / FOCUSED_REPAIR_AFTER_AGREEMENT_REPORT_002 / NOT_ACTIVE / NOT_CALIBRATED / NOT_VALIDATED`

## 1. Цель

Этот candidate исправляет только дефекты, оставшиеся после `ATOMIC_RECODE_PACKET_002` и `AGREEMENT_REPORT_002`. Он не меняет историческую схему и не открывает numeric EvidenceState.

## 2. Базовые поля

Каждый atomic evidence item кодируется раздельно:

```text
cutoff_admissibility = PASS | FAIL | CONDITIONAL
pressure_signal = 0 | 1
stabilizer_signal = 0 | 1
observed_event_strength = 0 | 1 | 2 | 3
projected_magnitude = 0 | 1 | 2 | 3 | NOT_APPLICABLE
coverage_scale = LOCAL | MULTI_LOCAL | REGIONAL | NATIONAL | CROSS_BORDER | UNKNOWN
evidence_quality = LOW | MEDIUM | HIGH
confidence = LOW | MEDIUM | HIGH
ambiguity_status = LOW | MEDIUM | HIGH
```

## 3. Cutoff rule

```text
FAIL => pressure_signal=0
FAIL => stabilizer_signal=0
FAIL => observed_event_strength=0
FAIL => projected_magnitude=0 or NOT_APPLICABLE
CONDITIONAL => NO_NUMERIC_CONTRIBUTION
```

## 4. Projection rule

Projection и observation больше не используют одно поле силы.

```text
claim_mode = OBSERVED | PROJECTED
```

Если `PROJECTED`:

```text
observed_event_strength = 0
projected_magnitude = 0..3
```

Если `OBSERVED`:

```text
projected_magnitude = NOT_APPLICABLE
```

Guards:

```text
PROJECTION != OBSERVED_COUNT
OBSERVED_EVENT_STRENGTH != PROJECTED_RISK_MAGNITUDE
```

## 5. Information rule

Для information item обязательны два независимых поля:

```text
message_content_direction = ESCALATORY | DEESCALATORY | NEUTRAL | UNKNOWN
system_pressure_role = PRESSURE | STABILIZER | NEUTRAL | UNKNOWN
```

Запрещён shortcut:

```text
DEESCALATORY_MESSAGE_CONTENT => STABILIZER_SIGNAL
```

Сообщение может звучать успокаивающе и одновременно выполнять роль pressure/manipulation signal в системной модели.

## 6. Strength rubric

`observed_event_strength` измеряет только силу наблюдаемого события/изменения, а не качество источника и не охват.

```text
0 NONE_OR_NOT_OBSERVED
1 WEAK_OR_LOCALIZED
2 SUBSTANTIAL_SUSTAINED_OR_MULTI_LOCAL
3 SEVERE_SYSTEM_WIDE_OR_OPERATIONALLY_CRITICAL
```

Для `3` требуется явное основание хотя бы одного типа:

```text
SYSTEM_WIDE
OPERATIONALLY_CRITICAL
NATIONAL_FUNCTION_DISRUPTION
LARGE_SCALE_DIRECT_HUMAN_SECURITY_IMPACT
```

Если формулировка вроде `near paralysis` относится к системе, но scope/denominator неполон, coder может выбрать 2 или REVIEW_REQUIRED; 3 требует явного reason.

## 7. Coverage scale rule

Coverage scale не выводится из strength.

```text
EVENT_STRENGTH != COVERAGE_SCALE
```

Для масштаба нужен явный scope evidence:

- `LOCAL` — одна локация/сообщество;
- `MULTI_LOCAL` — несколько явно названных локальных зон;
- `REGIONAL` — регион/штат/область;
- `NATIONAL` — источник прямо заявляет национальный охват или национальную систему;
- `CROSS_BORDER` — несколько стран/трансграничная институциональная или информационная система;
- `UNKNOWN` — scope нельзя вывести честно.

```text
NO_EXPLICIT_SCOPE => UNKNOWN
NO_DENOMINATOR => DO_NOT_INFER_POPULATION_SCALE
```

## 8. Countermeasure rule

Countermeasure может иметь:

```text
stabilizer_signal = 1
```

но это не означает доказанный эффект.

```text
COUNTERMEASURE_EXISTS != THREAT_REDUCTION
STABILIZER_SIGNAL != PROVEN_STABILIZATION
```

## 9. Sensor rule

```text
sensor_status = PRESENT_VALUE_NOT_IMPORTED | VALUE_IMPORTED | NOT_SENSOR
```

Если sensor-only и значение не импортировано:

```text
pressure_signal = 0
stabilizer_signal = 0
observed_event_strength = 0
```

## 10. Candidate gate

v0.3 может стать `ACTIVE_CANDIDATE` только если focused recode packet 003 показывает:

```text
cutoff agreement = 100%
sensor rule violations = 0
projection rule violations = 0
pressure/stabilizer agreement >= 90%
remaining disagreement concentrated in strength/scale boundary only
```

Numeric EvidenceState остаётся заблокирован до отдельного gate review.
