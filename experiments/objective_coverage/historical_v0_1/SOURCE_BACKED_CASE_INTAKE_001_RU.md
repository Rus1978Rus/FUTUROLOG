# SOURCE-BACKED CASE INTAKE 001

**Статус:** `SOURCE_INTAKE / 8_CASES / PRIMARY_OR_INSTITUTIONAL_SOURCES_PREFERRED / CASE_CARDS_NOT_YET_COMPLETE`

## 1. Цель

Собрать первую восьмёрку исторических макросистемных переходов для последующей нормализации в `HISTORICAL_TRANSITION_CASE_CARD_v0_1`.

Этот документ не является blind packet и не используется как outcome-hidden input. Он служит evaluator/source layer.

## 2. Россия 1917 — отречение Николая II

**Transition family:** `REGIME_COLLAPSE_STATE_TRANSFORMS`

**Anchor outcome:** отречение Николая II 2/15 марта 1917; затем отказ Михаила принять верховную власть без решения Учредительного собрания.

**Primary/institutional source anchors:**
- U.S. Office of the Historian, FRUS 1917/1918 Russia, chapter on March Revolution and abdication.
- Telegram of Ambassador Francis, March 17/18, 1917.

**Why useful:** формальные институты, армия и бюрократия существовали, но политическая исполнимость и лояльность критических узлов быстро изменились.

**Candidate cutoffs:**
- pre-collapse: before mass mutiny/elite convergence;
- near-threshold: before abdication telegram becomes known;
- post-threshold evaluator-only.

**Key dimensions:** command executability; garrison loyalty; Duma/elite coordination; war pressure; transport/logistics; alternative authority.

## 3. Румыния 1989 — падение режима Чаушеску

**Transition family:** `PERSONALIZED_REGIME_COLLAPSE / STATE_SURVIVES`

**Institutional source anchors:**
- U.S. Office of the Historian FRUS Romania series establishes late-1980s deterioration of relations, human-rights/economic disputes and the highly personalized Ceausescu regime context.

**Source gap:** exact December 1989 cutoff chronology still requires dedicated primary-source intake (contemporaneous diplomatic cables, Romanian archival records, broadcast/event timestamps). Do not infer threshold mechanics solely from retrospective summaries.

**Why useful:** apparent public compliance under repression versus latent cohesion; cascade of public defiance; critical-node defection; executability of coercive capacity.

**Candidate cutoffs:** before Timișoara escalation; before 21 Dec Bucharest rally; immediately after public rally disruption but before regime fall.

## 4. СССР 1991 — системная фрагментация

**Transition family:** `SYSTEM_FRAGMENTATION`

**Institutional source anchors:**
- U.S. Office of the Historian, “The Collapse of the Soviet Union.”
- FRUS 1989–1992, USSR volume/chapter structure through August 1991.

**Observed evaluator outcome anchors:** failed August coup weakened Gorbachev and strengthened Yeltsin; subsequent republican independence moves; CIS formation in December; Gorbachev resignation 25 Dec 1991.

**Why useful:** formal central capacity coexists with declining effective cohesion; multiple alternative legitimacy centers; elite/node defection; federation/republic exit option.

**Candidate cutoffs:** before August coup; immediately after coup failure; before Belavezha/CIS agreement.

## 5. Китай 1989 — regime survival under mass pressure

**Transition family:** `SURVIVE_BY_REPRESSION / STATE_AND_REGIME_SURVIVE`

**Source status:** dedicated source intake still required. Prefer FRUS China 1989 documents, declassified diplomatic cables, official contemporaneous records and independent institutional archives.

**Why useful:** high mass mobilization does not imply regime collapse; coercive capacity must be separated from political usability and command execution; elite cohesion/fragmentation needs dated evidence.

**Candidate cutoffs:** before martial-law enforcement; before final military clearing; short post-event slice evaluator-only.

## 6. Беларусь 2020 — regime survival without foreign troop deployment

**Transition family:** `SURVIVE_UNDER_MASS_PRESSURE / EXTERNAL_SUPPORT_AVAILABLE`

**Institutional source anchors:**
- OSCE ODIHR, 10 Aug 2020: reports intimidation and disproportionate police force after the election, widespread injuries/arrests and calls for dialogue.
- UN Human Rights Council resolutions on Belarus 2020 aftermath.

