# BLIND_FORCE_SIGNALING_COMPARATIVE_PACKET 001

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_CODING / CASE_NAMES_HIDDEN / OUTCOMES_HIDDEN / NON_NUMERIC_VALIDATION`

## 1. Назначение

Этот пакет проверяет, может ли кодировщик различать типы силовой траектории по наблюдаемым признакам на cutoff, не зная названий стран и дальнейшего исхода.

Кодировщик НЕ должен:

- использовать интернет;
- пытаться идентифицировать кейсы;
- восстанавливать страны по датам;
- использовать знание последующих событий;
- превращать `current_intent_status=UNKNOWN` в уверенный вывод о намерении;
- считать высокий signaling самостоятельным доказательством будущего применения силы.

## 2. Guards

```text
SHOW_OF_FORCE != INTENT_TO_USE_FORCE
PAST_FORCE_USE != CURRENT_INTENT
PAST_RESTRAINT != FUTURE_RESTRAINT
TEMPORARY_DEESCALATION != DURABLE_RESTRAINT
REASSURANCE_SIGNAL != PROVEN_PEACE
FORCE_ALREADY_USED -> FIRST_USE_PROPENSITY_NO_LONGER_LATENT
CURRENT_INTENT = UNKNOWN unless directly evidenced
HIGH_SIGNALING != WAR_TRIGGER
```

## 3. Задача кодировщика

Для каждого кейса заполнить:

```text
case_id
first_use_state = LATENT | ALREADY_USED | UNKNOWN
signaling_level = LOW | MODERATE | HIGH | NOT_PRIMARY
relevant_force_use_prior = ABSENT | PRESENT | STRONG | UNKNOWN | NOT_REQUIRED
costly_reassurance = ABSENT | WEAK | PRESENT | STRONG | UNKNOWN
communication_state = WORKING | PARTIAL | DEGRADED | NOT_PRIMARY | UNKNOWN
constraint_visibility = LOW | MODERATE | HIGH | UNKNOWN
current_intent = UNKNOWN | DIRECTLY_EVIDENCED
trajectory_class =
  A_SIGNALING_WITH_REAL_STABILIZERS |
  B_HIGH_RISK_ESCALATORY_CONFIGURATION |
  C_FORCE_ALREADY_USED_MONITOR_EXPANSION |
  D_INSUFFICIENT_TO_CLASSIFY
confidence = LOW | MEDIUM | HIGH
reason
```

`trajectory_class` — не прогноз исхода и не probability. Это классификация наблюдаемой конфигурации на cutoff.

## 4. Case A

Snapshot cutoff hidden from coder.

Observed profile:

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

Observability limits:

- exact operational readiness unknown;
- closed rules of engagement unknown;
- domestic thresholds unknown;
- cost tolerance unknown.

## 5. Case B

Snapshot cutoff hidden from coder.

Observed profile:

```text
signaling_intensity = HIGH_OR_ELEVATED
current_force_state = ACTIVE_MILITARY_FRICTION_RISK / FIRST_USE_NOT_ESTABLISHED_IN_THIS_SNAPSHOT
past_force_use_prior = PRESENT_IN_BROADER_HISTORY_BUT_NOT_USED_AS_CURRENT_INTENT
reassurance_signal = STRONG_COSTLY_REASSURANCE_PRESENT
military_communication_or_deconfliction = FORMAL_HOTLINE_AND_DECONFLICTION_MECHANISM_PRESENT
constraint_evidence = ALLIANCE_FRAMEWORK + DIRECT_DECONFLICTION_CHANNEL_VISIBLE
cost_tolerance_evidence = UNKNOWN
current_intent_status = UNKNOWN
```

Observability limits:

- closed naval/air rules of engagement unknown;
- willingness to back down in a specific incident unknown;
- domestic red lines unknown;
- operational orders unknown.

## 6. Case C

Snapshot cutoff hidden from coder.

Observed profile:

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

Observability limits:

- operational intent unknown;
- leadership decision threshold unknown;
- force employment plans unknown;
- real cost tolerance unknown;
- non-public intelligence excluded.

## 7. Case D

Snapshot cutoff hidden from coder.

Observed profile:

```text
signaling_intensity = NOT_PRIMARY_QUESTION_ANYMORE
current_force_state = FORCE_ALREADY_USED / LETHAL_FORCE_OBSERVED
past_force_use_prior = NOT_NEEDED_TO_ESTABLISH_FIRST_USE_PROPENSITY
reassurance_signal = NO_COMPARABLE_COSTLY_REASSURANCE_SIGNAL_IN_THIS_SNAPSHOT
military_communication_or_deconfliction = NOT_A_PRIMARY_STABILIZING_FEATURE_IN_AVAILABLE_EVIDENCE
constraint_evidence = INTERNATIONAL_CONDEMNATION_VISIBLE
cost_tolerance_evidence = PARTIALLY_REVEALED_BY_CONTINUED_FORCE_USE_BUT NOT NUMERICALLY_INFERRED
current_intent_status = EXPANSION_INTENT_UNKNOWN
```

Observability limits:

- chain of command behind individual incidents unknown;
- future escalation policy unknown;
- exact rules of engagement unknown;
- internal dissent unknown.

## 8. Output template

```csv
case_id,first_use_state,signaling_level,relevant_force_use_prior,costly_reassurance,communication_state,constraint_visibility,current_intent,trajectory_class,confidence,reason
A,,,,,,,,,,
B,,,,,,,,,,
C,,,,,,,,,,
D,,,,,,,,,,
```

## 9. Expected invariants for later mechanical check

These are evaluator-side rules and should not be shown as expected labels to the external coder beyond the guards already stated:

```text
D: first_use_state must not remain LATENT if force already observed
A/B/C: current_intent should remain UNKNOWN absent direct evidence
B: strong reassurance + working deconfliction must not be silently discarded
C: strong relevant prior must not be converted into current intent
HIGH signaling alone must not determine trajectory class
```

## 10. После внешнего кодирования

Сравниваются:

```text
first_use_state_agreement
current_intent_guard_violations
trajectory_class_agreement
reassurance_recognition
communication_state_agreement
prior_to_intent_leakage_count
high_signaling_shortcut_count
```

Majority vote не является truth. Расхождения используются для диагностики профиля и инструкции.

## 11. Статус

```text
BLIND_FORCE_SIGNALING_COMPARATIVE_PACKET_001_READY
CASE_NAMES_HIDDEN
OUTCOMES_HIDDEN
NUMERIC_PROBABILITY_NOT_REQUESTED
READY_FOR_COPILOT_GROK_CLAUDE_STRESS_TEST
```
