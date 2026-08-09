# BULK_EVIDENCE_COLLECTION_STATUS v0.1

**Статус:** `BULK_COLLECTION_CONTINUES / BATCH_006_ADDED / NOT_READY_FOR_EVIDENCE_STATE`

## Что сделано

После `HISTORICAL_SCHEMA_FREEZE_v0_1_RU.md` продолжается фактическое наполнение двух исторических корпусов по одной и той же замороженной схеме.

Созданы intake-пакеты Batch 001–006 для:

- `russia_ukraine/`;
- `myanmar_post_coup_civil_war/`.

## Batch 006 — Россия–Украина

Добавлены contemporaneous и структурные источники по health layer (слою здоровья):

- WHO 9 Dec 2021: низкий по региональным меркам уровень государственного финансирования здравоохранения и выявленные COVID слабости/недофинансирование;
- WHO/European Observatory 23 Nov 2021: высокий out-of-pocket burden (доля прямых платежей населения) как фактор уязвимости доступа;
- WHO May 2021: институциональная сложность незавершённой health/decentralization reform под давлением пандемии;
- WHO Feb 2021: улучшения infection prevention and control как ограниченный stabilizer;
- OHCHR Sep 2021: contemporaneous human-rights report как дополнительный институциональный sensor для group-specific и conflict-affected условий;
- WHO 2023 summary of 2021 PHC surveys помещён в `RETROSPECTIVE_ONLY`, потому что дата сбора в 2021 не равна публичной наблюдаемости в 2021.

Ключевой результат: health/COVID слой теперь имеет одновременно pressure и stabilizer evidence без ретроспективной подмены cutoff.

## Batch 006 — Мьянма

Усилены displacement и observation layers:

- подтверждена последовательность contemporaneous UNHCR displacement overview sensors на 28 Jun, 5 Jul, 12 Jul и 19 Jul 2021;
- numeric totals по этим картам всё ещё НЕ импортированы без извлечения underlying map/data;
- UNICEF May 2021 дал ранний event-based displacement signal: более 2,000 человек бежали/скрывались после боевых действий в Kayin, при новых перемещениях также в Kachin, northern Shan и Bago;
- падение reported COVID cases/deaths после переворота занесено как observation-process warning, а не как доказательство падения реальной распространённости;
- добавлен структурный climate/disaster baseline World Bank по высокой уязвимости Myanmar к floods/landslides и сильной региональной неоднородности ущерба;
- UNICEF multisector humanitarian continuity добавлен как ограниченный stabilizer;
- OCHA July 2021 snapshot добавлен как дополнительный contemporaneous observation channel, независимый от UNHCR map catalog.

## Observation & Coverage guards

Batch 006 усиливает:

```text
DATA_COLLECTION_TIME != PUBLIC_OBSERVABILITY_TIME
REPORTED_CASE_DECLINE != PREVALENCE_DECLINE
SENSOR_EXISTS != NUMERIC_VALUE_VALIDATED
REGIONAL_EVENT_COUNT != NATIONAL_RATE
HISTORICAL_DISASTER_VULNERABILITY != CURRENT_DISASTER_EVENT
HUMANITARIAN_CONTINUITY != ADEQUATE_COVERAGE
HEALTH_SYSTEM_WEAKNESS != SOCIAL_COLLAPSE
OUT_OF_POCKET_BURDEN != CONFLICT_CAUSE
```

Сохраняются все ранее принятые guards, включая:

```text
OBSERVABILITY != PREVALENCE
VISIBLE_EXCEPTION != BASE_RATE
NATIONAL_AVERAGE != LOCAL_PRESSURE
CONTEMPORANEOUS_SIGNAL != RETROSPECTIVE_RECONSTRUCTION
EVIDENCE_GAP != ZERO_PHENOMENON
```

## Что сознательно НЕ сделано

- `EvidenceState` не рассчитан;
- UNHCR weekly map catalog не превращён в придуманные displacement totals;
- retrospective WHO survey results 2023 не импортированы в 2021 cutoff;
- health-system pressure не превращён в causal explanation войны;
- historical climate vulnerability не выдана за конкретный climate shock 2021;
- гуманитарные программы не объявлены доказанной стабилизацией.

## Оставшиеся крупные пробелы перед первым EvidenceState

### Россия–Украина

1. contemporaneous information operations / agenda amplification 2021–early 2022;
2. язык, культура, collective memory и религиозные институты с допустимыми cutoff-источниками;
3. regional household inequality и food/water/fuel access;
4. original release timing по нужным точкам резервов;
5. дополнительные stabilizers и negative controls;
6. извлечь group-specific subclaims из contemporaneous OHCHR reports, не расширяя их за пределы источника.

### Мьянма

1. извлечь numeric displacement totals из underlying UNHCR maps;
2. diaspora / donations / resistance financing из contemporaneous primary sources;
3. contemporaneous information operations / rumours / propaganda / counter-propaganda;
4. этнические/религиозные group-specific signals;
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
