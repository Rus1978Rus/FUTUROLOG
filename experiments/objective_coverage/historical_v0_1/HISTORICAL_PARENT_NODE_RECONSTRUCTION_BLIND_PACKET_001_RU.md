# HISTORICAL PARENT NODE RECONSTRUCTION — BLIND PACKET 001

**PACKET_SCHEMA_ID:** `HPNR-001-V1`

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_TEST / STRUCTURE_ONLY / COUNTRY_LABELS_HIDDEN / NARRATIVE_LAYER_INCLUDED / OUTCOME_LABELS_HIDDEN`

## 1. Цель

Проверить, способен ли кодировщик отличить:

- реальную institutional parent relation;
- successor/continuator status;
- historical continuity claim;
- позднейшую narrative reconstruction;
- настоящий `PARENT_NODE_SUBSTITUTION` от корректной памяти о прежней иерархии.

Это НЕ тест политических симпатий и НЕ вопрос «какой народ кому принадлежит».

## 2. Guards

```text
SUCCESSOR_OF_SYSTEM != FORMER_OWNER_OF_OTHER_SYSTEM_MEMBERS
CONTINUATOR_STATUS != PARENTAL_OWNERSHIP_OF_CO_MEMBERS
HISTORICAL_CONTINUITY_CLAIM != INSTITUTIONAL_PREDECESSOR_STRUCTURE
FORMAL_DISSOLUTION != COGNITIVE_DISSOLUTION
LIVING_WITNESSES != STABLE_SHARED_MEMORY
RETROSPECTIVE_PERIODIZATION != CONTEMPORARY_SYSTEM_IDENTITY
CLAIMED_PARENT != OBSERVED_PARENT
SHARED_HISTORY != PRIOR_ADMINISTRATIVE_SUBORDINATION
```

## 3. Допустимые значения

```text
formal_parent_relation = SAME_PARENT_SYSTEM | DIRECT_SUBORDINATION | NO_PARENT_RELATION | UNKNOWN
successor_structure = SINGLE_CONTINUATOR | MULTIPLE_SUCCESSORS | SUCCESSOR_WITHOUT_EXCLUSIVE_CONTINUATOR | UNKNOWN
continuity_claim_state = ABSENT | PRESENT_WEAK | PRESENT_STRONG | DOMINANT | UNKNOWN
retrospective_parent_claim = ORIGINAL_PARENT | SUCCESSOR_AS_PARENT | NO_PARENT_CLAIM | MIXED | UNKNOWN
parent_node_substitution = NO | POSSIBLE | OBSERVED | NOT_ASSESSABLE
identity_structure_lag = NONE | LOW | MEDIUM | HIGH | UNKNOWN
claim_evidence_role = LEGAL_INSTITUTIONAL | HISTORICAL_IDENTITY | POLITICAL_NARRATIVE | MIXED | UNKNOWN
confidence = LOW | MEDIUM | HIGH
```

## 4. Blind cases

### PN-A4

T0 institutional topology:

```text
SYSTEM-P
├── UNIT-A
├── UNIT-B
├── UNIT-C
└── UNIT-D
```

A и B имеют собственные республиканские/региональные институты внутри P. B не является административной частью A.

T1 dissolution:
- P прекращает функционировать как единый союзный центр;
- A, B, C, D становятся отдельными государственными субъектами.

T2 successor structure:
- A получает наиболее сильную международную и институциональную преемственность с P;
- при этом B продолжает существовать как отдельное признанное государство.

T3 later narrative:
- в части политического и массового дискурса появляется формула, что B «отделился от A»;
- одновременно существует рамка, что B вышел из P и никогда не был административным подразделением A внутри P.

### PN-B7

T0 institutional topology:

```text
FEDERATION-Q
├── REPUBLIC-X
├── REPUBLIC-Y
├── REPUBLIC-Z
└── REPUBLIC-W
```

X, Y, Z, W являются составными республиками одного федеративного государства.

T1 dissolution:
- федерация прекращает существование;
- X и один союзный с ним компонент заявляют, что именно они продолжают прежнее государство;
- другие бывшие республики это оспаривают;
- внешние государства и международные организации не признают автоматическую исключительную преемственность X над всей прежней федерацией.

T2 later narrative:
- в части дискурса X описывается как естественный центр прежней федерации;
- Y/Z/W иногда описываются как территории, «ушедшие от X».

### PN-C2

T0 institutional topology:

```text
STATE-R
├── LAND-M
└── LAND-N
```

N юридически и административно входит в состав R как подчинённая территория; M является центральной территорией R.

T1 separation:
- N выходит из состава R и становится самостоятельным государством.

T2 later narrative:
- распространено утверждение, что N «отделился от R».

### PN-D9

T0 institutional topology:

```text
DUAL-MONARCHY-S
├── CROWN-HALF-U
└── CROWN-HALF-V
    ├── REGION-K
    └── REGION-L