**Important distinction:** Russian political/economic/security backing and discussed/available support must not be coded as observed deployment of Russian troops for suppressing protests.

**Why useful:** external support availability/expectation versus actual deployment; coercive-node loyalty; persistence of mass mobilization without regime collapse.

**Candidate cutoffs:** election eve; 10 Aug; later mass-protest peak before stabilization.

## 7. Казахстан 2022 — regime survival with CSTO deployment

**Transition family:** `SURVIVE_BY_EXTERNAL_SUPPORT + INTERNAL_COERCION`

**Institutional source anchors:**
- CSTO official record: collective peacekeeping contingents deployed and withdrawal completed by 19 Jan 2022.

**Important distinction:** CSTO deployment is an observed external stabilizer; its exact causal contribution to regime survival must not be assumed from mere presence.

**Why useful:** paired control for Belarus: external support `AVAILABLE/EXPECTED` versus `DEPLOYED`.

**Candidate cutoffs:** before CSTO request; immediately after deployment decision; before withdrawal.

## 8. ЮАР 1990–1994 — negotiated power transfer, state survives

**Transition family:** `NEGOTIATED_TRANSFORMATION / POWER_TRANSFER_STATE_SURVIVES`

**Institutional source anchors:**
- U.S. Office of the Historian, “The End of Apartheid.”

**Observed evaluator outcome anchors:** de Klerk lifted bans on ANC/other organizations and political prisoners were released in 1990; negotiations led to democratic elections; Mandela elected in April 1994.

**Why useful:** loss of ruling-group political monopoly without state collapse; incumbent-elite exit option; sanctions/economic pressure; negotiated guarantees and continued institutional capacity.

**Candidate cutoffs:** before Feb 1990 reforms; after Mandela release but before settlement; before 1994 election.

## 9. Родезия → Зимбабве 1965–1980 — war, sanctions, negotiated transfer

**Transition family:** `PROLONGED_RETENTION_WAR → NEGOTIATED_POWER_TRANSFER`

**Institutional source anchors:**
- FRUS 1977–1980 Southern Africa: Rhodesia chapter, Lancaster House negotiations, sanctions and cease-fire arrangements.
- UN decolonization records identify Southern Rhodesia’s transition to independent Zimbabwe in 1980.

**Observed evaluator outcome anchors:** Lancaster House all-party negotiations in 1979; continued sanctions during negotiations; cease-fire support; Zimbabwe independence in 1980.

**Why useful:** compares directly with South Africa while adding prolonged armed struggle, sanctions and international mediation.

**Candidate cutoffs:** before 1979 internal settlement election; during Lancaster House before settlement; immediately before cease-fire implementation.

## 10. First paired families

```text
Russia 1917 ↔ China 1989
  collapse vs survival under mass/internal pressure

Romania 1989 ↔ Belarus 2020
  personalized regime collapse vs personalized regime survival

Belarus 2020 ↔ Kazakhstan 2022
  external backing available/expected vs external force deployed

South Africa 1990–94 ↔ Rhodesia/Zimbabwe 1979–80
  negotiated majority rule with different preceding coercion/war trajectories

USSR 1991 ↔ future federation-survival control
  fragmentation vs federation surviving severe centrifugal pressure
```

## 11. Required next source work

Priority gaps:

1. Romania December 1989 contemporaneous chronology.
2. China 1989 contemporaneous chronology and elite/coercive command evidence.
3. Belarus external-support evidence separated into availability, expectation and deployment.
4. Kazakhstan pre-request and request/deployment timestamps.
5. Russia 1917 pre-abdication node-loyalty chronology.
6. USSR 1991 republic/elite/command snapshots before and after August coup.
7. South Africa negotiation guarantees/elite-exit-option evidence.
8. Rhodesia war-cost, sanctions, military pressure and negotiation snapshots.

## 12. Guards

```text
OUTCOME_SOURCE != BLIND_INPUT
POST_EVENT_SYNTHESIS != CUTOFF_KNOWLEDGE
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
MEDIATION_EXISTS != MEDIATION_EFFECTIVE
SANCTIONS_EXIST != SANCTIONS_CAUSED_TRANSITION
MASS_PROTEST != REGIME_COLLAPSE
NEGOTIATION != SUCCESSFUL_TRANSFORMATION
```
