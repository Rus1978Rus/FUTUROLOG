# HISTORICAL TEMPORAL SEQUENCE BENCHMARK DESIGN 001

**Статус:** `DESIGN_READY / REAL_HISTORY / SOURCE_BACKED_FAMILIES / OUTCOME_BLINDNESS_REQUIRED / NOT_NUMERICALLY_VALIDATED`

## 1. Цель

Перейти от одиночных snapshots к временным сериям и проверить, способен ли FUTUROLOG описывать изменение состояния системы:

```text
STABLE -> STRESSED -> DEGRADING -> THRESHOLD_NEAR -> TRANSITION_UNDERWAY
```

без знания дальнейшего исхода и без превращения любого кризиса в structural gap.

Ключевой вопрос:

```text
WHEN DOES TRAJECTORY BECOME STRUCTURALLY DISTINGUISHABLE?
```

То есть не «почему система потом рухнула», а «на каком датированном срезе появляются наблюдаемые признаки, которые меняют допустимый набор траекторий».

## 2. Обязательные guards

```text
HISTORICAL_OUTCOME != INPUT_FEATURE
LATER_EVENT != EARLIER_EVIDENCE
TEMPORAL_SEQUENCE != RETROSPECTIVE_STORY
HIGH_PRESSURE != THRESHOLD_NEAR
TRANSITION_UNDERWAY != STRUCTURAL_GAP
COERCIVE_ASSET_CAPACITY != COERCIVE_EXECUTABLE_CAPACITY
FORMAL_AUTHORITY != EXECUTED_COMMAND
ELITE_UNCERTAINTY != ELITE_DEFECTION
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
NEGOTIATION_EXISTS != NEGOTIATION_SUCCESS
TERRITORIAL_RELEASE != CORE_COLLAPSE
REGIME_CHANGE != STATE_COLLAPSE
```

## 3. Первый набор исторических семей

### FAM-01 — Российская империя 1917

Цель: от pressure accumulation к command erosion / node realignment / abdication threshold.

Нужны минимум 4 cutoff:
- до массового перехода гарнизона;
- после расширения беспорядков;
- после появления наблюдаемой дефекции/неисполнения;
- непосредственно перед отречением.

### FAM-02 — СССР 1989–1991

Цель: медленный вариант erosion central authority.

Источник Office of the Historian фиксирует: демократизация и многопартийные выборы ослабляли партийный контроль; к 1990–1991 рос конфликт Горбачёв–Ельцин, балтийские и кавказские республики требовали независимости; январь 1991 дал насилие в Литве/Латвии; неудачный августовский путч резко ослабил Горбачёва и усилил альтернативный российский центр; после путча Украина и Беларусь объявили независимость; в декабре лидеры России, Украины и Беларуси создали СНГ, фактически объявив конец Союза.

Нужны cutoff:
- 1989 до явной республиканской суверенизации;
- середина 1990 после роста альтернативных центров;
- январь 1991;
- 18 августа 1991 до путча;
- 22–24 августа 1991 после провала путча;
- начало декабря 1991 до Беловежских соглашений.

### FAM-03 — Румыния 17–22 декабря 1989

Уже имеется короткая плотная серия:

```text
17 Dec -> local lethal coercion
19 Dec -> central coordination still active
21 Dec -> broad public compliance degradation
22 Dec -> shifting security alignment + collapsing executability + alternative coordination
```

Использовать как high-speed transition family.

### FAM-04 — Беларусь 2020

Цель: сильное массовое давление без наблюдаемого режима collapse.

Нужны cutoff:
- 9–10 августа;
- 13–16 августа;
- 17–23 августа;
- начало сентября.

Критические оси: domestic coercive execution, organized critical-node defection, elite uncertainty, external backing available but not deployed, protest breadth.

### FAM-05 — Казахстан январь 2022

Цель: сравнить с Беларусь-2020 при фактическом внешнем развертывании.

Нужны cutoff:
- до запроса коллективной помощи;
- момент запроса;
- момент фактического deployment;
- после стабилизации и начала withdrawal.

Guard:

```text
EXTERNAL_FORCE_DEPLOYMENT != TRANSITION_UNDERWAY
```

### FAM-06 — Китай май–июнь 1989

Цель: survival control с высоким массовым давлением и сохраняющейся executable coercion.

Нужны cutoff:
- расширение протестов;
- введение военного положения;
- период до 3 июня при сохраняющейся неопределённости;
- не использовать само подавление как вход для более ранних срезов.

### FAM-07 — Британия: деколонизация после 1945

Это не один collapse-case, а family of controlled contraction.

