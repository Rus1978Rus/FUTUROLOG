# HISTORICAL PRE-THRESHOLD BLIND PACKET 001

**PACKET_SCHEMA_ID:** `HPTB-001-V1`

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_TEST / COUNTRY_LABELS_HIDDEN / OUTCOMES_HIDDEN / SOURCE_BACKED_SNAPSHOTS`

## 1. Цель

Проверить, способен ли кодировщик отличать:

- наличие силового ресурса от его фактической исполнимости;
- массовый протест от системного распада;
- реальную внешнюю поддержку от потенциальной;
- negotiated transition от collapse;
- degradation публичного подчинения от подтверждённой дефекции критических узлов.

Не угадывать реальные страны/события. Не использовать интернет. Не использовать знания о дальнейших исходах.

## 2. Guards

```text
STATE_CAPACITY != EXECUTABLE_CAPACITY
COERCIVE_ASSET_PRESENT != COERCIVE_ASSET_USABLE
MASS_PROTEST != REGIME_COLLAPSE
PUBLIC_DEFIANCE != ELITE_DEFECTION
ARMY_WITHDRAWAL != WHOLE_ARMY_DEFECTION
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
NEGOTIATION_EXISTS != NEGOTIATION_SUCCESS
FORMAL_AUTHORITY != EFFECTIVE_COMMAND_EXECUTION
```

## 3. Coding schema

Для каждого snapshot вернуть:

```text
observation_status = SUFFICIENT | INCOMPLETE
coercive_capacity_state = HIGH | MEDIUM | LOW | UNKNOWN
command_executability_state = STABLE | STRESSED | DEGRADING | COLLAPSING | UNKNOWN
critical_node_alignment = REGIME_ALIGNED | MIXED | SHIFTING | OPPOSITION_ALIGNED | UNKNOWN
public_compliance_signal = STABLE | DEGRADED_LOCAL | DEGRADED_BROAD | COLLAPSED | UNKNOWN
external_support_state = NONE_OBSERVED | AVAILABLE_NOT_DEPLOYED | DEPLOYED | UNKNOWN
negotiated_transition_channel = ABSENT | PRESENT | ACTIVE | UNKNOWN
structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | NOT_ASSESSABLE
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY | NO
max_3_discriminating_evidence_targets
confidence = LOW | MEDIUM | HIGH
reason
```

## 4. Blind snapshots

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

## 5. Output CSV

```csv
schema_marker,case_id,observation_status,coercive_capacity_state,command_executability_state,critical_node_alignment,public_compliance_signal,external_support_state,negotiated_transition_channel,structural_gap_status,hidden_factor_search_allowed,max_3_discriminating_evidence_targets,confidence,reason
HPTB-001-V1,AX-14,,,,,,,,,,,,
HPTB-001-V1,BV-27,,,,,,,,,,,,
HPTB-001-V1,CR-52,,,,,,,,,,,,
HPTB-001-V1,DK-83,,,,,,,,,,,,
HPTB-001-V1,EL-31,,,,,,,,,,,,
HPTB-001-V1,FM-46,,,,,,,,,,,,
HPTB-001-V1,GN-68,,,,,,,,,,,,
HPTB-001-V1,HP-75,,,,,,,,,,,,
HPTB-001-V1,JQ-92,,,,,,,,,,,,
```

## 6. Protocol gate

Result rejected before scoring if:

- schema_marker differs from `HPTB-001-V1`;
- case IDs differ;
- extra country/event identification is supplied;
- old residual schemas are used instead of this one.

## 7. Evaluator-only mapping — НЕ ПЕРЕДАВАТЬ внешнему кодировщику

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

Evaluator must not score based on historical outcome. Score only whether the coder preserves the distinctions encoded in the snapshot.

## 8. Status

```text
HISTORICAL_PRE_THRESHOLD_BLIND_PACKET_001 = READY
COUNTRY_LABELS_HIDDEN = YES
OUTCOMES_HIDDEN = YES
SOURCE_BACKED_INPUTS = YES
NUMERIC_FORESIGHT_USE = BLOCKED
```
