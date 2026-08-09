# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `BULK_COLLECTION_CONTINUES / BATCH_005_ADDED / NOT_READY_FOR_EVIDENCE_STATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` продолжается фактическое наполнение двух исторических корпусов по одной и той же замороженной схеме.

Созданы intake-пакеты Batch 001–005 для:

- `russia_ukraine/`;
- `myanmar_post_coup_civil_war/`.

## Batch 005 — Россия–Украина

Добавлены:

- contemporaneous Bank of Russia signal от 25 октября 2021: рекордный на тот момент профицит текущего счёта в Q3 2021 и сильный экспортный стоимостный поток;
- pre-invasion Bank of Russia signal от 27 января 2022: итоговый рекордный профицит текущего счёта за 2021 год, допустимый только для поздне-январских/февральских snapshot;
- исторический ряд международных резервов с отдельным observability caution: текущая таблица ЦБ подтверждает исторические значения, но original release timing каждого weekly point должен быть восстановлен до использования в конкретном cutoff;
- retrospective EEAS evidence о резком росте дезинформационных нарративов в последние три месяца перед 24.02.2022, оставленное как `RETROSPECTIVE_REFERENCE`, а не тайно импортированное в ранние snapshot;
- структурный факт существования институционального monitoring capacity по российской дезинформации до кризиса.

Ключевой результат: ресурсная способность России перед вторжением теперь подтверждается не только поздними энергетическими сводками, но и contemporaneous макроэкономическим источником Банка России. При этом `EXPORT_CAPACITY != MILITARY_ALLOCATION` сохраняется как обязательный guard.

## Batch 005 — Мьянма

Добавлены:

- четыре последовательных contemporaneous UNHCR displacement sensors: 28 июня, 5 июля, 12 июля и 19 июля 2021 года;
- они пока фиксируют существование датированных карт/геоданных, но numeric totals не импортируются до проверки underlying map/data;
- FAO contemporaneous evidence от 25 июля 2021 по Rakhine: зависимость сельских домохозяйств от agriculture/fisheries/aquaculture, повторяющаяся уязвимость к floods/cyclones/heavy rains и высокий food-insecurity burden;
- локальный FAO/EU aquaculture recovery intervention как ограниченный stabilizer;
- diaspora / donations / resistance financing оставлен как явный `EVIDENCE_GAP`, потому что в Batch 005 не найден достаточно сильный contemporaneous primary source для количественного импорта.

Важно: объявленный пробел не интерпретируется как отсутствие финансирования.

## Observation & Coverage guards

Batch 005 усиливает:

```text
MACRO_RESOURCE_CAPACITY != MILITARY_ALLOCATION
RESERVES != IMMEDIATELY_SPENDABLE_WAR_FINANCE
HISTORICAL_SERIES_VALUE != VERIFIED_CUTOFF_OBSERVABILITY
RETROSPECTIVE_DISINFORMATION_ANALYSIS != CONTEMPORANEOUS_INPUT
DISPLACEMENT_SENSOR_EXISTS != NUMERIC_TOTAL_VALIDATED
REGIONAL_CLIMATE_FOOD_STRESS != NATIONAL_PREVALENCE
EVIDENCE_GAP != ZERO_PHENOMENON
```

Сохраняются все ранее принятые guards, включая:

```text
OBSERVABILITY != PREVALENCE
VISIBLE_EXCEPTION != BASE_RATE
DATA_COLLECTION_TIME != PUBLIC_OBSERVABILITY_TIME
NATIONAL_AVERAGE != LOCAL_PRESSURE
CONTEMPORANEOUS_SIGNAL != RETROSPECTIVE_RECONSTRUCTION
```

## Что сознательно НЕ сделано

- `EvidenceState` не рассчитан;
- числа международных резервов не допущены автоматически во все ранние snapshot только потому, что они есть в текущем историческом ряду;
- поздний EEAS анализ не использован как будто он был опубликован до вторжения;
- экспортный профицит/резервы не превращены в доказательство конкретного военного решения;
- UNHCR map catalog pages не превращены в придуманные numeric displacement totals;
- отсутствие найденного contemporaneous primary source по финансированию сопротивления Мьянмы не трактуется как отсутствие самого потока.

## Оставшиеся крупные пробелы перед первым EvidenceState

### Россия–Украина

1. восстановить original release timing исторического ряда резервов для каждого нужного cutoff;
2. найти contemporaneous 2021/early-2022 source records по конкретным информационным операциям и amplification, чтобы заменить позднюю EEAS реконструкцию;
3. уточнить бюджетную/фискальную конверсию экспортных доходов без перехода к `REVENUE == WAR_FINANCE`;
4. здоровье/COVID вне образования;
5. язык, культура, коллективная память и религиозные институты;
6. regional household inequality и basic-needs access;
7. дополнительные stabilizers и negative controls.

### Мьянма

1. извлечь и валидировать numeric displacement data из contemporaneous UNHCR maps для нескольких cutoff;
2. этнические/религиозные group-specific сигналы;
3. вода и дополнительные climate/flood/agriculture records вне Rakhine;
4. diaspora / donations / resistance financing из contemporaneous primary sources;
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
