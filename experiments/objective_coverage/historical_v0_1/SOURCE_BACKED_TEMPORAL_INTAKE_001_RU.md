# SOURCE-BACKED TEMPORAL INTAKE 001

**Статус:** `SOURCE_BACKED / TEMPORAL_SERIES / PRE-BLIND_PREPARATION / NOT_NUMERICALLY_VALIDATED`

## 1. Назначение

Подготовить три временные серии для последующего blind temporal-sequence теста:

1. Российская империя 1917 — быстрый collapse.
2. СССР 1989–1991 — медленное системное размыкание и альтернативная координация.
3. Португалия 1961–1974/75 — накопительное перенапряжение периферии, военный раскол, затем controlled contraction/decolonization.

Задача intake — не объяснять исход задним числом, а фиксировать наблюдаемые состояния по датированным срезам.

## 2. Общие guards

```text
HISTORICAL_OUTCOME != INPUT_FEATURE
LATER_EVENT != EARLIER_KNOWLEDGE
PRESSURE_ACCUMULATION != THRESHOLD_NEAR
MILITARY_ASSET_EXISTS != EXECUTABLE_CAPACITY
FORMAL_CENTER_EXISTS != EFFECTIVE_CENTER
PERIPHERY_COST != CENTER_COLLAPSE
NEGOTIATED_RELEASE != SYSTEM_COLLAPSE
```

## 3. SERIES RUS-1917

### RUS-T0 — 25 Feb 1917 (старый стиль документа)

Наблюдаемое:
- ожидается заседание Думы;
- имеются ожидания организованных забастовок и демонстраций;
- губернатор Петрограда объявляет военное положение/военный режим и обещает его исполнение;
- силовая способность формально присутствует;
- массовая дефекция критических узлов ещё не зафиксирована в этом срезе.

Предварительный state:
```text
transition_instability_state = STRESSED
transition_signal = PRESSURE_ACCUMULATION
critical_node_alignment = UNKNOWN
command_executability_state = UNKNOWN/STRESSED
```

Источник: Office of the Historian, FRUS Russia, telegram 1056, Petrograd, Feb 25 1917.
https://history.state.gov/historicaldocuments/frus1918Russiav01/d1

### RUS-T1 — 7–12 Mar 1917 retrospective contemporaneous report

Наблюдаемое по консульскому отчёту:
- дефицит хлеба и других базовых товаров;
- забастовки и рост уличных беспорядков;
- полиция применяет силу, но не восстанавливает контроль;
- часть пехоты и казаков отказывается стрелять/разгонять толпу;
- появляются эпизоды конфликта между силовыми сегментами.

Предварительный state:
```text
transition_instability_state = DEGRADING
transition_signal = MULTI_SIGNAL
command_executability_state = DEGRADING
critical_node_alignment = MIXED/SHIFTING candidate
```

Источник: Office of the Historian, Consul Winship report, Mar 20 1917, describing events from Mar 7 onward.
https://history.state.gov/historicaldocuments/frus1918Russiav01/d10

### RUS-T2 — 14 Mar 1917

Наблюдаемое:
- революционеры контролируют Петроград;
- Дума отказывается исполнить приказ императора о роспуске/перерыве;
- организовано Временное правительство;
- большинство/все полки, направленные в Петроград, по прибытии присоединяются к революционерам.

Предварительный state:
```text
transition_instability_state = TRANSITION_UNDERWAY
transition_signal = MULTI_SIGNAL
command_executability_state = COLLAPSING
critical_node_alignment = SHIFTING / OPPOSITION_ALIGNED candidate
alternative_coordination_state = ACTIVE
```

Источник: Office of the Historian, Ambassador Francis telegram, Mar 14 1917.
https://history.state.gov/historicaldocuments/frus1918Russiav01/d2

### RUS-T3 — 15–18 Mar 1917

Наблюдаемое:
- отречение Николая II формально опубликовано;
- Михаил не принимает верховную власть без решения Учредительного собрания;
- полномочия переходят к Временному правительству;
- наблюдается смена центра формальной политической власти.

Это evaluator outcome-stage, не использовать как input для более ранних cutoff.

Источники:
https://history.state.gov/historicaldocuments/frus1918Russiav01/d4
https://history.state.gov/historicaldocuments/frus1918Russiav01/d6
https://history.state.gov/historicaldocuments/frus1918Russiav01/d7

## 4. SERIES USSR-1989-1991

### USSR-T0 — 1989

Наблюдаемое:
- либерализация политического режима и ослабление монополии партийного контроля;
- крах коммунистических режимов Восточной Европы создаёт внешний/системный фон;
- внутри СССР усиливаются движения за независимость в Прибалтике и на Кавказе;
- центральный союзный аппарат формально сохраняется.

