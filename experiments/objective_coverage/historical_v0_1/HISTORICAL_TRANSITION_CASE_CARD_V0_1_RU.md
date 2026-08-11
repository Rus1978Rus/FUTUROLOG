# HISTORICAL TRANSITION CASE CARD v0.1

**Статус:** `TEMPLATE / SOURCE_BACKED / CUTOFF_DISCIPLINE_REQUIRED / OUTCOME_BLIND_COMPATIBLE`

## 1. Идентификатор

- `case_id`
- `system_name`
- `transition_family`
- `geography`
- `time_window`

## 2. Cutoff

- `cutoff_datetime`
- `cutoff_rationale`
- `post_cutoff_knowledge_forbidden = YES`

## 3. Наблюдаемое состояние на cutoff

- `formal_state_capacity`
- `effective_command_execution`
- `coercive_capacity`
- `coercive_capacity_political_usability`
- `elite_cohesion`
- `critical_node_loyalty`
- `alternative_power_centers`
- `mass_mobilization`
- `economic_pressure`
- `resource_distribution_pressure`
- `perceived_fairness_pressure`
- `external_support_available`
- `external_support_deployed`
- `external_constraints`
- `communication_channels`
- `reassurance_or_stabilizers`
- `exit_option_for_incumbent_elite`
- `periphery_hold_cost`
- `value_after_relinquishing_control`

## 4. Structural observations

```text
INSTITUTIONS_EXIST != INSTITUTIONS_WILL_EXECUTE
COERCIVE_CAPACITY_EXISTS != COERCIVE_CAPACITY_IS_POLITICALLY_USABLE
FORMAL_STATE_CAPACITY != EFFECTIVE_COHESION
RESOURCE_ABUNDANCE != SYSTEM_COHESION
TERRITORIAL_LOSS != SYSTEMIC_LOSS
REGIME_COLLAPSE != STATE_COLLAPSE
```

## 5. Known mechanisms already in model

Перечислить механизмы, которыми текущая модель уже способна объяснить состояние. Не создавать hidden factor до проверки этого блока.

## 6. Observation sufficiency

- `observation_status = SUFFICIENT | INCOMPLETE`
- `missing_diagnostic_classes`
- `observation_recovery_targets`

Если `INCOMPLETE`:

```text
structural_gap_status = NOT_ASSESSABLE
hidden_factor_search_allowed = NO
```

## 7. Model expectation

Что текущая модель ожидает на коротком следующем горизонте при известных boundary conditions.

## 8. Residual check

- `observed_next_slice`
- `residual_persistence`
- `pre_hidden_resolution`
- `structural_gap_status`
- `hidden_factor_search_allowed`

## 9. Candidate trajectories — без выбора исхода

Допустимые классы:

```text
SURVIVE_BY_REPRESSION
SURVIVE_BY_EXTERNAL_SUPPORT
REFORM_AND_SURVIVE
NEGOTIATED_TRANSFORMATION
POWER_TRANSFER_STATE_SURVIVES
CONTROLLED_PERIPHERY_RELEASE
FORCED_PERIPHERY_LOSS
PROLONGED_RETENTION_WAR
REGIME_COLLAPSE_STATE_SURVIVES
SYSTEM_FRAGMENTATION
UNKNOWN
```

## 10. Discriminating evidence targets

Не «что подтверждает любимую гипотезу», а что различает минимум две конкурирующие траектории.

## 11. Outcome block — evaluator only

Заполняется отдельно и скрывается от blind coder:

- `actual_transition`
- `outcome_date`
- `distance_from_cutoff`
- `first_structurally_distinguishable_point`

## 12. Sources

Каждый factual claim должен иметь:

- `source_url`
- `publication_date`
- `source_type`
- `claim_supported`
- `cutoff_admissibility`
- `limitations`

## 13. Guards

```text
HISTORICAL_OUTCOME != INPUT_FEATURE
POST_EVENT_SYNTHESIS != CUTOFF_KNOWLEDGE
SURVIVED_CRISIS_t != LONG_TERM_STABILITY
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
EXPECTED_EXTERNAL_BACKING != OBSERVED_EXTERNAL_DEPLOYMENT
LOSS_OF_POLITICAL_MONOPOLY != LOSS_OF_ALL_ELITE_RESOURCES
UNKNOWN_OUTCOME != STRUCTURAL_GAP
```
