# AGREEMENT_REPORT 002

**Статус:** `ATOMIC_RECODE_MULTI_MODEL_COMPLETE / BASIC_RULES_STABILIZED / RESIDUAL_RUBRIC_AMBIGUITY / NUMERIC_EVIDENCESTATE_STILL_BLOCKED`

## 1. Что сравнивалось

Три внешние машинные кодировки одного и того же `ATOMIC_RECODE_PACKET_002_RU.md`:

- Copilot;
- Claude;
- Grok.

Цель: проверить, уменьшился ли disagreement после патчей v0.2: явных cutoff, атомизации mixed claims, раздельных pressure/stabilizer signals, отдельного sensor-only режима и разделения strength/scale/quality.

Это не outcome-blind validation. Все три модели могли знать исторические исходы из обучения.

## 2. Pairwise agreement по базовым полям

### cutoff_admissibility

```text
Copilot vs Claude: 11/11 = 100%
Copilot vs Grok:   11/11 = 100%
Claude vs Grok:    11/11 = 100%
```

### pressure_signal

```text
Copilot vs Claude: 10/11 = 90.9%
Copilot vs Grok:   10/11 = 90.9%
Claude vs Grok:    11/11 = 100%
```

### stabilizer_signal

```text
Copilot vs Claude: 10/11 = 90.9%
Copilot vs Grok:   10/11 = 90.9%
Claude vs Grok:    11/11 = 100%
```

### event_strength exact

```text
Copilot vs Claude: 8/11 = 72.7%
Copilot vs Grok:   8/11 = 72.7%
Claude vs Grok:    9/11 = 81.8%
```

### coverage_scale exact

```text
Copilot vs Claude: 8/11 = 72.7%
Copilot vs Grok:   10/11 = 90.9%
Claude vs Grok:    9/11 = 81.8%
```

## 3. Главный результат

По сравнению с packet 001 резко стабилизировались именно те правила, которые были критическими:

```text
CUTOFF_ZEROING: STABLE
SENSOR_ONLY_ZERO_STRENGTH: STABLE
RETROSPECTIVE_EXCLUSION: STABLE
PRESSURE_VS_STABILIZER: MOSTLY_STABLE
ATOMIC_CLAIM_HANDLING: IMPROVED
```

Все три модели одинаково исключили post-cutoff строки RU-A002-004 и MM-A002-006 с `0/0/0` directional contribution. Все три сохранили sensor-only MM-A002-007 с event_strength=0. Это означает, что основные leakage guards стали механически понятнее.

## 4. Остаточные disagreements

### RU-A002-002 — narrative denying threat

Copilot:
```text
pressure=0, stabilizer=1, event_strength=2
message=DEESCALATORY, system_role=STABILIZER
```

Claude/Grok:
```text
pressure=1, stabilizer=0, event_strength=1
system_role=PRESSURE
```

Это подтверждает необходимость строгого различия:

```text
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_ROLE
```

Само сообщение по содержанию может быть de-escalatory, но как элемент информационной манипуляции системно выполнять pressure role. Рубрика должна прямо запрещать вывод `DEESCALATORY_MESSAGE => STABILIZER`.

### MM-A002-002 — near paralysis of banking sector

Claude дал strength=3, Copilot/Grok strength=2.

Проблема теперь не directional, а граница `SUBSTANTIAL` vs `SEVERE`. Это допустимый остаточный тип disagreement, но требует операционального threshold для system-wide disruption.

### MM-A002-004 — coping behavior

Copilot/Claude: strength=2; Grok: strength=1. Coverage также расходится между `MULTI_LOCAL` и `UNKNOWN` у Claude.

Нужна явная шкала: наличие нескольких наблюдаемых household examples без denominator не должно автоматически задавать coverage_scale.

### MM-A002-005 — projection

Copilot дал event_strength=0, потому что projected; Claude/Grok дали pressure=1 и strength=2 при `claim_mode=PROJECTED`.

Это новый главный дефект: rubric говорит `PROJECTION != OBSERVED_COUNT`, но не определяет, может ли projection иметь отдельную `projected_strength` при нулевом `observed_event_strength`.

## 5. Результат stress test

```text
CUTOFF_AGREEMENT = 100%
CUTOFF_ZEROING_VIOLATIONS = 0
SENSOR_RULE_VIOLATIONS = 0
RETROSPECTIVE_IMPORT_VIOLATIONS = 0
PRESSURE_STABILIZER_AGREEMENT = HIGH_BUT_NOT_COMPLETE
STRENGTH_DISAGREEMENT = RESIDUAL
COVERAGE_SCALE_DISAGREEMENT = RESIDUAL
PROJECTION_SEMANTICS = NEEDS_PATCH
```

Это существенное улучшение относительно первой рубрики: disagreement теперь в основном сосредоточен в семантических границах `strength`, `coverage_scale`, `projection`, а не в базовой cutoff discipline.

## 6. Патчи для v0.3 candidate

```text
DEESCALATORY_MESSAGE_CONTENT != STABILIZER_SIGNAL
SYSTEM_PRESSURE_ROLE MUST BE CODED INDEPENDENTLY FROM MESSAGE_CONTENT_DIRECTION
OBSERVED_EVENT_STRENGTH != PROJECTED_RISK_MAGNITUDE
PROJECTION_ITEM => observed_event_strength = 0
PROJECTION_ITEM MAY HAVE projected_magnitude = 0|1|2|3
COVERAGE_SCALE REQUIRES EXPLICIT GEOGRAPHIC_OR_POPULATION_SCOPE EVIDENCE
NO_DENOMINATOR => COVERAGE_SCALE CANNOT BE INFERRED FROM EVENT_STRENGTH
SEVERE_REQUIRES_EXPLICIT_SYSTEM_WIDE_OR_OPERATIONALLY_CRITICAL_CRITERION
```

## 7. Gate decision

```text
ATOMIC_RECODE_PACKET_002: PASS_WITH_RESIDUAL_PATCHES
RUBRIC_V0_2_BASIC_GUARDS: PASS
RUBRIC_V0_2_STRENGTH_SCALE_CALIBRATION: PARTIAL
RUBRIC_V0_2_PROJECTION_HANDLING: FAIL_NEEDS_PATCH
READY_FOR_V0_3_CANDIDATE: YES
READY_FOR_NUMERIC_EVIDENCESTATE: NO
```

Следующий шаг:

```text
RUBRIC_V0_3_CANDIDATE
→ SMALL_RECODE_PACKET_003 focused on narrative/projection/strength/scale
→ AGREEMENT_REPORT_003
→ NUMERIC_GATE_REVIEW_002
```
