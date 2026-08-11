# HISTORICAL MACRO-SYSTEM TRANSITION MATRIX v0.1

**Статус:** `WORKING_MATRIX / CASE_SELECTION_STAGE / OUTCOME_BLIND_BENCHMARK_PREP / NOT_VALIDATED`

## 1. Назначение

Матрица нужна не для объяснения истории задним числом, а для подготовки outcome-blind benchmark FUTUROLOG.

Базовая единица анализа:

```text
SYSTEM_t0
→ OBSERVED PRESSURES / STABILIZERS / RESOURCE STRUCTURE / LEGITIMACY / CRITICAL NODES
→ AVAILABLE TRAJECTORIES
→ t1 OBSERVATION
→ NO_GAP | OBSERVATION_INCOMPLETE | STRUCTURAL_RESIDUAL
```

Жёсткие guards:

```text
HISTORICAL_OUTCOME != INPUT_FEATURE
KNOWN_COLLAPSE_CASE != COLLAPSE_LABEL_AT_CUTOFF
SURVIVED_CRISIS_t != LONG_TERM_STABILITY
REGIME_COLLAPSE != STATE_COLLAPSE
TERRITORIAL_LOSS != SYSTEMIC_LOSS
FORMAL_EMPIRE_CONTRACTION != NETWORK_INFLUENCE_CONTRACTION
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
STATE_CAPACITY != EXECUTABLE_CAPACITY
APPARENT_COMPLIANCE != REGIME_SUPPORT
```

## 2. Основные классы траекторий

### T1 — REGIME COLLAPSE / CENTRAL AUTHORITY FAILURE

Система сохраняет значительную формальную материальную способность, но критические узлы перестают действовать согласованно в пользу центра.

Кандидаты:

- Российская империя, февраль–март 1917 — отречение Николая II.
- Румыния, декабрь 1989 — падение режима Чаушеску.
- Иран, 1978–1979 — падение шахской монархии.

Ключевые различающие оси:

```text
COERCIVE_NODE_LOYALTY
COMMAND_EXECUTABILITY
ELITE_DEFECTION
ALTERNATIVE_POWER_CENTER
PUBLIC_DEFIANCE_VISIBILITY
EXPECTED_BEHAVIOR_OF_OTHER_CRITICAL_NODES
```

### T2 — SYSTEM DISSOLUTION / NODE EXIT

Не только смена правителя, а распад прежней макросистемы на несколько суверенных/автономных центров.

Кандидаты:

- СССР, 1989–1991.

Нужны дополнительные сопоставимые случаи:

- мирный распад федерации/союза;
- насильственный распад многонациональной системы;
- кризис федерации, закончившийся сохранением целостности.

Ключевые оси:

```text
CENTER_DEPENDENCE
REPUBLIC/REGIONAL_ALTERNATIVE_LEGITIMACY
NODE_EXIT_CAPACITY
ELITE_REDEPLOYMENT_OPTIONS
FISCAL_DEPENDENCE
SECURITY_CHAIN_FRAGMENTATION
```

### T3 — REGIME SURVIVAL UNDER MASS PRESSURE

Сильный внутренний кризис не приводит к быстрому разрушению режима.

Кандидаты:

- КНР, 1989.
- Беларусь, 2020.
- Казахстан, январь 2022.
- Франция, май 1968 — не авторитарный режим, но полезный контроль системной устойчивости под массовым давлением.

Ключевые оси:

```text
COERCIVE_NODE_LOYALTY
ELITE_COHESION
COMMAND_EXECUTABILITY
EXTERNAL_SUPPORT_AVAILABLE
EXTERNAL_FORCE_DEPLOYED
ALTERNATIVE_POWER_CENTER_STRENGTH
PROTEST_COORDINATION
REGIME_COORDINATION
```

Специальный pair:

```text
BELARUS_2020:
external backing available / signaling present
but no external-force deployment for protest suppression

KAZAKHSTAN_2022:
external collective-security force physically deployed
```

Guard:

```text
EXPECTED_EXTERNAL_BACKING != DEPLOYED_EXTERNAL_FORCE
```

### T4 — CONTROLLED CONTRACTION / PERIPHERY RELEASE

Центр отказывается от части прежнего пространства или прямого контроля, но сохраняет ядро системы.

Кандидаты:

- Британская деколонизация после 1945.
- Французская деколонизация после 1945.

Не кодировать Британию или Францию одной строкой. Нужны территориальные subcases.

Британия — кандидаты:

- Индия 1947.
- Гана 1957.
- Кения 1950s–1963.
- Малайя 1948–1957.
- Родезия как особый конфликтный узел.
- Гонконг 1984–1997 как поздняя договорная передача.

Франция — кандидаты:

- Индокитай 1946–1954.
- Алжир 1954–1962.
- Марокко 1956.
- Тунис 1956.
- Французская Африка южнее Сахары, 1958–1960.

