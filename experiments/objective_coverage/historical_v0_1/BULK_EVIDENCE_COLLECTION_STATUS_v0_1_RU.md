# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `BULK_COLLECTION_CONTINUES / BATCH_002_ADDED / NOT_READY_FOR_EVIDENCE_STATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` продолжается фактическое наполнение двух исторических корпусов.

Созданы intake-пакеты:

- `russia_ukraine/evidence_intake_batch_001.csv`;
- `russia_ukraine/evidence_intake_batch_002.csv`;
- `myanmar_post_coup_civil_war/evidence_intake_batch_001.csv`;
- `myanmar_post_coup_civil_war/evidence_intake_batch_002.csv`.

Batch 002 расширяет не военный и не только экономический слой.

### Россия–Украина: Batch 002

Добавлены свидетельства по:

- длительному внутреннему перемещению и проблемам доступа к пенсиям/социальным услугам вдоль линии соприкосновения;
- локальному социальному и семейному разделению из-за ограничений пересечения линии соприкосновения;
- COVID-давлению на образование и риску усиления образовательного неравенства;
- институциональной адаптации системы высшего образования как стабилизатору;
- программам интеграции ВПЛ и durable solutions (долговременным решениям) как стабилизирующему контуру.

### Мьянма: Batch 002

Добавлены свидетельства по:

- пред-переворотному COVID/бедностному давлению;
- Civil Disobedience Movement как межпрофессиональной сети;
- врачам, медсёстрам, госслужащим, преподавателям, юристам, религиозным лидерам, молодёжи и женщинам как разным social-group nodes (узлам социальных групп);
- интернет-ограничениям как одновременно социальному воздействию и искажению наблюдаемости;
- спаду экономики, занятости, банковских/платёжных, логистических, телекоммуникационных и публичных услуг;
- росту цен на импортные товары и топливо, аграрным input-cost (затратам на ресурсы производства) и кредитным ограничениям;
- ограниченному временному улучшению мобильности и логистики в мае-июне 2021 как стабилизатору;
- третьей волне COVID и ограниченной способности системы здравоохранения.

## Observation & Coverage применены

В Batch 002 для каждой строки предусмотрены поля:

```text
source_family
access_mode
original_source_status
cutoff_admissibility
independence_group
coverage_segment
base_rate_status
information_amplification_status
possible_coordination_status
representation_reality_gap_status
```

Особенно важно:

```text
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
- отсутствие записи не интерпретируется как отсутствие процесса;
- один source family не считается независимым множественным подтверждением.

## Следующий collection batch — Batch 003

### Россия–Украина

Приоритет:

1. институциональное доверие и ожидания;
2. regional inequality (региональное неравенство) и household pressure (давление на домохозяйства);
3. идентичность / язык / культура / коллективная память;
4. религиозные институты и межгрупповые связи;
5. здоровье и COVID вне образовательного слоя;
6. информационная экология, информационные операции и agenda amplification (усиление повестки);
7. contemporaneous 2021 energy/revenue data, чтобы заменить поздние ретроспективные сводки;
8. food / water / fuel access на региональном уровне;
9. дополнительные stabilizers: локальные связи, работающие институты, адаптация и международные механизмы.

### Мьянма

Приоритет:

1. образование / студенты / учителя;
2. этнические, религиозные и региональные группы;
3. migration / displacement;
4. food / water access отдельно от общего макроэкономического давления;
5. климат / наводнения / сельское хозяйство;
6. малые вооружённые и невооружённые группы и их coalescence;
7. diaspora / donations / resistance financing;
8. информационные операции, слухи, propaganda / counter-propaganda и representation-reality gaps;
9. stabilizers и counter-pressures.

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