Предварительный state:
```text
transition_instability_state = STRESSED
transition_signal = PRESSURE_ACCUMULATION
alternative_coordination_state = EMERGING
```

Источник: Office of the Historian, Collapse of the Soviet Union.
https://history.state.gov/milestones/1989-1992/collapse-soviet-union

### USSR-T1 — May–Jun 1990

Наблюдаемое:
- усиливается политический конфликт Горбачёв–Ельцин;
- после выборов 1990 появляются конкурирующие политические центры и программы реформ;
- республиканская/российская политическая автономия становится практически значимой;
- СССР формально продолжает существовать, союзные структуры функционируют.

Предварительный state:
```text
transition_instability_state = DEGRADING candidate
transition_signal = ALTERNATIVE_COORDINATION
critical_node_alignment = MIXED candidate
alternative_coordination_state = ACTIVE
```

Источник: Office of the Historian, Collapse of the Soviet Union.
https://history.state.gov/milestones/1989-1992/collapse-soviet-union

### USSR-T2 — Jan 1991

Наблюдаемое:
- кризис вокруг контроля центра над республиками усиливается;
- в Литве и Латвии происходит насилие;
- советские танки используются против демократических/независимостных выступлений;
- силовой ресурс центра по-прежнему физически и оперативно существует;
- одновременно требования независимости республик сохраняются.

Предварительный state:
```text
transition_instability_state = DEGRADING
transition_signal = MULTI_SIGNAL
coercive_asset_capacity = HIGH
coercive_executable_capacity = PRESENT but insufficient for cohesion inference
```

Источник: Office of the Historian, Collapse of the Soviet Union.
https://history.state.gov/milestones/1989-1992/collapse-soviet-union

### USSR-T3 — Jul 1991

Наблюдаемое:
- Горбачёв остаётся международно признанным союзным руководителем;
- США подписывают START с ним;
- одновременно администрация США увеличивает контакты с Ельциным;
- вопрос реального политического капитала центра уже открыт.

Предварительный state:
```text
transition_instability_state = DEGRADING / THRESHOLD_NEAR candidate
transition_signal = ALTERNATIVE_COORDINATION
critical_node_alignment = MIXED candidate
```

Источник: Office of the Historian, Collapse of the Soviet Union.
https://history.state.gov/milestones/1989-1992/collapse-soviet-union

### USSR-T4 — 19–21 Aug 1991

Наблюдаемое:
- попытка переворота против Горбачёва;
- Ельцин и российский политический центр выступают как самостоятельный центр сопротивления;
- путч терпит неудачу;
- союзная политическая вертикаль после события оказывается заметно слабее;
- партийный центр начинает размыкаться.

Предварительный state:
```text
transition_instability_state = TRANSITION_UNDERWAY
transition_signal = MULTI_SIGNAL
alternative_coordination_state = ACTIVE
critical_node_alignment = SHIFTING
```

Источник: Office of the Historian, Collapse of the Soviet Union.
https://history.state.gov/milestones/1989-1992/collapse-soviet-union

### USSR-T5 — Aug–Sep 1991

Наблюдаемое:
- после путча Украина и Беларусь объявляют независимость;
- прибалтийские государства добиваются международного признания;
- возникает уже не просто политическая оппозиция центру, а сеть альтернативных суверенных центров.

Предварительный state:
```text
transition_instability_state = TRANSITION_UNDERWAY
transition_signal = ALTERNATIVE_COORDINATION / MULTI_SIGNAL
center_periphery_cost_state = UNSUSTAINABLE candidate
```

Источники:
https://history.state.gov/milestones/1989-1992/collapse-soviet-union
https://history.state.gov/countries/belarus
https://history.state.gov/countries/lithuania

### USSR-T6 — Dec 1991

Наблюдаемое:
- Россия, Украина и Беларусь формируют СНГ;
- политическая конструкция Союза фактически прекращает функционировать;
- 25 декабря Горбачёв уходит с поста президента СССР.

Outcome-stage. Не использовать как вход для более ранних cutoff.

Источник:
https://history.state.gov/milestones/1989-1992/collapse-soviet-union

## 5. SERIES PRT-1961-1975

### PRT-T0 — 1961

Наблюдаемое:
- международное давление на португальскую колониальную систему усиливается;
- внешние наблюдатели уже рассматривают долговечность португальской империи в Африке как сомнительную;
- политический центр в Лиссабоне всё ещё придерживается удержания заморских территорий.

Предварительный state:
```text
transition_instability_state = STRESSED
transition_signal = PRESSURE_ACCUMULATION
center_periphery_cost_state = RISING candidate
```

Источник: Office of the Historian, telegram on Portugal/colonies, Dec 5 1961.
https://history.state.gov/historicaldocuments/frus1961-63v13/d331

### PRT-T1 — 1960s–early 1970s

