# LATENT_PRESSURE / CROSS_DOMAIN_ACCUMULATION v0.1

**Статус:** `DESIGN_DRAFT / CROSS_CASE / NOT_CORE_SCORE / NOT_CALIBRATED / NOT_VALIDATED`

## 1. Назначение

Этот слой предназначен для медленных процессов, которые по отдельности могут выглядеть безобидно, но при длительном совместном движении меняют устойчивость системы.

Ключевая идея:

```text
SMALL_CHANGE × MANY_DOMAINS × LONG_DURATION × SYNCHRONIZATION
!=
ONE_LOUD_EVENT
```

Слой не ищет одну «коренную причину». Он фиксирует PRESSURE (давление), STABILIZER (стабилизатор) и UNKNOWN (неизвестность) по разным доменам.

## 2. Обязательные домены

```text
DEMOGRAPHY_AND_MIGRATION
SOCIAL_FABRIC_AND_TRUST
SOCIAL_INEQUALITY_AND_DISTRIBUTION
IDENTITY_AND_GROUP_BOUNDARIES
RELIGION_AND_RELIGIOUS_INSTITUTIONS
CULTURE_AND_COLLECTIVE_MEMORY
INFORMATION_ECOLOGY
EDUCATION
HEALTH_AND_PSYCHOSOCIAL_STRESS
CRIMINAL_AND_SHADOW_ECONOMY
TECHNOLOGY_AND_INFRASTRUCTURE
CLIMATE_AND_ENVIRONMENT
FOOD_SECURITY
WATER_SECURITY
FUEL_AND_ENERGY_ACCESS
LAND_AND_RESOURCE_ACCESS
```

Новые домены добавляются только версионно.

## 3. Базовые потребности и физическая среда

Для еды, воды и топлива разделять наличие и реальный доступ:

```text
FOOD_AVAILABLE != FOOD_AFFORDABLE
WATER_EXISTS != SAFE_WATER_ACCESS
FUEL_EXISTS != FUEL_DELIVERABLE
NATIONAL_SUPPLY != LOCAL_ACCESS
COUNTRY_NORMAL != REGION_NORMAL
```

Климатические события не считаются автоматической причиной конфликта:

```text
CLIMATE_EVENT != CONFLICT_CAUSE
```

Нужен промежуточный механизм: урожай, цена, доход, миграция, доступ к воде, инфраструктура или иной доказуемый канал.

## 4. Социальное неравенство как отдельный домен

`SOCIAL_INEQUALITY_AND_DISTRIBUTION` нельзя сводить только к коэффициенту Джини.

Минимальные подоси:

```text
income_inequality
wealth_inequality
regional_inequality
urban_rural_gap
group_based_inequality
service_access_gap
housing_and_food_affordability
youth_unemployment
social_mobility
perceived_unfairness
status_loss
```

## 5. Неравенство относительно механизма легитимации

Политический режим не задаётся только ярлыком `democracy / authoritarian`.

Для каждого кейса отдельно устанавливается:

```text
LEGITIMACY_BEARING_GROUP
```

то есть группа или группы, реально участвующие в воспроизводстве и легитимации существующей системы.

### 5.1. Реальная или номинальная демократия

Отдельно отслеживать:

```text
ACTIVE_ELECTORATE_INEQUALITY_PRESSURE
```

Это давление неравенства на политически активный электорат: голосующих, вовлечённых граждан, членов партий/профсоюзов/общественных организаций и иных доказуемо активных групп.

### 5.2. Недемократическая система

Отдельно отслеживать:

```text
LEGITIMIZING_STRATUM_INEQUALITY_PRESSURE
```

Это давление на слой, который поддерживает или воспроизводит систему: конкретный состав не предполагается заранее и должен устанавливаться evidence (свидетельствами) для каждой страны.

Возможные группы — бюрократия, силовые структуры, армия, госслужащие, бизнес-группы, религиозные институты, региональные или этнические группы — только если их роль доказана для данного кейса.

### 5.3. Потеря статуса и разрыв ожиданий

