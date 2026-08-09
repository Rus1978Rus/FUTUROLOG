# NEGATIVE CONTROL TARGETED BACKFILL 010

**Статус:** `TARGETED_NEGATIVE_CONTROL_BACKFILL / CONTEMPORANEOUS_COUNTERSIGNALS_ADDED / NOT_VALIDATION`

## 1. Цель

После `SECOND_CODING_CHECK_001` числовой EvidenceState остаётся заблокирован. Этот backfill не ищет искусственный баланс. Он добавляет contemporaneous counter-signals и partial-normality signals, которые могли бы уменьшить риск hindsight selection.

```text
BALANCED_RECORD_COUNT != BALANCED_REALITY
COUNTERSIGNAL != PROOF_OF_SAFETY
TEMPORARY_DEESCALATION != RESOLVED_CONFLICT
LOCAL_FUNCTION != SYSTEM_STABILITY
```

## 2. Россия–Украина

### RU-NC-010-001 — partial troop pullback, May 2021

Источник: NATO, 6 May 2021.

Contemporaneous observation: NATO Secretary General stated that Russia had withdrawn some troops from Ukraine's border after the spring build-up. At the same time, tens of thousands remained and NATO assessed the overall presence as still significantly above the level before the increase in tensions.

Coding:

```text
role = COUNTERSIGNAL / PARTIAL_DEESCALATION
strength = SUBSTANTIAL_BUT_INCOMPLETE
cutoff_admissibility = ADMISSIBLE_AFTER_2021_05_06
```

Guard:

```text
PARTIAL_WITHDRAWAL != FULL_DEESCALATION
```

### RU-NC-010-002 — localized ceasefires supporting infrastructure, July 2021

Источник: OSCE SMM daily reports, July 2021.

OSCE repeatedly recorded that the mission facilitated and monitored localized ceasefires enabling operation or maintenance of critical civilian infrastructure. Individual daily reports also show large day-to-day variation in recorded ceasefire violations.

Coding:

```text
role = STABILIZER / LOCAL_FUNCTIONAL_CONTINUITY
strength = WEAK_TO_SUBSTANTIAL_LOCAL
cutoff_admissibility = DATE_SCOPED
```

Guards:

```text
LOCALIZED_CEASEFIRE != GENERAL_CEASEFIRE
LOWER_DAILY_COUNT != DURABLE_DEESCALATION
DAILY_EVENT_COUNT != LONG_TERM_BASE_RATE
```

### RU-NC-010-003 — diplomatic channels remained explicitly available

Источник: NATO statements, April and December 2021.

NATO publicly called for de-escalation and diplomatic engagement and stated openness to focused dialogue with Russia. This is evidence that diplomatic channels and de-escalatory alternatives remained part of the contemporaneous state space; it is not evidence that they would succeed.

Coding:

```text
role = COUNTERSIGNAL / DIPLOMATIC_OPTION_SPACE
strength = WEAK
```

Guard:

```text
DIPLOMATIC_CHANNEL_EXISTS != DIPLOMATIC_SUCCESS_PROBABLE
```

## 3. Мьянма

### MM-NC-010-001 — partial logistics and mobility stabilization, May–June 2021

Источник: World Bank Myanmar Economic Monitor, July 2021.

The World Bank reported initial signs of stabilization in some areas during May and June: mobility improved and logistics disruptions eased. It simultaneously reported that overall economic activity remained very weak and that the COVID third wave threatened renewed contraction.

Coding:

```text
role = COUNTERSIGNAL / PARTIAL_FUNCTIONAL_RECOVERY
strength = SUBSTANTIAL_BUT_LOCAL_OR_PARTIAL
cutoff_admissibility = ADMISSIBLE_AFTER_PUBLICATION_2021_07_23
```

Guards:

```text
PARTIAL_RECOVERY != SYSTEM_RECOVERY
LOGISTICS_IMPROVEMENT != POLITICAL_STABILIZATION
```

### MM-NC-010-002 — bank branches/interventions as incomplete stabilizer

The same contemporaneous World Bank assessment recorded bank branch reopenings and interventions by the Central Bank of Myanmar, while cash shortages and limited payment access persisted.

Coding:

```text
role = STABILIZER / INSTITUTIONAL_FUNCTION_ATTEMPT
strength = WEAK_TO_SUBSTANTIAL
```

Guard:

```text
SERVICE_REOPENING != SERVICE_NORMALIZATION
POLICY_INTERVENTION != EFFECTIVE_STABILIZATION
```

### MM-NC-010-003 — easing of some internet restrictions

The July 2021 World Bank monitor recorded some loosening of internet restrictions, including the end of nightly fixed-line broadband blocks and access to some whitelisted online services, while access remained constrained.

Coding:

```text
role = COUNTERSIGNAL / ACCESS_PARTIAL_RECOVERY
strength = WEAK
```

Guard:

```text
PARTIAL_ACCESS_RESTORATION != OPEN_INFORMATION_ENVIRONMENT
```

## 4. Что этот backfill исправляет

Он уменьшает риск, что corpus построен только из событий, которые после знания исхода выглядят как предвестники эскалации.

Он НЕ доказывает отсутствие selection bias. Для этого нужны:

- systematic false-positive analogue cases;
- blind second coder;
- agreement report;
- повторный gate review.

## 5. Gate

```text
TARGETED_COUNTERSIGNALS: PASS
CONTEMPORANEOUS_COUNTERSIGNALS: PASS
ARTIFICIAL_BALANCING: NO
FALSE_POSITIVE_ANALOGUES: STILL_REQUIRED
BLIND_SECOND_CODER: STILL_REQUIRED
NUMERIC_EVIDENCESTATE: BLOCKED
```
