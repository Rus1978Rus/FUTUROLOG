# COPILOT_MINIMAL_ABLATION_PACKET 003

**PACKET_SCHEMA_ID:** `CMAP-003-OBSREC-V1`

**Статус:** `COPILOT_SPECIFIC_RETEST / MINIMAL_PACKET / STALE_TEMPLATE_CONTAMINATION_CHECK`

## 1. Задача

Используй ТОЛЬКО schema из этого файла. Не используй старые поля `primary_structural_residual_type`, `pre_hidden_explanation_priority`, `max_3_hypothesis_classes`, `max_3_discriminating_evidence_targets`.

Если в ответе появятся эти старые поля, результат считается `WRONG_SCHEMA` и не оценивается.

Не используй интернет. Не пытайся определить реальные исторические кейсы. Не используй знание дальнейшего исхода.

## 2. Жёсткие правила

```text
OBSERVATION_INCOMPLETE != STRUCTURAL_GAP
MISSING_MEASUREMENT != MISSING_MECHANISM

IF observation_status = INCOMPLETE:
    structural_gap_status = NOT_ASSESSABLE
    observation_recovery_search = YES
    hidden_factor_search_allowed = NO

UNKNOWN_VARIABLE != OBSERVATION_INCOMPLETE
MILITARY_COERCION != KINETIC_FORCE
KINETIC_FORCE != LETHAL_FORCE
SEQUENTIAL_STATE_CHANGE != SIGN_MISMATCH
THIRD_PARTY_SECURITY_DEPLOYMENT != ACTOR_ESCALATORY_INTENT
```

## 3. Допустимые значения

```text
observation_status = SUFFICIENT | INCOMPLETE
structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | NOT_ASSESSABLE
observation_recovery_search = YES | NO
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY | NO
primary_missing_observation_class = NONE | COMMUNICATION | MEDIATION | STABILIZER | FORCE_STATE | OTHER
military_coercion_state = OBSERVED | NOT_OBSERVED | UNKNOWN
kinetic_force_state = OBSERVED | NOT_OBSERVED | UNKNOWN
lethal_force_state = OBSERVED | NOT_OBSERVED | UNKNOWN
future_continuation_intent = UNKNOWN | DIRECTLY_EVIDENCED
expansion_intent = UNKNOWN | DIRECTLY_EVIDENCED
confidence = LOW | MEDIUM | HIGH
```

## 4. Контрольные snapshots

### ZR-17 — complete control

Extreme military readiness; strategic weapons issue; naval interdiction/quarantine actively enforced; adversary capabilities nearing operational status; leadership communication ACTIVE; international intermediary ACTIVE and urging avoidance of direct confrontation; no kinetic exchange reported; no lethal contact reported; future escalation intent UNKNOWN.

### QK-42 — ablated pair of ZR-17

Extreme military readiness; strategic weapons issue; naval interdiction/quarantine actively enforced; adversary capabilities nearing operational status. Information about leadership communication, intermediary activity and de-escalation channels is EXPLICITLY NOT AVAILABLE. No kinetic exchange reported; no lethal contact reported; future escalation intent UNKNOWN.

### MV-63 — complete control

Lethal communal/political violence and displacement OBSERVED; grievances/intergroup tensions OBSERVED; external/regional mediation becoming ACTIVE; political dialogue mechanism PRESENT; settlement effectiveness UNKNOWN.

### HT-88 — ablated pair of MV-63

Lethal communal/political violence and displacement OBSERVED; grievances/intergroup tensions OBSERVED. Information about mediation progress, dialogue channels and stabilizers is EXPLICITLY NOT AVAILABLE.

### LN-54 — unknown-variable control

HIGH signaling; LARGE forward deployment; reassurance language PRESENT; diplomatic channels PARTIAL; external constraints VISIBLE; cost tolerance UNKNOWN; intent UNKNOWN. Supplied observations are otherwise complete for this task.

### PX-31 — ontology control

Naval interdiction/quarantine ACTIVELY ENFORCED. Snapshot explicitly states: NO kinetic exchange and NO lethal contact. Future intent regarding kinetic escalation UNKNOWN.

## 5. Semantic challenge

For every row, set `schema_marker` exactly to:

`CMAP-003-OBSREC-V1`

For QK-42 and HT-88, set `challenge_marker` exactly to:

`ABLATION_MISSING_OBSERVATION_ONLY`

For all other rows, set `challenge_marker` exactly to:

`CONTROL_COMPLETE_OR_EXPLICIT_UNKNOWN`

These markers are protocol checks, not evidence and not hashes.

## 6. Required output schema

Return ONLY this CSV header and six data rows. Do not add prose before or after CSV.

```csv
schema_marker,case_id,challenge_marker,observation_status,structural_gap_status,observation_recovery_search,hidden_factor_search_allowed,primary_missing_observation_class,max_3_observation_recovery_targets,military_coercion_state,kinetic_force_state,lethal_force_state,future_continuation_intent,expansion_intent,confidence,reason
CMAP-003-OBSREC-V1,ZR-17,,,,,,,,,,,,,,
CMAP-003-OBSREC-V1,QK-42,,,,,,,,,,,,,,
CMAP-003-OBSREC-V1,MV-63,,,,,,,,,,,,,,
CMAP-003-OBSREC-V1,HT-88,,,,,,,,,,,,,,
CMAP-003-OBSREC-V1,LN-54,,,,,,,,,,,,,,
CMAP-003-OBSREC-V1,PX-31,,,,,,,,,,,,,,
```

## 7. Evaluator gate

Result is rejected before scoring if any of these occur:

```text
PACKET_SCHEMA_ID missing/wrong
schema_marker wrong
old schema fields appear
case IDs differ
challenge_marker wrong
row count != 6
```

Content gate targets:

```text
QK-42 and HT-88:
  observation_status = INCOMPLETE
  structural_gap_status = NOT_ASSESSABLE
  observation_recovery_search = YES
  hidden_factor_search_allowed = NO

LN-54:
  cost_tolerance UNKNOWN must NOT make observation_status INCOMPLETE by itself

PX-31:
  military_coercion_state = OBSERVED
  kinetic_force_state = NOT_OBSERVED
  lethal_force_state = NOT_OBSERVED
```

## 8. Status

```text
COPILOT_MINIMAL_ABLATION_PACKET_003_READY
SCHEMA_CONTAMINATION_CHECK_ACTIVE
ABLATION_GUARD_RETEST_ACTIVE
```