# AGREEMENT_REPORT_001

**Статус:** `MULTI_MODEL_PILOT_COMPLETE / MACHINE_CODERS_NOT_OUTCOME_BLIND / RUBRIC_PATCH_REQUIRED / NUMERIC_EVIDENCESTATE_STILL_BLOCKED`

## 1. Что сравнивалось

Замороженный `FIRST_CODING_LEDGER_001.csv` механически сравнен с тремя внешними машинными кодировками, полученными пользователем из отдельных систем: Copilot, Grok и Claude.

Важно: это независимость по системе/контексту, но не доказанная outcome-blindness. Современные модели могли знать исторический исход из обучения. Поэтому результаты годятся для проверки устойчивости рубрики и обнаружения неоднозначностей, но не закрывают требование настоящего outcome-blind human/temporal coder.

## 2. Метрики относительно FIRST_CODING_LEDGER_001

| coder | exact_direction_agreement | exact_strength_agreement | mean_absolute_strength_difference | cutoff_admissibility_agreement* |
|---|---:|---:|---:|---:|
| Copilot | 6/10 = 60% | 5/10 = 50% | 0.9 | 9/10 = 90% |
| Grok | 8/10 = 80% | 10/10 = 100% | 0.0 | 10/10 = 100% |
| Claude | 10/10 = 100% | 7/10 = 70% | 0.3 | 8/10 = 80% |

`*` Cutoff comparison uses the frozen ledger cutoff scopes as the expected admissibility interpretation: contemporaneous items PASS; explicitly retrospective/excluded items FAIL. Where an external coder returned CONDITIONAL against a frozen post-publication scope, this counts as disagreement.

## 3. Где расходятся кодировщики

### RU-EV-007-003

First: `+1 / 1`.

Copilot: `-1 / 2`; Grok: `+1 / 1`; Claude: `+1 / 1`.

Проблема: один и тот же информационный нарратив можно ошибочно прочитать как "стабилизирующий восприятие" вместо давления/манипуляции. Рубрика должна явно различать `MESSAGE_CONTENT_DIRECTION` и `SYSTEM_PRESSURE_DIRECTION`.

### RU-EV-007-005

First: `-1 / 1`.

Copilot: `+1 / 1`; Grok: `0 / 1`; Claude: `-1 / 1` с HIGH ambiguity.

Это главный dual-use item: заявление о защите одновременно может быть (a) стабилизатором/контрмерой и (b) индикатором того, что угроза воспринимается серьёзно. Один scalar direction теряет это различие.

### RU-EV-007-006

First: `0 / 0`, excluded by cutoff.

Copilot сохранил `+1 / 3` при `FAIL`; Grok и Claude дали `0 / 0, FAIL`.

Проблема: рубрика должна явно требовать `cutoff_admissibility = FAIL => coded_direction = 0 AND coded_strength = 0` для состояния на данном cutoff. Иначе запрещённое знание продолжает неявно влиять на направление/силу.

### MM-EV-003-003

First: `+1 / 2`.

Copilot/Grok: `+1 / 2`; Claude: `+1 / 3`.

Проблема: не определена граница между SUBSTANTIAL и SEVERE для системного, но неполно наблюдаемого нарушения.

### MM-EV-003-004

First: `-1 / 1`.

Copilot: `-1 / 1`; Grok: `0 / 1`; Claude: `-1 / 1` с HIGH ambiguity.

Проблема аналогична RU-EV-007-005: подготовка буфера может быть стабилизатором и одновременно индикатором ожидаемого ухудшения.

### MM-EV-003-005

First: `+1 / 2`.

Copilot: `+1 / 3`; Grok: `+1 / 2`; Claude: `+1 / 1` и CONDITIONAL cutoff.

Проблема: item смешивает observed coping behavior и projection. Нужна декомпозиция claim на атомарные evidence units перед strength coding.

### MM-EV-003-007

First: `0 / 0`, excluded.

Copilot сохранил `+1 / 3` при `FAIL`; Grok и Claude: `0 / 0, FAIL`.

Повторяется дефект RU-EV-007-006: FAIL должен механически обнулять directional contribution.

### MM-EV-003-008

First: `0 / 0`.

Copilot: `0 / 1, CONDITIONAL`; Grok: `0 / 0, PASS`; Claude: `0 / 0, CONDITIONAL`.

Проблема: sensor existence не является directional strength. Для sensor-only evidence сила должна кодироваться отдельно от event-pressure strength либо оставаться 0.

## 4. Дефекты blind packet, подтверждённые внешним прогоном

1. Глобальные cutoff dates недостаточно операциональны для всей серии; формулировка `early 2021` допускает разные трактовки.
2. В некоторых строках сам факт указания `Target cutoff` только для проблемных элементов может служить подсказкой ожидаемого exclusion.
3. `coded_strength` смешивает интенсивность сигнала, масштаб/охват и качество наблюдения.
4. Один `coded_direction` плохо работает для dual-use evidence: countermeasure может одновременно быть stabilizer и threat-perception signal.
5. Смешанные claims (observed + projected) нужно атомизировать до кодирования.
6. Правило обнуления cutoff-failed evidence не было сформулировано механически.

## 5. Обязательные патчи rubric v0.2

```text
CUTOFF_FAIL => DIRECTIONAL_CONTRIBUTION_ZERO
CUTOFF_FAIL => STRENGTH_CONTRIBUTION_ZERO
SIGNAL_STRENGTH != COVERAGE_SCALE
SIGNAL_STRENGTH != EVIDENCE_QUALITY
COUNTERMEASURE_EXISTS != THREAT_REDUCTION
THREAT_PERCEPTION_SIGNAL != PRESSURE_EVENT
SENSOR_EXISTENCE != EVENT_STRENGTH
MIXED_CLAIM => ATOMIZE_BEFORE_CODING
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_DIRECTION
```

Для dual-use evidence рекомендуется не заставлять кодировщика выбирать один знак. Минимальный v0.2 должен разрешить отдельные поля `pressure_signal` и `stabilizer_signal` либо отдельные атомарные evidence rows.

## 6. Решение gate

```text
MULTI_MODEL_SECOND_CODING_PILOT = COMPLETE
RUBRIC_STABILITY = PARTIAL
DIRECTION_AGREEMENT = VARIABLE
STRENGTH_AGREEMENT = VARIABLE
CUTOFF_RULE_NEEDS_PATCH = YES
TRUE_OUTCOME_BLIND_SECOND_CODER = NOT_PROVEN
NUMERIC_EVIDENCESTATE = BLOCKED
NEXT = RUBRIC_V0_2_PATCH_AND_RECODE
```

Мы не выбираем кодировщика, который "лучше совпал" с first ledger, и не усредняем три ответа в новый truth label. Расхождения используются как диагностический материал для исправления рубрики.
