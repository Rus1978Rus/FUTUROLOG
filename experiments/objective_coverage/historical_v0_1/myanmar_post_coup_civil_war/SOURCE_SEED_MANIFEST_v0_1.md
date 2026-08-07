# SOURCE_SEED_MANIFEST v0.1 — MYANMAR POST-COUP CIVIL-WAR ESCALATION

**Статус:** `SEED_ONLY / NOT_COMPLETE / NOT_NUMERIC_INPUT_YET`

Этот manifest (реестр источников) фиксирует начальные source families для сбора historical evidence. Наличие источника здесь не означает автоматического включения каждого его материала в snapshot.

## UN / OHCHR

- OHCHR — Human Rights Situation / February 2021: contemporaneous monitoring of the coup, detentions, assembly restrictions and repression.
- OHCHR — 1 April 2021 regional release: by then documented large-scale lethal repression and renewed fighting with ethnic armed organizations.
- OHCHR A/HRC/48/67 and supplementary chronology: emerging armed resistance, NUG/PDF formation and armed clashes across multiple administrative areas. Late publication must be separated into `OUTCOME_ONLY` versus contemporaneously knowable facts.
- OHCHR Special Rapporteur later chronology: useful only for outcome verification of the sequence local defence forces → PDF formation → September declaration; not allowed as pre-cutoff evidence unless the underlying item was published before cutoff.

## REUTERS

- 29 January 2021: military pressure over the November election and explicit coup fears before parliament convened.
- 30 March 2021: renewed ethnic armed conflict and discussion of a broader anti-coup/federal armed alignment.

Each Reuters item must retain original publication timestamp and must not be replaced by a later retrospective story when building a snapshot.

## WORLD BANK

- Myanmar Economic Monitor / July 2021 and associated July 2021 release: severe economic contraction, labour/income effects, banking/payment constraints, logistics and telecommunications disruption, currency depreciation and trade stress.
- Pre-coup 2020 Myanmar Economic Monitor material may be used as economic baseline / negative control, with COVID effects explicitly separated from post-coup shock.

## ASEAN / DIPLOMACY

ASEAN Five-Point Consensus and related contemporaneous diplomatic statements are candidate counter-signal/de-escalation evidence. They must be collected with exact publication dates before use in observed_noise or counter-signal coding.

## Local independent media

Potentially useful for high-frequency evidence, but:

```text
LOCAL_REPORT_COUNT != SOURCE_INDEPENDENCE
```

Each local outlet requires provenance review, source-family assignment, publication-time verification and duplicate/syndication checks.

## Collection rule

Before the first numerical snapshot, each evidence item must have:

```text
item_id
source_family
publisher
original_publication_time
retrieval_time
url_or_archive_locator
evidence_class
direction
strength
pipeline_steps_completed
cutoff_eligibility
provenance_status
```

## Current limitation

This seed manifest is intentionally insufficient for an honest `observed_noise` estimate because counter-signals/de-escalation evidence have not yet been collected systematically.

Status until that work is done:

`COUNTER_SIGNAL_COLLECTION_REQUIRED`.
