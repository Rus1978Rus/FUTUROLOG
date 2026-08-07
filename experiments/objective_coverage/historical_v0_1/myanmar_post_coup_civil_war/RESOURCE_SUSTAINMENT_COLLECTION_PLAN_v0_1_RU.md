# RESOURCE_SUSTAINMENT_COLLECTION_PLAN v0.1
## Myanmar post-coup civil-war pilot

**Статус:** `COLLECTION_PLAN_FROZEN / EVIDENCE_NOT_YET_COMPLETE / NOT_VALIDATED`

## 1. Цель

Параллельно с обычным historical evidence collection собрать ресурсную картину конфликта на каждом cutoff.

Не вопрос «кто хороший / кто плохой», а вопрос:

```text
какие actor имеют какие ресурсы;
откуда ресурсы поступают;
насколько потоки устойчивы;
какие каналы заменяемы;
какие bottleneck (узкие места) ограничивают продолжение действий.
```

## 2. Actor families

Минимум:

```text
MILITARY_STATE_APPARATUS
NUG_PDF_NETWORKS
ETHNIC_ARMED_ORGANIZATIONS
LOCAL_DEFENSE_FORCES
EXTERNAL_STATE_ACTORS
DIASPORA_AND_DONOR_NETWORKS
COMMERCIAL_INTERMEDIARIES
```

Actor family — аналитическая категория. Она не означает единую командную структуру.

## 3. Обязательные resource classes

Для каждого snapshot явно искать evidence и counterevidence по:

```text
PUBLIC_FINANCE
EXPORT_REVENUE
FOREIGN_EXCHANGE_ACCESS
ARMS_AND_AMMUNITION
FUEL_AND_ENERGY
LOGISTICS_AND_BORDER_ACCESS
NATURAL_RESOURCE_REVENUE
TERRITORIAL_TAXATION
DIASPORA_AND_DONATIONS
INFORMAL_FINANCE
LOCAL_PRODUCTION
CAPTURED_RESOURCES
HUMAN_RESOURCES
COMMUNICATIONS
SANCTIONS_PRESSURE_OR_EVASION
```

## 4. Запрет подтверждающего отбора

Для каждого предполагаемого потока искать:

```text
SUPPORTING_EVIDENCE
COUNTEREVIDENCE
ALTERNATIVE_EXPLANATION
```

Пример:

```text
рост торговли
```

не кодируется автоматически как:

```text
финансирование стороны конфликта
```

Нужно различать:

```text
GENERAL_ECONOMIC_RELATION
SYSTEMIC_REVENUE_SUPPORT
DIRECT_TRANSFER
MILITARY_MATERIAL_TRANSFER
UNRESOLVED
```

## 5. Snapshot discipline

На каждом cutoff сохраняется только информация, которая была публично доступна не позже cutoff.

Поздний расследовательский материал может использоваться только:

- для post-hoc audit (последующей проверки), что тогда существовало;
- НЕ для увеличения pre-cutoff score, если соответствующий факт не был доступен системе в тот момент.

Инвариант:

```text
LATER_DISCOVERY_OF_OLD_FLOW
!=
FLOW_OBSERVABLE_AT_OLD_CUTOFF
```

## 6. Source priorities

Приоритет:

1. бюджетные/таможенные/торговые данные;
2. санкционные и enforcement records (материалы правоприменения);
3. официальные экспортно-импортные данные;
4. международные финансовые организации;
5. проверяемые расследования с документами;
6. авторитетные новостные источники;
7. заявления actor;
8. unverified OSINT.

Уровень источника хранится отдельно от содержания claim (утверждения).

## 7. Потоки для military/state side

Не предполагать заранее существование конкретного внешнего финансиста. Искать:

```text
налоговые поступления;
валютные доходы;
доходы от газа / нефти / добычи / экспорта;
доходы military-linked enterprises;
банковский и валютный доступ;
закупки оружия;
топливо;
транспорт;
внешнюю торговлю;
санкционные ограничения;
обход ограничений;
критические поставщики.
```

## 8. Потоки для resistance side

Искать отдельно:

```text
пожертвования внутри страны;
диаспору;
краудфандинг;
территориальные налоги / сборы;
помощь существующих ethnic armed organizations;
оружие местного производства;
захваченное оружие/боеприпасы;
трансграничную логистику;
убежища / safe areas;
неформальные системы переводов;
человеческий ресурс.
```

Не объединять NUG/PDF, локальные PDF/LDF и EAO в единого actor без evidence конкретной связи.

## 9. Выход каждого snapshot

Минимальный resource-state report:

```text
actor_id
known_flows
unknown_domains
resource_diversification
external_dependency
internal_revenue_capacity
logistics_viability
replacement_options
critical_bottlenecks
sanctions_pressure
flow_persistence
resource_uncertainty
```

Пока значения могут быть categorical (категориальными):

```text
LOW / MEDIUM / HIGH / UNKNOWN
```

Не переводить их в единый числовой funding score на v0.1.

## 10. Ключевой будущий аналитический вопрос

После накопления последовательности snapshots можно проверять гипотезу:

```text
ESCALATION_SIGNAL
+
RESOURCE_SUSTAINMENT
→ более устойчивый переход к длительному конфликту
```

против:

```text
ESCALATION_SIGNAL
+
RESOURCE_EXHAUSTION_OR_BOTTLENECK
→ высокий текущий конфликтный сигнал, но меньшая устойчивость продолжения
```

Это гипотеза для проверки, а не утверждённая формула.

## 11. Связь с Objective/Coverage

Resource layer поставляет предметные свидетельства. Objective/Coverage продолжает оценивать честность доказательной картины.

```text
HIGH_RESOURCE_SIGNAL + LOW_RESOURCE_COVERAGE
!=
HIGH_CONFIDENCE_RESOURCE_CONCLUSION
```

## 12. Следующий шаг

Заполнить `resource_flow_manifest_template.csv` реальными историческими evidence-items одновременно с основным source manifest, начиная с самых ранних pre-coup snapshots и не перескакивая сразу к известным post-event результатам.