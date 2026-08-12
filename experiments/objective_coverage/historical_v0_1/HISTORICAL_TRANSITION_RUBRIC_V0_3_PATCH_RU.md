# HISTORICAL TRANSITION RUBRIC v0.3 — PATCH

**Статус:** `PATCH_CANDIDATE / BASED_ON_REAL_HISTORY_RECODE_002 / NOT_NUMERICALLY_VALIDATED`

## 1. Hidden-factor gate — жёсткая механика

```text
NO_GAP => hidden_factor_search_allowed = NO
NOT_ASSESSABLE => hidden_factor_search_allowed = NO
YES_SEARCH_TRIGGER_ONLY requires structural_gap_status in {CONDITIONAL_GAP, OPEN_GAP}
```

Наличие discriminating evidence targets не означает hidden-factor search. Цели могут относиться к observation recovery или известным competing explanations.

## 2. Двойная достаточность наблюдений

```text
observation_status_state = SUFFICIENT | INCOMPLETE
observation_status_gap = SUFFICIENT | INCOMPLETE
```

`state=SUFFICIENT` допускается, если имеющихся наблюдений достаточно, чтобы ограничить transition state даже при UNKNOWN отдельных dimensions.

`gap=SUFFICIENT` требует минимального диагностического набора:

```text
command_executability_state != UNKNOWN
AND critical_node_alignment != UNKNOWN
OR explicit evidence that these dimensions are not required for the tested residual
```

Если критически важный node/command dimension отсутствует:

```text
observation_status_gap = INCOMPLETE
structural_gap_status = NOT_ASSESSABLE
hidden_factor_search_allowed = NO
```

## 3. Transition instability anchors

### STABLE
Нет значимого наблюдаемого ухудшения исполнения/координации; давление может существовать, но system execution сохраняется.

### STRESSED
Сильное давление и/или broad noncompliance, но command execution остаётся stable/stressed и materially relevant node realignment не наблюдается.

### DEGRADING
Есть наблюдаемое ухудшение одного или нескольких execution dimensions, но критический переход ещё не наблюдается.

### THRESHOLD_NEAR
Требуется минимум один прямой critical transition marker:

- `command_executability_state = DEGRADING` или `COLLAPSING`, или
- `critical_node_alignment = MIXED` или `SHIFTING`, или
- alternative coordination с material control/function,

и минимум один дополнительный reinforcing transition signal.

```text
MASS_PROTEST + STRESSED_COMMAND <= DEGRADING
```

### TRANSITION_UNDERWAY
Наблюдается сам переход состояния системы: collapsing executable capacity, direct critical-node realignment, negotiated institutional transfer/reconfiguration already active, либо эквивалентная material transition.

```text
TRANSITION_UNDERWAY != STRUCTURAL_GAP
```

## 4. External support

```text
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_STABILIZATION_EFFECT
EXTERNAL_FORCE_DEPLOYMENT != TRANSITION_UNDERWAY
```

`transition_signal = EXTERNAL_STABILIZATION` допускается только если наблюдается материализованный стабилизирующий механизм/действие, а не просто наличие союзника или обещания помощи.

При одновременном внутреннем давлении и реально действующем внешнем stabilizer:

```text
transition_signal = MULTI_SIGNAL
```

может быть предпочтительнее чистого `EXTERNAL_STABILIZATION`.

## 5. Critical-node alignment

```text
EXTERNAL_OR_NONSTATE_ARMED_OPPOSITION != CRITICAL_NODE_DEFECTION
```

`MIXED` требует, чтобы хотя бы один materially relevant node из incumbent execution network действовал независимо/против центра, пока другие остаются aligned.

`SHIFTING` требует наблюдаемого directional movement.

Elite uncertainty, opposition existence, sanctions, protests или civil conflict сами по себе не создают MIXED.

## 6. Coercive asset capacity

Не повышать `coercive_asset_capacity` на основании тяжести кризиса.

```text
CRISIS_SEVERITY != ASSET_SCALE
FORMAL_EMERGENCY_POWER != EXECUTABLE_CAPACITY
```

Если snapshot подтверждает наличие значимых силовых ресурсов, но их масштаб неоперационален:

```text
coercive_asset_capacity = MEDIUM or UNKNOWN
```

если HIGH прямо не поддержан описанием.

## 7. Evidence targets split

В следующей schema развести:

```text
observation_recovery_targets
known_explanation_discrimination_targets
hidden_factor_discrimination_targets
```

Чтобы наличие обычных поисковых целей не выглядело как разрешение hidden-factor search.

## 8. Status

```text
HISTORICAL_TRANSITION_RUBRIC_V0_3_PATCH = READY
REAL_HISTORY_RECODE_002_IMPORTED = YES
TRANSITION_SIGNAL = DESCRIPTIVE_ONLY
STRUCTURAL_GAP = MODEL_RESIDUAL_ONLY
NUMERIC_USE = BLOCKED
NEXT = EXPAND_REAL_CASE_FAMILIES + TEMPORAL_SEQUENCE_TEST
```
