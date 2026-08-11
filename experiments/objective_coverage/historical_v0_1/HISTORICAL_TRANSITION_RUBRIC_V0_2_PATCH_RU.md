# HISTORICAL_TRANSITION_RUBRIC v0.2 — PATCH

**Статус:** `PATCH_CANDIDATE / BASED_ON_REAL_HISTORY_BLIND_TEST_001 / NOT_NUMERICALLY_VALIDATED`

## 1. Разделить transition state и structural gap

```text
transition_instability_state = STABLE | STRESSED | DEGRADING | THRESHOLD_NEAR | TRANSITION_UNDERWAY | UNKNOWN
structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | NOT_ASSESSABLE
```

Guards:

```text
HIGH_TRANSITION_RISK != STRUCTURAL_GAP
THRESHOLD_NEAR != STRUCTURAL_GAP
TRANSITION_UNDERWAY != STRUCTURAL_GAP
OBSERVED_COMMAND_COLLAPSE != STRUCTURAL_GAP
SYSTEM_TRANSITION != MODEL_FAILURE
```

Structural gap допускается только если после применения наблюдаемых transition variables конфигурация остаётся необъяснённой текущей моделью.

## 2. Двойная достаточность наблюдений

```text
observation_status_state = SUFFICIENT | INCOMPLETE
observation_status_gap = SUFFICIENT | INCOMPLETE
```

State coding может быть возможен при недостаточности данных для hidden-gap inference.

Если `observation_status_gap = INCOMPLETE`:

```text
structural_gap_status = NOT_ASSESSABLE
hidden_factor_search_allowed = NO
```

## 3. Силовой ресурс

Разделить:

```text
coercive_asset_capacity = HIGH | MEDIUM | LOW | UNKNOWN
coercive_executable_capacity = HIGH | MEDIUM | LOW | UNKNOWN
command_executability_state = STABLE | STRESSED | DEGRADING | COLLAPSING | UNKNOWN
```

Guards:

```text
COERCIVE_ASSET_PRESENT != COERCIVE_ASSET_USABLE
ASSET_CAPACITY != EXECUTABLE_CAPACITY
FORMAL_COMMAND != EXECUTED_COMMAND
```

## 4. Critical-node alignment

```text
REGIME_ALIGNED = no observed materially relevant organized defection
MIXED = at least one materially relevant critical node/bloc acts independently or against incumbent alignment while others remain aligned
SHIFTING = directional movement of critical-node alignment is directly observed
OPPOSITION_ALIGNED = dominant relevant nodes are observed aligned against incumbent
UNKNOWN = evidence insufficient
```

Guard:

```text
ELITE_UNCERTAINTY != ELITE_DEFECTION
```

## 5. Public compliance

```text
public_compliance_signal = STABLE | DEGRADED_LOCAL | DEGRADED_BROAD | COLLAPSED | UNKNOWN
```

Rules:

```text
NO_EXPLICIT_PUBLIC_SCOPE => UNKNOWN or minimum directly supported scope
PUBLIC_COMPLIANCE_SCOPE != CRISIS_SEVERITY
VIOLENCE != BROAD_NONCOMPLIANCE
PROTEST_IN_CAPITAL != NATIONAL_COMPLIANCE_COLLAPSE
```

## 6. External support

Оставить проверенное разделение:

```text
NONE_OBSERVED
AVAILABLE_NOT_DEPLOYED
DEPLOYED
UNKNOWN
```

Guard:

```text
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
```

## 7. Negotiated transition

```text
negotiated_transition_channel = ABSENT | PRESENT | ACTIVE | UNKNOWN
```

Guards:

```text
NEGOTIATION_EXISTS != NEGOTIATION_SUCCESS
NEGOTIATED_TRANSITION != STATE_COLLAPSE
UNKNOWN_SETTLEMENT_OUTCOME != STRUCTURAL_GAP
```

## 8. Transition signal

Добавить:

```text
transition_signal = NONE | PRESSURE_ACCUMULATION | COMMAND_EROSION | NODE_REALIGNMENT | ALTERNATIVE_COORDINATION | NEGOTIATED_RECONFIGURATION | EXTERNAL_STABILIZATION | MULTI_SIGNAL | UNKNOWN
```

Это descriptive state, не прогноз outcome.

## 9. Hidden-factor gate

```text
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY
```

разрешается только если:

```text
observation_status_gap = SUFFICIENT
AND transition variables coded
AND known stabilizers/pressures considered
AND structural contradiction persists
```

Не использовать structural gap как шкалу кризисности.

## 10. Status

```text
HISTORICAL_TRANSITION_RUBRIC_V0_2_PATCH = READY
REAL_HISTORY_BLIND_TEST_001_PATCHES_IMPORTED = YES
NUMERIC_USE = BLOCKED
NEXT = BLIND_RECODE_002
```
