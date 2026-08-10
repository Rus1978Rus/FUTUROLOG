# BROAD_RESIDUAL_SET_DESIGN 001

**Статус:** `HISTORICAL_CASESET_DESIGN / 10_PLUS_CASE_TARGET / SOURCE_GROUNDED / NOT_YET_BLIND_PACKET`

## 1. Цель

Расширить Structural Gap Inference за пределы четырёх исходных snapshots и проверить три режима:

1. `NO_GAP` — наблюдаемая конфигурация объясняется известными давлениями, стабилизаторами и ограничениями;
2. `SEARCH_TRIGGER` — остаётся устойчивый residual после проверки наблюдаемости/масштаба/лага;
3. `OBSERVABILITY_TRAP` — специально неполный snapshot, где неизвестность не должна превращаться в hidden cause.

Главный guard:

```text
UNKNOWN_VARIABLE != STRUCTURAL_GAP
MISSING_MEASUREMENT != MISSING_MECHANISM
```

## 2. Состав широкого набора

Набор должен включать не менее 12 snapshots, чтобы не было простого баланса 2x2.

### RSET-01 — исходный Case A
Высокий signaling + forward deployment + force-use prior + reassurance + partial channels + visible constraints.
Предварительная evaluator-категория: `NO_GAP_OR_OBSERVABILITY_ONLY`.

### RSET-02 — исходный Case B
Высокое напряжение + costly reassurance + formal deconfliction/hotline + visible constraints.
Предварительная evaluator-категория: `NO_GAP`.

### RSET-03 — исходный Case C
Высокий signaling + unusual concentration + relevant force-use prior + no costly withdrawal + degraded communication.
Предварительная evaluator-категория: `CONDITIONAL_SEARCH_TRIGGER`.

### RSET-04 — исходный Case D
Force already used + lethal force + no comparable costly reassurance + expansion intent unknown.
Предварительная evaluator-категория: `NO_FIRST_USE_GAP / EXPANSION_QUESTION_ONLY`.

### RSET-05 — Кубинский ракетный кризис, 24–26 октября 1962
Source-grounded features: quarantine, high readiness, offensive missile sites nearing readiness, DEFCON escalation, simultaneous direct/indirect communication and UN efforts to avoid direct naval confrontation.
Purpose: extreme danger where communication/reassurance mechanisms coexist with escalation.
Expected use: distinguish `danger` from `structural gap`; test timing-sensitive residual.

### RSET-06 — Таиланд–Камбоджа, февраль–июль 2011
Source-grounded features: repeated armed incidents around Preah Vihear; Security Council call for permanent ceasefire; ASEAN mediation; later ICJ provisional demilitarized zone and immediate withdrawal order.
Purpose: force already used but institutional de-escalation mechanisms visible.
Expected use: no latent first-use inference; evaluate expansion vs stabilization.

### RSET-07 — Кения, 2–31 января 2008
Source-grounded features: disputed election followed by large-scale violence, deaths/displacement and communal targeting; simultaneously growing mediation by AU/Kofi Annan, dialogue and legal/political settlement mechanisms.
Purpose: internal political violence with genuine stabilizer emerging while violence is ongoing.
Expected use: test whether system invents hidden cause instead of representing observed grievance + mediation.

### RSET-08 — Корейский полуостров, август 2015
Source-grounded features: DMZ landmine incident injuring soldiers, high tension and call for Armistice compliance/dialogue; later inter-Korean agreement and regular dialogue mechanism.
Purpose: high-risk interstate/military case with a rapid negotiated de-escalation path.
Expected use: false-positive/NO_GAP candidate depending snapshot date.

### RSET-09 — Косово/Сербия, 29 сентября 2023
Source-grounded features: rising northern Kosovo tensions after violent attack; KFOR already present; NATO authorized additional forces; coordination with Belgrade/Pristina/EULEX/OSCE/UN and explicit call for EU-facilitated dialogue.
Purpose: violence + third-party security stabilizer + reinforcement that can itself look escalatory.
Expected use: test `STABILIZER_FORCE_DEPLOYMENT != ESCALATORY_INTENT`.

