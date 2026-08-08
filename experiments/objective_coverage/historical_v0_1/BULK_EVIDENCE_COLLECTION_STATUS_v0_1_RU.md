# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `BULK_COLLECTION_CONTINUES / BATCH_003_ADDED / NOT_READY_FOR_EVIDENCE_STATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` продолжается фактическое наполнение двух исторических корпусов.

Созданы intake-пакеты:

- `russia_ukraine/evidence_intake_batch_001.csv`;
- `russia_ukraine/evidence_intake_batch_002.csv`;
- `russia_ukraine/evidence_intake_batch_003.csv`;
- `myanmar_post_coup_civil_war/evidence_intake_batch_001.csv`;
- `myanmar_post_coup_civil_war/evidence_intake_batch_002.csv`;
- `myanmar_post_coup_civil_war/evidence_intake_batch_003.csv`.

## Batch 003 — Россия–Украина

Добавлены contemporaneous (доступные тогда) источники по:

- institutional trust sensor (сенсор институционального доверия) KIIS декабря 2021;
- восприятию угрозы вторжения;
- оценке достаточности дипломатических и оборонных действий правительства;
- региональным различиям в отношении к ЕС/НАТО;
- структурным институциональным слабостям по World Bank SCD 2021;
- образовательной устойчивости и инвестициям в модернизацию как stabilizer (стабилизатор).

Важно: survey attitude (опросное отношение) не считается объективной вероятностью вторжения и не превращается автоматически в causal factor (причинный фактор).

## Batch 003 — Мьянма

Добавлены contemporaneous источники по:

- росту цен на еду и топливо уже в марте 2021;
- сильной региональной неоднородности ценового давления;
- банковским, remittance (денежные переводы) и cash-access ограничениям;
- contingency food stocks (резервам продовольствия) WFP как stabilizer;
- риску роста городского голода и household debt (долгов домохозяйств);
- масштабированию продовольственной помощи;
- displacement (перемещению населения) и отдельному contemporaneous UNHCR sensor на 21 июня 2021;
- World Bank household survey как потенциальному pre-coup baseline (базе до переворота), но с отдельным observability caution: дата самих наблюдений и дата публичной доступности метаданных не должны смешиваться.

## Observation & Coverage применены

Batch 003 усиливает следующие guards:

```text
SURVEY_ATTITUDE != OBJECTIVE_EVENT_PROBABILITY
NATIONAL_AVERAGE != LOCAL_PRESSURE
MARKET_PRICE != HOUSEHOLD_FOOD_INSECURITY
PROGRAM_TARGET != PROGRAM_EFFECT
RETROSPECTIVE_TOTAL != EARLY_CUTOFF_INPUT
DATA_COLLECTION_TIME != PUBLIC_OBSERVABILITY_TIME
```

Кроме того сохраняются:

```text
OBSERVABILITY != PREVALENCE
TEST_POSITIVITY != POPULATION_PREVALENCE
EVENT_REPORTING != POPULATION_RATE
INTERNET_SHUTDOWN != REDUCED_SOCIAL_ACTIVITY
HUMANITARIAN_PROGRAM != PROVEN_STABILIZATION
```

## Что сознательно НЕ сделано

- не рассчитан `EvidenceState`;
- не назначены числовые оценки latent pressure;
- не заполнены отсутствующие домены придуманными значениями;
- retrospective evidence не перенесено в ранние snapshot;
- один source family не считается независимым множественным подтверждением;
- поздние сводные данные не используются как будто они были доступны раньше;
- нет попытки объявить один survey, один гуманитарный отчёт или один price monitor доказательством системного состояния страны.

## Оставшиеся крупные пробелы перед первым EvidenceState

### Россия–Украина

1. contemporaneous 2021 energy/revenue data для замены поздних энергетических сводок;
2. здоровье/COVID вне образовательного слоя;
3. язык, культура, коллективная память и религиозные институты — только из источников, реально доступных к cutoff;
4. информационные операции / amplification / representation-reality gaps;
5. regional household inequality и basic-needs access;
6. дополнительные stabilizers и negative controls.

### Мьянма

1. образование / учителя / студенты с contemporaneous 2021 источниками;
2. этнические, религиозные и региональные group-specific signals;
3. contemporaneous displacement counts по нескольким cutoff, а не только year-end totals;
4. вода, климат, наводнения, сельское хозяйство отдельно от общей экономики;
5. малые вооружённые/невооружённые группы и их coalescence;
6. diaspora / donations / resistance financing;
7. информационные операции и representation-reality gaps;
8. дополнительные stabilizers / counter-pressures.

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
