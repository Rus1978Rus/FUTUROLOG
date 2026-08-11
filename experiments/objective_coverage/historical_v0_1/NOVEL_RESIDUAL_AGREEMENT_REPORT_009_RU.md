# NOVEL_RESIDUAL AGREEMENT REPORT 009

**Статус:** `THREE_MODEL_NOVEL_RESIDUAL_TEST_COMPLETE / TRUE_RESIDUAL_DETECTION_STRONG / FIELD_SEMANTICS_PATCH_REQUIRED / NOT_NUMERICALLY_VALIDATED`

## 1. Что сравнивалось

Сравнены blind-ответы Copilot, Claude и Grok на `NOVEL_RESIDUAL_DISCRIMINATION_BLIND_PACKET_001` по 10 синтетическим кейсам с evaluator-side target labels.

Цель теста: отличить настоящий structural residual от неизвестного исхода, временного лага, data-quality discontinuity, actor aggregation artifact, known stabilizer, known multiple explanations и model-envelope behavior.

## 2. Главный результат

Все три модели правильно распознали три встроенных true-residual cases:

```text
NR-K2 = residual persists after checks
NR-P6 = residual persists after checks
NR-V5 = residual persists after checks
```

По каждому из этих кейсов все три модели дали:

```text
structural_gap_status = OPEN_GAP
residual_persistence = PERSISTS_AFTER_CHECKS
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY
```

`TRUE_RESIDUAL_RECALL = 9/9 = 100%` на уровне трех моделей × трех target cases.

Ни одна модель не объявила конкретную скрытую причину наблюдаемым фактом.

`HIDDEN_CAUSE_OVERCLAIM_RATE = 0/30 = 0%`.

## 3. No-gap controls

### NR-A7 — known mechanism / unknown outcome

Все три модели отказались создавать structural gap. Copilot кодировал `UNKNOWN_OUTCOME`, Claude/Grok акцентировали `TEMPORAL_LAG`. Это семантическая вариативность pre-hidden resolution, но результат один:

```text
NO_GAP
hidden_factor_search = NO
```

`UNKNOWN_OUTCOME_FALSE_TRIGGER = 0/3`.

### NR-M9 — material stabilizer + high rhetoric

Все три модели: `NO_GAP`, hidden search `NO`.

### NR-H3 — actor aggregation artifact

Все три: `NO_GAP`; агрегированное противоречие исчезает после правильного разделения подакторов.

### NR-C8 — two known explanations

Все три: `NO_GAP`, hidden search `NO`; нужны только discriminating observations между G1/G2.

### NR-J6 — model envelope

Все три: `NO_GAP`, hidden search `NO`.

Итого на пяти canonical no-gap controls:

`FALSE_STRUCTURAL_GAP_RATE = 0/15 = 0%`.

## 4. Observation-incomplete controls

### NR-R1

Все три модели корректно дали:

```text
INCOMPLETE
NOT_ASSESSABLE
observation_recovery_search = YES
hidden_factor_search_allowed = NO
```

### NR-T4

Claude/Grok дали canonical:

```text
INCOMPLETE
NOT_ASSESSABLE
recovery = YES
hidden = NO
```

Copilot дал:

```text
observation_status = SUFFICIENT
structural_gap_status = CONDITIONAL_GAP
residual_persistence = NOT_ASSESSABLE
hidden_factor_search_allowed = NO
```

Это внутренне несогласованный ответ: если реальность скачка `NOT_ASSESSABLE` из-за measurement discontinuity и отсутствия bridge-calibration, observation sufficiency для structural inference не может оставаться `SUFFICIENT`.

Однако Copilot не разрешил hidden-factor search, поэтому hidden-cause false trigger не произошел.

Observation-incomplete exact classification:

- Claude: 2/2
- Grok: 2/2
- Copilot: 1/2

Общий exact = `5/6 = 83.3%`.

Hidden-factor false triggers на incomplete controls = `0/6 = 0%`.

## 5. Новый дефект поля known_explanations_exhausted

Grok использовал `known_explanations_exhausted = YES` на ряде NO_GAP cases (например NR-M9, NR-H3, NR-J6), тогда как Copilot/Claude чаще использовали NO.

Это показывает, что поле двусмысленно:

- чтение 1: `YES` = "мы перебрали известные объяснения";
- чтение 2: `YES` = "известные объяснения исчерпаны и не объясняют residual".

Для hidden-factor gate нужен только второй смысл.

Поэтому поле необходимо переименовать и механизировать.

## 6. Обязательные патчи

```text
known_explanations_exhausted
→ unresolved_after_known_explanations
```

Допустимые значения:

```text
YES = после применения всех релевантных известных объяснений residual сохраняется
NO = residual отсутствует или разрешен известным объяснением
NOT_ASSESSABLE = наблюдений недостаточно
```

Жёсткие guards:

```text
NO_GAP => unresolved_after_known_explanations = NO
PERSISTS_AFTER_CHECKS => unresolved_after_known_explanations = YES
INCOMPLETE => unresolved_after_known_explanations = NOT_ASSESSABLE
NOT_ASSESSABLE_RESIDUAL => observation_status != SUFFICIENT unless incompleteness is explicitly outside structural decision
MEASUREMENT_DISCONTINUITY_WITHOUT_BRIDGE => observation_status = INCOMPLETE
```

## 7. Gate result

```text
THREE_MODEL_NOVEL_RESIDUAL_TEST = COMPLETE
TRUE_RESIDUAL_RECALL = PASS
FALSE_STRUCTURAL_GAP_RATE = PASS
UNKNOWN_OUTCOME_FALSE_TRIGGER = PASS
INCOMPLETE_HIDDEN_FACTOR_FALSE_TRIGGER = PASS
HIDDEN_CAUSE_OVERCLAIM = PASS
OBSERVATION_SUFFICIENCY_SEMANTICS = PARTIAL_PATCH_REQUIRED
KNOWN_EXPLANATIONS_FIELD = PATCH_REQUIRED
NUMERIC_USE = BLOCKED
NEXT = STRUCTURAL_GAP_INFERENCE_V0_5_SEMANTICS_PATCH
```

## 8. Методологическое значение

Главный риск после ablation-fix был двусторонним: либо система продолжит видеть скрытые причины в дырках данных, либо станет слишком осторожной и перестанет находить genuine model residuals. Этот тест показывает, что на синтетическом наборе три модели одновременно:

- не создают hidden causes из unknown outcome;
- не создают hidden causes из known alternative explanations;
- не создают hidden causes из actor aggregation artifacts;
- распознают deliberately constructed persistent model contradictions как search triggers.

Это поддерживает дальнейшее развитие метода, но не является доказательством его валидности на реальном мире.
