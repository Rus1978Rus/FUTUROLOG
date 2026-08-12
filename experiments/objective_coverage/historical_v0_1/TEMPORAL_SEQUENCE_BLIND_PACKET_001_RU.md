# TEMPORAL SEQUENCE BLIND PACKET 001

**PACKET_SCHEMA_ID:** `TSB-001-V1`

**Статус:** `READY_FOR_EXTERNAL_MULTI_MODEL_TEST / TEMPORAL_ORDER_VISIBLE / COUNTRY_LABELS_HIDDEN / OUTCOMES_HIDDEN / SOURCE_BACKED`

## 1. Цель

Проверить, способен ли кодировщик по последовательности состояний определить **первую точку, где траектория становится структурно отличимой от обычного кризиса**, не зная страны и дальнейшего исхода.

Это не задача «угадать падение режима». Нужно различать:

```text
PRESSURE_ACCUMULATION
DEGRADING
THRESHOLD_NEAR
TRANSITION_UNDERWAY
```

и не путать их со structural gap.

## 2. Guards

```text
HISTORICAL_OUTCOME != INPUT_FEATURE
LATER_EVENT != EARLIER_KNOWLEDGE
PRESSURE_ACCUMULATION != THRESHOLD_NEAR
MILITARY_ASSET_EXISTS != EXECUTABLE_CAPACITY
FORMAL_CENTER_EXISTS != EFFECTIVE_CENTER
PERIPHERY_COST != CENTER_COLLAPSE
NEGOTIATED_RELEASE != SYSTEM_COLLAPSE
THRESHOLD_NEAR != CERTAIN_OUTCOME
TRANSITION_UNDERWAY != STRUCTURAL_GAP
```

## 3. Coding values

```text
transition_instability_state = STABLE | STRESSED | DEGRADING | THRESHOLD_NEAR | TRANSITION_UNDERWAY | UNKNOWN
transition_signal = NONE | PRESSURE_ACCUMULATION | COMMAND_EROSION | NODE_REALIGNMENT | ALTERNATIVE_COORDINATION | CENTER_PERIPHERY_OVERSTRETCH | NEGOTIATED_RECONFIGURATION | MULTI_SIGNAL | UNKNOWN
critical_node_alignment = REGIME_ALIGNED | MIXED | SHIFTING | OPPOSITION_ALIGNED | UNKNOWN
command_executability_state = STABLE | STRESSED | DEGRADING | COLLAPSING | UNKNOWN
alternative_coordination_state = ABSENT | EMERGING | ACTIVE | DOMINANT | UNKNOWN
center_periphery_cost_state = LOW | RISING | HIGH | UNSUSTAINABLE | UNKNOWN
trajectory_distinguishability = NOT_YET | WEAKLY_DISTINGUISHABLE | STRUCTURALLY_DISTINGUISHABLE | TRANSITION_OBSERVED | UNKNOWN
```

`STRUCTURALLY_DISTINGUISHABLE` означает: текущая последовательность уже содержит прямой differentiator, отделяющий её от простого давления/протеста/стоимости, но конечный исход всё ещё не считается предрешённым.

## 4. SERIES A

### A-T0
- ожидаются организованные забастовки и демонстрации;
- вводится военный режим/военное положение;
- силовой ресурс формально присутствует;
- массовая дефекция критических узлов не наблюдается.

### A-T1
- дефицит базовых товаров и рост уличных беспорядков;
- полиция применяет силу, но контроль не восстанавливается;
- часть пехоты и конных частей отказывается стрелять/разгонять толпу;
- наблюдаются конфликты между силовыми сегментами.

### A-T2
- протестно-революционные силы контролируют столичный политический центр;
- представительный орган не исполняет распоряжение верховной власти о прекращении работы;
- создаётся альтернативное правительство;
- направляемые в столицу военные части по прибытии переходят на сторону новой координации.

## 5. SERIES B

### B-T0
- политическая либерализация ослабляет прежнюю монополию центральной партии;
- в нескольких периферийных регионах усиливаются движения за независимость;
- центральный аппарат формально сохраняется;
- альтернативная координация только появляется.

### B-T1
- усиливается конфликт между союзным центром и крупным республиканским политическим центром;
- после конкурентных выборов появляются практически значимые альтернативные политические программы и центры;
- центральные структуры продолжают функционировать.

### B-T2
- центр применяет силовые средства в части периферии;
- физическая coercive capacity остаётся высокой;
- требования независимости не исчезают;
- использование силы не восстанавливает политическую монополию центра.

### B-T3
- формальный союзный лидер сохраняет международное признание;
- внешние акторы одновременно расширяют контакты с альтернативным республиканским центром;
- вопрос реального политического капитала центра становится открытым.

