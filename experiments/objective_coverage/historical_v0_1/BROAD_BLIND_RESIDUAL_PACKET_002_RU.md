# BROAD_BLIND_RESIDUAL_PACKET 002

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_STRESS_TEST / 12_CASES / ANONYMIZED / OUTCOMES_HIDDEN`

## 1. Задача

Для каждого обезличенного snapshot определить, существует ли настоящий structural gap. Не пытаться определить страну/событие. Не использовать будущий исход.

Перед hidden-factor hypothesis обязательно проверить: data quality, cutoff leakage, source dependence, observability gap, wrong scale, wrong actor aggregation, temporal lag, omitted known stabilizer/pressure.

## 2. Guards

```text
UNKNOWN_VARIABLE != STRUCTURAL_GAP
MISSING_MEASUREMENT != MISSING_MECHANISM
DANGEROUS_STATE != STRUCTURAL_GAP
MODEL_RESIDUAL != PROOF_OF_HIDDEN_FACTOR
OBSERVABILITY_GAP_CAN_MIMIC_HIDDEN_CAUSE
PAST_FORCE_USE != CURRENT_INTENT
PAST_REASSURANCE != DURABLE_RESTRAINT
THIRD_PARTY_SECURITY_DEPLOYMENT != ACTOR_ESCALATORY_INTENT
FORCE_ALREADY_USED != EXPANSION_INTENT_EVIDENCED
NO_GAP => primary_structural_residual_type=NONE
NO_GAP => hidden_factor_search_allowed=NO
```

## 3. Snapshots

### Q01
HIGH signaling; LARGE unusual concentration near target; relevant past force-use prior PRESENT; no comparable costly withdrawal signal; communication DEGRADED; political/economic costs VISIBLE; cost tolerance UNKNOWN; current intent UNKNOWN.

### Q02
Armed incidents already occurred in disputed border zone; external institutions call for permanent ceasefire; regional mediation mechanism ACTIVE; provisional demilitarization/withdrawal mechanism AVAILABLE; expansion intent UNKNOWN.

### Q03
HIGH/ELEVATED signaling and active military-friction risk; first use NOT established; STRONG costly reassurance; FORMAL hotline/deconfliction mechanism; alliance/direct constraints VISIBLE; intent UNKNOWN.

### Q04
Disputed political process followed by lethal communal/political violence and displacement; grievances and intergroup tensions OBSERVED; external/regional mediation becoming ACTIVE; political dialogue mechanism PRESENT; settlement effectiveness not yet known.

### Q05
Military confrontation at extreme readiness; strategic weapons issue; naval interdiction/quarantine underway; readiness escalated; adversary capabilities nearing operational status; direct/indirect leadership communication ACTIVE; international intermediary urging both sides to avoid direct confrontation; current intent regarding first strike UNKNOWN.

### Q06
FORCE_ALREADY_USED; lethal force OBSERVED; no comparable costly reassurance; international condemnation VISIBLE; cost tolerance partially revealed by continued force use; expansion intent UNKNOWN.

### Q07
Military/territorial tension with violent incident already observed; third-party peacekeeping force PRESENT and reinforced; reinforcement explicitly tasked with maintaining safe environment; multiple coordination channels ACTIVE; political dialogue channel PRESENT; parties called to de-escalate; expansion intent UNKNOWN.

### Q08
HIGH signaling; LARGE forward deployment; no general withdrawal confirmed; past force-use prior PRESENT; reassurance language PRESENT; diplomatic channels PARTIAL; nuclear/international constraints VISIBLE; cost tolerance UNKNOWN; intent UNKNOWN.

### Q09
Border-security incident injures military personnel; tensions elevated; armistice obligations and dialogue explicitly invoked by international actor; communication/negotiation route remains available; no broad force expansion established in snapshot; intent UNKNOWN.

### Q10
Territorial dispute; formal dialogue/peace declaration exists from an earlier phase; later unilateral legal/political step is described by regional organization as renewed escalation and threat to regional peace; no assumption that earlier reassurance remains effective; current force-use intent UNKNOWN.

### Q11
Military confrontation at extreme readiness; strategic weapons issue; naval interdiction/quarantine underway; readiness escalated; adversary capabilities nearing operational status. Information about leadership communication, intermediary activity and de-escalation channels is NOT AVAILABLE IN THIS SNAPSHOT. Current intent UNKNOWN.

### Q12
Disputed political process followed by lethal communal/political violence and displacement; grievances/intergroup tensions OBSERVED. Information about mediation progress, dialogue channels and stabilizers is NOT AVAILABLE IN THIS SNAPSHOT. Expansion/continuation dynamics UNKNOWN.

## 4. Coding schema

Для каждого Q01–Q12 вернуть:

- `structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | UNKNOWN`
- `primary_structural_residual_type = NONE | LOGICAL_INCONSISTENCY | PERSISTENT_BEHAVIORAL | MISSING_LINK | SCALE_MISMATCH | TIMING_MISMATCH | SIGN_MISMATCH | OBSERVABILITY_RESIDUAL`
- `pre_hidden_explanation_priority = DATA_QUALITY | OBSERVABILITY | SCALE | TEMPORAL_LAG | KNOWN_STABILIZER_PRESSURE | NONE | UNKNOWN`
- `hidden_factor_search_allowed = NO | YES_SEARCH_TRIGGER_ONLY`
- `max_3_hypothesis_classes`
- `max_3_discriminating_evidence_targets`
- `current_force_use_state = NOT_OBSERVED | OBSERVED | UNKNOWN`
- `continuation_intent_at_observed_level = UNKNOWN | DIRECTLY_EVIDENCED`
- `expansion_intent = UNKNOWN | DIRECTLY_EVIDENCED`
- `confidence = LOW | MEDIUM | HIGH`
- `reason`

Если `NO_GAP`, hypothesis/evidence target fields должны быть пустыми/NONE.

## 5. Output CSV

```csv
case_id,structural_gap_status,primary_structural_residual_type,pre_hidden_explanation_priority,hidden_factor_search_allowed,max_3_hypothesis_classes,max_3_discriminating_evidence_targets,current_force_use_state,continuation_intent_at_observed_level,expansion_intent,confidence,reason
Q01,,,,,,,,,,,
Q02,,,,,,,,,,,
Q03,,,,,,,,,,,
Q04,,,,,,,,,,,
Q05,,,,,,,,,,,
Q06,,,,,,,,,,,
Q07,,,,,,,,,,,
Q08,,,,,,,,,,,
Q09,,,,,,,,,,,
Q10,,,,,,,,,,,
Q11,,,,,,,,,,,
Q12,,,,,,,,,,,
```

## 6. Запреты

- Не угадывать названия стран.
- Не использовать знание последующего исхода.
- Не считать неизвестный intent скрытым фактором.
- Не считать отсутствие данных доказательством тайного механизма.
- Не считать peacekeeping reinforcement доказательством эскалационного намерения стороны конфликта.
- Не считать сам факт mediation доказательством успешной стабилизации.

## 7. Status

```text
BROAD_BLIND_RESIDUAL_PACKET_002_READY
12_CASES
COUNTRY_LABELS_HIDDEN
OUTCOMES_HIDDEN
CONTROLLED_OBSERVABILITY_ABLATIONS_INCLUDED
READY_FOR_EXTERNAL_CODERS
```
