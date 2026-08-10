# STRUCTURAL_GAP_INFERENCE v0.3 PATCH

**Статус:** `PATCH_CANDIDATE / ABLATION_GUARD_HARDENED / NOT_RUNTIME / NOT_NUMERICALLY_VALIDATED`

## 1. Главный новый принцип

После broad blind test вводится промежуточное состояние, которое отделяет отсутствие наблюдения от structural gap.

```text
OBSERVATION_INCOMPLETE != STRUCTURAL_GAP
```

Новая последовательность:

```text
OBSERVATIONS
→ OBSERVABILITY_CHECK
→ if REQUIRED_FIELD_MISSING:
     OBSERVATION_INCOMPLETE
     TARGETED_DATA_COLLECTION
     NO_HIDDEN_FACTOR_SEARCH
→ else MODEL_CONSISTENCY_CHECK
→ only then CONDITIONAL/OPEN STRUCTURAL GAP
```

## 2. Новые статусы

`analysis_state`:

```text
MODEL_EXPLAINS
OBSERVATION_INCOMPLETE
CONDITIONAL_STRUCTURAL_GAP
OPEN_STRUCTURAL_GAP
UNKNOWN
```

`OBSERVATION_INCOMPLETE` означает: недостаточно данных, чтобы решить, существует ли structural gap. Это не residual class и не лицензия на missing-factor hypotheses.

## 3. Hard ablation guard

```text
KNOWN_OBSERVATION_ABLATION => analysis_state=OBSERVATION_INCOMPLETE
KNOWN_OBSERVATION_ABLATION => hidden_factor_search_allowed=NO
MISSING_STABILIZER_DATA != ABSENT_STABILIZER
MISSING_COMMUNICATION_DATA != DEGRADED_COMMUNICATION
MISSING_MEASUREMENT != MISSING_MECHANISM
```

Сначала разрешён только поиск отсутствующего наблюдения.

## 4. Open-gap gate

`OPEN_STRUCTURAL_GAP` запрещён, если существует непроверенная простая observability explanation.

```text
PLAUSIBLE_OBSERVABILITY_EXPLANATION_UNRESOLVED
=> OPEN_STRUCTURAL_GAP_FORBIDDEN
```

Максимум:

```text
OBSERVATION_INCOMPLETE
```

или, если observations достаточны, но observability explanation лишь частично возможна:

```text
CONDITIONAL_STRUCTURAL_GAP
```

## 5. NO_GAP schema validation

Если:

```text
analysis_state = MODEL_EXPLAINS
```

то автоматически:

```text
primary_structural_residual_type = NONE
hidden_factor_search_allowed = NO
hypothesis_classes = NONE
discriminating_hidden_factor_targets = NONE
```

Это должно проверяться валидатором, а не только prose rule.

## 6. Разделение наблюдательного поиска и hidden-factor search

Добавляются два разных поля:

```text
observation_recovery_search_allowed = YES | NO
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY | NO
```

При `OBSERVATION_INCOMPLETE`:

```text
observation_recovery_search_allowed = YES
hidden_factor_search_allowed = NO
```

## 7. Force-use ontology patch

Старое поле `current_force_use_state` удаляется из будущей схемы как неоднозначное.

Вместо него:

```text
military_coercion_state = NOT_OBSERVED | OBSERVED | UNKNOWN
kinetic_force_state = NOT_OBSERVED | OBSERVED | UNKNOWN
lethal_force_state = NOT_OBSERVED | OBSERVED | UNKNOWN
```

Пример:

```text
naval_quarantine/interdiction
may be military_coercion_state=OBSERVED
while kinetic_force_state may remain UNKNOWN/NOT_OBSERVED
and lethal_force_state may remain NOT_OBSERVED
```

Guards:

```text
MILITARY_COERCION != KINETIC_FORCE
KINETIC_FORCE != LETHAL_FORCE
```

## 8. Intent patch

Сохраняются отдельные поля:

```text
continuation_intent_at_observed_level
expansion_intent
```

Но ни одно не выводится автоматически из capability/signaling.

```text
ONGOING_ACTION may support CONTINUATION_AT_OBSERVED_LEVEL
ONGOING_ACTION != EXPANSION_INTENT
```

## 9. Temporal sequencing patch

```text
EARLIER_REASSURANCE + LATER_ESCALATORY_STEP != STRUCTURAL_GAP
SEQUENTIAL_STATE_CHANGE != SIGN_MISMATCH
PAST_REASSURANCE != CURRENT_RESTRAINT
```

Перед `SIGN_MISMATCH` проверить:

1. changed time;
2. changed leadership/actor composition;
3. changed incentives;
4. changed external constraints;
5. expired or non-implemented prior commitment.

Если temporal/context change уже объясняет переход, `MODEL_EXPLAINS` допустим.

## 10. Stabilizer-effect patch

```text
STABILIZER_PRESENT != STABILIZER_EFFECTIVE
STABILIZER_EFFECT_UNKNOWN != STRUCTURAL_GAP
MEDIATION_PRESENT != SUCCESS
MEDIATION_EFFECT_UNKNOWN != MISSING_MECHANISM
```

Unknown effectiveness создаёт measurement task, а не missing-factor hypothesis.

## 11. Structural-gap admission criteria

Structural gap допускается только если одновременно:

```text
A. observations sufficient for tested relation
B. no unresolved data-quality blocker
C. no unresolved observation-ablation blocker
D. no simpler scale/actor/timing explanation
E. current model still leaves persistent contradiction/residual
F. residual generates discriminating evidence plan
```

Если A–D не пройдены — structural-gap search запрещён.

## 12. Search types

### Observation recovery search

Ищет отсутствующие данные:

- status of hotline/channel;
- mediation activity;
- missing denominator;
- missing deployment/withdrawal confirmation;
- missing source family.

Не создаёт hidden-factor hypothesis.

### Structural hypothesis search

Разрешён только после admission criteria и ищет различающие evidence targets между несколькими NOT_OBSERVED hypothesis classes.

## 13. Новые guards

```text
UNKNOWN_VARIABLE != STRUCTURAL_GAP
KNOWN_OBSERVATION_ABLATION != REAL_WORLD_HIDDEN_CAUSE
OBSERVATION_RECOVERY_SEARCH != HIDDEN_FACTOR_SEARCH
STABILIZER_EFFECT_UNKNOWN != STRUCTURAL_GAP
SEQUENTIAL_STATE_CHANGE != SIGN_MISMATCH
MILITARY_COERCION != KINETIC_FORCE
KINETIC_FORCE != LETHAL_FORCE
NO_GAP_FIELDS_MUST_BE_SCHEMA_CONSISTENT
```

## 14. Следующий тест

Нужен targeted `ABLATION_RETEST_001`:

- Q11/Q12 analogues с явно удалёнными полями;
- paired full-information versions;
- 4–6 новых synthetic ablations;
- test criterion: hidden-factor false-trigger rate on known ablations = 0% target, <=10% provisional ceiling;
- observation-recovery trigger rate on known ablations = 100% target.

## 15. Gate

```text
STRUCTURAL_GAP_V0_3_PATCH = READY_FOR_RETEST
ABLATION_FALSE_TRIGGER_PROBLEM = PATCHED_IN_SCHEMA
RUNTIME = BLOCKED
NUMERIC_USE = BLOCKED
NEXT = ABLATION_RETEST_001
```
