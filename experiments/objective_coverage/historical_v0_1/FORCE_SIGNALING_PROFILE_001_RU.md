# FORCE_SIGNALING_PROFILE 001

**Статус:** `CONCEPTUAL_PROFILE / EVIDENCE_GROUNDED / NOT_CALIBRATED / NOT_NUMERICALLY_ACTIVE`

## 1. Зачем нужен профиль

Военная демонстрация силы и реальная готовность перейти к применению силы — разные вещи.

В кризисном поведении государства могут использовать мобилизацию, учения, переброску сил, демонстрационные развертывания и угрозы как costly signals, чтобы повысить правдоподобие требования или сдерживания. Но сам факт такого сигнала не доказывает намерение начать войну.

Базовые guards:

```text
SHOW_OF_FORCE != INTENT_TO_USE_FORCE
MILITARY_SIGNAL != WAR_DECISION
PAST_FORCE_USE != AUTOMATIC_FUTURE_FORCE_USE
PAST_RESTRAINT != GUARANTEED_FUTURE_RESTRAINT
```

## 2. Профиль актора, а не вечный тип страны

Профиль кодируется для конкретного актора в конкретный период и кризисный контекст.

```text
actor_id
period
crisis_context
capability
signaling_intensity
force_use_history
use_of_force_propensity
cost_tolerance
escalation_threshold
institutional_constraints
alliance_constraints
expected_external_costs
reassurance_signals
coercive_signals
confidence
```

Страна не получает постоянный ярлык «боится/не боится применять силу».

## 3. Две независимые оси

### A. SIGNALING_INTENSITY

Что наблюдаем:
- mobilization;
- exercises;
- forward deployment;
- show of force;
- explicit threats;
- military alerts;
- coercive deadlines;
- visible risk-taking.

### B. USE_OF_FORCE_PROPENSITY

Что наблюдаем:
- фактические предыдущие переходы к применению силы в сопоставимых кризисах;
- willingness to accept escalation risk;
- повторяемость перехода threat -> action;
- willingness to continue despite costs;
- наличие/отсутствие institutional or alliance brakes.

Эти оси нельзя сливать.

```text
HIGH_SIGNALING + LOW_FORCE_PROPENSITY
HIGH_SIGNALING + HIGH_FORCE_PROPENSITY
LOW_SIGNALING + HIGH_FORCE_PROPENSITY
LOW_SIGNALING + LOW_FORCE_PROPENSITY
```

## 4. COST_TOLERANCE

`cost_tolerance` — отдельная переменная.

Она описывает наблюдаемую готовность руководства терпеть:
- military losses;
- sanctions/economic losses;
- reputational damage;
- diplomatic isolation;
- domestic political cost;
- prolonged uncertainty.

Guard:

```text
CAPABILITY != COST_TOLERANCE
COST_TOLERANCE != IRRATIONALITY
```

## 5. ESCALATION_THRESHOLD

Вместо бинарного «применит/не применит силу» хранится переходная структура:

```text
THREAT
→ PREPARATION
→ COMMITMENT
→ LIMITED_FORCE
→ EXPANDED_FORCE
```

Для каждого перехода кодируется evidence того, насколько легко актор пересекает следующий порог.

Нельзя выводить следующий уровень только из предыдущего.

```text
PREPARATION != COMMITMENT
COMMITMENT != FORCE_USE
LIMITED_FORCE != EXPANDED_FORCE
```

## 6. Past behavior — осторожное использование

История поведения может влиять на оценку credibility, но не является судьбой.

Past actions используются только как contextual prior (контекстный prior / исходное ожидание), а не как доказательство текущего решения.

```text
PAST_ACTION = CONTEXTUAL_PRIOR
CURRENT_PREPARATION = CURRENT_EVIDENCE
CURRENT_INTENT = NOT_DIRECTLY_OBSERVED_UNLESS_EXPLICITLY_EVIDENCED
```

## 7. Coercive signaling vs reassurance

Профиль должен хранить одновременно:

```text
COERCIVE_SIGNAL
REASSURANCE_SIGNAL
```

Потому что актор может одновременно повышать давление и оставлять выход из кризиса.

Примеры reassurance:
- hotline/deconfliction;
- explicit limits;
- troop withdrawal;
- reciprocal restraint;
- negotiation channel;
- conditional off-ramp.

Guard:

```text
COERCION_PRESENT != REASSURANCE_ABSENT
REASSURANCE_PRESENT != LOW_RISK
```

## 8. Связь с false-positive analogues

Профиль должен быть особенно полезен для различения:

```text
HIGH_SIGNALING / HIGH_REASSURANCE / HIGH_CONSTRAINTS
```

и

```text
HIGH_SIGNALING / LOW_REASSURANCE / HIGH_COST_TOLERANCE / LOW_CONSTRAINTS
```

Оба случая внешне могут выглядеть как опасная военная эскалация, но механизмы перехода к force-use различаются.

Это НЕ разрешение автоматически понижать risk при наличии переговоров или автоматически повышать его при истории войн.

## 9. Evidence sources

Для профиля предпочтительны:
- contemporaneous official statements;
- verified force deployments;
- crisis timelines;
- deconfliction/reassurance records;
- historical crisis behavior;
- institutional/legal constraints;
- alliance commitments;
- sanctions/economic exposure;
- post-event material только для later validation, не для cutoff input.

## 10. Научная опора

Литература по coercive diplomacy различает deterrence и compellence и рассматривает costly signals, risk-taking и credibility как отдельные элементы кризисного поведения. Военные демонстрации могут повышать правдоподобие угроз, но также создавать misperception и повышать риск эскалации.

Исследования crisis bargaining отдельно рассматривают military mobilization/show-of-force как costly signals. Есть и эмпирическая литература по deterrence, где прошлое поведение и характер дипломатической взаимности могут влиять на вероятность успеха сдерживания, но не сводятся к одной переменной «репутация».

## 11. Status

```text
FORCE_SIGNALING_PROFILE_001_CREATED
NOT_NUMERICALLY_ACTIVE
READY_FOR_FALSE_POSITIVE_ANALOGUE_ANNOTATION
REQUIRES_HISTORICAL_CALIBRATION
```
