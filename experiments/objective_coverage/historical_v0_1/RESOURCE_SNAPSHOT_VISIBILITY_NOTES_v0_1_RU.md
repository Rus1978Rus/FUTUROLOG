# RESOURCE_SNAPSHOT_VISIBILITY_NOTES v0.1

**Статус:** `WORKING / EPISTEMIC_VISIBILITY_ONLY / NOT_RESOURCE_COMPLETENESS`

## Что сделано

Для двух пилотных корпусов создан слой `resource_snapshot_visibility_v0_1.csv`, который отвечает на узкий вопрос:

> какие resource-flow records (записи о ресурсных потоках) из текущего manifest уже были публично доступны FUTUROLOG к конкретному historical cutoff?

Это НЕ отвечает на вопрос «какие ресурсы реально существовали в мире». Это только текущая исторически допустимая видимость.

## Правило

```text
FLOW_EXISTED_AT_T
!=
FLOW_WAS_PUBLICLY_OBSERVABLE_AT_T

PUBLISHED_LATER_ABOUT_OLD_FLOW
!=
AVAILABLE_BEFORE_CUTOFF

ZERO_VISIBLE_RECORDS
!=
ZERO_RESOURCE_FLOWS
```

## Russia–Ukraine

Текущий manifest содержит доинвазионно допустимые официальные записи о помощи Украине: USAI $125 млн (01.03.2021), USAI $150 млн (11.06.2021), а также запись о $60 млн, публично подтверждаемую текущим источником с 08.12.2021. Он также содержит действовавший до вторжения санкционный контур ЕС.

Две крупные записи о российской энергетической базе (`RU-RF-004`, `RU-RF-006`) намеренно исключены из всех cutoff до 24.02.2022, потому что используемые в текущем manifest сводные источники опубликованы уже после вторжения. Их существование как экономики 2021 года не даёт права подсовывать позднее знание ранней модели.

## Myanmar

По текущему manifest первая допустимая запись появляется 25.03.2021: Treasury о MEHL/MEC. Затем 08.04.2021 появляется Myanma Gems Enterprise, 21.04.2021 — timber/pearl enterprises, а 29.06.2021 — текущий Global Witness corpus по jade economy.

Поэтому ранние Myanmar snapshots сейчас показывают `visible_flow_count=0`. Это НЕ утверждение, что до марта 2021 у армии или других акторов не было ресурсной базы. Это означает только, что текущий resource manifest пока не содержит более ранних, датированных и допустимых evidence records.

Это автоматически создаёт следующую исследовательскую задачу:

`BACKFILL_PRE_EXISTING_RESOURCE_EVIDENCE_WITH_CONTEMPORANEOUS_SOURCES`

То есть искать документы, опубликованные ДО соответствующего cutoff, которые уже тогда описывали военные холдинги, государственные предприятия, пограничную экономику и финансирование вооружённых организаций.

## Источниковая опора текущих records

Текущие записи опираются, в частности, на официальные публичные документы:

- U.S. DoD, 01.03.2021 — $125m USAI Ukraine package;
- U.S. DoD, 11.06.2021 — $150m USAI Ukraine package;
- U.S. Treasury, 25.03.2021 — MEHL/MEC as major military economic resources;
- U.S. Treasury, 08.04.2021 — Myanma Gems Enterprise;
- U.S. Treasury, 21.04.2021 — timber and pearl enterprises.

## Следующий gate

1. backfill contemporaneous pre-cutoff resource evidence;
2. добавить source-family independence;
3. вычислить resource provenance coverage по snapshot;
4. только потом переводить resource evidence в EvidenceState / Objective-Coverage input.

Инвариант:

```text
CURRENT_MANIFEST_COVERAGE
!=
WORLD_RESOURCE_COVERAGE
```
