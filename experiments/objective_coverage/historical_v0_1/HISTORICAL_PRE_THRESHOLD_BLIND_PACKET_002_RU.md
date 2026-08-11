# HISTORICAL PRE-THRESHOLD BLIND PACKET 002

**PACKET_SCHEMA_ID:** `HPTB-002-V2`

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_RECODE / V0_2_RUBRIC / COUNTRY_LABELS_HIDDEN / OUTCOMES_HIDDEN / SOURCE_BACKED_SNAPSHOTS`

## 1. Цель

Повторно закодировать те же реальные пред-пороговые snapshots после исправлений `HISTORICAL_TRANSITION_RUBRIC v0.2`.

Главная проверка:

```text
TRANSITION_INSTABILITY
!=
STRUCTURAL_GAP
```

Кодировщик должен отдельно оценить состояние перехода и отдельно — неполноту модели.

Не угадывать страны/события. Не использовать интернет. Не использовать знания о дальнейших исходах.

## 2. Guards

```text
HIGH_TRANSITION_RISK != STRUCTURAL_GAP
THRESHOLD_NEAR != STRUCTURAL_GAP
TRANSITION_UNDERWAY != STRUCTURAL_GAP
OBSERVED_COMMAND_COLLAPSE != STRUCTURAL_GAP
SYSTEM_TRANSITION != MODEL_FAILURE
COERCIVE_ASSET_PRESENT != COERCIVE_ASSET_USABLE
ASSET_CAPACITY != EXECUTABLE_CAPACITY
FORMAL_COMMAND != EXECUTED_COMMAND
ELITE_UNCERTAINTY != ELITE_DEFECTION
PUBLIC_COMPLIANCE_SCOPE != CRISIS_SEVERITY
PROTEST_IN_CAPITAL != NATIONAL_COMPLIANCE_COLLAPSE
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
NEGOTIATION_EXISTS != NEGOTIATION_SUCCESS
UNKNOWN_SETTLEMENT_OUTCOME != STRUCTURAL_GAP
```

## 3. Coding schema

```text
observation_status_state = SUFFICIENT | INCOMPLETE
observation_status_gap = SUFFICIENT | INCOMPLETE
coercive_asset_capacity = HIGH | MEDIUM | LOW | UNKNOWN
coercive_executable_capacity = HIGH | MEDIUM | LOW | UNKNOWN
command_executability_state = STABLE | STRESSED | DEGRADING | COLLAPSING | UNKNOWN
critical_node_alignment = REGIME_ALIGNED | MIXED | SHIFTING | OPPOSITION_ALIGNED | UNKNOWN
public_compliance_signal = STABLE | DEGRADED_LOCAL | DEGRADED_BROAD | COLLAPSED | UNKNOWN
external_support_state = NONE_OBSERVED | AVAILABLE_NOT_DEPLOYED | DEPLOYED | UNKNOWN
negotiated_transition_channel = ABSENT | PRESENT | ACTIVE | UNKNOWN
transition_instability_state = STABLE | STRESSED | DEGRADING | THRESHOLD_NEAR | TRANSITION_UNDERWAY | UNKNOWN
transition_signal = NONE | PRESSURE_ACCUMULATION | COMMAND_EROSION | NODE_REALIGNMENT | ALTERNATIVE_COORDINATION | NEGOTIATED_RECONFIGURATION | EXTERNAL_STABILIZATION | MULTI_SIGNAL | UNKNOWN
structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | NOT_ASSESSABLE
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY | NO
confidence = LOW | MEDIUM | HIGH
```

Если `observation_status_gap = INCOMPLETE`:

```text
structural_gap_status = NOT_ASSESSABLE
hidden_factor_search_allowed = NO
```

Structural gap разрешён только если после кодирования наблюдаемых transition variables остаётся структурное противоречие, которое текущая схема не объясняет.

## 4. Critical-node rule

```text
REGIME_ALIGNED = no observed materially relevant organized defection
MIXED = at least one materially relevant critical node/bloc acts independently or against incumbent while others remain aligned
SHIFTING = directional movement of critical-node alignment is directly observed
OPPOSITION_ALIGNED = dominant relevant nodes observed aligned against incumbent
UNKNOWN = evidence insufficient
```

Простая `elite uncertainty` не является `MIXED`.

## 5. Blind snapshots

### AX-14
Mass unrest observed locally. Coercive capacity active and substantial. Live-fire authorization exists. Central coordination active. Army loyalty unknown. Command executability only partially observed. Public compliance degraded locally.

### BV-27
Unrest persists. Central administrative coordination remains active. Information suppression/denial active. Army institutional cohesion unknown. Regime executable coercion observed but stressed.

### CR-52
Protest diffusion has reached the national capital. Public compliance signal sharply degraded. Coercive assets remain present. Critical-node loyalty uncertain. Command executability under stress.

### DK-83
Coercive assets remain physically present. Army/security alignment is shifting. Regime executable capacity is collapsing. Alternative political coordination is emerging. Formal regime authority is still claimed.

### EL-31
Large-scale political protest is present. State coercive capacity remains substantial and command chains are active. A formal emergency/martial-law framework is invoked. No evidence in the snapshot shows broad security-node defection. External military support is not deployed. Future regime durability unknown.

### FM-46
Large-scale unrest follows a disputed political event. Domestic coercive institutions remain active. External political/economic backing from a powerful ally is observable, but no foreign combat/security force deployment is observed in the snapshot. Critical-node loyalty appears mostly regime-aligned, though some elite uncertainty exists. Future outcome unknown.

### GN-68
Violent unrest and attacks on state facilities are observed. Domestic coercive response is active. A formal collective-security request is made and external forces are physically deployed. The external contingent's declared mission is limited in scope/time. Internal political outcome remains unknown.

### HP-75
A previously excluded opposition movement is legalized; a major political prisoner is released; formal negotiations begin between incumbent authorities and opposition representatives. State institutions and security structures remain functioning. No evidence in the snapshot establishes state collapse. Distribution of future political power is unresolved.

### JQ-92
A long-running armed political conflict is accompanied by sanctions and international non-recognition of the incumbent constitutional arrangement. A negotiated conference produces a transition framework, cease-fire arrangements, and a route to recognized majority-rule elections. Existing state apparatus remains in place during transition. Final durability unknown.

## 6. Output CSV

```csv
schema_marker,case_id,observation_status_state,observation_status_gap,coercive_asset_capacity,coercive_executable_capacity,command_executability_state,critical_node_alignment,public_compliance_signal,external_support_state,negotiated_transition_channel,transition_instability_state,transition_signal,structural_gap_status,hidden_factor_search_allowed,max_3_discriminating_evidence_targets,confidence,reason
HPTB-002-V2,AX-14,,,,,,,,,,,,,,,,
HPTB-002-V2,BV-27,,,,,,,,,,,,,,,,
HPTB-002-V2,CR-52,,,,,,,,,,,,,,,,
HPTB-002-V2,DK-83,,,,,,,,,,,,,,,,
HPTB-002-V2,EL-31,,,,,,,,,,,,,,,,
HPTB-002-V2,FM-46,,,,,,,,,,,,,,,,
HPTB-002-V2,GN-68,,,,,,,,,,,,,,,,
HPTB-002-V2,HP-75,,,,,,,,,,,,,,,,
HPTB-002-V2,JQ-92,,,,,,,,,,,,,,,,
```

## 7. Protocol gate

Reject before scoring if:

- schema_marker differs from `HPTB-002-V2`;
- case IDs differ;
- country/event identification is supplied;
- old `HPTB-001` schema is used;
- `transition_instability_state` is omitted;
- `coercive_asset_capacity` and `coercive_executable_capacity` are collapsed into one field.

## 8. Evaluator-only mapping — НЕ ПЕРЕДАВАТЬ внешнему кодировщику

```text
AX-14 = Romania 17 Dec 1989
BV-27 = Romania 19 Dec 1989
CR-52 = Romania 21 Dec 1989
DK-83 = Romania 22 Dec 1989 threshold
EL-31 = China May 1989 pre-suppression control
FM-46 = Belarus Aug 2020
GN-68 = Kazakhstan Jan 2022
HP-75 = South Africa 1990 negotiated transition opening
JQ-92 = Rhodesia/Zimbabwe 1979 transition framework
```

Evaluator must score snapshot discipline, not known historical outcome.

## 9. Gate targets

```text
structural_gap false-positive rate on explained transition states -> minimize
transition_instability agreement -> improve vs packet 001
asset vs executable capacity collapse violations = 0
available vs deployed external support violations = 0
elite uncertainty -> MIXED shortcut violations = 0
negotiated transition -> collapse shortcut violations = 0
```

## 10. Status

```text
HISTORICAL_PRE_THRESHOLD_BLIND_PACKET_002 = READY
RUBRIC_V0_2_IMPORTED = YES
REAL_HISTORY_RECODE = READY
NUMERIC_FORESIGHT_USE = BLOCKED
```
