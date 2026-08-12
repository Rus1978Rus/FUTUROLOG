# HISTORICAL PARENT NODE RECONSTRUCTION TEST 001

**Статус:** `CONCEPT_FIXED / CROSS_CASE_HISTORICAL_TEST / SOURCE_BACKED_DESIGN / NOT_YET_BLIND_CODED`

## 1. Цель

Проверить механизм, при котором после распада сложной политической системы один из её бывших компонентов или государств-преемников начинает ретроспективно занимать место всей предшествующей системы в коллективной памяти, политической риторике или исторической идентичности.

Ключевой вопрос:

> Может ли прежняя структура `PARENT_SYSTEM -> CHILD_A + CHILD_B + ...` со временем реконструироваться как `CHILD_A -> CHILD_B + ...`, даже если институционально CHILD_B никогда не был частью CHILD_A внутри исходной системы?

## 2. Базовые guards

```text
RETROSPECTIVE_PERIODIZATION != CONTEMPORARY_SYSTEM_IDENTITY
FORMAL_DISSOLUTION != COGNITIVE_DISSOLUTION
SUCCESSOR_OF_SYSTEM != FORMER_OWNER_OF_OTHER_SYSTEM_MEMBERS
SHARED_HISTORICAL_IDENTITY_CLAIM != LEGAL_POLITICAL_UNITY
LIVING_WITNESSES != STABLE_SHARED_MEMORY
DOMINANT_SUCCESSOR != PREDECESSOR_SYSTEM
CONTINUATOR_STATUS != PARENTAL_OWNERSHIP_OF_CO_MEMBERS
NARRATIVE_PARENT != INSTITUTIONAL_PARENT
```

## 3. Основной механизм-кандидат

```text
PARENT_SYSTEM
  -> COMPONENT_A
  -> COMPONENT_B
  -> COMPONENT_C

DISSOLUTION

COMPONENT_A becomes dominant continuator / strongest successor

later narrative:
COMPONENT_A -> COMPONENT_B / COMPONENT_C
```

Рабочее имя:

```text
PARENT_NODE_SUBSTITUTION
```

Связанная гипотеза:

```text
SUCCESSOR_IDENTITY_CAPTURE
```

То есть доминирующий преемник способен постепенно присваивать идентичность всей предшествующей системы.

## 4. Развести четыре уровня родства

Для каждого case/time slice кодировать отдельно:

```text
formal_parent_at_T
institutional_parent_at_T
claimed_historical_parent_at_T
retrospectively_assigned_parent
```

Дополнительные оси:

```text
continuator_status
international_recognition_structure
public_identity_frame
elite_identity_frame
legal_state_structure
living_witness_density
narrative_parent_strength
parent_node_substitution_status
```

## 5. CASE FAMILY A — USSR

### Структурный baseline

СССР был союзным государством, включавшим союзные республики. Российская СФСР и Украинская ССР являлись союзными республиками одной союзной системы, а не отношением `Russia -> Ukraine`.

### Dissolution / continuity distinction

К концу 1991 года СССР распался. Российская Федерация была воспринята как государство-продолжатель СССР для ряда международных институциональных целей, включая членство в ООН и постоянное место в Совете Безопасности. Это является continuity/continuator relation, но само по себе не превращает остальные бывшие союзные республики в бывшие административные части России.

### Narrative reconstruction target

Проверять появление формул типа:

```text
Ukraine separated from Russia
Belarus separated from Russia
former Russian lands left Russia
```

отдельно от формул:

```text
Ukraine became independent from / after dissolution of USSR
USSR dissolved into successor states
```

Не кодировать политическую риторику как юридический факт.

## 6. CASE FAMILY B — YUGOSLAVIA

SFRY состояла из шести республик. После распада Сербия и Черногория заявили, что их Федеративная Республика Югославия является продолжателем SFRY. США и международная практика не приняли тезис о единственном продолжателе SFRY; позиция США состояла в том, что SFRY распалась без единственного successor state.

Это хороший отрицательный/частичный контроль:

```text
SUCCESSOR_CLAIM exists
but
EXTERNAL_RECOGNITION_OF_SOLE_CONTINUATION = absent
```

Проверять, усиливает ли отсутствие признанного единственного continuator-а сопротивление parent-node substitution.

## 7. CASE FAMILY C — CZECHOSLOVAKIA

Использовать как сильный отрицательный контроль.

После "бархатного развода" ни Чехия, ни Словакия не закрепили за собой единоличную международную идентичность всей Чехословакии; обе рассматривались как новые successor states.

Ожидаемый контрольный эффект:

```text
NO_DOMINANT_CONTINUATOR
-> LOWER_PARENT_NODE_SUBSTITUTION_PRESSURE candidate
```

## 8. CASE FAMILY D — UNITED KINGDOM / IRELAND

Ирландское Свободное государство в 1922 году рассматривалось как отделившаяся часть, тогда как остаточный United Kingdom сохранил международную правосубъектность.

Это нужен контрастный случай, где:

