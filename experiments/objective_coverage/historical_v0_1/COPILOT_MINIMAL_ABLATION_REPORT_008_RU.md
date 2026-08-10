# COPILOT_MINIMAL_ABLATION_REPORT_008

**Статус:** `VALID_RESPONSE / SCHEMA_CONTAMINATION_RESOLVED / ABLATION_GUARD_PASS / ONE_SEMANTIC_OVERTRIGGER_REMAINS`

## 1. Protocol compliance

Copilot returned the exact current schema marker `CMAP-003-OBSREC-V1`, the six required case IDs and the required challenge markers. Old residual-schema fields were absent.

Therefore:

```text
PACKET_SCHEMA_COMPLIANCE = PASS
STALE_TEMPLATE_CONTAMINATION = NOT_OBSERVED
RESULT_VALID_FOR_SCORING = YES
```

## 2. Ablation controls

### QK-42

```text
observation_status = INCOMPLETE
structural_gap_status = NOT_ASSESSABLE
observation_recovery_search = YES
hidden_factor_search_allowed = NO
```

PASS.

### HT-88

```text
observation_status = INCOMPLETE
structural_gap_status = NOT_ASSESSABLE
observation_recovery_search = YES
hidden_factor_search_allowed = NO
```

PASS.

Copilot therefore achieved:

```text
ablation_hidden_factor_false_trigger_rate = 0/2 = 0%
observation_recovery_trigger_rate = 2/2 = 100%
```

Together with the already valid Grok and Claude retests, the three-model ablation guard target is now met on this small controlled set.

## 3. Ontology control

PX-31:

```text
military_coercion_state = OBSERVED
kinetic_force_state = NOT_OBSERVED
lethal_force_state = NOT_OBSERVED
```

PASS.

This supports the distinction:

```text
MILITARY_COERCION != KINETIC_FORCE
KINETIC_FORCE != LETHAL_FORCE
```

## 4. Unknown-variable control

LN-54:

```text
observation_status = SUFFICIENT
structural_gap_status = NO_GAP
```

PASS. Unknown cost tolerance did not become observation incompleteness or a hidden-factor trigger.

```text
UNKNOWN_VARIABLE != OBSERVATION_INCOMPLETE
UNKNOWN_VARIABLE != STRUCTURAL_GAP
```

## 5. Remaining semantic overtrigger: MV-63

Copilot coded the complete-control MV-63 as:

```text
SUFFICIENT
CONDITIONAL_GAP
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY
```

Reason: settlement effectiveness is unknown.

This is too permissive under the intended method. The snapshot already contains observed grievances/tensions plus active mediation and political dialogue. Unknown effectiveness of a stabilizer is not by itself evidence that the causal model contains a missing structural mechanism.

Required rule:

```text
STABILIZER_EFFECTIVENESS_UNKNOWN != STRUCTURAL_GAP
KNOWN_MECHANISM_WITH_UNKNOWN_OUTCOME != MISSING_MECHANISM
```

A future structural gap can be opened only if later observations conflict with what the model can explain, not merely because outcome/effectiveness has not yet been measured.

## 6. Three-model ablation gate

On the controlled missing-observation pairs, valid responses now exist from Grok, Claude and Copilot.

```text
THREE_MODEL_ABLATION_VALID_RESPONSES = 3/3
HIDDEN_FACTOR_FALSE_TRIGGER_ON_ABLATIONS = 0/6 = 0%
OBSERVATION_RECOVERY_TRIGGER_ON_ABLATIONS = 6/6 = 100%
ABLATION_GUARD = PASS_ON_SMALL_CONTROLLED_SET
```

This is not general validation. Sample size is only two ablation types per coder, and the models are not independent human coders or outcome-blind systems.

## 7. Next patch

Add:

```text
STABILIZER_EFFECTIVENESS_UNKNOWN != STRUCTURAL_GAP
KNOWN_MECHANISM_WITH_UNKNOWN_OUTCOME != MISSING_MECHANISM
UNKNOWN_OUTCOME != MODEL_RESIDUAL
```

Then stop repeating the same ablations. Next test should contain novel structural-gap cases where the model actually fails despite sufficient observation, plus matched no-gap controls.

## 8. Status

```text
COPILOT_MINIMAL_RETEST_VALID = YES
SCHEMA_CONTAMINATION_PROBLEM = RESOLVED_FOR_THIS_PACKET
ABLATION_GUARD_3_MODEL = PASS_SMALL_SET
ONTOLOGY_CONTROL = PASS
UNKNOWN_VARIABLE_CONTROL = PASS
SEMANTIC_OVERTRIGGER_MV63 = PATCH_REQUIRED
STRUCTURAL_GAP_INFERENCE_GENERAL_VALIDATION = NOT_CLAIMED
NEXT = NOVEL_RESIDUAL_DISCRIMINATION_SET_001
```
