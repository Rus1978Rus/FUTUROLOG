# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `BULK_COLLECTION_STARTED / BATCH_001_SEEDED / NOT_READY_FOR_EVIDENCE_STATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` начато фактическое наполнение двух исторических корпусов.

Созданы первые intake-пакеты:

- `russia_ukraine/evidence_intake_batch_001.csv`;
- `myanmar_post_coup_civil_war/evidence_intake_batch_001.csv`.

В них разделены:

- contemporaneous evidence (свидетельства, доступные в момент исторического cutoff);
- pre-existing structural context (структурный контекст, опубликованный заранее);
- retrospective-only material (материал, опубликованный позже и запрещённый как вход в более ранний snapshot);
- quarantined/recheck rows (строки, которым ещё нельзя доверять до восстановления точного источника или даты).

## Что сознательно НЕ сделано

- не рассчитан `EvidenceState`;
- не назначены числовые оценки latent pressure;
- не заполнены отсутствующие домены придуманными значениями;
- retrospective evidence не перенесено в ранние snapshot;
- отсутствие записи не интерпретируется как отсутствие процесса.

## Следующий collection batch

Приоритет поиска для обоих кейсов одинаков по замороженной схеме.

### Россия–Украина

1. демография и миграция;
2. институциональное доверие и ожидания;
3. социальное неравенство и regional inequality (региональное неравенство);
4. идентичность / язык / культура / память;
5. религиозные институты и межгрупповые связи;
6. здоровье и COVID;
7. образование;
8. информационная экология и возможное amplification (усиление);
9. food / water / fuel household access (еда / вода / топливо на уровне домохозяйств);
10. contemporaneous 2021 energy/revenue data (данные 2021 года по энергетике и доходам), чтобы заменить retrospective-only источники;
11. stabilizers (стабилизаторы): социальные связи, институты, международные механизмы, локальная адаптация.

### Мьянма

1. Civil Disobedience Movement и профессиональные группы;
2. медицина / COVID / доступ к здравоохранению;
3. образование / студенты / учителя;
4. интернет-ограничения и изменение наблюдаемости;
5. этнические / религиозные / региональные группы;
6. migration / displacement (миграция / перемещение);
7. food / fuel / water access;
8. климат / наводнения / сельское хозяйство;
9. малые вооружённые и невооружённые группы и их coalescence (сближение / объединение);
10. diaspora / donations / resistance financing (диаспора / пожертвования / финансирование сопротивления);
11. stabilizers и counter-pressures (противодавление), а не только эскалация.

## Observation & Coverage обязательны

Каждый следующий evidence item должен получить по возможности:

```text
source_family
access_mode
original_source_status
publication_time
cutoff_admissibility
independence_group
coverage_segment
base_rate_status
information_amplification_status
possible_coordination_status
representation_reality_gap_status
```

`UNKNOWN` допустим. Выдуманное значение — нет.

## Gate до EvidenceState

Переход к числовому EvidenceState разрешается только когда:

1. есть минимум несколько независимых source families по ключевым доменам;
2. есть pressure и stabilizer evidence;
3. retrospective-only строки механически исключены из ранних cutoff;
4. известны основные topology gaps (дыры покрытия);
5. незаполненные домены явно перечислены;
6. нет необходимости менять замороженную схему v0.1.

До этого правильный статус:

`PARTIAL_EVIDENCE / COLLECTION_CONTINUES`.