National Archives указывает, что после войны британская политика ориентировалась на постепенное ответственное самоуправление; при этом Британия была готова силой сопротивляться некоторым движениям (Кения, Малайя). Независимость Индии 1947 ускорила процесс; к 1960 речь Макмиллана «Wind of Change» уже отражала более быстрое сворачивание империи.

Нужны подсерии:
- Индия 1942–1947;
- Гана 1950-е–1957;
- Кения 1952–1963;
- Малайя 1948–1957;
- Нигерия 1950-е–1960.

Цель: различать

```text
CONTROLLED_RELEASE
FORCED_RELEASE
REPRESSION_THEN_RELEASE
CORE_PRESERVATION
```

### FAM-08 — Франция: mixed decolonization

Нужны подсерии:
- Индокитай;
- Алжир;
- Марокко/Тунис как более переговорные контрпримеры.

Цель: внутри одного метропольного центра сравнить, почему разные периферии ведут к войне, переговорам или быстрому transfer.

### FAM-09 — Португалия 1961–1975

Office of the Historian прямо фиксирует, что переворот 25 апреля 1974 был вызван африканской политикой Лиссабона и расколом, который она создала внутри армии; после переворота начались переговоры с африканскими движениями, а летом–осенью 1974 появились cease-fire и transition arrangements.

Нужны cutoff:
- ранняя стадия колониальных войн;
- рост военной нагрузки;
- 1973 до открытого coup threshold;
- 24 апреля 1974;
- сразу после переворота;
- переговорные переходы к независимости.

Это важный case:

```text
PERIPHERY_HOLDING_COST
-> MILITARY_INTERNAL_FRICTION
-> CORE_REGIME_TRANSITION
```

### FAM-10 — ЮАР 1990–1994

Цель: regime transformation with state continuity.

Нужны cutoff:
- до legalization opposition;
- освобождение Манделы;
- начало официальных переговоров;
- кризисы переговоров;
- предвыборный переход.

### FAM-11 — Родезия/Зимбабве 1978–1980

Цель: negotiated transition after war, sanctions and non-recognition.

Нужны cutoff:
- pre-Lancaster deadlock;
- opening of conference;
- transition framework;
- cease-fire implementation;
- pre-election period.

## 4. Общая schema временного среза

```text
family_id
snapshot_id
cutoff_date
observation_status_state
observation_status_gap
coercive_asset_capacity
coercive_executable_capacity
command_executability_state
critical_node_alignment
public_compliance_signal
external_support_state
negotiated_transition_channel
center_periphery_cost_state
alternative_coordination_state
transition_instability_state
transition_signal
structural_gap_status
hidden_factor_search_allowed
```

Новые поля:

```text
center_periphery_cost_state = LOW | RISING | HIGH | UNSUSTAINABLE | UNKNOWN
alternative_coordination_state = ABSENT | EMERGING | FUNCTIONAL | COMPETING_CENTER | UNKNOWN
```

## 5. Temporal rules

Каждый snapshot кодируется независимо по информации, доступной на cutoff.

```text
SNAPSHOT_t+1 MAY CHANGE PRIOR
SNAPSHOT_t+1 MAY NOT REWRITE SNAPSHOT_t
```

После кодирования всей серии evaluator строит только descriptive trajectory:

```text
STATE_t0 -> STATE_t1 -> STATE_t2 ...
```

Запрещено оценивать ранний snapshot как ошибочный только потому, что позже известен collapse/survival.

## 6. Benchmark outputs

Для каждой семьи считать:

```text
FIRST_STRESSED_CUTOFF
FIRST_DEGRADING_CUTOFF
FIRST_THRESHOLD_NEAR_CUTOFF
FIRST_TRANSITION_UNDERWAY_CUTOFF
FIRST_CRITICAL_NODE_REALIGNMENT_CUTOFF
FIRST_EXECUTABLE_CAPACITY_DROP_CUTOFF
```

Если соответствующее состояние не наблюдалось:

```text
NOT_REACHED_WITHIN_OBSERVED_WINDOW
```

## 7. Основной comparative test

После построения траекторий сравнить семьи, не используя outcome как feature:

```text
Romania 1989 vs China 1989
Belarus 2020 vs Kazakhstan 2022
Russia 1917 vs USSR 1991
Britain controlled contraction vs Portugal costly retention
South Africa negotiated transformation vs Rhodesia negotiated-after-war
Britain vs France within decolonization
```

## 8. Status

```text
HISTORICAL_TEMPORAL_SEQUENCE_BENCHMARK_DESIGN_001 = READY
REAL_HISTORY = YES
SOURCE_BACKED_EXPANSION = IN_PROGRESS
OUTCOME_BLINDNESS = REQUIRED
NEXT = SOURCE_BACKED_TEMPORAL_INTAKE_001
NUMERIC_FORESIGHT_USE = BLOCKED
```
