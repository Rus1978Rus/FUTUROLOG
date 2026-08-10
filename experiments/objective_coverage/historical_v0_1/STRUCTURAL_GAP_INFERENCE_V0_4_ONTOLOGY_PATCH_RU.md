# STRUCTURAL_GAP_INFERENCE v0.4 — ONTOLOGY PATCH

**Статус:** `PATCH_CANDIDATE / ABLATION_CORE_GUARD_SUPPORTED_2_OF_2 / THIRD_CODER_PENDING / NOT_NUMERICALLY_VALIDATED`

## 1. Причина патча

`ABLATION_RETEST_001` стабилизировал главный guard `OBSERVATION_INCOMPLETE -> observation recovery, not hidden-factor search`, но выявил неоднозначности в описании ongoing force/coercion и намерения.

## 2. Action vs intent split

Старое поле:

```text
continuation_intent_at_observed_level
```

слишком неоднозначно и выводится из active operation по-разному.

Заменить на:

```text
current_action_state = NOT_OBSERVED | ONGOING_OBSERVED | ENDED_OBSERVED | UNKNOWN
future_continuation_intent = UNKNOWN | DIRECTLY_EVIDENCED
expansion_intent = UNKNOWN | DIRECTLY_EVIDENCED
```

Guards:

```text
CURRENT_ACTION_CONTINUATION_STATE != FUTURE_CONTINUATION_INTENT
ONGOING_OBSERVED != FUTURE_INTENT_PROVEN
CURRENT_COERCIVE_OPERATION != INTENT_TO_ESCALATE
```

## 3. Force ontology

Оставить отдельные оси:

```text
military_coercion_state = OBSERVED | NOT_OBSERVED | UNKNOWN
kinetic_force_state = OBSERVED | NOT_OBSERVED | UNKNOWN
lethal_force_state = OBSERVED | NOT_OBSERVED | UNKNOWN
```

Жёсткие guards:

```text
MILITARY_COERCION != KINETIC_FORCE
KINETIC_FORCE != LETHAL_FORCE
VIOLENCE != MILITARY_COERCION
VIOLENT_INCIDENT != LETHAL_FORCE
```

`military_coercion_state=OBSERVED` требует evidence использования military/security coercive instrument, а не просто наличия политического/communal violence.

Если snapshot сообщает `violent incident`, но не сообщает lethal/non-lethal характер:

```text
lethal_force_state = UNKNOWN
```

Не использовать `NOT_OBSERVED`, если отсутствие летальности не подтверждено.

## 4. Observation sufficiency

```text
UNKNOWN_LATENT_VARIABLE != OBSERVATION_INCOMPLETE
```

Например `cost tolerance = UNKNOWN` сам по себе не делает snapshot incomplete. `INCOMPLETE` применяется только когда для данного structural-gap decision отсутствует конкретный класс наблюдений, который в paired/full snapshot известен как диагностически необходимый или который rubric явно требует до оценки gap.

## 5. Ablation rule

```text
KNOWN_ABLATION_OF_DIAGNOSTIC_OBSERVATION
=> observation_status = INCOMPLETE
=> structural_gap_status = NOT_ASSESSABLE
=> observation_recovery_search = YES
=> hidden_factor_search_allowed = NO
```

Это не зависит от того, насколько опасно выглядит оставшееся состояние.

## 6. Hidden-factor gate

Hidden-factor search разрешается только после:

```text
observation_status = SUFFICIENT
AND
structural residual persists under current model
AND
known stabilizers/pressures checked
AND
scale/lag/actor aggregation checked
```

Даже тогда:

```text
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY
hypothesis_status = NOT_OBSERVED
```

## 7. Status

```text
STRUCTURAL_GAP_V0_4_ONTOLOGY_PATCH = READY
ABLATION_CORE_GUARD = SUPPORTED_BY_GROK_AND_CLAUDE
COPILOT_CORRECT_PACKET_RETEST = PENDING
NUMERIC_USE = BLOCKED
```
