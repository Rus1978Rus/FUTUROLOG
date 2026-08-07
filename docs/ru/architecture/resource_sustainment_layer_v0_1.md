# RESOURCE_SUSTAINMENT_LAYER v0.1
## Ресурсная устойчивость конфликтов и кризисов

**Статус:** `DESIGN_DRAFT / CROSS_CASE / NOT_CORE_SCORE / NOT_CALIBRATED / NOT_VALIDATED`

## 1. Назначение

FUTUROLOG должен анализировать не только то, что участник конфликта делает, но и за счёт каких ресурсов он способен продолжать действия.

Ключевой вопрос:

```text
WHO
→ PROVIDES WHAT
→ TO WHOM
→ THROUGH WHICH CHANNEL
→ HOW REGULARLY
→ FOR WHICH CAPABILITY
→ WITH WHAT BOTTLENECKS
→ WHAT HAPPENS IF THE FLOW STOPS
```

Это не сводится к денежному финансированию.

## 2. Основной инвариант

```text
TRADE_RELATION != WAR_FINANCING
CORRELATION != MATERIAL_SUPPORT
RESOURCE_ACCESS != RESOURCE_CONTROL
DECLARED_SUPPORT != DELIVERED_SUPPORT
MONEY_AVAILABLE != OPERATIONAL_CAPABILITY
```

Любая связь между внешним actor (участником) и стороной конфликта должна хранить тип связи и доказательную основу. Нельзя автоматически превращать торговлю, дипломатическую близость или совпадение интересов в утверждение о финансировании войны.

## 3. Resource classes (классы ресурсов)

Минимальный словарь:

```text
PUBLIC_FINANCE
TAX_REVENUE
FOREIGN_EXCHANGE_RESERVES
EXTERNAL_FINANCIAL_AID
CREDIT
ARMS_AND_AMMUNITION
FUEL_AND_ENERGY
INDUSTRIAL_PRODUCTION
RAW_MATERIALS
EXPORT_REVENUE
LOGISTICS_AND_TRANSPORT
COMMUNICATIONS
FOOD_AND_BASIC_SUPPLY
HUMAN_RESOURCES
DIASPORA_AND_DONATIONS
CAPTURED_RESOURCES
ILLICIT_OR_SHADOW_TRADE
TERRITORIAL_REVENUE
SANCTIONS_EVASION_CAPACITY
```

Словарь расширяемый, но новые классы добавляются версионно.

## 4. Resource-flow graph (граф ресурсных потоков)

Базовое ребро:

```text
SOURCE_ACTOR
→ CHANNEL
→ RECEIVER_ACTOR
→ RESOURCE_CLASS
→ CAPABILITY
→ ACTION
```

Пример структуры без утверждения о конкретном конфликте:

```text
external donor
→ banking channel
→ actor A
→ EXTERNAL_FINANCIAL_AID
→ payroll / procurement capacity
→ sustained operations
```

Другой вариант:

```text
resource territory
→ extraction / taxation
→ actor B
→ TERRITORIAL_REVENUE
→ logistics / recruitment
→ continued resistance
```

## 5. Обязательные поля каждого потока

```text
flow_id
case_id
source_actor_id
receiver_actor_id
intermediary_actor_ids
resource_class
resource_description
channel_type
start_time
end_time_or_open
amount_value
amount_unit
amount_status
frequency
regularity
purpose_claimed
capability_supported
directness
legal_status
source_family
original_publication_time
provenance_status
evidence_quality
confidence
alternative_explanations
counterevidence_ids
```

### amount_status

```text
EXACT
ESTIMATED_RANGE
ORDER_OF_MAGNITUDE
UNKNOWN
```

Отсутствие суммы не делает поток равным нулю.

### directness

```text
DIRECT
INDIRECT
SYSTEMIC
UNRESOLVED
```

`SYSTEMIC` означает, что поток поддерживает общую экономическую способность actor, но не доказано, что он направлен на конкретное военное действие.

## 6. Resource Sustainment State

Для каждого actor и snapshot система должна уметь описать отдельно:

```text
resource_availability
resource_diversification
external_dependency
internal_revenue_capacity
logistics_viability
replacement_options
sanctions_pressure
bottleneck_severity
flow_persistence
resource_uncertainty
```

Пока это отдельные показатели, а не одна итоговая цифра.

## 7. Почему нельзя сразу делать один funding_score

Одинаковая сумма денег может иметь разный эффект.

```text
MONEY
+ NO_FUEL
+ NO_AMMUNITION
+ BROKEN_LOGISTICS
→ LOW_OPERATIONAL_CONVERSION
```

и наоборот:

```text
MODEST_MONEY
+ LOCAL_PRODUCTION
+ TERRITORIAL_TAXATION
+ SHORT_LOGISTICS
→ POSSIBLE_HIGH_SUSTAINMENT
```

Поэтому вводится различие:

