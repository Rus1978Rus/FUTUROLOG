# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `BULK_COLLECTION_CONTINUES / BATCH_007_ADDED / NOT_READY_FOR_EVIDENCE_STATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` продолжается фактическое наполнение двух исторических корпусов по одной и той же замороженной схеме.

Созданы intake-пакеты Batch 001–007 для:

- `russia_ukraine/`;
- `myanmar_post_coup_civil_war/`.

## Batch 007 — Россия–Украина

Главный прогресс — contemporaneous information ecology (информационная экология) 2021.

Добавлены:

- EUvsDisinfo 23 Dec 2021: более 2,700 новых примеров pro-Kremlin disinformation в базе за 2021, примерно треть из них была направлена против Украины;
- EUvsDisinfo 16 Dec 2021: Украина как крупнейшая цель внутри накопленного мониторингового корпуса;
- отдельный contemporaneous case 6 Dec 2021: нарратив о том, что предупреждения о российской агрессии являются выдуманной истерией;
- отдельный contemporaneous case 2 Sep 2021: нарратив о внешнем контроле Украины со стороны США;
- EU Foreign Affairs Council Jan 2022: strengthening resilience against cyber/hybrid attacks and foreign information manipulation как stabilizing institutional response;
- поздний EEAS spike analysis 2022 сохранён только как `RETROSPECTIVE_REFERENCE` и не импортирован в 2021/early-2022 snapshots.

Ключевое различие:

```text
NARRATIVE_EXISTS != POPULATION_BELIEF
DATABASE_CASE_COUNT != EXPOSURE_RATE
EXPOSURE != BEHAVIORAL_EFFECT
```

Таким образом, information-operations gap частично закрыт именно допустимыми по cutoff записями, а не поздней реконструкцией.

## Batch 007 — Мьянма

Добавлены:

- ещё два contemporaneous UNHCR displacement sensors: 31 May и 21 Jun 2021;
- OHCHR/UN 11 Jun 2021: эскалация в Kayah, Chin и Kachin, особенно в районах со значительными этническими и религиозными меньшинствами;
- UNHCR/UN Myanmar 28 Jul 2021: local community and faith groups helping an estimated 200,000 newly displaced people как локальная stabilizing capacity;
- Human Rights Council resolution of 12 Jul 2021 concerning Rohingya Muslims and other minorities как contemporaneous institutional minority-specific signal;
- OHCHR 1 Apr 2021: early flight/displacement from renewed fighting with ethnic armed organizations, including Kayin;
- UN Myanmar Research Digest Jul 2021 как свидетельство multi-source observation ecosystem across household, sectoral and group-specific assessments.

Numeric totals из UNHCR карт по-прежнему НЕ импортированы без извлечения underlying PDF/data.

## Observation & Coverage guards

Batch 007 усиливает:

```text
NARRATIVE_EXISTS != POPULATION_BELIEF
DATABASE_CASE_COUNT != POPULATION_EXPOSURE
EXPOSURE != BEHAVIORAL_EFFECT
MONITORED_MEDIA != WHOLE_INFORMATION_SPACE
MINORITY_REGION_VIOLENCE != NATIONAL_RELIGIOUS_CONFLICT
LOCAL_ASSISTANCE_NETWORK != NATIONAL_STABILIZATION
INSTITUTIONAL_CONCERN != POPULATION_PREVALENCE
SENSOR_EXISTS != NUMERIC_VALUE_VALIDATED
```

Сохраняются все ранее принятые guards, включая:

```text
OBSERVABILITY != PREVALENCE
VISIBLE_EXCEPTION != BASE_RATE
DATA_COLLECTION_TIME != PUBLIC_OBSERVABILITY_TIME
NATIONAL_AVERAGE != LOCAL_PRESSURE
CONTEMPORANEOUS_SIGNAL != RETROSPECTIVE_RECONSTRUCTION
EVIDENCE_GAP != ZERO_PHENOMENON
```

## Что сознательно НЕ сделано

- `EvidenceState` не рассчитан;
- число disinformation cases не превращено в процент людей, которые увидели или приняли нарратив;
- отдельный информационный кейс не объявлен доказательством централизованной операции без отдельной attribution evidence;
- поздний EEAS spike analysis не импортирован как contemporaneous 2021 input;
- этническая/религиозная концентрация насилия в отдельных регионах Мьянмы не превращена в тезис о nationwide religious war;
- локальная гуманитарная помощь не объявлена доказанной стабилизацией страны;
- UNHCR map catalog всё ещё не используется как источник придуманных numeric totals.

## Оставшиеся крупные пробелы перед первым EvidenceState

### Россия–Украина

1. язык, культура, collective memory и религиозные институты с допустимыми cutoff-источниками;
2. regional household inequality и food/water/fuel access;
3. original release timing по нужным точкам международных резервов;
4. дополнительные stabilizers и negative controls;
5. measurement of information reach / audience exposure, если contemporaneous данные доступны;
6. group-specific subclaims из contemporaneous human-rights and social reports.

### Мьянма

1. извлечь numeric displacement totals из underlying UNHCR maps;
2. diaspora / donations / resistance financing из contemporaneous primary sources;
3. contemporaneous information operations / rumours / propaganda / counter-propaganda;
4. более детальные ethnic/religious group-specific signals без смешения групп;
5. конкретные 2021 water/flood/agriculture shocks вне structural baseline;
6. ранняя датировка взаимодействия малых resistance groups;
7. дополнительные stabilizers и negative controls.

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
