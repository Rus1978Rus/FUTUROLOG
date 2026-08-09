# FORMAL_GAP_AUDIT v0.1

**Статус:** `FORMAL_GAP_AUDIT_COMPLETE / PRE_EVIDENCESTATE_NOT_READY / TARGETED_BACKFILL_REQUIRED`

## Назначение

Аудит выполнен после Batch 001–007 для двух исторических пилотных кейсов: Россия–Украина и Мьянма. Он не вычисляет риск, не делает прогноз и не запускает EvidenceState. Цель — определить, какие части замороженной схемы уже покрыты данными, какие покрыты частично и какие пробелы блокируют честный dry run.

## Классы покрытия

- `COVERED_WORKING` — есть рабочая основа для нечислового dry run.
- `PARTIAL` — данные есть, но покрытие узкое, локальное или зависит от малого числа source families.
- `SENSOR_ONLY` — подтверждено существование сенсора/документа, но содержимое ещё не импортировано в пригодной форме.
- `RETROSPECTIVE_ONLY` — материал полезен как контроль, но запрещён для раннего cutoff.
- `EVIDENCE_GAP` — нужный класс данных пока не закрыт.

Guards:

```text
DOMAIN_PRESENT != DOMAIN_WELL_COVERED
SOURCE_COUNT != INDEPENDENT_CONFIRMATION
SENSOR_PRESENT != MEASUREMENT_IMPORTED
RETROSPECTIVE_KNOWLEDGE != CUTOFF_KNOWLEDGE
```

## Россия–Украина

`COVERED_WORKING`:
- historical causal depth;
- resource sustainment и внешняя поддержка;
- sanctions / macro-resource signals;
- displacement / IDP / contact-line access;
- education / COVID learning pressure + adaptation;
- institutional expectations / threat perception;
- health-system pressure + stabilizers;
- contemporaneous information-manipulation narratives;
- energy-market stress как multi-causal signal.

`PARTIAL`:
- social inequality / household distribution;
- identity / language / collective memory;
- religion / religious institutions;
- food / water / fuel household access;
- stabilizers вне education/health/IDP;
- complete observation-topology map.

`RETROSPECTIVE_ONLY / CAUTION`:
- поздние synthesis по информационным операциям;
- часть поздних энергетических сводок;
- historical reserve series без восстановленного original release timing каждого cutoff point.

Critical gaps:
1. regional household inequality / affordability;
2. language-culture-memory с несколькими независимыми source families;
3. religious institutions / intergroup relations;
4. household food/water/fuel access;
5. topology-of-coverage map;
6. negative controls.

## Мьянма

`COVERED_WORKING`:
- historical causal depth;
- military business / resource base;
- pre-coup COVID/poverty pressure;
- Civil Disobedience Movement and professional groups;
- internet restrictions / observation degradation;
- macroeconomic, banking/payment/logistics pressure;
- food/fuel prices and regional heterogeneity;
- humanitarian stabilizers;
- education pressure + pre-coup adaptation;
- displacement event evidence;
- ethnic/religious minority exposure in conflict-affected regions;
- community/religious humanitarian assistance;
- climate/disaster structural vulnerability and Rakhine agriculture/fisheries pressure.

`PARTIAL`:
- social inequality / legitimizing strata;
- water security;
- small-group coalescence and fragmentation;
- content-level information operations / rumours / propaganda;
- systematic ethnic/religious group coverage;
- institutional stabilizers.

`SENSOR_ONLY`:
- multiple UNHCR weekly displacement map products May–July 2021: dates are known, but numeric totals from underlying map/data are not yet validated/imported.

Critical gaps:
1. numeric displacement snapshots for several cutoff dates;
2. diaspora/donations/external-support provenance for non-state actors;
3. content-level contemporaneous information-operation evidence;
4. direct water-access / flood-impact records beyond structural baseline;
5. earlier and better-resolved timelines for small-group formation/coalescence;
6. negative controls and stronger stabilizer coverage.

## Cross-case comparability

Одинаковая замороженная схема применена к обоим кейсам, но наблюдаемость несимметрична.

Россия–Украина сильнее покрыта по macro/energy/resource signals, polling/institutional attitudes, formal health/education evidence и contemporaneous disinformation cataloguing.

Мьянма сильнее покрыта по local food/fuel stress, displacement/humanitarian evidence, professional-group mobilization, internet shutdown / sensor degradation и community-level response.

```text
SAME_SCHEMA != SAME_OBSERVABILITY
CROSS_CASE_SCORE_DIFFERENCE != TRUE_STATE_DIFFERENCE
```

## Gate assessment

```text
MULTIPLE_SOURCE_FAMILIES: PARTIAL_PASS
PRESSURE_AND_STABILIZERS: PARTIAL_PASS
RETROSPECTIVE_CUTOFF_GUARD: PASS
TOPOLOGY_GAPS_IDENTIFIED: PASS
MISSING_DOMAINS_EXPLICIT: PASS
SAME_FROZEN_SCHEMA: PASS
READY_FOR_NUMERIC_EVIDENCESTATE: NO
READY_FOR_NON_NUMERIC_PRE_EVIDENCESTATE_DRY_RUN: ALMOST
```

## Следующий шаг

Вместо ещё одного широкого Batch 008 нужен `TARGETED_BACKFILL_008` только по blocking gaps. После него проводится повторный gap audit. Если critical `EVIDENCE_GAP` по обязательным слоям закрыты, разрешается `PRE_EVIDENCESTATE_DRY_RUN` — нечисловой прогон. Числовой EvidenceState остаётся заблокирован до отдельного calibration/evaluation gate.

## Статус

```text
FORMAL_GAP_AUDIT_COMPLETE
SCHEMA_FREEZE_PRESERVED
TARGETED_BACKFILL_REQUIRED
NUMERIC_EVIDENCESTATE_BLOCKED
NON_NUMERIC_DRY_RUN_NEAR_READY
NOT_VALIDATED
```
