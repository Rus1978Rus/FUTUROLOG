# NOVEL RESIDUAL DISCRIMINATION SET 001

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_TEST / SYNTHETIC_STRUCTURE / OUTCOME_FREE / NOT_NUMERICALLY_VALIDATED`

## 1. Цель

Проверить следующий уровень `STRUCTURAL_GAP_INFERENCE`: после того как ablation guard научился отличать отсутствие наблюдений от скрытого механизма, проверить различение:

```text
KNOWN_MECHANISM_WITH_UNKNOWN_OUTCOME
!=
STRUCTURAL_RESIDUAL
```

и одновременно убедиться, что система не подавляет настоящий residual, когда наблюдаемость достаточна, известные механизмы проверены, но наблюдаемая конфигурация остаётся несовместимой с текущей моделью.

Тест синтетический. Это намеренно: evaluator знает, где gap встроен конструкцией, а внешний кодировщик не получает target labels.

## 2. Обязательная лестница

```text
1 OBSERVATION_SUFFICIENCY
2 DATA_QUALITY / SOURCE_DEPENDENCE
3 SCALE / ACTOR_AGGREGATION
4 TEMPORAL_LAG
5 KNOWN_PRESSURES
6 KNOWN_STABILIZERS
7 MODEL_EXPECTATION
8 OBSERVED_STATE
9 RESIDUAL_PERSISTENCE
10 ONLY THEN STRUCTURAL_GAP
```

## 3. Guards

```text
OBSERVATION_INCOMPLETE != STRUCTURAL_GAP
UNKNOWN_VARIABLE != STRUCTURAL_GAP
UNKNOWN_OUTCOME != MODEL_RESIDUAL
STABILIZER_EFFECTIVENESS_UNKNOWN != STRUCTURAL_GAP
KNOWN_MECHANISM_WITH_UNKNOWN_OUTCOME != MISSING_MECHANISM
DANGEROUS_STATE != STRUCTURAL_GAP
SURPRISING_EVENT != STRUCTURAL_GAP
TEMPORAL_CHANGE != STRUCTURAL_GAP
MODEL_RESIDUAL != PROOF_OF_HIDDEN_FACTOR
STRUCTURAL_GAP != IDENTIFIED_HIDDEN_CAUSE
```

Если `observation_status=INCOMPLETE`:

```text
structural_gap_status=NOT_ASSESSABLE
observation_recovery_search=YES
hidden_factor_search_allowed=NO
```

Если настоящий residual сохраняется при `SUFFICIENT`:

```text
hidden_factor_search_allowed=YES_SEARCH_TRIGGER_ONLY
hypotheses=NOT_OBSERVED
```

## 4. Novel blind cases

### NR-A7
Наблюдаемость достаточна. Организация публично вводит новый защитный механизм. Механизм реально развёрнут и его использование подтверждено. Через короткое время неблагоприятные события продолжаются примерно на прежнем уровне. Известно, что механизм рассчитан на постепенный эффект и оценочный период ещё не закончился. Других противоречий между моделью и наблюдением нет. Итоговая эффективность пока UNKNOWN.

### NR-K2
Наблюдаемость достаточна. Текущая модель утверждает: при сочетании факторов `P + Q`, если ограничитель `R` активен, переход системы в состояние `Z` в рассматриваемом временном окне не должен происходить. `P`, `Q` и активность `R` независимо подтверждены; временное окно подтверждено; scale и actor aggregation совпадают; источники независимы. Состояние `Z` тем не менее устойчиво наблюдается в нескольких независимых измерениях. Ошибка измерения, lag и известный альтернативный pathway в текущем model inventory не объясняют наблюдение.

### NR-M9
Наблюдаемость достаточна. После периода высокой напряжённости появляется проверяемый costly stabilizer: ресурсы физически отведены, hotline активна, ограничения соблюдаются. Напряжённая риторика остаётся высокой. Текущая модель допускает coexistence риторики и материальной деэскалации. Будущий исход неизвестен.

### NR-T4
Snapshot содержит наблюдаемый скачок результата после изменения политики. Но одновременно изменилась методика измерения результата и часть старых источников была заменена новыми. Нет bridge-calibration между старой и новой методикой. Неизвестно, является ли скачок реальным или measurement discontinuity.

### NR-P6
Наблюдаемость достаточна. Модель ожидает, что после исчезновения входного давления `D` показатель `Y` вернётся к baseline в течение максимум 2 циклов. `D` подтверждённо исчезает; measurement continuity подтверждена; другие известные давления и stabilizers учтены; scale неизменен. После 7 циклов `Y` остаётся устойчиво далеко от baseline без наблюдаемого известного поддерживающего механизма.

### NR-H3
Наблюдаемость достаточна. Два подактора были ошибочно объединены в один actor-level ряд. После разделения оказывается, что один подактор деэскалирует, второй эскалирует; агрегированный ряд создавал кажущееся противоречие «одновременной эскалации и деэскалации». После правильной actor aggregation остаточного противоречия нет.

### NR-C8
Наблюдаемость достаточна. Система совершает дорогостоящее действие, которое текущая модель объясняет одной из двух уже известных целей `G1` или `G2`. Наблюдения совместимы с обеими целями и не позволяют выбрать между ними. Обе цели уже присутствуют в model inventory; ни одна не требует нового механизма. Нужны discriminating observations для выбора между известными объяснениями.

### NR-V5
Наблюдаемость достаточна. Текущая модель содержит два независимо проверенных отношения: `A -> B` и `B -> C` при фиксированных boundary conditions. В данном snapshot A устойчиво наблюдается, B устойчиво НЕ наблюдается, но C устойчиво наблюдается. Boundary conditions подтверждены; временные лаги покрыты; measurement continuity есть; альтернативный известный pathway `A -> C` отсутствует в текущем model inventory. Это повторяется в нескольких независимых наблюдениях.

### NR-R1
Snapshot неполный: известен результат `Z`, но отсутствуют диагностически необходимые наблюдения о состоянии ограничителя `R`, который определяет, должна ли текущая модель допускать `Z`. Источник прямо сообщает, что состояние R не измерялось.

### NR-J6
Наблюдаемость достаточна. После внешнего шока система меняет состояние, но изменение происходит внутри заранее заданного диапазона реакции текущей модели и в ожидаемый временной лаг. Масштаб эффекта высокий, однако не выходит за model envelope. Будущий исход неизвестен.

## 5. Output schema

```csv
case_id,observation_status,structural_gap_status,residual_persistence,observation_recovery_search,hidden_factor_search_allowed,pre_hidden_resolution,known_explanations_exhausted,max_3_hypothesis_classes,max_3_discriminating_evidence_targets,confidence,reason
```

Допустимые значения:

```text
observation_status = SUFFICIENT | INCOMPLETE
structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | NOT_ASSESSABLE
residual_persistence = NONE | RESOLVED_BY_KNOWN_FACTOR | PERSISTS_AFTER_CHECKS | NOT_ASSESSABLE
observation_recovery_search = YES | NO
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY | NO
pre_hidden_resolution = NONE | UNKNOWN_OUTCOME | TEMPORAL_LAG | DATA_QUALITY | OBSERVABILITY | ACTOR_AGGREGATION | KNOWN_STABILIZER_PRESSURE | KNOWN_MULTIPLE_EXPLANATIONS | MODEL_ENVELOPE
known_explanations_exhausted = YES | NO | NOT_ASSESSABLE
confidence = LOW | MEDIUM | HIGH
```

## 6. Evaluator labels — НЕ ПЕРЕДАВАТЬ внешнему кодировщику

```text
NR-A7 = NO_GAP / UNKNOWN_OUTCOME
NR-K2 = OPEN_GAP candidate / PERSISTS_AFTER_CHECKS
NR-M9 = NO_GAP / KNOWN_STABILIZER_PRESSURE
NR-T4 = NOT_ASSESSABLE / DATA_QUALITY
NR-P6 = OPEN_GAP candidate / PERSISTS_AFTER_CHECKS
NR-H3 = NO_GAP / ACTOR_AGGREGATION
NR-C8 = NO_GAP / KNOWN_MULTIPLE_EXPLANATIONS
NR-V5 = OPEN_GAP candidate / PERSISTS_AFTER_CHECKS
NR-R1 = NOT_ASSESSABLE / OBSERVABILITY
NR-J6 = NO_GAP / MODEL_ENVELOPE
```

Для `NR-K2`, `NR-P6`, `NR-V5` правильный смысл не «скрытая причина найдена», а:

```text
CURRENT_MODEL_INCOMPLETE_OR_MISSPECIFIED = SEARCH_HYPOTHESIS
HIDDEN_CAUSE_IDENTIFIED = NO
```

## 7. Основные метрики

```text
TRUE_RESIDUAL_RECALL
FALSE_STRUCTURAL_GAP_RATE
OBSERVATION_INCOMPLETE_FALSE_TRIGGER_RATE
UNKNOWN_OUTCOME_FALSE_TRIGGER_RATE
KNOWN_EXPLANATION_SUPPRESSION_RATE
HIDDEN_CAUSE_OVERCLAIM_RATE
```

Минимальный pilot target:

```text
Ablation/incomplete hidden-factor false trigger = 0
Unknown-outcome hidden-factor false trigger = 0
True residual cases recognized as search-trigger >= 2/3 per coder
No case may claim hidden cause as observed fact
```

## 8. Методологическое основание

Этот тест не утверждает, что residual автоматически означает latent variable. Современная литература по model misspecification и omitted-variable bias показывает, что ошибочная спецификация и пропущенные переменные могут искажать выводы, но evidence обычно недоопределяет единственную причинную структуру. Поэтому residual используется как основание для discriminating search, а не как доказательство конкретной скрытой причины.

## 9. Status

```text
NOVEL_RESIDUAL_DISCRIMINATION_SET_001 = READY
SYNTHETIC_GROUND_TRUTH = EVALUATOR_ONLY
EXTERNAL_BLIND_PACKET = NEXT
NUMERIC_USE = BLOCKED
```