Ключевые оси:

```text
VALUE_OF_HOLDING_NODE
COST_OF_HOLDING_NODE
VALUE_AFTER_RELINQUISHING_CONTROL
MILITARY_MAINTENANCE_COST
SETTLER_POPULATION_STAKES
POST_EXIT_NETWORK_VALUE
CORE_SYSTEM_RESILIENCE
```

Guards:

```text
TERRITORIAL_LOSS != SYSTEMIC_LOSS
DIRECT_CONTROL_DOWN != NETWORK_VALUE_DOWN
RESOURCE_RELEASE_CAN_INCREASE_CORE_STABILITY
```

### T5 — OVERSTRETCH / FAILED RETENTION

Центр продолжает удерживать периферию при растущих военных, бюджетных и политических издержках; удержание само становится фактором системного давления.

Кандидат:

- Португалия, колониальные войны 1961–1974 → Революция гвоздик и последующая деколонизация.

Нужны контрпримеры:

- долгий дорогой конфликт, который центр выдержал;
- периферийная война, завершившаяся частичным удержанием;
- отказ от периферии до режима-кризиса.

Ключевые оси:

```text
OVERSTRETCH
MILITARY_MANPOWER_BURDEN
FISCAL_BURDEN
ELITE/MILITARY_DISAFFECTION
EXPECTED_VALUE_OF_RETENTION
EXIT_OPTION_FROM_EMPIRE
```

### T6 — INTERNAL POWER TRANSFER / STATE SURVIVES

Политическая монополия одной группы заканчивается, но государственный аппарат и значительная часть экономической структуры продолжают существовать.

Кандидаты:

- ЮАР, 1990–1994 — демонтаж апартеида и переход к всеобщему избирательному праву.
- Родезия/Зимбабве, 1965–1980 — переход после войны, санкций и переговоров.

Ключевые оси:

```text
OLD_ELITE_EXIT_OPTION
PHYSICAL_SECURITY_AFTER_TRANSFER
PROPERTY_EXPECTATIONS
POLITICAL_PARTICIPATION_AFTER_TRANSFER
WAR_COST
SANCTIONS/EXTERNAL_PRESSURE
MAJORITY_MOBILIZATION
NEGOTIATED_GUARANTEES
```

Guard:

```text
LOSS_OF_ELITE_POLITICAL_MONOPOLY != LOSS_OF_ALL_ELITE_RESOURCES
```

### T7 — POWER TRANSFER + MASS EXIT / SETTLER EXIT

Передача власти сопровождается крупным исходом ранее привилегированной группы.

Кандидаты:

- Французский Алжир, особенно 1962 и исход pieds-noirs.

Нужны сравнения:

- ЮАР 1994 — старая элита в значительной мере остаётся.
- Родезия/Зимбабве — промежуточная траектория с последующей эмиграцией части белого населения.

Ключевые оси:

```text
EXPECTED_SECURITY_AFTER_TRANSFER
EXPECTED_PROPERTY_SECURITY
IDENTITY/SETTLER_ATTACHMENT
LEGAL_STATUS_AFTER_TRANSFER
EXIT_LOGISTICS
EXTERNAL_DESTINATION_AVAILABLE
```

### T8 — REFORM / NEGOTIATED TRANSFORMATION

Система меняет правила и распределение власти до полного разрушения центра.

Кандидаты для поиска:

- negotiated regime transitions;
- constitutional power-sharing transitions;
- authoritarian liberalization that survives;
- federation reform preventing breakup.

Эта ячейка пока недостаточно наполнена и является приоритетной.

### T9 — REPRESSION + SURVIVAL, BUT DELAYED FAILURE

Режим переживает конкретный кризис, но это не гарантирует долгосрочную устойчивость.

Кандидат:

- Польша, 1980–1981 как immediate-survival control; последующий конец коммунистического режима анализируется отдельно и не импортируется в ранний cutoff.

Guard:

```text
SURVIVED_CRISIS_t != LONG_TERM_REGIME_STABILITY
```

## 3. Первая сравнительная матрица

| Family | Collapse/Transform case | Survival/Alternative case | Главная различающая переменная-кандидат |
|---|---|---|---|
| Personalized regime crisis | Romania 1989 | Belarus 2020 | coercive-node loyalty / external backing / elite defection |
| Mass challenge to regime | Iran 1979 | China 1989 | command executability / elite cohesion / alternative center |
| Monarchy/central authority failure | Russia 1917 | search control | military/elite node defection |
| Union/federation dissolution | USSR 1991 | search preservation control | node exit capacity / alternative legitimacy |
| External stabilizer | Belarus 2020 | Kazakhstan 2022 | expected backing vs actual deployment |
| Imperial contraction | Britain post-1945 | France post-1945 | cost/value of holding node / post-exit network value |
| Failed retention | Portugal 1961–74 | search endurance control | overstretch / military burden / elite military disaffection |
| Minority-rule transition | South Africa 1990–94 | Rhodesia/Zimbabwe 1965–80 | negotiated exit option / war cost / guarantees |
| Settler exit | Algeria 1962 | South Africa 1994 | security/property expectations after transfer |

