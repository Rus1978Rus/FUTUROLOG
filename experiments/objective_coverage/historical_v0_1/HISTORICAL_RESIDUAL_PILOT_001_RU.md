# HISTORICAL_RESIDUAL_PILOT 001

**Статус:** `BLIND_CASE_RESIDUAL_ANALYSIS_COMPLETE / HYPOTHESIS_GENERATION_ONLY / NO_OUTCOME_LABELS_USED / NOT_VALIDATED`

## 1. Цель

Проверить `STRUCTURAL_GAP_INFERENCE_001` на четырёх обезличенных force-signaling snapshots A–D. Анализ использует только признаки, доступные в blind packet. Названия стран и будущие исходы не используются как вход.

Задача не угадать, чем закончится кризис, а определить:

1. где текущая модель уже объясняет наблюдаемую конфигурацию без скрытого фактора;
2. где остаётся residual;
3. какого класса недостающая структура могла бы этот residual объяснить;
4. какое различающее свидетельство нужно искать;
5. когда residual должен быть признан артефактом наблюдаемости или слабости модели.

## 2. Pre-hidden-factor checklist

Для каждого residual сначала проверяются:

```text
DATA_ERROR?
CUTOFF_LEAKAGE?
SOURCE_DEPENDENCE?
OBSERVATION_GAP?
WRONG_SCALE?
WRONG_ACTOR_AGGREGATION?
TEMPORAL_LAG?
KNOWN_STABILIZER_OMITTED?
KNOWN_PRESSURE_OMITTED?
```

Только после отрицательного/неполного результата разрешён `MISSING_STRUCTURE_HYPOTHESIS`.

---

## 3. Case A

### Наблюдаемая конфигурация

```text
HIGH signaling
LARGE forward deployment
NO general withdrawal confirmed at cutoff
past force-use prior PRESENT
reassurance language PRESENT
partial diplomatic channels PRESENT
nuclear/international constraints visible
intent UNKNOWN
```

### Residual A-R1

**Тип:** `R6 SIGN_MISMATCH / R2 PERSISTENT_BEHAVIORAL_RESIDUAL`

Тension:

```text
VISIBLE_HIGH_CONSTRAINTS
+ DIALOGUE_OFFRAMPS
+ MUTUAL_WITHDRAWAL_LANGUAGE
+ LARGE_FORWARD_DEPLOYMENT_PERSISTS
```

Текущая модель умеет представить и давление, и стабилизаторы, поэтому hidden-factor hypothesis не требуется автоматически. Residual появляется только если persistence deployment продолжается заметно дольше, чем предполагает observable bargaining/de-escalation process.

### Hypothesis set

```text
A-H1 signaling is primarily coercive bargaining, not preparation for first strike
A-H2 domestic/political cost of backing down is high
A-H3 operational readiness is lower than deployment visibility suggests
A-H4 leadership believes constraints make opponent concession more likely
A-H5 reciprocal withdrawal sequencing problem prevents first move
A-H6 public observation overstates actual escalation readiness
```

### Discriminating evidence

Искать до cutoff:

- фактические изменения readiness/logistics, а не только troop counts;
- withdrawal sequencing proposals;
- reciprocal confidence-building steps;
- changes in leave, ammunition, medical/logistics posture;
- evidence that forces are moving from signaling posture to employment posture;
- domestic rhetoric penalizing compromise versus language preparing public for compromise.

### Falsification logic

Если появляются проверяемые reciprocal withdrawal steps и readiness снижается, гипотезы о скрытом низком пороге применения силы ослабевают. Если наоборот логистика/готовность растут при исчезновении reassurance, residual меняет класс в сторону commitment transition.

---

## 4. Case B

### Наблюдаемая конфигурация

```text
HIGH_OR_ELEVATED signaling
ACTIVE military friction risk
first use not established
STRONG costly reassurance
FORMAL hotline/deconfliction mechanism
alliance/direct constraints visible
intent UNKNOWN
```

### Residual B-R1

**Тип:** `NO_HIDDEN_FACTOR_REQUIRED / CONTROL_CASE`

На cutoff явного противоречия нет. Модель уже содержит механизм, который объясняет одновременное существование высокой напряжённости и сдерживания:

```text
HIGH_SIGNALING
+ WORKING_DECONFLICTION
+ COSTLY_REASSURANCE
+ VISIBLE_CONSTRAINTS
```

Это важный negative control для Structural Gap Inference. Система НЕ должна создавать hidden-factor hypothesis только потому, что ситуация выглядит опасной.

### Search plan

Вместо поиска тайных причин проверять устойчивость observable stabilizers:

- hotline actually used?
- exercises/incidents reduced?
- mechanism survives new incidents?
- withdrawal/separation measures appear?
- reassurance costly or merely declarative?

### Guard

```text
DANGEROUS_CONFIGURATION != STRUCTURAL_GAP
MODEL_CAN_EXPLAIN_STATE => DO_NOT_INVENT_HIDDEN_FACTOR
```

---

## 5. Case C

### Наблюдаемая конфигурация

```text
HIGH signaling
LARGE unusual concentration near target
STRONG relevant past force-use prior
NO comparable costly withdrawal signal
communication channels DEGRADED
political/economic costs visible
cost tolerance UNKNOWN
intent UNKNOWN
```

### Residual C-R1

**Тип:** `R2 PERSISTENT_BEHAVIORAL_RESIDUAL + R5 TIMING_MISMATCH`

Tension:

```text
VISIBLE_EXPECTED_COSTS
+ DIPLOMATIC_OFFRAMPS_EXIST
+ RELEVANT_FORCE_USE_PRIOR
+ LARGE_UNUSUAL_PREPARATION_PERSISTS
+ NO_COMPARABLE_COSTLY_REASSURANCE
```

