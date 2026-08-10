# STRUCTURAL_GAP_INFERENCE v0.2 PATCH

**Статус:** `PATCH_CANDIDATE / SEARCH_TRIGGER_ONLY / NOT_RUNTIME / NOT_NUMERIC`

## 1. Что исправляется

Blind residual stress test показал, что базовая логика работает, но v0.1 недостаточно строго различает:

- неизвестную переменную и структурный gap;
- observation limit и structural residual;
- CONDITIONAL_GAP и OPEN_GAP;
- уже наблюдаемое применение силы и намерение расширить силу;
- hypothesis naming и качество discriminating evidence.

## 2. Новые guards

```text
UNKNOWN_VARIABLE != STRUCTURAL_GAP
MISSING_MEASUREMENT != MISSING_MECHANISM
OBSERVABILITY_LIMIT != STRUCTURAL_RESIDUAL
NO_GAP => primary_structural_residual_type = NONE
UNRESOLVED_OBSERVABILITY_ALTERNATIVE => MAX_GAP_STATUS = CONDITIONAL_GAP
OPEN_GAP requires observability alternative materially checked and insufficient
FORCE_ALREADY_USED != EXPANSION_INTENT_EVIDENCED
HYPOTHESIS_NAME_AGREEMENT != HYPOTHESIS_QUALITY
```

Сохраняются:

```text
MODEL_RESIDUAL != PROOF_OF_HIDDEN_FACTOR
MISSING_FACTOR_HYPOTHESIS != OBSERVED_FACT
UNEXPLAINED_BEHAVIOR != ACTOR_IRRATIONALITY
PERSISTENT_PREPARATION != COMMITMENT
```

## 3. Gap status v0.2

### NO_GAP
Текущая модель непротиворечиво объясняет наблюдаемую конфигурацию. Неизвестные поля/слепые зоны могут существовать, но не создают structural residual.

Требование:

```text
primary_structural_residual_type = NONE
hidden_factor_search_allowed = NO
```

### CONDITIONAL_GAP
Есть реальный residual, но хотя бы одна обычная альтернатива — observation gap, scale error, lag, omitted known factor — ещё способна его объяснить и не проверена достаточно.

```text
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY
```

### OPEN_GAP
Residual сохраняется после materially sufficient checks обычных объяснений. Это всё ещё не доказательство hidden factor.

```text
OPEN_GAP != HIDDEN_FACTOR_PROVEN
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY
```

### UNKNOWN
Недостаточно информации даже для решения о наличии residual.

## 4. Observation limits отдельно

Добавляются поля:

```text
observation_limit_status = NONE | PRESENT | SEVERE | UNKNOWN
observation_limit_classes = []
```

Observation limit не кодируется как structural residual type.

## 5. Intent split

Старое поле `current_intent` считается слишком широким.

Вводятся:

```text
current_force_use_state = NOT_USED | USED_OBSERVED | UNKNOWN
continuation_intent_at_observed_level = UNKNOWN | DIRECTLY_EVIDENCED
expansion_intent = UNKNOWN | DIRECTLY_EVIDENCED
```

Если force already used:

```text
current_force_use_state = USED_OBSERVED
```

но:

```text
USED_OBSERVED != EXPANSION_INTENT_EVIDENCED
```

## 6. Search-trigger criteria

Hidden-factor search разрешается только если одновременно:

```text
A actual residual exists
B residual is not merely missing measurement
C simpler explanations were checked in order
D at least one discriminating evidence target can be generated
```

Если D не выполняется, hypothesis remains too vague and search is blocked.

## 7. Hypothesis evaluation

Hypothesis classes не обязаны совпадать между кодировщиками по названию.

Вместо этого оцениваются:

```text
falsifiability
ability_to_generate_discriminating_evidence
cutoff_admissibility_of_targets
independence_of_targets
ability_to_reduce_competing_hypotheses
```

Красивое объяснение без различающего теста не проходит.

## 8. Revised coding form

```text
case_id
structural_gap_status
primary_structural_residual_type
observation_limit_status
observation_limit_classes
pre_hidden_explanation_priority
hidden_factor_search_allowed
hypothesis_classes_max3
required_discriminating_evidence_targets_max3
current_force_use_state
continuation_intent_at_observed_level
expansion_intent
confidence
reason
```

## 9. Gate до runtime

```text
1 broader blind residual set >= 10 cases
2 at least 3 NO_GAP negative controls
3 at least 3 genuine search-trigger candidates
4 adversarial missing-data cases
5 hallucination test: unknown field must not become gap
6 hypothesis expiry rule
7 provenance for every search-trigger hypothesis
8 external review
```

## 10. Текущий статус

```text
STRUCTURAL_GAP_INFERENCE_v0_2_PATCH_CREATED
SEARCH_TRIGGER_LOGIC_PROMISING
UNKNOWN_FIELD_GUARD_ADDED
OBSERVATION_LIMIT_SPLIT_ADDED
INTENT_SPLIT_ADDED
OPEN_VS_CONDITIONAL_RULE_ADDED
RUNTIME_BLOCKED
NUMERIC_USE_BLOCKED
NEXT = BROADER_BLIND_RESIDUAL_SET_002
```
