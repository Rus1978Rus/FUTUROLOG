# HISTORICAL_DEPTH_MANIFEST_SCHEMA v0.1

**Статус:** `WORKING_SCHEMA / NOT_VALIDATED / NOT_CAUSAL_PROOF`

Назначение: хранить исторические узлы и связи для Historical Causal Depth Layer (слоя исторической причинной глубины) без подмены хронологии причинностью.

## Узел

Каждый historical node (исторический узел) должен содержать:

```text
node_id
case_id
depth_level
period_start
period_end
node_type
short_label
claim
source_class
source_ref
confidence
alternative_interpretations
counterevidence_or_limitations
status
```

Допустимые `depth_level`:

```text
H0 CURRENT_SIGNAL
H1 PROXIMATE_PRECONDITION
H2 STRUCTURAL_DRIVER
H3 INSTITUTIONAL_HISTORICAL_FORMATION
H4 META_SYSTEM_CONDITION
H5 PRECURSOR_TO_META_CONDITION
```

## Связь

Каждая связь хранится отдельно:

```text
edge_id
case_id
from_node
to_node
relation_type
mechanism_claim
strength
source_ref
confidence
alternative_mechanism
status
```

Допустимые `relation_type`:

```text
PRECEDES
ENABLES
CONSTRAINS
AMPLIFIES
REDUCES
INSTITUTIONALIZES
RESOURCE_LINK
SECURITY_LINK
IDENTITY_LINK
ECONOMIC_LINK
CONTESTED_CAUSAL_CANDIDATE
```

## Защитные правила

```text
EARLIER != CAUSAL
STRUCTURAL_DRIVER != IMMEDIATE_TRIGGER
TRIGGER != ROOT_CAUSE
META_CONDITION != DIRECT_CAUSE
ONE_NARRATIVE != COMPLETE_HISTORY
CORRELATION != MECHANISM
HISTORICAL_DEPTH != HISTORICAL_INEVITABILITY
```

Исторический узел может быть хорошо подтверждён как факт, но его роль в причинной цепи может оставаться `CONTESTED_CAUSAL_CANDIDATE`.