Модель показывает более опасную конфигурацию, но всё ещё не знает intent. Structural gap появляется в вопросе: **почему дорогостоящая подготовка сохраняется несмотря на видимые внешние издержки и наличие offramps?**

### Hypothesis set

```text
C-H1 leadership discounts expected sanctions/economic costs
C-H2 leadership expects rapid/low-cost coercive or military success
C-H3 objective has high non-economic/ideological/security value
C-H4 domestic political cost of retreat exceeds external cost
C-H5 preparation serves coercive bargaining and will stop after concession
C-H6 private intelligence/assessment differs sharply from public estimates
C-H7 public force picture exaggerates actual employment readiness
C-H8 internal deadline/commitment exists but is not observable
```

### Discriminating evidence

Искать не общий "агрессивный тон", а признаки, разделяющие H1–H8:

- logistics compatible with sustained combat versus reversible signaling;
- reserve/medical/ammunition/fuel posture;
- changes in diplomatic demands: negotiable vs non-negotiable;
- elite/public preparation for costs;
- economic insulation measures taken before cutoff;
- evidence of expectation of quick success;
- observable willingness to accept partial concessions;
- costly withdrawal/reduction if bargaining goals are met;
- sudden shortening of decision window or ultimatum structure.

### Important guard

```text
STRONG_PRIOR + HIGH_SIGNALING != CURRENT_INTENT_PROVEN
```

Residual may justify targeted search, not a declaration of hidden war plan.

---

## 6. Case D

### Наблюдаемая конфигурация

```text
FORCE_ALREADY_USED
LETHAL_FORCE_OBSERVED
no comparable costly reassurance
international condemnation visible
cost tolerance partially revealed by continued force use
expansion intent UNKNOWN
```

### Residual D-R1

**Тип:** `R3 MISSING_LINK / R5 TIMING_MISMATCH`

First-use residual is closed: force is already observed. The missing question is transition from episodic force to broader/systematic repression.

```text
OBSERVED_LETHAL_FORCE
→ ?
→ POSSIBLE_EXPANSION_IN_SCALE / GEOGRAPHY / WEAPON_TYPE / SYSTEMATICITY
```

### Hypothesis set

```text
D-H1 incidents are locally driven and not a centralized expansion policy
D-H2 centralized policy authorizes progressively broader repression
D-H3 escalation depends on protest persistence/geographic spread
D-H4 internal security-force cohesion/dissent constrains expansion
D-H5 international costs are discounted
D-H6 violence is intended as short, high-intensity deterrent rather than sustained campaign
```

### Discriminating evidence

- repeated pattern across commands/regions;
- common rules/orders or synchronized tactics;
- weapon-type escalation;
- detention/prosecution architecture expanding alongside force;
- defections/refusals/internal dissent;
- geographic diffusion independent of local incidents;
- evidence of centralized authorization;
- costly restraint after international pressure versus continued escalation.

### Guard

```text
FORCE_ALREADY_USED != SYSTEMATIC_EXPANSION_PROVEN
```

---

## 7. Cross-case residual comparison

| Case | Hidden-factor need at cutoff | Main residual | Best immediate action |
|---|---|---|---|
| A | CONDITIONAL | persistence despite constraints/offramps | inspect readiness + reciprocity sequence |
| B | NO / NEGATIVE CONTROL | none requiring hidden structure | monitor stabilizer durability |
| C | YES_AS_SEARCH_TRIGGER_ONLY | costly preparation persists without costly reassurance | discriminate bargaining vs commitment transition |
| D | YES_AS_SEARCH_TRIGGER_ONLY | link from observed force to expansion/systematicity | inspect command pattern + geographic/tactical diffusion |

Этот результат важен: `STRUCTURAL_GAP_INFERENCE` не срабатывает одинаково на каждый опасный кризис. Case B выступает обязательным control, где hidden inference должен быть подавлен.

## 8. New guards from pilot

```text
DANGEROUS_STATE != STRUCTURAL_GAP
MODEL_EXPLAINS_STATE => NO_HIDDEN_FACTOR_SEARCH
PERSISTENT_PREPARATION != COMMITMENT
COSTLY_PREPARATION + NO_COSTLY_REASSURANCE => SEARCH_TRIGGER, NOT INTENT_PROOF
FORCE_ALREADY_USED => SHIFT_RESIDUAL_FROM_FIRST_USE_TO_EXPANSION
HIDDEN_FACTOR_SEARCH_MUST_HAVE_NEGATIVE_CONTROL
```

## 9. Residual ledger seed

```text
A-R1 | SIGN/PERSISTENCE | CONDITIONAL | observation/readiness check first
B-R1 | CONTROL_NO_GAP | RESOLVED_AS_MODEL_EXPLAINED | no hidden-factor hypothesis
C-R1 | PERSISTENT_BEHAVIOR/TIMING | OPEN | discriminating search required
D-R1 | MISSING_LINK/TIMING | OPEN | expansion-mechanism search required
```

## 10. Что пилот НЕ доказывает

- не доказывает, какой кейс приведёт к войне;
- не доказывает ни одну hidden-factor hypothesis;
- не оценивает probability;
- не использует будущий исход как label;
- не разрешает numeric contribution inferred factors;
- не заменяет внешний blind coding.

## 11. Gate result

```text
HISTORICAL_RESIDUAL_PILOT_001 = COMPLETE
NEGATIVE_CONTROL_BEHAVIOR = PASS_CONCEPTUALLY
HYPOTHESIS_GENERATION = DIFFERENTIATED_BY_CASE
INTENT_INVENTION = BLOCKED
NUMERIC_USE = BLOCKED
NEXT = BLIND_RESIDUAL_CODER_PACKET_001 + DISCRIMINATING_EVIDENCE_BACKFILL
```
