# AGREEMENT_REPORT 004 — BLIND RESIDUAL CODING

**Статус:** `MULTI_MODEL_RESIDUAL_STRESS_TEST_COMPLETE / SEARCH_TRIGGER_LOGIC_PROMISING / TAXONOMY_PATCH_REQUIRED / NOT_VALIDATED`

## 1. Вход

Сравнены три внешние машинные кодировки `BLIND_RESIDUAL_CODER_PACKET_001_RU.md`: Grok, Copilot и Claude.

Пакет скрывал названия стран и исходы и требовал сначала проверить обычные объяснения/наблюдаемость, а только затем разрешать missing-structure hypothesis.

Это multi-model stress test, а не outcome-blind human validation.

## 2. Главный результат

По центральному вопросу метода согласие высокое:

- Case B: 3/3 -> `NO_GAP`, hidden search `NO`.
- Case C: 3/3 -> hidden search `YES_SEARCH_TRIGGER_ONLY`.
- Case D: 3/3 -> `NO_GAP`, hidden search `NO`.
- Case A: 2/3 -> `NO_GAP`, hidden search `NO`; Copilot дал `CONDITIONAL_GAP`.

То есть все три модели различили по крайней мере один настоящий search-trigger case (C) и не стали запускать hidden-factor search для B/D.

## 3. Case A — неизвестность не должна сама создавать gap

Grok и Claude: `NO_GAP`.
Copilot: `CONDITIONAL_GAP` из-за отсутствия подтверждённого отвода, неизвестной cost tolerance и неполной наблюдаемости.

Диагноз: rubric недостаточно жёстко различает `UNKNOWN FIELD` и `MODEL RESIDUAL`.

Patch:

```text
UNKNOWN_VARIABLE != STRUCTURAL_GAP
MISSING_MEASUREMENT != MISSING_MECHANISM
OBSERVABILITY_LIMIT != GAP unless it creates an actual contradiction/residual
```

Если high signaling + deployment + reassurance + visible constraints совместимы с текущей моделью, отсутствие знания cost tolerance само по себе не создаёт hidden-factor search.

## 4. Case B — сильный negative control PASS

Все три кодировщика дали:

```text
NO_GAP
hidden_factor_search_allowed = NO
current_intent = UNKNOWN
```

Сильные costly reassurance + formal deconfliction + visible constraints были распознаны как достаточное объяснение сосуществования опасности и сдерживания.

Это важный PASS:

```text
DANGEROUS_STATE != STRUCTURAL_GAP
KNOWN_STABILIZERS_CAN_EXPLAIN_DANGER_PLUS_RESTRAINT
```

## 5. Case C — search trigger воспроизводится

Все три модели разрешили только поисковый триггер, но не факт скрытой причины.

Grok: `CONDITIONAL_GAP / MISSING_LINK`.
Copilot: `OPEN_GAP / OBSERVABILITY_RESIDUAL`.
Claude: `CONDITIONAL_GAP / PERSISTENT_BEHAVIORAL`.

Общее ядро совпало:

```text
HIGH costly preparation
+ no comparable costly reassurance
+ degraded communication
+ visible external costs
=> investigate missing structure / discriminating evidence
```

Но статус OPEN vs CONDITIONAL расходится. Поскольку degraded communication/observability ещё может имитировать hidden cause, вводится правило:

```text
UNRESOLVED_OBSERVABILITY_ALTERNATIVE => MAX_GAP_STATUS = CONDITIONAL_GAP
OPEN_GAP requires observability alternative materially checked and insufficient
```

## 6. Case D — проблема поля current_intent

Grok/Copilot: `current_intent = UNKNOWN`.
Claude: `DIRECTLY_EVIDENCED`, но explicitly только для продолжения силы на уже наблюдаемом уровне; expansion intent оставлен UNKNOWN.

Это не обязательно substantive disagreement — поле `current_intent` оказалось слишком широким.

Нужно разделить:

```text
current_force_use_state = NOT_USED | USED_OBSERVED | UNKNOWN
continuation_intent_at_observed_level = UNKNOWN | DIRECTLY_EVIDENCED
expansion_intent = UNKNOWN | DIRECTLY_EVIDENCED
```

Guard:

```text
FORCE_ALREADY_USED != EXPANSION_INTENT_EVIDENCED
```

## 7. Внутренняя несогласованность `NO_GAP + residual_type`

Grok дал:

- Case A: `NO_GAP` + `OBSERVABILITY_RESIDUAL`;
- Case D: `NO_GAP` + `PERSISTENT_BEHAVIORAL`.

Это показывает дефект схемы. Если `structural_gap_status = NO_GAP`, структурный residual type должен быть `NONE`. Наблюдательные ограничения должны храниться отдельно.

Patch:

```text
NO_GAP => primary_structural_residual_type = NONE
OBSERVATION_LIMIT != STRUCTURAL_RESIDUAL
```

Вводится отдельное поле `observation_limit_status`.

## 8. Hypothesis quality

Case C породил разные hypothesis classes. Это ожидаемо и не должно решаться majority vote.

Полезнее оценивать не совпадение названий гипотез, а качество discriminating targets:

- withdrawal/redeployment evidence;
- sustainment logistics / fuel / medical / munitions staging;
- personnel rotation/mobilization patterns;
- status of communication channels;
- structure and pricing of demands vs withdrawal conditions;
- explicit cost-tolerance indicators.

Критерий хорошей hypothesis class:

```text
IT_GENERATES_DISCRIMINATING_EVIDENCE
AND
DOES_NOT_BECOME_FACT_BY_INFERENCE
```

## 9. Механические метрики

На 4 cases:

```text
hidden_search_decision unanimous = 3/4 cases
hidden_search_decision majority-consistent = 4/4 cases
B negative-control pass = 3/3
C search-trigger recognition = 3/3
D latent-first-use error = 0/3
A/C force-use-prior-to-intent leakage = 0/6 relevant judgments
A/B/C current intent UNKNOWN = 9/9
```

Case D current-intent field is schema-ambiguous and excluded from a simple agreement score pending field split.

## 10. Решение

```text
STRUCTURAL_GAP_SEARCH_TRIGGER_LOGIC = PROMISING
HIDDEN_CAUSE_INVENTION_CONTROL = PASS_IN_SMALL_PILOT
NEGATIVE_CONTROL_B = PASS
SEARCH_TRIGGER_C = PASS
UNKNOWN_FIELD_VS_GAP_RULE = PATCH_REQUIRED
NO_GAP_RESIDUAL_TYPE_CONSISTENCY = PATCH_REQUIRED
CURRENT_INTENT_FIELD = SPLIT_REQUIRED
OPEN_VS_CONDITIONAL_RULE = PATCH_REQUIRED
NUMERIC_USE = BLOCKED
RUNTIME_USE = BLOCKED
NEXT = STRUCTURAL_GAP_INFERENCE_V0_2_PATCH + BROADER_BLIND_RESIDUAL_SET
```

Majority vote не используется как truth label. Расхождения используются для исправления метода.