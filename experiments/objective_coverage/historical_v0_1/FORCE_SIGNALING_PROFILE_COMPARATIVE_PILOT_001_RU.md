# FORCE_SIGNALING_PROFILE — COMPARATIVE PILOT 001

**Статус:** `COMPARATIVE_PILOT / QUALITATIVE_ONLY / NOT_CALIBRATED / NOT_VALIDATED`

## 1. Назначение

Этот пилот проверяет, помогает ли `FORCE_SIGNALING_PROFILE` различать:

- демонстрацию силы как сигнал;
- подготовку к реальному применению силы;
- фактическое применение силы;
- reassurance / deconfliction / partial withdrawal;
- готовность терпеть издержки.

Профиль применяется к актору в конкретный период, а не к стране как вечной характеристике.

Ключевые guards:

```text
SHOW_OF_FORCE != INTENT_TO_USE_FORCE
PAST_FORCE_USE != CURRENT_INTENT
PAST_RESTRAINT != FUTURE_RESTRAINT
CURRENT_FORCE_USE = OBSERVED_EVENT
CURRENT_INTENT != DIRECTLY_OBSERVED
REASSURANCE_SIGNAL != PROVEN_DEESCALATION
```

## 2. Оси

```text
SIGNALING_INTENSITY
CURRENT_FORCE_USE_STATUS
PAST_FORCE_USE_PRIOR
REASSURANCE_SIGNAL
DECONFLICTION_CAPACITY
COST_TOLERANCE_EVIDENCE
ESCALATION_THRESHOLD_EVIDENCE
CONSTRAINTS
```

Шкала пока качественная: `LOW / MEDIUM / HIGH / OBSERVED / UNKNOWN`.

## 3. Россия — Украина, 2021–23 февраля 2022

### Наблюдаемое

- Весной 2021 НАТО фиксировало значительное российское военное наращивание вокруг Украины.
- В мае 2021 НАТО сообщало, что часть войск была отведена, но десятки тысяч оставались в регионе.
- В ноябре–декабре 2021 НАТО снова фиксировало необычную крупную концентрацию сил и прямо указывало, что Россия ранее уже применяла подобные военные возможности для агрессивных действий против Украины.

### Qualitative profile

```text
SIGNALING_INTENSITY = HIGH
CURRENT_FORCE_USE_STATUS = NOT_YET_OBSERVED_AT_PRE_2022_02_24_CUTOFF
PAST_FORCE_USE_PRIOR = HIGH_RELEVANCE
REASSURANCE_SIGNAL = PRESENT_BUT_REVERSIBLE
DECONFLICTION_CAPACITY = PARTIAL / DIPLOMATIC_CHANNELS_EXISTED
COST_TOLERANCE_EVIDENCE = UNKNOWN_TO_HIGH_CANDIDATE / NOT_DIRECTLY_OBSERVED
ESCALATION_THRESHOLD_EVIDENCE = LOWER_THAN_PURE_SHOW_OF_FORCE_CASES_CANDIDATE
CONSTRAINTS = PRESENT_BUT_NOT_DECISIVE
```

### Guard

Весенний partial withdrawal 2021 нельзя ретроспективно объявлять "обманом" без contemporaneous evidence намерения. Он является реальным reassurance/de-escalation signal того момента, который позже оказался недостаточным для долгосрочного вывода.

```text
TEMPORARY_DEESCALATION != DURABLE_RESTRAINT
```

## 4. Индия–Пакистан, 2001–2002

### Наблюдаемое

- Кризис сопровождался крупной военной конфронтацией и ядерным контекстом.
- В мае 2002 представитель Пакистана в ООН публично описывал условия, при которых действия Индии будут рассматриваться как агрессия, и напоминал об отсутствии у Пакистана обязательства no-first-use ядерного оружия.
- 17 октября 2002 Генеральный секретарь ООН приветствовал решение Индии и Пакистана частично отвести войска от приграничных районов и выразил надежду на существенную деэскалацию.

### Qualitative profile

```text
SIGNALING_INTENSITY = HIGH
CURRENT_FORCE_USE_STATUS = LIMITED_CONFLICT_CONTEXT / NO_FULL_SCALE_INTERSTATE_WAR_IN_SELECTED_HORIZON
PAST_FORCE_USE_PRIOR = HIGH
REASSURANCE_SIGNAL = STRONG_LATE
DECONFLICTION_CAPACITY = PRESENT_THROUGH_DIPLOMATIC_CHANNELS
COST_TOLERANCE_EVIDENCE = HIGH_BUT_BOUNDED
ESCALATION_THRESHOLD_EVIDENCE = HIGH_RISK_BUT_NOT_CROSSED_TO_FULL_SCALE_WAR_IN_HORIZON
CONSTRAINTS = STRONG, INCLUDING NUCLEAR_RISK AND EXTERNAL_DIPLOMATIC_PRESSURE
```

### Почему это хороший false-positive analogue

Высокая демонстрация силы и высокая credible-use prior существовали одновременно, но траектория в выбранном горизонте завершилась partial withdrawal, а не полномасштабной войной.

## 5. Греция–Турция, Восточное Средиземноморье 2020

### Наблюдаемое

- НАТО создало двусторонний военный de-confliction mechanism после серии технических встреч.
- Механизм включал secure hotline и был предназначен для снижения риска инцидентов и аварий на море и в воздухе.
- НАТО отдельно подчёркивало, что механизм создаёт пространство для дипломатических усилий, а не решает сам спор.