```

После распада S возникает несколько государств. Ни U, ни V не становятся общепризнанным единственным продолжателем всего S.

T1 later memory:
- в массовой и политической памяти новые государства чаще описываются как возникшие после распада S;
- нет устойчивой доминирующей формулы, что K/L «отделились от U» только потому, что U стало одним из крупнейших преемников.

### PN-E5

T0 identity topology:
- политическая система T считает себя носителем древней имперской легитимности;
- между древним исходным центром и T прошли династические, территориальные и институциональные преобразования;
- современники T широко используют язык продолжения древней империи.

T1 later historiography:
- позднейшие историки различают древнее государство и T как разные политические конструкции;
- современники T не обязательно воспринимали это различие так же.

В этом кейсе нет простой административной схемы «A владел B»; вопрос касается continuity identity, а не территориального parent ownership.

### PN-F8

T0 institutional topology:

```text
UNION-V
├── COUNTRY-J
└── COUNTRY-K
```

J и K являются отдельными государственными компонентами союза V, но у J значительно больший демографический, военный и дипломатический вес.

T1 dissolution:
- V распадается;
- J и K продолжают существовать отдельно;
- международная практика трактует их как два successor states, без автоматического признания J единственным продолжателем всего V.

T2 later narrative:
- несмотря на асимметрию размеров, устойчивой массовой формулы «K отделился от J» не возникает.

## 5. Задание

Для каждого кейса закодируй только структуру, данную в packet.

Не определяй реальные страны/империи.
Не используй интернет.
Не исправляй packet знаниями извне.

Особенно различай:

```text
successor dominance
continuator status
actual institutional parent
later claimed parent
```

`PARENT_NODE_SUBSTITUTION = OBSERVED` разрешён только если later claimed parent структурно заменяет исходный parent node.

## 6. Output CSV

```csv
schema_marker,case_id,formal_parent_relation,successor_structure,continuity_claim_state,retrospective_parent_claim,parent_node_substitution,identity_structure_lag,claim_evidence_role,max_3_discriminating_evidence_targets,confidence,reason
HPNR-001-V1,PN-A4,,,,,,,,,,
HPNR-001-V1,PN-B7,,,,,,,,,,
HPNR-001-V1,PN-C2,,,,,,,,,,
HPNR-001-V1,PN-D9,,,,,,,,,,
HPNR-001-V1,PN-E5,,,,,,,,,,
HPNR-001-V1,PN-F8,,,,,,,,,,
```

## 7. Protocol gate

Reject before scoring if:
- `schema_marker != HPNR-001-V1`;
- case IDs changed;
- real countries/events named;
- external facts introduced;
- `successor/continuator` is automatically converted into `former parent`;
- continuity identity is automatically converted into territorial ownership.

Верни только CSV: header + 6 rows. Без пояснений до или после CSV.

## 8. Evaluator-only target logic — НЕ ПЕРЕДАВАТЬ ВНЕШНЕМУ КОДИРОВЩИКУ

```text
PN-A4: SAME_PARENT_SYSTEM / SINGLE_CONTINUATOR or strong-continuator analogue / SUCCESSOR_AS_PARENT / PARENT_NODE_SUBSTITUTION=OBSERVED
PN-B7: SAME_PARENT_SYSTEM / disputed-or-nonexclusive continuation / SUCCESSOR_AS_PARENT / PARENT_NODE_SUBSTITUTION=POSSIBLE-or-OBSERVED depending strictness
PN-C2: DIRECT_SUBORDINATION / later claim matches prior structure / PARENT_NODE_SUBSTITUTION=NO
PN-D9: SAME_PARENT_SYSTEM or composite-parent structure / MULTIPLE_SUCCESSORS / ORIGINAL_PARENT / PARENT_NODE_SUBSTITUTION=NO
PN-E5: no simple territorial parent relation / continuity identity case / substitution of parent ownership should NOT be inferred
PN-F8: SAME_PARENT_SYSTEM / MULTIPLE_SUCCESSORS / ORIGINAL_PARENT-or-NO_PARENT_CLAIM / PARENT_NODE_SUBSTITUTION=NO
```

## 9. Status

```text
HISTORICAL_PARENT_NODE_RECONSTRUCTION_BLIND_PACKET_001 = READY
COUNTRY_LABELS = HIDDEN
NARRATIVE_LAYER = ACTIVE
PARENT_NODE_SUBSTITUTION_TEST = ACTIVE
NUMERIC_USE = BLOCKED
```
