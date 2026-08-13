# HPNR schema v0.2 notes

Статус: semantic patch / next-test preparation / not final.

## Parent relation

CO_MEMBER_OF_SAME_PARENT != DIRECT_SUBORDINATION.

If topology is P -> {A,B,...} and B is not administratively inside A, then formal_parent_relation = SAME_PARENT_SYSTEM.

## Separate substitution signal from prevalence

Use:

parent_node_substitution_signal = ABSENT | PRESENT | NOT_APPLICABLE | UNKNOWN

parent_node_substitution_prevalence = ISOLATED | CONTESTED | SUBSTANTIAL | DOMINANT | UNKNOWN | NOT_APPLICABLE

parent_node_substitution_assessment = NO | POSSIBLE | OBSERVED | NOT_ASSESSABLE | NOT_APPLICABLE

Mapping:
- ABSENT -> NO
- PRESENT + ISOLATED/CONTESTED -> POSSIBLE
- PRESENT + SUBSTANTIAL/DOMINANT -> OBSERVED
- NOT_APPLICABLE -> NOT_APPLICABLE

## Continuity identity boundary

CONTINUITY_IDENTITY_CLAIM != TERRITORIAL_PARENT_RELATION.

If a case concerns only historical or imperial continuity and does not contain a meaningful parent-child territorial topology, code substitution fields as NOT_APPLICABLE.

## Split successor dominance from continuator status

successor_weight = DOMINANT | COEQUAL | MIXED | UNKNOWN

exclusive_continuator_status = YES | NO | DISPUTED | UNKNOWN | NOT_APPLICABLE

successor_count_structure = SINGLE_SUCCESSOR | MULTIPLE_SUCCESSORS | UNKNOWN

DOMINANT_SUCCESSOR != EXCLUSIVE_CONTINUATOR.
EXCLUSIVE_CONTINUATOR != FORMER_PARENT.
SUCCESSOR_WEIGHT != PARENT_RELATION.

## Reference-frame fields

Add:

institutional_parent_at_T0
claimed_parent_at_later_T
reference_frame = LEGAL | INSTITUTIONAL | HISTORICAL_IDENTITY | POLITICAL_NARRATIVE | MIXED

This permits explicit representation of institutional_parent_at_T0 = P and claimed_parent_at_later_T = A without converting a narrative claim into factual topology.

## Additional invariants

LIVING_WITNESS != SHARED_MEMORY_STABILITY
MEMORY_CONTINUITY != INSTITUTIONAL_CONTINUITY
SUCCESSOR_DOMINANCE != HISTORICAL_PARENTAGE
RETROSPECTIVE_PARENT_CLAIM != OBSERVED_PARENT_RELATION
NARRATIVE_PREVALENCE != FACTUAL_VALIDITY

## Next-test target

Use new cases rather than repeating HPNR-001. Include strong positive, weak/contested, genuine direct-subordination control, continuity-only, dominant-successor-without-substitution, multiple-successor identity-capture attempt, living-witness divergence, and long identity-lag case.
