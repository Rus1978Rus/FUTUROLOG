# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `BULK_COLLECTION_CONTINUES / BATCH_004_ADDED / NOT_READY_FOR_EVIDENCE_STATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` продолжается фактическое наполнение двух исторических корпусов по одной и той же замороженной схеме.

Созданы intake-пакеты Batch 001–004 для:

- `russia_ukraine/`;
- `myanmar_post_coup_civil_war/`.

## Batch 004 — Россия–Украина

Добавлены:

- contemporaneous IEA signal от 21 сентября 2021 по европейскому газовому рынку;
- отдельное различение contemporaneous и retrospective энергетических данных;
- IEA multi-causal guard: рост цен на газ в 2021 не сводится к одной причине;
- информационный manipulation/disinformation domain как подтверждённый класс наблюдения, но поздние EEAS материалы помещены в `RETROSPECTIVE_ONLY / QUARANTINED_FOR_2021_BACKFILL`, а не импортированы задним числом в 2021.

Ключевой результат: ранний энергетический пробел частично закрыт оригинальным источником 2021 года, но точные contemporaneous данные по российским экспортным доходам/бюджетной конверсии ещё требуются.

## Batch 004 — Мьянма

Добавлены:

- образование как отдельный pressure layer: более 60 занятых силовиками школ/университетских кампусов в 13 штатах/регионах по совместному заявлению UNICEF/UNESCO/Save the Children от 19 марта 2021;
- pre-coup education adaptation capacity как stabilizer: цифровые материалы, teacher training и COVID-safe reopening support в 2020;
- бегство гражданских служащих, студентов, активистов и отдельных defectors как group-specific displacement signal;
- emergence (возникновение) разных anti-coup resistance groups с обязательным различением NUG/PDF и независимых local defense groups;
- coalescence и fragmentation рассматриваются одновременно, без автоматического объединения всех сопротивляющихся акторов в одну сеть.

## Observation & Coverage guards

Batch 004 усиливает:

```text
CONTEMPORANEOUS_SIGNAL != RETROSPECTIVE_RECONSTRUCTION
ENERGY_STRESS != SINGLE_CAUSE
ENERGY_REVENUE != MILITARY_EXPENDITURE
DISINFORMATION_DOMAIN_EXISTS != SPECIFIC_2021_CAMPAIGN_PROVEN
SCHOOL_OCCUPATION_REPORTS != NATIONAL_EDUCATION_PREVALENCE
ARMED_GROUP_PROLIFERATION != UNIFIED_COMMAND
COALESCENCE_SIGNAL != COMPLETE_COALITION
```

Сохраняются все ранее принятые guards, включая:

```text
OBSERVABILITY != PREVALENCE
VISIBLE_EXCEPTION != BASE_RATE
DATA_COLLECTION_TIME != PUBLIC_OBSERVABILITY_TIME
NATIONAL_AVERAGE != LOCAL_PRESSURE
```

## Что сознательно НЕ сделано

- `EvidenceState` не рассчитан;
- поздние источники не импортированы в ранние cutoff;
- информационная операция не объявлена доказанной только по выгоде конкретному актору;
- энергетическая зависимость не превращена автоматически в мотив или финансирование войны;
- появление множества вооружённых групп в Мьянме не трактуется как единое управление;
- eventful evidence (яркие события) не используется как denominator (знаменатель) состояния общества.

## Оставшиеся крупные пробелы перед первым EvidenceState

### Россия–Украина

1. contemporaneous 2021 данные по российским экспортным доходам, бюджету/резервам и их доступности до cutoff;
2. contemporaneous 2021 материалы по информационным операциям и amplification, а не поздние реконструкции;
3. здоровье/COVID вне образования;
4. язык, культура, коллективная память и религиозные институты;
5. regional household inequality и basic-needs access;
6. дополнительные stabilizers и negative controls.

### Мьянма

1. несколько contemporaneous displacement snapshots с числовыми данными;
2. этнические/религиозные group-specific сигналы;
3. вода, климат, наводнения и agriculture;
4. diaspora / donations / resistance financing;
5. contemporaneous information operations / rumours / propaganda / counter-propaganda;
6. дополнительные stabilizers и negative controls;
7. более ранняя датировка появления и взаимодействия конкретных малых resistance groups.

## Gate до EvidenceState

Переход к числовому EvidenceState разрешается только когда:

1. есть несколько независимых source families по ключевым доменам;
2. представлены pressure и stabilizer evidence;
3. retrospective-only строки механически исключены из ранних cutoff;
4. известны основные topology gaps;
5. незаполненные домены явно перечислены;
6. одинаковая замороженная схема применена к обоим кейсам;
7. нет необходимости менять `HISTORICAL_SCHEMA_FREEZE v0.1`.

До этого правильный статус:

`PARTIAL_EVIDENCE / COLLECTION_CONTINUES`.
