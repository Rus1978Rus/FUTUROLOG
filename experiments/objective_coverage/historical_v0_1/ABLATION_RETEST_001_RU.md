# ABLATION_RETEST 001

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_STRESS_TEST / OBSERVATION_RECOVERY_VS_HIDDEN_FACTOR_SPLIT / V0_3_PATCH_TEST`

## 1. Цель

Проверить, устранил ли `STRUCTURAL_GAP_INFERENCE_V0_3_PATCH` главный дефект broad residual test: превращение отсутствующих данных в ложный structural gap и разрешение hidden-factor search.

Целевые показатели:

```text
hidden_factor_false_trigger_rate_on_ablation = 0%
observation_recovery_trigger_rate_on_ablation = 100%
```

## 2. Основные guards

```text
OBSERVATION_INCOMPLETE != STRUCTURAL_GAP
UNKNOWN_VARIABLE != STRUCTURAL_GAP
MISSING_MEASUREMENT != MISSING_MECHANISM
OBSERVATION_RECOVERY_SEARCH != HIDDEN_FACTOR_SEARCH
ABLATION_INDUCED_GAP != REAL_WORLD_HIDDEN_CAUSE
NO_GAP => hidden_factor_search_allowed=NO
OBSERVATION_INCOMPLETE => hidden_factor_search_allowed=NO
OBSERVATION_INCOMPLETE => observation_recovery_search=YES
```

Дополнительно:

```text
MILITARY_COERCION != KINETIC_FORCE
KINETIC_FORCE != LETHAL_FORCE
SEQUENTIAL_STATE_CHANGE != SIGN_MISMATCH
PAST_REASSURANCE != DURABLE_RESTRAINT
```

## 3. Coding schema

Для каждого кейса вернуть:

```text
case_id
observation_status = SUFFICIENT | INCOMPLETE | UNKNOWN
structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | NOT_ASSESSABLE
observation_recovery_search = NO | YES
hidden_factor_search_allowed = NO | YES_SEARCH_TRIGGER_ONLY
primary_missing_observation_class = NONE | COMMUNICATION | MEDIATION | STABILIZER | FORCE_POSTURE | COST_TOLERANCE | TEMPORAL_CONTEXT | OTHER
max_3_observation_recovery_targets
military_coercion_state = NOT_OBSERVED | OBSERVED | UNKNOWN
kinetic_force_state = NOT_OBSERVED | OBSERVED | UNKNOWN
lethal_force_state = NOT_OBSERVED | OBSERVED | UNKNOWN
continuation_intent_at_observed_level = UNKNOWN | DIRECTLY_EVIDENCED
expansion_intent = UNKNOWN | DIRECTLY_EVIDENCED
confidence = LOW | MEDIUM | HIGH
reason
```

Если `observation_status=INCOMPLETE`, то:

```text
structural_gap_status=NOT_ASSESSABLE
observation_recovery_search=YES
hidden_factor_search_allowed=NO
```

## 4. Кейсы

### ABL-01 — полный snapshot

Military confrontation at extreme readiness; strategic weapons issue; naval interdiction/quarantine underway; readiness escalated; adversary capabilities nearing operational status; direct/indirect leadership communication ACTIVE; international intermediary urging both sides to avoid direct confrontation; current intent regarding first strike UNKNOWN.

### ABL-02 — ablated version of ABL-01

Military confrontation at extreme readiness; strategic weapons issue; naval interdiction/quarantine underway; readiness escalated; adversary capabilities nearing operational status. Information about leadership communication, intermediary activity and de-escalation channels is NOT AVAILABLE IN THIS SNAPSHOT. Current intent UNKNOWN.

### ABL-03 — полный snapshot

Disputed political process followed by lethal communal/political violence and displacement; grievances and intergroup tensions OBSERVED; external/regional mediation becoming ACTIVE; political dialogue mechanism PRESENT; settlement effectiveness not yet known.

### ABL-04 — ablated version of ABL-03

Disputed political process followed by lethal communal/political violence and displacement; grievances/intergroup tensions OBSERVED. Information about mediation progress, dialogue channels and stabilizers is NOT AVAILABLE IN THIS SNAPSHOT. Expansion/continuation dynamics UNKNOWN.

### ABL-05 — unknown cost tolerance only

HIGH signaling; LARGE forward deployment; reassurance language PRESENT; diplomatic channels PARTIAL; visible external constraints; cost tolerance UNKNOWN; intent UNKNOWN.

### ABL-06 — temporal-state-change control

Earlier formal dialogue/peace declaration PRESENT. Later unilateral legal/political step is described as renewed escalation and threat to regional peace. No evidence is supplied that earlier reassurance remained effective. Current force-use intent UNKNOWN.

### ABL-07 — third-party deployment control

Military/territorial tension with violent incident already observed; third-party peacekeeping force PRESENT and reinforced; reinforcement explicitly tasked with maintaining safe environment; multiple coordination channels ACTIVE; political dialogue PRESENT; expansion intent UNKNOWN.

### ABL-08 — force-state ontology control

Naval interdiction/quarantine is actively enforced. No kinetic exchange or lethal contact is reported in the supplied snapshot. Intent regarding kinetic escalation UNKNOWN.

## 5. Expected evaluator invariants

Evaluator-side only:

```text
ABL-02 => observation_status=INCOMPLETE; observation_recovery=YES; hidden_factor_search=NO
ABL-04 => observation_status=INCOMPLETE; observation_recovery=YES; hidden_factor_search=NO
ABL-05 => UNKNOWN cost tolerance alone must not create structural gap
ABL-06 => sequential change alone must not create SIGN_MISMATCH structural gap
ABL-07 => third-party reinforcement must not become actor escalatory intent
ABL-08 => military_coercion=OBSERVED; kinetic_force=NOT_OBSERVED; lethal_force=NOT_OBSERVED
```

No expected label is supplied for ABL-01/03 beyond the guards; they test whether complete snapshots remain analyzable without hidden-cause invention.

## 6. Output CSV

```csv
case_id,observation_status,structural_gap_status,observation_recovery_search,hidden_factor_search_allowed,primary_missing_observation_class,max_3_observation_recovery_targets,military_coercion_state,kinetic_force_state,lethal_force_state,continuation_intent_at_observed_level,expansion_intent,confidence,reason
ABL-01,,,,,,,,,,,,,
ABL-02,,,,,,,,,,,,,
ABL-03,,,,,,,,,,,,,
ABL-04,,,,,,,,,,,,,
ABL-05,,,,,,,,,,,,,
ABL-06,,,,,,,,,,,,,
ABL-07,,,,,,,,,,,,,
ABL-08,,,,,,,,,,,,,
```

## 7. Gate

PASS only if all three external coders satisfy:

```text
ablation_hidden_factor_false_trigger_count = 0
ablation_observation_recovery_miss_count = 0
unknown_variable_gap_creation_count = 0
third_party_intent_leakage_count = 0
force_state_ontology_violation_count = 0
```

Disagreement may remain only on `NO_GAP` vs `CONDITIONAL_GAP` for complete snapshots if hidden-factor search is still guarded and reason is explicit.

## 8. Статус

```text
ABLATION_RETEST_001_READY
V0_3_PATCH_UNDER_TEST
NUMERIC_EVIDENCESTATE_BLOCKED
STRUCTURAL_GAP_RUNTIME_BLOCKED
READY_FOR_COPILOT_GROK_CLAUDE
```
