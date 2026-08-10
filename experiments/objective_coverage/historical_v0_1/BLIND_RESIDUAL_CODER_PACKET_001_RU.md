# BLIND_RESIDUAL_CODER_PACKET 001

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_STRESS_TEST / CASE_NAMES_HIDDEN / OUTCOMES_HIDDEN / STRUCTURAL_GAP_METHOD_UNDER_TEST`

## 1. Назначение

Проверить, способен ли внешний кодировщик применять Structural Gap Inference без выдумывания скрытых причин. Кодировщик получает только обезличенные snapshots A–D и должен сначала проверить, нужен ли hidden-factor search вообще.

## 2. Обязательный порядок

Перед missing-factor hypothesis проверить:

```text
1 DATA_ERROR?
2 CUTOFF_LEAKAGE?
3 SOURCE_DEPENDENCE?
4 OBSERVATION_GAP?
5 WRONG_SCALE?
6 WRONG_ACTOR_AGGREGATION?
7 TEMPORAL_LAG?
8 KNOWN_STABILIZER_OMITTED?
9 KNOWN_PRESSURE_OMITTED?
10 ONLY THEN: MISSING_STRUCTURE_HYPOTHESIS
```

## 3. Guards

```text
DANGEROUS_STATE != STRUCTURAL_GAP
MODEL_RESIDUAL != PROOF_OF_HIDDEN_FACTOR
MISSING_FACTOR_HYPOTHESIS != OBSERVED_FACT
UNEXPLAINED_BEHAVIOR != ACTOR_IRRATIONALITY
OBSERVABILITY_GAP_CAN_MIMIC_HIDDEN_CAUSE
PERSISTENT_PREPARATION != COMMITMENT
FORCE_ALREADY_USED != SYSTEMATIC_EXPANSION_PROVEN
CURRENT_INTENT = UNKNOWN unless directly evidenced
```

## 4. Case A

```text
HIGH signaling
LARGE forward deployment
NO general withdrawal confirmed
past force-use prior PRESENT
reassurance language PRESENT
diplomatic channels PARTIAL
nuclear/international constraints VISIBLE
cost tolerance UNKNOWN
intent UNKNOWN
```

## 5. Case B

```text
HIGH_OR_ELEVATED signaling
ACTIVE military friction risk
first use NOT established
STRONG costly reassurance
FORMAL hotline/deconfliction mechanism
alliance/direct constraints VISIBLE
cost tolerance UNKNOWN
intent UNKNOWN
```

## 6. Case C

```text
HIGH signaling
LARGE unusual concentration near target
STRONG relevant past force-use prior
NO comparable costly withdrawal signal
communication DEGRADED
political/economic costs VISIBLE
cost tolerance UNKNOWN
intent UNKNOWN
```

## 7. Case D

```text
FORCE_ALREADY_USED
LETHAL_FORCE observed
NO comparable costly reassurance
international condemnation VISIBLE
cost tolerance partially revealed by continued force use
expansion intent UNKNOWN
```

## 8. Coding task

Для каждого case заполнить:

```text
case_id
structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | UNKNOWN
primary_residual_type = NONE | LOGICAL_INCONSISTENCY | PERSISTENT_BEHAVIORAL | MISSING_LINK | SCALE_MISMATCH | TIMING_MISMATCH | SIGN_MISMATCH | OBSERVABILITY_RESIDUAL
pre_hidden_explanation_priority = DATA_QUALITY | OBSERVABILITY | SCALE | TEMPORAL_LAG | KNOWN_STABILIZER_PRESSURE | NONE | UNKNOWN
hidden_factor_search_allowed = NO | YES_SEARCH_TRIGGER_ONLY
max_3_hypothesis_classes
max_3_discriminating_evidence_targets
current_intent = UNKNOWN | DIRECTLY_EVIDENCED
confidence = LOW | MEDIUM | HIGH
reason
```

Если текущая модель уже объясняет конфигурацию, необходимо дать `NO_GAP` и НЕ создавать hidden-factor hypotheses.

## 9. Output template

```csv
case_id,structural_gap_status,primary_residual_type,pre_hidden_explanation_priority,hidden_factor_search_allowed,max_3_hypothesis_classes,max_3_discriminating_evidence_targets,current_intent,confidence,reason
A,,,,,,,,,
B,,,,,,,,,
C,,,,,,,,,
D,,,,,,,,,
```

## 10. Evaluator-side invariants

```text
B should allow NO_GAP if stabilizers explain coexistence of danger + restraint
D must not be coded as latent first-use problem
A/C must not convert force-use prior into current intent
NO_GAP => hidden_factor_search_allowed=NO
OPEN/CONDITIONAL gap => hypotheses remain NOT_OBSERVED
```

## 11. Status

```text
BLIND_RESIDUAL_CODER_PACKET_001_READY
OUTCOME_LABELS_HIDDEN
HIDDEN_CAUSE_INVENTION_FORBIDDEN
READY_FOR_COPILOT_GROK_CLAUDE_STRESS_TEST
```