## 4. Cross-cutting state variables

Все case packets должны по возможности собирать одни и те же оси:

```text
LEGITIMACY
PERCEIVED_LEGITIMACY_BY_CRITICAL_GROUP
COERCIVE_CAPACITY
COMMAND_EXECUTABILITY
CRITICAL_NODE_LOYALTY
ELITE_COHESION
ELITE_EXIT_OPTION
ALTERNATIVE_POWER_CENTER
MASS_MOBILIZATION
SMALL_GROUP_FRICTION
SOCIAL_INEQUALITY
ECONOMIC_PRESSURE
FOOD/FUEL/WATER_PRESSURE
EXTERNAL_SUPPORT_AVAILABLE
EXTERNAL_FORCE_DEPLOYED
INTERNATIONAL_PRESSURE
INFORMATION_ENVIRONMENT
PROPAGANDA / DISINFORMATION
RESOURCE_DISTRIBUTION
CENTER_DEPENDENCE
NODE_EXIT_CAPACITY
COST_OF_HOLDING_NODE
VALUE_AFTER_RELEASE
SUCCESSION_RESILIENCE
```

## 5. Новый cohesion layer

Из исторического донорного обсуждения принимается как HYPOTHESIS LAYER, не как доказанный закон:

```text
SYSTEM_COHESION_AND_RESOURCE_DISTRIBUTION
```

Поля-кандидаты:

```text
COOPERATION_BENEFIT_BALANCE
PERCEIVED_NET_BENEFIT
PERCEIVED_FAIRNESS
INTEGRATION_MODE
EXIT_COST
ALTERNATIVE_ATTRACTIVENESS
CENTER_DEPENDENCE
CRITICAL_NODE_LOYALTY
SUCCESSION_RESILIENCE
```

Guards:

```text
NET_BENEFIT != PERCEIVED_NET_BENEFIT
RESOURCE_ABUNDANCE != SYSTEM_COHESION
POVERTY != SYSTEM_COLLAPSE
APPARENT_COMPLIANCE != REGIME_SUPPORT
```

## 6. Benchmark construction rule

Каждый реальный case строится минимум в 2–4 cutoff snapshots.

Пример:

```text
t0 = до открытого кризиса
t1 = кризис уже заметен, outcome ещё не очевиден
t2 = critical-node behavior начинает меняться
t3 = threshold / transition near-observable
```

Кодировщик не получает:

```text
country label if avoidable
famous names if removable
future outcome
after-cutoff synthesis
retrospective causal labels
```

После каждого cutoff сравнивается:

```text
MODEL_EXPECTATION
OBSERVED_NEXT_SLICE
RESIDUAL_STATUS
TRAJECTORY_SET
MISSING_DISCRIMINATING_OBSERVATION
```

## 7. Пустые ячейки — что искать дальше

Приоритет A:

1. федерация/союз под угрозой распада, который сохранился;
2. дорогая периферийная война без collapse центра;
3. minority-rule transition, закончившийся без массового исхода старой элиты;
4. minority-rule transition, закончившийся массовым исходом;
5. negotiated authoritarian transition with elite safety guarantees;
6. crisis where external support was expected but never deployed and regime nevertheless survived/failed.

Приоритет B:

7. экономический/systemic contraction without political collapse;
8. крупный кризис с реальной elite defection, но без смены режима;
9. сильный протест при расколе силового аппарата, но без collapse;
10. case where resource release clearly improved core stability.

## 8. Следующий этап

```text
NEXT = SOURCE-BACKED CASE INTAKE
```

Для первой волны собрать первичные/близкие к первичным источники и cutoff chronology по 8 якорным кейсам:

```text
Russia 1917
Romania 1989
USSR 1991
Belarus 2020
Kazakhstan 2022
Britain decolonization subcase
France decolonization subcase
South Africa 1990–94 / Rhodesia 1965–80 pair
```

После этого создать `HISTORICAL_TRANSITION_CASE_CARD_v0_1` и одинаково заполнить все cases.

## 9. Status

```text
HISTORICAL_MACROSYSTEM_TRANSITION_MATRIX_V0_1 = READY
CASE_FAMILIES = DEFINED
ANCHOR_CASES = SELECTED
CONTROL_GAPS = IDENTIFIED
SOURCE_BACKED_INTAKE = NEXT
OUTCOME_BLIND_BENCHMARK = NOT_YET_READY
```