```text
CONTINUATOR_STATE really is the residual parent polity
```

то есть формула "Ireland separated from the United Kingdom" имеет другую структурную основу, чем формула "Ukraine separated from Russia".

Этот кейс нужен, чтобы тест не объявлял любое narrative continuity parent-node substitution.

## 9. CASE FAMILY E — HOLY ROMAN / ROMAN IMPERIAL CONTINUITY

Не использовать современную периодизацию как исходное знание для contemporaneous layer.

Кодировать:

```text
contemporary_system_identity
continuity_claim_state
institutional_structure
retrospective_periodization
```

Цель — проверить зеркальный процесс: система может продолжать считать себя той же имперской сущностью намного дольше, чем позднейшие историки готовы считать её тем же государственным образованием.

Это не идентично parent-node substitution, но является важным control-class для `IDENTITY_STRUCTURE_LAG`.

## 10. CASE FAMILY F — AUSTRIA-HUNGARY

Нужен как дополнительный отрицательный/смешанный контроль.

После распада империи Австрия не стала бесспорно интерпретироваться как единственная "сама Австро-Венгрия", от которой остальные государства якобы отсоединились. Проверять, какие структурные условия препятствовали захвату parent identity одним successor node.

## 11. Источниковые опоры

### USSR / continuator distinction

Британский правительственный обзор международно-правовой практики приводит распад СССР как пример, где Российская Федерация была воспринята как государство, продолжающее правосубъектность СССР и сохранила членство в ООН и постоянное место в Совете Безопасности. Это доказывает continuity relation, но не parental ownership остальных союзных республик.

### Yugoslavia

Office of the Historian фиксирует, что Сербия и Черногория претендовали на статус successor state SFRY, но США заняли позицию: SFRY распалась без единственного successor state.

### Czechoslovakia

Правительственный legal analysis UK использует распад Чехословакии как пример, где оба новых государства стали successor states и ни одно не заявило непрерывность всей прежней системы.

### UK / Ireland

Тот же анализ приводит Ирландское Свободное государство как случай отделения, при котором United Kingdom продолжил прежнюю международную правосубъектность.

## 12. Гипотезы для проверки, НЕ правила

```text
H1: DOMINANT_CONTINUATOR_STATUS increases probability of SUCCESSOR_IDENTITY_CAPTURE.

H2: HIGH population/territory share retained by one successor increases probability of retrospective parent substitution.

H3: INTERNATIONAL_CONTINUITY recognition can spill over from legal continuity into public historical identity.

H4: LONG shared-language/media space increases persistence of old system identity after formal dissolution.

H5: CENTRALIZED_HISTORICAL_NARRATIVE can transform "successor of system" into "former owner of co-members".

H6: LIVING_WITNESSES reduce but do not eliminate narrative reconstruction.

H7: NO_SINGLE_CONTINUATOR reduces probability of parent-node substitution.
```

Все H1-H7 имеют статус `TESTABLE_HYPOTHESIS / NOT_PROVEN`.

## 13. Blind-test design

Внешнему кодировщику не показывать названия стран и конечные политические нарративы.

Для каждой серии дать:

```text
T0 institutional topology
T1 dissolution topology
T2 successor structure
T3 international continuity treatment
T4 public/elite narrative sample
```

Попросить отдельно определить:

```text
institutional_parent_at_T0
continuator_at_T3
narrative_parent_at_T4
parent_node_substitution_status
```

Допустимые значения:

```text
parent_node_substitution_status =
NONE
WEAK_CANDIDATE
OBSERVED_NARRATIVE_SUBSTITUTION
STRUCTURALLY_CORRECT_CONTINUATOR_RELATION
NOT_ASSESSABLE
```

## 14. Critical distinction

Главный discriminating pair:

```text
CASE 1
A and B were co-members of P.
After dissolution A is continuator.
Later B is narrated as having separated from A.
=> possible PARENT_NODE_SUBSTITUTION.

CASE 2
B was legally part of A.
After separation A continues.
Later B is narrated as having separated from A.
=> no substitution; structurally correct parent relation.
```

Это делает тест falsifiable и защищает от идеологического кодирования.

## 15. Связь с FUTUROLOG

Этот механизм нужен не только для исторической памяти. Он может влиять на реальные future trajectories через:

```text
territorial claims
revisionist legitimacy
public support for reintegration
classification of war as civil vs interstate
perceived incompleteness of prior dissolution
elite narrative mobilization
identity-based grievance persistence
```

Но guard обязателен:

```text
NARRATIVE_EXISTS != POLICY_INTENT
POLICY_INTENT != EXECUTION
IDENTITY_CLAIM != LEGAL_CLAIM_VALIDITY
```

## 16. Status

```text
HISTORICAL_PARENT_NODE_RECONSTRUCTION_TEST_001 = READY_FOR_SOURCE_DEEPENING
BLIND_PACKET = NEXT
NUMERIC_USE = BLOCKED
CAUSAL_CLAIMS = BLOCKED
```
