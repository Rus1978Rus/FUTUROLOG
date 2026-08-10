# FORCE_SIGNALING_DATED_SNAPSHOTS 001

**Статус:** `DATED_SNAPSHOTS_CREATED / SOURCE_GROUNDED / NON_NUMERIC / OUTCOME_LABELS_WITHHELD_FROM_SNAPSHOT_FIELDS / NOT_VALIDATED`

## 1. Назначение

Этот пакет применяет одну и ту же форму `FORCE_SIGNALING_PROFILE` к четырём историческим кризисам на фиксированной дате. Поля описывают только то, что было наблюдаемо к cutoff. Будущий исход не используется как вход snapshot.

Ключевые guards:

```text
SHOW_OF_FORCE != INTENT_TO_USE_FORCE
PAST_FORCE_USE != CURRENT_INTENT
PAST_RESTRAINT != FUTURE_RESTRAINT
TEMPORARY_DEESCALATION != DURABLE_RESTRAINT
FORCE_ALREADY_USED -> FIRST_USE_PROPENSITY_NO_LONGER_LATENT
REASSURANCE_SIGNAL != PROVEN_PEACE
CURRENT_INTENT = UNKNOWN unless directly evidenced
```

## 2. Единая форма snapshot

```text
case_id
snapshot_cutoff
signaling_intensity
current_force_state
past_force_use_prior
reassurance_signal
military_communication_or_deconfliction
constraint_evidence
cost_tolerance_evidence
current_intent_status
key_observability_limits
```

Значения качественные и не являются вероятностями.

---

## 3. India–Pakistan 2001–2002

**Snapshot cutoff:** `2002-01-24T23:59:59Z`

### Наблюдаемое к cutoff

Генеральный секретарь ООН и пакистанская сторона публично обсуждали сохранявшуюся крупную концентрацию сил на границе и линии контроля. В материалах встречи подчёркивалось, что непосредственная задача — военная деэскалация и возвращение сил к мирным позициям; одновременно декларировалась готовность к диалогу и взаимной реакции на шаги по отводу сил.

### Profile

```text
signaling_intensity = HIGH
current_force_state = LARGE_FORWARD_DEPLOYMENT / NO_GENERAL_WITHDRAWAL_CONFIRMED_AT_CUTOFF
past_force_use_prior = PRESENT_BUT_NOT_NUMERICALLY_CODED_HERE
reassurance_signal = DIALOGUE_AND_MUTUAL_WITHDRAWAL_LANGUAGE_PRESENT
military_communication_or_deconfliction = PARTIAL_DIPLOMATIC_CHANNELS_PRESENT
constraint_evidence = NUCLEAR_RISK + INTERNATIONAL_DIPLOMATIC_PRESSURE_VISIBLE
cost_tolerance_evidence = UNKNOWN
current_intent_status = UNKNOWN
```

### Blind spots

- точный operational readiness обеих сторон;
- закрытые правила применения силы;
- реальные внутриполитические thresholds;
- достоверная оценка willingness to absorb casualties/economic costs.

---

## 4. Greece–Turkey Eastern Mediterranean 2020

**Snapshot cutoff:** `2020-10-01T23:59:59Z`

### Наблюдаемое к cutoff

После серии технических встреч военных представителей Греции и Турции НАТО объявило о создании bilateral military de-confliction mechanism. Механизм предназначался для снижения риска инцидентов и аварий в Восточном Средиземноморье и включал прямую hotline для деэскалации на море и в воздухе.

### Profile

```text
signaling_intensity = HIGH_OR_ELEVATED
current_force_state = ACTIVE_MILITARY_FRICTION_RISK / FIRST_USE_NOT_ESTABLISHED_IN_THIS_SNAPSHOT
past_force_use_prior = PRESENT_IN_BROADER_HISTORY_BUT_NOT_USED_AS_CURRENT_INTENT
reassurance_signal = STRONG_COSTLY_REASSURANCE_PRESENT
military_communication_or_deconfliction = FORMAL_HOTLINE_AND_NATO_MECHANISM_PRESENT
constraint_evidence = ALLIANCE_FRAMEWORK + DIRECT_DECONFLICTION_CHANNEL_VISIBLE
cost_tolerance_evidence = UNKNOWN
current_intent_status = UNKNOWN
```

### Blind spots

- закрытые naval/air rules of engagement;
- реальная готовность сторон отступить в конкретном инциденте;
- внутренние политические red lines;
- operational orders, недоступные публично.

---

## 5. Russia–Ukraine 2021

**Snapshot cutoff:** `2021-11-30T23:59:59Z`

### Наблюдаемое к cutoff

