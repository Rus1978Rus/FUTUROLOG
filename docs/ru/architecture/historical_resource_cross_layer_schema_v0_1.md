# HISTORICAL_RESOURCE_CROSS_LAYER_SCHEMA v0.1

**Статус:** `DESIGN_DRAFT / CROSS_LAYER / NO_CAUSAL_AUTOMATION / NOT_VALIDATED`

## Назначение

Связать Historical Causal Depth Layer (историческая причинная глубина) с Resource Sustainment Layer (ресурсная устойчивость), не превращая историческую последовательность или экономическую связь в доказанную причинность.

Базовая конструкция:

```text
HISTORICAL_NODE
→ CROSS_LAYER_RELATION
→ RESOURCE_FLOW_OR_RESOURCE_STRUCTURE
→ CAPABILITY
→ OBSERVED_ACTION_OR_PERSISTENCE
```

## Допустимые типы связей

```text
CREATES_RESOURCE_STRUCTURE
ENABLES_RESOURCE_ACCESS
SHAPES_REVENUE_BASE
SHAPES_LOGISTICS_ROUTE
SHAPES_EXTERNAL_DEPENDENCY
SHAPES_DOMESTIC_PRODUCTION
SHAPES_TERRITORIAL_REVENUE
SHAPES_SANCTIONS_EXPOSURE
SHAPES_REPLACEMENT_OPTIONS
CONSTRAINS_RESOURCE_ACCESS
AMPLIFIES_RESOURCE_DEPENDENCY
RESOURCE_STRUCTURE_PERSISTS_FROM
RESOURCE_STRUCTURE_TRANSFORMS_FROM
```

Эти типы описывают кандидатную структурную связь. Они не равны утверждению о мотивации или прямой причине конфликта.

## Обязательные поля cross-layer edge

```text
cross_edge_id
case_id
historical_node_id
resource_target_type
resource_target_id_or_class
relation_type
mechanism_claim
period_start
period_end
source_ref
evidence_quality
confidence
alternative_interpretations
counterevidence_or_limitations
status
```

`resource_target_type`:

```text
FLOW
RESOURCE_CLASS
RESOURCE_STRUCTURE
BOTTLENECK
ROUTE
REVENUE_BASE
DEPENDENCY
CAPABILITY
```

## Защитные инварианты

```text
HISTORICAL_PRECEDENT != RESOURCE_CAUSE
RESOURCE_STRUCTURE != WAR_MOTIVE
RESOURCE_ACCESS != RESOURCE_USE
RESOURCE_USE != OPERATIONAL_EFFECT
TRADE_ROUTE != MILITARY_SUPPLY_ROUTE
STATE_REVENUE != MILITARY_EXPENDITURE
LONG_TERM_DEPENDENCY != IMMEDIATE_TRIGGER
```

Если конкретный material flow (материальный поток) ещё не подтверждён, edge должен иметь статус `PENDING_FLOW_EVIDENCE`, а не подставной flow_id.

## Временная дисциплина

Для исторического backtest (ретроспективного теста) каждая связь должна различать:

- `historical_truth_time` — когда структура/поток существовал;
- `public_observability_time` — когда это было доступно наблюдателю;
- `cutoff_eligibility` — мог ли FUTUROLOG знать это в конкретном snapshot.

Инвариант:

```text
KNOWN_NOW_ABOUT_PAST != OBSERVABLE_THEN
```

## Использование в FUTUROLOG

Cross-layer graph не входит напрямую в `effective_confidence`.

Он поставляет структурные признаки:

```text
resource_path_dependency
resource_path_redundancy
historical_persistence
institutional_resource_lock_in
resource_conversion_constraints
```

Objective/Coverage отдельно оценивает доказательную полноту этих признаков.

## Текущий статус

`READY_FOR_SEED_CANDIDATE_EDGES / NOT_READY_FOR_CAUSAL_SCORING`