### Qualitative profile

```text
SIGNALING_INTENSITY = MEDIUM_TO_HIGH
CURRENT_FORCE_USE_STATUS = NO_MAJOR_INTERSTATE_FORCE_USE_IN_SELECTED_HORIZON
PAST_FORCE_USE_PRIOR = NONZERO_HISTORICAL / NOT_USED_AS_CURRENT_INTENT_PROOF
REASSURANCE_SIGNAL = HIGH
DECONFLICTION_CAPACITY = HIGH_RELATIVE_TO_OTHER_CASES
COST_TOLERANCE_EVIDENCE = UNKNOWN
ESCALATION_THRESHOLD_EVIDENCE = CONSTRAINED_BY_ALLIANCE_AND_HOTLINE_MECHANISMS
CONSTRAINTS = STRONG_INSTITUTIONAL_AND_ALLIANCE_CONSTRAINTS
```

### Отличительный признак

Здесь важна не низкая демонстрация силы, а наличие работающего механизма, который уменьшает вероятность случайного перехода от демонстрации к столкновению.

```text
HIGH_SIGNALING + HIGH_DECONFLICTION != HIGH_FORCE_USE_PROBABILITY_AUTOMATICALLY
```

## 6. Мьянма, февраль–апрель 2021

### Наблюдаемое

- Уже 28 февраля 2021 OHCHR сообщало о применении lethal и less-than-lethal force против мирных демонстраций и как минимум 18 погибших.
- 27 марта ООН сообщала о десятках убитых гражданских и самом высоком на тот момент дневном числе погибших с начала протестов.
- 1 апреля OHCHR сообщало о не менее 510 убитых мирных протестующих и использовании тяжёлого оружия, пулемётов и снайперов.
- 13 апреля Верховный комиссар ООН по правам человека описывала усиление применения military-grade и indiscriminate weaponry.

### Qualitative profile

```text
SIGNALING_INTENSITY = HIGH
CURRENT_FORCE_USE_STATUS = OBSERVED
PAST_FORCE_USE_PRIOR = HIGH_RELEVANCE
REASSURANCE_SIGNAL = WEAK_TO_ABSENT_IN_SELECTED_WINDOW
DECONFLICTION_CAPACITY = LOW
COST_TOLERANCE_EVIDENCE = HIGH_CANDIDATE_FROM_CONTINUED_REPRESSION
ESCALATION_THRESHOLD_EVIDENCE = ALREADY_CROSSED
CONSTRAINTS = PRESENT_EXTERNALLY BUT WEAKLY_EFFECTIVE_IN_SELECTED_WINDOW
```

### Критическое различие

Для Мьянмы вопрос "готов ли актор перейти от угрозы к силе" после конца февраля 2021 уже неверно поставлен: применение силы стало наблюдаемым фактом.

```text
OBSERVED_FORCE_USE != PROPENSITY_ESTIMATE
```

После этого профиль должен оценивать уже не вероятность первого применения силы, а вероятность расширения масштаба, типов средств и географии насилия.

## 7. Что профиль добавляет к false-positive аналогу

Обычный pressure detector может увидеть во всех кейсах:

```text
TROOP/MILITARY ACTIVITY
THREATS
HIGH TENSION
INFORMATION PRESSURE
POLITICAL CONFLICT
```

Но `FORCE_SIGNALING_PROFILE` добавляет различители:

```text
HAS_FORCE_ALREADY_BEEN_USED?
IS_REASSURANCE_COSTLY_AND_OBSERVABLE?
IS_THERE_A_REAL_DECONFLICTION_CHANNEL?
DOES_THE_ACTOR_HAVE_RELEVANT_RECENT_FORCE_USE_PRIOR?
ARE_CONSTRAINTS_OPERATIONAL_OR_MERELY_DECLARED?
DOES_THE_ACTOR_REVERSE_PREPARATION_OR_CONTINUE_IT?
```

## 8. Новые guards

```text
CAPABILITY != PROPENSITY
PROPENSITY != INTENT
INTENT != OUTCOME
REASSURANCE_DECLARATION != REASSURANCE_ACTION
HOTLINE_EXISTS != HOTLINE_USED_EFFECTIVELY
PARTIAL_WITHDRAWAL != CRISIS_RESOLVED
FORCE_ALREADY_USED => FIRST_USE_PROPENSITY_NO_LONGER_LATENT
```

## 9. Следующий тест

Перед numeric use требуется построить dated actor snapshots и проверить, улучшает ли профиль различение:

```text
RUSSIA_UKRAINE_2021_2022
INDIA_PAKISTAN_2001_2002
GREECE_TURKEY_2020
MYANMAR_2021
```

без просмотра последующего исхода внутри каждого snapshot.

Минимальный результат должен быть не "кто агрессивнее", а объяснимый набор различий по signalling, observed force use, reassurance, deconfliction и constraints.

## 10. Статус

```text
FORCE_SIGNALING_COMPARATIVE_PILOT_001_CREATED
FALSE_POSITIVE_DIFFERENTIATORS_IDENTIFIED
QUALITATIVE_ONLY
NO_NUMERIC_WEIGHT_ASSIGNED
NOT_CALIBRATED
NOT_VALIDATED
```
