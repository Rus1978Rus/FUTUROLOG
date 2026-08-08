# RESOURCE_BACKFILL_STATUS v0.1

Статус: `PARTIAL_BACKFILL / CONTEMPORANEOUS_EVIDENCE_ADDED / NOT_COMPLETE / NOT_READY_FOR_FINAL_SCORING`

## Что сделано

Для обоих исторических корпусов добавлен отдельный contemporaneous backfill (досбор источников, опубликованных ДО соответствующих cutoff).

### Myanmar

Ранний пробел частично закрыт источниками 2015–2019 годов:

- UN Fact-Finding Mission: военные бизнес-структуры MEHL/MEC и широкий корпоративный контур;
- Global Witness: jade economy (нефритовая экономика), связи с военными компаниями и отдельными вооружёнными акторами;
- UN economic-interests report: более ста идентифицированных military businesses (военных предприятий) в разных секторах.

Практическое следствие:

```text
ZERO_VISIBLE_RESOURCE_RECORDS_BEFORE_2021-03-25
```

больше нельзя трактовать даже как "в текущем корпусе нет ранних подтверждений" без оговорки: теперь такие подтверждения есть и они существовали публично до переворота.

Но они описывают в основном STRUCTURAL_RESOURCE_BASE (структурную ресурсную базу), а не конкретные post-coup operational flows (операционные потоки после переворота).

### Russia–Ukraine

Подтверждены pre-invasion (до вторжения) ресурсы/ограничения:

- US security assistance packages 2021;
- действующий санкционный контур ЕС;
- отдельный кандидатный сигнал по газовой взаимозависимости, который пока требует восстановления оригинальной публикации IEA сентября 2021 года, поскольку найденная страница является позднейшим synthesis (сводным материалом).

## Новое правило для snapshot visibility

Нужно различать минимум три класса:

```text
FLOW_VISIBLE_AT_CUTOFF
STRUCTURAL_RESOURCE_BASE_VISIBLE_AT_CUTOFF
RETROSPECTIVE_ONLY
```

`STRUCTURAL_RESOURCE_BASE_VISIBLE_AT_CUTOFF` означает: структура ресурса была известна, но конкретный текущий поток или его объём на этом cutoff не подтверждён.

## Защитные инварианты

```text
STRUCTURAL_RESOURCE_BASE != CURRENT_FLOW
CURRENT_FLOW != OPERATIONAL_CONVERSION
PUBLIC_CORPORATE_CONTROL != SPECIFIC_MILITARY_SPENDING
HISTORICAL_REVENUE_LINK != CURRENT_CONFLICT_FINANCING
LATER_SYNTHESIS_OF_OLD_FACT != CONTEMPORANEOUS_SOURCE
```

## Что ещё не закрыто

Myanmar:
- contemporaneous pre-coup oil/gas foreign-exchange evidence;
- конкретные early-2021 cross-border finance/logistics channels;
- post-coup resistance funding before mid-2021;
- actor-by-actor separation of EAO/PDF/NUG flows.

Russia–Ukraine:
- contemporaneous 2021 Russian oil/gas budget revenue publications;
- contemporaneous export/customs statistics available before each cutoff;
- National Wealth Fund / reserves state visible before invasion;
- European gas dependency data published before February 2022;
- non-US external assistance available to Ukraine before cutoff.

## Текущий gate

Не запускать историческую A/B/C evaluation (проверку формул) как финальный результат до закрытия критических дыр resource provenance coverage (покрытия происхождения ресурсных данных).

Допускается только diagnostic dry-run (диагностический пробный прогон) с явным статусом `PARTIAL_EVIDENCE`.