```text
RESOURCE_VOLUME
!=
RESOURCE_CONVERSION_TO_CAPABILITY
```

## 8. Bottleneck logic (логика узких мест)

FUTUROLOG должен искать не только большие потоки, но и критические зависимости.

Примеры классов bottleneck (узкого места):

```text
SINGLE_SUPPLIER_DEPENDENCY
SINGLE_ROUTE_DEPENDENCY
FUEL_DEPENDENCY
AMMUNITION_DEPENDENCY
FOREIGN_EXCHANGE_DEPENDENCY
PORT_OR_BORDER_DEPENDENCY
COMMUNICATIONS_DEPENDENCY
INDUSTRIAL_COMPONENT_DEPENDENCY
RECRUITMENT_DEPENDENCY
```

Сильный денежный поток не должен автоматически компенсировать полный провал критического bottleneck.

## 9. Partner switching и redundancy

Из будущего Strategic Interaction Layer импортируется только структурный принцип:

```text
ONE_CRITICAL_PROVIDER
→ HIGH_DEPENDENCY

MULTIPLE_SUBSTITUTABLE_PROVIDERS
→ HIGHER_REDUNDANCY
```

Это не доказательство политической надёжности партнёров. Это оценка заменяемости ресурсного потока.

## 10. Связь с Objective / Coverage

Resource Sustainment не входит напрямую в `effective_confidence`.

Он поставляет evidence (свидетельства) и отдельные domain features (предметные признаки).

Objective/Coverage затем оценивает:

```text
сколько ресурсной картины мы вообще видим;
насколько источники независимы;
насколько данные свежи;
насколько полный pipeline;
сколько противоречий и шума.
```

Инвариант:

```text
RESOURCE_SUSTAINMENT_SCORE
!=
EVIDENCE_CONFIDENCE
```

## 11. Связь с Notarius / provenance

Каждый material flow (материальный поток) должен быть трассируем до источника.

```text
CLAIMED_TRANSFER
→ SOURCE
→ ORIGINAL_DATE
→ PARSED_VALUE
→ NORMALIZED_FLOW
→ ANALYTIC_USE
```

Непроверенный пересказ не получает статус VERIFIED FLOW.

## 12. Типы доказательств

Приоритетные классы:

```text
OFFICIAL_BUDGET_OR_CUSTOMS_DATA
SANCTIONS_OR_ENFORCEMENT_RECORD
AUDITED_OR_REGULATORY_DISCLOSURE
TRADE_DATA
SATELLITE_OR_LOGISTICS_OBSERVATION
COURT_OR_SEIZURE_RECORD
CREDIBLE_INVESTIGATIVE_REPORT
CREDIBLE_NEWS_REPORT
ACTOR_CLAIM
UNVERIFIED_OSINT
```

`ACTOR_CLAIM` не становится фактом только потому, что заявление официальное.

## 13. Historical evaluation extension

Для каждого historical snapshot добавляется параллельный resource record:

```text
snapshot_id
actor_id
known_resource_flows_at_cutoff
unknown_resource_domains
critical_bottlenecks
replacement_options
resource_counterevidence
resource_provenance_coverage
```

Запрещено использовать сведения о поставке/финансировании, опубликованные после cutoff, как будто они были известны системе до cutoff.

## 14. Первый пилот: Myanmar

Для Myanmar post-coup civil-war pilot отслеживаются как минимум две стороны/семейства actor:

```text
MILITARY_STATE_APPARATUS
ANTI_COUP_RESISTANCE_NETWORKS
```

и отдельно связанные ethnic armed organizations (этнические вооружённые организации), где доказана собственная ресурсная база или материальная связь.

Особое внимание:

```text
state revenue and foreign-exchange access
state-owned / military-linked economic assets
arms / fuel / logistics access
border trade
natural-resource revenue
territorial taxation
local donations / diaspora support
informal transfer channels
captured material
cross-border sanctuary / logistics
```

Ни один внешний actor заранее не маркируется как `FUNDER`. Статус появляется только из evidence-records.

## 15. Второй пилот: Russia–Ukraine

Тот же слой применяется без изменения схемы:

```text
public budgets
energy/export revenue
external aid
weapons supply
industrial capacity
foreign-exchange constraints
sanctions pressure / evasion
logistics
critical components
replacement suppliers
```

Это позволяет проверять переносимость схемы между асимметричной гражданской войной и межгосударственной войной.

## 16. Текущий статус

```text
DESIGN_ACCEPTED_FOR_HISTORICAL_DATA_COLLECTION
NO_SINGLE_RESOURCE_SCORE
NO_CAUSAL_FINANCING_CLAIMS_WITHOUT_EVIDENCE
NOT_CALIBRATED
NOT_VALIDATED
```

Следующий шаг: добавить resource-flow manifests к обоим историческим корпусам и собирать их синхронно с обычным evidence collection.