### B-T4
- происходит попытка переворота внутри центральной системы;
- альтернативный республиканский центр действует как самостоятельный центр сопротивления;
- переворот терпит неудачу;
- центральная политическая вертикаль после события заметно слабее;
- партийный центр начинает размыкаться.

### B-T5
- несколько крупных периферийных единиц объявляют независимость;
- часть периферийных центров получает внешнее признание;
- возникает сеть альтернативных суверенных центров, а не просто оппозиция внутри единого центра.

## 6. SERIES C

### C-T0
- международное давление на заморскую систему усиливается;
- долговечность контроля над периферией ставится под сомнение внешними наблюдателями;
- политический центр по-прежнему придерживается удержания территорий.

### C-T1
- несколько периферийных движений ведут длительную вооружённую борьбу;
- колониальная/периферийная проблема становится длительной военной нагрузкой;
- центр сохраняет контроль, но стоимость удержания накапливается.

### C-T2
- влиятельный военный руководитель публично утверждает невозможность военного решения периферийной проблемы и необходимость политического решения;
- это вызывает политический кризис;
- раскол внутри вооружённых сил по вопросу периферийной политики становится наблюдаемым политическим фактором.

### C-T3
- организованное военное движение свергает прежнее правительство;
- лоялистское сопротивление ограничено;
- новое военное руководство быстро устанавливает контроль.

## 7. Задание по каждой серии

Вернуть кодировку каждого временного шага и отдельно указать:

```text
first_structurally_distinguishable_step
first_transition_observed_step
```

Если серия до конца не достигает соответствующего состояния, использовать `NONE`.

Нельзя использовать последующий исход как основание для более раннего шага.

## 8. Output CSV — step rows

```csv
schema_marker,series_id,step_id,transition_instability_state,transition_signal,critical_node_alignment,command_executability_state,alternative_coordination_state,center_periphery_cost_state,trajectory_distinguishability,confidence,reason
TSB-001-V1,A,A-T0,,,,,,,,,
TSB-001-V1,A,A-T1,,,,,,,,,
TSB-001-V1,A,A-T2,,,,,,,,,
TSB-001-V1,B,B-T0,,,,,,,,,
TSB-001-V1,B,B-T1,,,,,,,,,
TSB-001-V1,B,B-T2,,,,,,,,,
TSB-001-V1,B,B-T3,,,,,,,,,
TSB-001-V1,B,B-T4,,,,,,,,,
TSB-001-V1,B,B-T5,,,,,,,,,
TSB-001-V1,C,C-T0,,,,,,,,,
TSB-001-V1,C,C-T1,,,,,,,,,
TSB-001-V1,C,C-T2,,,,,,,,,
TSB-001-V1,C,C-T3,,,,,,,,,
```

## 9. Output CSV — series summary

После step rows вернуть второй CSV:

```csv
schema_marker,series_id,first_structurally_distinguishable_step,first_transition_observed_step,distinguishing_feature_class,confidence,reason
TSB-001-V1,A,,,,,
TSB-001-V1,B,,,,,
TSB-001-V1,C,,,,,
```

`distinguishing_feature_class`:

```text
COMMAND_EXECUTION_FAILURE
CRITICAL_NODE_REALIGNMENT
ALTERNATIVE_CENTER_MATURATION
CENTER_PERIPHERY_OVERSTRETCH
NEGOTIATED_RECONFIGURATION
MULTI_FACTOR
UNKNOWN
```

## 10. Protocol gate

Результат отклоняется до scoring, если:

- schema_marker не `TSB-001-V1`;
- изменены series/step IDs;
- кодировщик пытается назвать реальные страны/события;
- последовательность переставлена;
- позднее событие используется для обоснования более ранней кодировки;
- `THRESHOLD_NEAR` трактуется как доказательство конечного исхода.

## 11. Evaluator-only mapping — НЕ ПЕРЕДАВАТЬ внешнему кодировщику

```text
A = Russian Empire 1917
B = USSR 1989–1991
C = Portugal 1961–1974
```

Предварительные evaluator hypotheses, НЕ ground truth:

```text
A first structurally distinguishable candidate = A-T1
A transition observed = A-T2

B first structurally distinguishable candidate = B-T1 or B-T3
B transition observed = B-T4

C first structurally distinguishable candidate = C-T2
C transition observed = C-T3
```

Эти labels требуют внешнего agreement и не являются валидированными.

## 12. Status

```text
TEMPORAL_SEQUENCE_BLIND_PACKET_001 = READY
SOURCE_BACKED = YES
TEMPORAL_ORDER_VISIBLE = YES
COUNTRY_LABELS_HIDDEN = YES
OUTCOMES_HIDDEN = YES
NUMERIC_FORESIGHT_USE = BLOCKED
```