### RSET-10 — Гайана–Венесуэла, декабрь 2023 / апрель 2024 split
Source-grounded features: territorial dispute and Argyle dialogue/peace framework, followed by later CARICOM warning that Venezuelan legislation represented renewed escalation and threatened regional peace.
Purpose: temporal reversal — stabilizer exists at t1, renewed pressure at t2.
Expected use: test `PAST_REASSURANCE != DURABLE_RESTRAINT` and cutoff discipline.

### RSET-11 — OBSERVABILITY TRAP synthetic ablation of RSET-05
Remove communication/back-channel and UN de-escalation fields while retaining military escalation fields. Mark snapshot as deliberately incomplete on evaluator side only.
Purpose: see whether coder invents hidden commitment/intent rather than prioritizing `OBSERVABILITY`.
Expected use: `OBSERVABILITY_RESIDUAL`, hidden-factor search blocked or conditional only.

### RSET-12 — OBSERVABILITY TRAP synthetic ablation of RSET-07
Retain violence/deaths/displacement; remove mediation progress and political-dialogue fields from coder view. Evaluator retains knowledge that stabilizer information was omitted.
Purpose: test `KNOWN_STABILIZER_OMITTED?` pre-hidden ladder.
Expected use: coder should flag missing/unknown stabilizer environment rather than assert hidden extremist/elite mechanism.

## 3. Почему нужны synthetic ablations

Исторические кейсы сами по себе не дают контролируемого знания о том, чего кодировщик "не видит". Ablation позволяет взять один и тот же исторический snapshot и намеренно удалить один класс наблюдений.

Это создаёт экспериментальную пару:

```text
FULL_SNAPSHOT vs ABLATED_SNAPSHOT
```

Если Structural Gap Inference начинает создавать hidden-factor hypotheses только после удаления наблюдаемых стабилизаторов, это сигнал чувствительности к observability, а не доказательство хорошего causal inference.

## 4. Метрики

- `NO_GAP_precision`
- `search_trigger_rate`
- `hidden_cause_invention_rate`
- `observability_first_rate`
- `ablation_flip_rate`
- `current_intent_overclaim_rate`
- `first_use_vs_expansion_confusion_rate`
- `stabilizer_force_misclassification_rate`
- `temporal_reassurance_leakage_rate`

## 5. Новые guards для широкого теста

```text
THIRD_PARTY_SECURITY_DEPLOYMENT != ACTOR_ESCALATORY_INTENT
PAST_REASSURANCE != DURABLE_RESTRAINT
FULL_SNAPSHOT_RESULT != ABLATED_SNAPSHOT_RESULT_EXPECTATION
ABLATION_INDUCED_GAP != REAL_WORLD_HIDDEN_CAUSE
VIOLENCE_ALREADY_OBSERVED => FIRST_USE_NOT_LATENT
MEDIATION_EXISTS != MEDIATION_EFFECTIVE
MEDIATION_PROGRESS != CONFLICT_RESOLVED
```

## 6. Источники, использованные для отбора

- U.S. Office of the Historian: Cuban Missile Crisis chronology and communications, October 1962.
- ICJ: Cambodia v. Thailand provisional measures, 18 July 2011.
- UN Secretary-General / DPPA: Kenya post-election violence and mediation, January–February 2008.
- UN Secretary-General: Korean Peninsula DMZ incident and 24 August 2015 agreement.
- NATO: Kosovo tensions and KFOR reinforcement, 29 September–October 2023.
- CARICOM: Guyana–Venezuela escalation statement referencing the Argyle Declaration, April 2024.

## 7. Следующий артефакт

`BROAD_BLIND_RESIDUAL_PACKET_002_RU`:
- 12 anonymized snapshots;
- randomized order;
- no country names;
- no outcome labels;
- no evaluator categories;
- identical coding schema for every row;
- separate evaluator key not supplied to external coders.

## 8. Status

```text
BROAD_RESIDUAL_SET_DESIGN_001 = COMPLETE
HISTORICAL_CASES_SELECTED = 10_REAL_OR_EXISTING + 2_CONTROLLED_ABLATIONS
BLIND_PACKET = NEXT
NUMERIC_EVIDENCESTATE = BLOCKED
```
