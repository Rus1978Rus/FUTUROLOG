# BLIND_SECOND_CODER_PACKET 001

**Статус:** `READY_FOR_EXTERNAL_OR_SEPARATE_CODER / FIRST_LEDGER_HIDDEN_BY_PROTOCOL / NO_OUTCOME_LABELS_IN_PACKET`

## 1. Назначение

Этот пакет предназначен для настоящей второй кодировки подмножества evidence без просмотра `FIRST_CODING_LEDGER_001.csv` и без просмотра первого результата.

Coder должен получить только:

1. этот пакет;
2. frozen coding rubric;
3. тексты выбранных evidence claims и их cutoff metadata;
4. source limitations.

Coder НЕ должен получать:

- `FIRST_CODING_LEDGER_001.csv`;
- `SECOND_CODING_CHECK_001_RU.md`;
- итог события как подсказку;
- post-event synthesis для pre-event cutoff;
- готовый expected score.

## 2. Rubric

Direction:

```text
+1 SUPPORTS_PRESSURE_OR_ESCALATION
 0 NEUTRAL_OR_UNCLEAR_OR_EXCLUDED
-1 COUNTERSIGNAL_OR_STABILIZER
```

Strength:

```text
0 EXCLUDED_OR_NOT_DIRECTIONAL
1 WEAK
2 SUBSTANTIAL
3 SEVERE
```

Для каждого item coder обязан записать:

```text
item_id
coded_direction
coded_strength
coding_reason
ambiguity_status = LOW | MEDIUM | HIGH
cutoff_admissibility = PASS | FAIL | CONDITIONAL
```

## 3. Guards

```text
NARRATIVE_EXISTS != POPULATION_BELIEF
PROGRAM_EXISTS != PROGRAM_EFFECTIVE
PROJECTION != OBSERVED_COUNT
SENSOR_EXISTS != NUMERIC_VALUE_VALIDATED
RETROSPECTIVE_KNOWLEDGE != CUTOFF_KNOWLEDGE
PRESSURE != OUTCOME
STABILIZER != PROVEN_STABILIZATION
```

## 4. Blind items — Россия–Украина

### RU-EV-007-001

Publication: 2021-12-23

Claim: EUvsDisinfo reported that more than 2,700 pro-Kremlin disinformation examples had been added in 2021 and roughly one-third targeted Ukraine, making Ukraine the main target in that monitored dataset during the year.

Limitations: curated monitoring database; not representative of all media consumption or public beliefs; example count is not population prevalence.

### RU-EV-007-003

Publication: 2021-12-06

Claim: EUvsDisinfo documented a pro-Kremlin narrative portraying warnings of Russian aggression as fabricated hysteria.

Limitations: proves existence of a monitored narrative case; does not establish reach, belief adoption or behavioral effect.

### RU-EV-007-005

Publication: 2022-01-24

Claim: EU foreign ministers called for stronger resilience and response capabilities against cyber/hybrid attacks and foreign information manipulation while reaffirming support for Ukraine and diplomatic mechanisms.

Limitations: policy commitment does not prove mitigation effectiveness.

### RU-EV-007-006

Publication: 2022-10-24

Target cutoff: before 2022-02-24.

Claim: a later EEAS synthesis reported a sharp increase in some monitored pro-Kremlin narratives during the three months before 24 February 2022.

Limitations: synthesis was published after the target cutoff.

## 5. Blind items — Мьянма

### MM-EV-003-001

Publication: 2021-03-16

Claim: WFP reported monitored food-price and fuel-price increases after the coup, including substantial palm-oil and fuel increases and smaller rice increases in some monitored areas.

Limitations: monitored markets are not every household or market; price changes varied by township.

### MM-EV-003-003

Publication: 2021-03-16

Claim: WFP reported near paralysis of the banking sector, slowing remittances and widespread cash-availability limits.

Limitations: does not fully measure informal finance channels.

### MM-EV-003-004

Publication: 2021-03-16

Claim: WFP reported building contingency food stocks to preserve assistance to more than 360,000 people if cash or market supply became constrained.

Limitations: prepared assistance does not prove needs were fully met or broader instability reduced.

### MM-EV-003-005

Publication: 2021-04-22

Claim: WFP warned that poverty, COVID-19 and political crisis were combining to increase hunger; it projected up to 3.4 million additional people could become hungry within six months and described observed coping behaviors such as skipped meals and debt.

Limitations: projected total is not an observed count; household examples are not a population denominator.

### MM-EV-003-007

Publication: 2021-12-31

Target cutoff: early 2021.

Claim: UNHCR year-end reporting recorded large post-coup displacement totals.

Limitations: year-end synthesis is not admissible for early-2021 cutoffs.

### MM-EV-003-008

Publication: 2021-06-21

Claim: UNHCR published a dated displacement overview, establishing contemporaneous geospatial monitoring.

Limitations: this establishes a sensor/document, not a validated numeric displacement claim until the underlying map/data are extracted.

## 6. Output template

```csv
item_id,coded_direction,coded_strength,coding_reason,ambiguity_status,cutoff_admissibility
RU-EV-007-001,,,,,
RU-EV-007-003,,,,,
RU-EV-007-005,,,,,
RU-EV-007-006,,,,,
MM-EV-003-001,,,,,
MM-EV-003-003,,,,,
MM-EV-003-004,,,,,
MM-EV-003-005,,,,,
MM-EV-003-007,,,,,
MM-EV-003-008,,,,,
```

## 7. После получения second code

Сравнение проводится механически с `FIRST_CODING_LEDGER_001.csv`.

Минимальные показатели:

```text
exact_direction_agreement
exact_strength_agreement
mean_absolute_strength_difference
cutoff_admissibility_agreement
high_ambiguity_count
```

Если disagreement концентрируется в одном типе evidence, проблема должна быть исправлена в rubric v0.2, а не вручную «подогнана» в результатах.

## 8. Статус

```text
BLIND_PACKET_READY
TRUE_SECOND_CODER_RESULT_MISSING
AGREEMENT_REPORT_BLOCKED_UNTIL_SECOND_CODE
NUMERIC_EVIDENCESTATE_BLOCKED
```
