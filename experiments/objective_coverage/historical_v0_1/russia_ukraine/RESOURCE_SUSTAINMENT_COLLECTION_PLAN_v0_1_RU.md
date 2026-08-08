# RESOURCE_SUSTAINMENT_COLLECTION_PLAN v0.1 — Russia–Ukraine

**Статус:** `COLLECTION_PLAN / NO_SINGLE_RESOURCE_SCORE / NOT_VALIDATED`

## Цель

Собирать ресурсную картину для исторического кейса Россия–Украина так, чтобы отдельно видеть способность каждого actor (участника) поддерживать действия во времени и не превращать торговлю или государственные доходы в автоматическое утверждение о военном финансировании.

## Actor families

Минимально раздельно:

```text
RUSSIAN_STATE_AND_MILITARY_APPARATUS
UKRAINIAN_STATE_AND_DEFENCE_APPARATUS
EXTERNAL_STATE_SUPPORTERS
COMMERCIAL_AND_LOGISTICS_INTERMEDIARIES
```

При необходимости actor дробится дальше. Внешняя страна не получает статус `FUNDER` только из-за торговли, дипломатической поддержки или политической близости.

## Resource classes

Отслеживать как минимум:

```text
PUBLIC_FINANCE
TAX_REVENUE
FOREIGN_EXCHANGE_RESERVES
EXPORT_REVENUE
FUEL_AND_ENERGY
ARMS_AND_AMMUNITION
INDUSTRIAL_PRODUCTION
LOGISTICS_AND_TRANSPORT
EXTERNAL_FINANCIAL_AID
CREDIT
HUMAN_RESOURCES
CRITICAL_COMPONENTS
SANCTIONS_EVASION_CAPACITY
```

## Особые направления для pre-2022 snapshots

- нефтегазовые и другие экспортные доходы как общая государственная ресурсная база;
- украинские бюджетные, валютные и оборонные ограничения;
- поставки вооружений и обучение, реально наблюдаемые до каждого cutoff;
- промышленная и ремонтная база;
- железнодорожная, автомобильная, морская и трубопроводная логистика;
- критические импортные компоненты;
- валютные и финансовые ограничения;
- заменяемость поставщиков и маршрутов;
- состояние энергетической инфраструктуры и взаимозависимостей.

## Запрет на hindsight leakage

Нельзя использовать данные, впервые опубликованные после 24 февраля 2022 года, как будто они были доступны FUTUROLOG в декабре 2021 или январе 2022.

Позднейшие расследования могут использоваться для `historical_truth`, но должны иметь отдельное поле `public_observability_time` и не попадать в pre-cutoff EvidenceState.

## Cross-layer integration

Исторические nodes (узлы) связываются с ресурсными структурами через `historical_resource_cross_edges_v0_1.csv`.

Сначала допускается статус:

```text
PENDING_FLOW_EVIDENCE
```

и только после появления конкретного evidence-record создаётся подтверждённый resource flow.

## Следующий шаг

Создать и заполнить `resource_flow_manifest_v0_1.csv` синхронно с обычным historical evidence collection.