Наблюдаемое:
- несколько африканских движений ведут вооружённую борьбу за независимость;
- колониальная проблема становится длительной военной нагрузкой;
- центр сохраняет контроль, но стоимость удержания периферии накапливается.

Не давать numeric severity без отдельного источника.

Предварительный state:
```text
transition_instability_state = STRESSED / DEGRADING candidate
transition_signal = PRESSURE_ACCUMULATION
center_periphery_cost_state = HIGH candidate
```

Источник-контекст: Office of the Historian, Angola Crisis 1974–75.
https://history.state.gov/milestones/1969-1976/angola

### PRT-T2 — Feb–Mar 1974

Наблюдаемое:
- публикация книги Антониу де Спинолы утверждает невозможность военного решения африканской проблемы и необходимость политического решения;
- публикация вызывает политический кризис;
- раскол внутри вооружённых сил, связанный с африканской политикой, становится наблюдаемым политическим фактором.

Предварительный state:
```text
transition_instability_state = DEGRADING / THRESHOLD_NEAR candidate
transition_signal = NODE_REALIGNMENT
critical_node_alignment = MIXED/SHIFTING candidate
center_periphery_cost_state = HIGH
```

Источники:
https://history.state.gov/historicaldocuments/frus1969-76v28/d98
https://history.state.gov/historicaldocuments/frus1969-76ve15p2Ed2/ch3

### PRT-T3 — 25 Apr 1974

Наблюдаемое:
- военный переворот свергает правительство;
- мятеж организован военным движением;
- лоялистское сопротивление ограничено;
- новое военное руководство быстро устанавливает контроль.

Предварительный state:
```text
transition_instability_state = TRANSITION_UNDERWAY
transition_signal = NODE_REALIGNMENT / MULTI_SIGNAL
command_executability_state = COLLAPSING for old regime
critical_node_alignment = SHIFTING / OPPOSITION_ALIGNED candidate
```

Источник: Office of the Historian, Kissinger memorandum, Apr 29 1974.
https://history.state.gov/historicaldocuments/frus1969-76v28/d98

### PRT-T4 — Jul–Sep 1974

Наблюдаемое:
- новое руководство публично движется к независимости африканских территорий;
- начинаются переговоры с движениями освобождения;
- в Мозамбике достигаются соглашение, прекращение огня и переходное правительство;
- contraction происходит через negotiated release, а не через распад португальского государства.

Предварительный state:
```text
transition_instability_state = TRANSITION_UNDERWAY
transition_signal = NEGOTIATED_RECONFIGURATION
center_periphery_cost_state = RELEASE_IN_PROGRESS
negotiated_transition_channel = ACTIVE
```

Источник: Office of the Historian, Editorial Note, Portugal/Africa negotiations.
https://history.state.gov/historicaldocuments/frus1969-76v28/d101

### PRT-T5 — 1975

Наблюдаемое:
- процесс деколонизации продолжается;
- Мозамбик получает независимость 25 июня 1975;
- Ангольский переход осложняется конкуренцией между несколькими вооружёнными движениями и перерастает в отдельный конфликт.

Outcome-stage для оценки различия:
```text
CORE_STATE_SURVIVES
FORMAL_EMPIRE_CONTRACTS
PERIPHERY_OUTCOMES_DIVERGE
```

Источники:
https://history.state.gov/historicaldocuments/frus1969-76v28/d101
https://history.state.gov/milestones/1969-1976/angola

## 6. Ключевые различающие оси между тремя сериями

```text
RUS-1917:
rapid command erosion + critical-node defection + alternative center

USSR-1989-91:
slow alternative-center growth + republican sovereignty + failed central restoration

PRT-1961-74:
periphery maintenance burden + military internal split + negotiated contraction after regime transition
```

Главный guard:

```text
SAME FINAL LOSS_OF_OLD_CONFIGURATION
!=
SAME TRANSITION_MECHANISM
```

## 7. Следующий benchmark

На основе intake построить `TEMPORAL_SEQUENCE_BLIND_PACKET_001`, где:
- реальные названия и даты скрыты;
- серия сохраняет внутренний порядок T0→Tn;
- outcome-stage удалён;
- кодировщик отдельно отмечает first distinguishable transition point;
- evaluator сравнивает, когда появляется первый устойчивый `DEGRADING`, `THRESHOLD_NEAR`, `TRANSITION_UNDERWAY`;
- structural gap остаётся отдельной осью и не заменяет transition signal.

## 8. Status

```text
SOURCE_BACKED_TEMPORAL_INTAKE_001 = READY
RUS_1917 = INCLUDED
USSR_1989_1991 = INCLUDED
PORTUGAL_1961_1975 = INCLUDED
SOURCE_BACKED = YES
BLIND_PACKET = NEXT
NUMERIC_FORESIGHT_USE = BLOCKED
```