НАТО публично описывало концентрацию российских сил как значительную и необычную, при этом прямо подчёркивало, что уверенности в намерениях России нет. Одновременно отмечались heightened rhetoric и disinformation, а также известный prior применения Россией силы против Украины и других соседей. НАТО призывало к прозрачности и деэскалации и сохраняло готовность к диалогу, хотя дипломатические каналы NATO–Russia к тому моменту были ухудшены после приостановки российской миссии при НАТО.

### Profile

```text
signaling_intensity = HIGH
current_force_state = LARGE_UNUSUAL_CONCENTRATION_NEAR_TARGET
past_force_use_prior = STRONG_RELEVANT_PRIOR_PRESENT
reassurance_signal = DIPLOMATIC_CALLS_PRESENT_BUT_NO_COMPARABLE_COSTLY_WITHDRAWAL_SIGNAL_IN_THIS_SNAPSHOT
military_communication_or_deconfliction = DEGRADED_RELATIVE_TO_IDEAL
constraint_evidence = THREAT_OF_POLITICAL_AND_ECONOMIC_COSTS_VISIBLE
cost_tolerance_evidence = UNKNOWN_AT_CUTOFF
current_intent_status = UNKNOWN
```

### Blind spots

- operational intent;
- actual decision threshold inside leadership;
- force employment plans;
- true cost tolerance;
- information from non-public intelligence.

---

## 6. Myanmar 2021

**Snapshot cutoff:** `2021-02-28T23:59:59Z`

### Наблюдаемое к cutoff

UN Human Rights Office сообщал, что полиция и военные уже применили lethal and less-than-lethal force против мирных протестующих в нескольких городах; по информации ООН, к этому дню было не менее 18 погибших и более 30 раненых.

### Profile

```text
signaling_intensity = NOT_PRIMARY_QUESTION_ANYMORE
current_force_state = FORCE_ALREADY_USED / LETHAL_FORCE_OBSERVED
past_force_use_prior = NOT_NEEDED_TO_ESTABLISH_FIRST_USE_PROPENSITY
reassurance_signal = NO_COMPARABLE_COSTLY_REASSURANCE_SIGNAL_IN_THIS_SNAPSHOT
military_communication_or_deconfliction = NOT_A_PRIMARY_STABILIZING_FEATURE_IN_AVAILABLE_EVIDENCE
constraint_evidence = INTERNATIONAL_CONDEMNATION_VISIBLE
cost_tolerance_evidence = PARTIALLY_REVEALED_BY_CONTINUED_FORCE_USE_BUT NOT_NUMERICALLY_INFERRED
current_intent_status = EXPANSION_INTENT_UNKNOWN
```

После этого cutoff профиль должен переключаться с вопроса `WILL_FORCE_BE_USED?` на:

```text
WILL_FORCE_EXPAND_IN_SCALE?
WILL_FORCE_EXPAND_IN_GEOGRAPHY?
WILL_FORCE_EXPAND_IN_WEAPON_TYPE?
WILL_REPRESSION_BECOME_SYSTEMATIC?
```

### Blind spots

- chain of command behind individual incidents;
- future escalation policy;
- exact rules of engagement;
- internal dissent inside security forces.

---

## 7. Cross-case differentiators

На этой стадии наиболее полезны не сами громкие демонстрации силы, а различия в следующих observable features:

```text
A. FORCE_ALREADY_USED?
B. RELEVANT_PAST_FORCE_USE_PRIOR?
C. COSTLY_REASSURANCE_PRESENT?
D. FORMAL_DECONFLICTION_CHANNEL_PRESENT?
E. ACTUAL_WITHDRAWAL / FORCE_REDUCTION PRESENT?
F. COMMUNICATION_CHANNEL DEGRADED OR WORKING?
G. CURRENT_INTENT DIRECTLY OBSERVED OR UNKNOWN?
```

## 8. Важный вывод для false-positive design

Высокий `signaling_intensity` встречается и в случаях, которые не переходят в крупную войну. Поэтому он не должен быть самостоятельным trigger.

Предварительная логика проверки:

```text
HIGH_SIGNALING
+ COSTLY_REASSURANCE
+ WORKING_DECONFLICTION
+ OBSERVED_FORCE_REDUCTION
may indicate a different trajectory than
HIGH_SIGNALING
+ RELEVANT_FORCE_USE_PRIOR
+ DEGRADED_CHANNELS
+ NO_COSTLY_REASSURANCE
```

Это не causal law и не probability formula. Это набор различающих признаков для дальнейшего historical test.

## 9. Статус

```text
DATED_FORCE_SIGNALING_SNAPSHOTS_001_COMPLETE
FOUR_CASE_FORM_UNIFIED
INTENT_NOT_INVENTED
NUMERIC_SCORING_NOT_APPLIED
READY_FOR_BLIND_COMPARATIVE_CODING_PACKET
NOT_VALIDATED
```