Отдельные признаки:

```text
STATUS_LOSS_OF_LEGITIMACY_GROUP
EXPECTATION_REALITY_GAP
```

Фиксируется не только абсолютная бедность, но и ухудшение положения группы относительно её собственного прошлого, ожидаемого общественного договора и других групп.

## 6. Guard-правила

```text
INEQUALITY != DISCONTENT
DISCONTENT != DELEGITIMIZATION
DELEGITIMIZATION != PROTEST
PROTEST != CONFLICT
STATUS_LOSS != RADICALIZATION
RELIGIOUS_DIFFERENCE != RELIGIOUS_CONFLICT
CULTURAL_CHANGE != POLITICAL_CAUSE
DEMOGRAPHIC_CHANGE != THREAT
```

Переход между состояниями должен иметь отдельную доказательную связь.

## 7. Единица записи

Каждая запись latent pressure должна иметь:

```text
pressure_id
case_id
snapshot_id
domain
subdomain
geography
affected_group
legitimacy_role
signal_direction
magnitude_class
persistence_class
change_rate_class
pressure_or_stabilizer
claim
mechanism_to_next_layer
source_family
original_publication_time
source_ref
cutoff_admissibility
evidence_quality
confidence
counterevidence
alternative_explanations
status
```

### signal_direction

```text
INCREASING
DECREASING
STABLE
MIXED
UNKNOWN
```

### pressure_or_stabilizer

```text
PRESSURE
STABILIZER
MIXED
UNKNOWN
```

## 8. Cross-domain accumulation

Слой не должен просто складывать баллы.

Сначала проверяются:

```text
PERSISTENCE
SYNCHRONIZATION
DOMAIN_DIVERSITY
GEOGRAPHIC_OVERLAP
GROUP_OVERLAP
MECHANISTIC_LINKS
COUNTERVAILING_STABILIZERS
EVIDENCE_COVERAGE
```

Высокое междоменное накопление допустимо только когда несколько доменов движутся согласованно во времени и есть доказательства их пересечения через группы, территорию или механизм.

Инвариант:

```text
MANY_WEAK_SIGNALS != STRONG_CAUSAL_CLAIM
```

## 9. Стабилизаторы обязательны

Для каждого PRESSURE-класса искать STABILIZER-класс.

Примеры:

```text
rising_prices ↔ wage_support / subsidies
polarization ↔ cross-group institutions
resource_shortage ↔ substitution / imports
status_loss ↔ mobility / compensation
migration_pressure ↔ absorption capacity
religious_tension ↔ interfaith institutions
```

Отсутствие найденного стабилизатора не означает его отсутствия в реальности.

## 10. Связь с Historical Depth и Resource Sustainment

```text
HISTORICAL_DEPTH
→ STRUCTURAL_CONTEXT
→ LATENT_PRESSURE / STABILIZERS
→ RESOURCE_SUSTAINMENT
→ CAPABILITY / CONSTRAINT
→ OBSERVED_ACTION
```

Эта стрелка не является автоматической причинной цепью. Каждый edge (ребро) требует отдельной доказательной записи.

## 11. Связь с Objective/Coverage

Latent Pressure не входит напрямую в `effective_confidence`.

Objective/Coverage оценивает качество и полноту evidence (свидетельств) по этому слою.

```text
LATENT_PRESSURE_LEVEL != EVIDENCE_CONFIDENCE
```

## 12. Пилотные кейсы

Одинаковая схема применяется к:

```text
RUSSIA_UKRAINE_2021_2022
MYANMAR_POST_COUP_2021
```

Нельзя добавлять признак только потому, что он известен как важный для одного из двух исходов. Схема должна оставаться переносимой.

## 13. Текущий статус

```text
DESIGN_ACCEPTED_FOR_HISTORICAL_COLLECTION
NO_SINGLE_LATENT_PRESSURE_SCORE
NO_AUTOMATIC_CAUSAL_CHAIN
NOT_CALIBRATED
NOT_VALIDATED
```
