# ROMANIA DECEMBER 1989 — THRESHOLD EXTRACTION 001

**Статус:** `SOURCE_BACKED_EXTRACTION / PRE_THRESHOLD_AND_THRESHOLD / NOT_OUTCOME_BLIND_BY_ITSELF / READY_FOR_BLIND_PACKET_IMPORT`

## 1. Цель

Закрыть ранее незаполненный участок 21–22 декабря 1989 года: переход от формально действующей командной вертикали к наблюдаемой эрозии её исполнимости и смене поведения военных узлов.

## 2. Датированные наблюдения

### 17 декабря 1989 — force capacity явно существует

Документированный приказ Министерства национальной обороны предусматривает боеприпасы, танки, вооружённые патрули и право применения огня после предупреждения. Это подтверждает наличие формальной силовой способности режима и действующей командной структуры на раннем этапе кризиса.

**Кодируемое наблюдение:**

```text
COERCIVE_CAPACITY_EXISTS = YES
COMMAND_CHANNEL_EXISTS = YES
COMMAND_EXECUTABILITY = NOT_YET_PROVEN_STABLE
```

### 19 декабря 1989 — официальный центр сохраняет информационный контроль

Телеграмма МИД посольствам предписывает отрицать знание событий в Тимишоаре и трактовать внешние вопросы как вмешательство во внутренние дела. Это подтверждает, что центральный аппарат ещё действует координированно как государственная машина.

**Кодируемое наблюдение:**

```text
CENTRAL_ADMINISTRATIVE_COORDINATION = OBSERVED
PUBLIC_INFORMATION_CONTROL_ATTEMPT = OBSERVED
```

### 20–21 декабря — признаки различия между наличием армии и её готовностью выполнять режимную функцию

Ретроспективная реконструкция на базе свидетельств и архивных материалов фиксирует, что в Тимишоаре части армии позволяли гражданам проходить, были сообщения об отказах выполнять приказы, а затем армия стала уходить в казармы. При этом источник отдельно предупреждает: такой отход мог быть приказан сверху, а не быть спонтанной массовой дефекцией.

**Guard:**

```text
ARMY_WITHDRAWAL != PROOF_OF_BOTTOM_UP_DEFECTION
REFUSAL_REPORTS != WHOLE_ARMY_DEFECTION
```

Но даже при приказном отходе это является наблюдением снижения пригодности армии для продолжения прямого подавления в прежнем режиме.

### 21 декабря — публичный контроль режима становится наблюдаемо нестабильным

Массовая публичная демонстрация в Бухаресте перестаёт функционировать как односторонняя демонстрация поддержки. Для blind-use важен не итог, а изменение state variable:

```text
PUBLIC_COMPLIANCE_SIGNAL = DEGRADED
COMMON_KNOWLEDGE_OF_DEFIANCE = INCREASING
```

### 22 декабря — командная исполнимость меняется качественно

Современные сообщения и последующая документация фиксируют, что армейские части перешли на сторону протестующих; в Бухаресте солдат приветствовали как находящихся «на стороне народа», а армия вступала в столкновения с силами, ассоциированными с Securitate.

Это уже не просто наличие недовольства. Это наблюдаемый переход между состояниями:

```text
COERCIVE_CAPACITY_EXISTS = YES
REGIME_EXECUTABLE_CAPACITY = COLLAPSING
CRITICAL_SECURITY_NODE_ALIGNMENT = SHIFTING
```

## 3. Structural distinction

Румынский кейс важен тем, что показывает:

```text
STATE_FORCE_ASSET_PRESENT
!=
REGIME_FORCE_ASSET_USABLE
```

и:

```text
FORMAL_COMMAND_STRUCTURE
!=
EFFECTIVE_COMMAND_EXECUTION
```

До 22 декабря режим формально обладает армией, силовыми ведомствами, администрацией и информационным аппаратом. Но к threshold меняется не физическое наличие этих ресурсов, а их функциональная связность с режимом.

## 4. Blind snapshot candidates

### RO-T0 — 17 декабря

```text
mass unrest = OBSERVED_LOCAL
coercive capacity = HIGH / ACTIVE
live-fire authorization = PRESENT
central coordination = ACTIVE
army loyalty = UNKNOWN
command executability = PARTIALLY_OBSERVED
public compliance = DEGRADED_LOCAL
```

### RO-T1 — 19 декабря

```text
unrest persistence = OBSERVED
central administrative coordination = ACTIVE
information suppression/denial = ACTIVE
army institutional cohesion = UNKNOWN
regime executable coercion = OBSERVED_BUT_STRESSED
```

### RO-T2 — 21 декабря

```text
protest diffusion = NATIONAL_CAPITAL_REACHED
public compliance signal = SHARPLY_DEGRADED
coercive assets = PRESENT
critical node loyalty = UNCERTAIN
command executability = UNDER_STRESS
```

### RO-T3 — 22 декабря pre-flight / threshold

```text
coercive assets = PRESENT
army alignment = SHIFTING
regime executable capacity = COLLAPSING
alternative political coordination = EMERGING
formal regime authority = STILL_CLAIMED
```

## 5. Guards

```text
MASS_PROTEST != REGIME_COLLAPSE
ARMY_EXISTS != ARMY_WILL_EXECUTE
ARMY_WITHDRAWAL != SPONTANEOUS_DEFECTION_PROVEN
SECURITY_NODE_SHIFT != WHOLE_STATE_COLLAPSE
PUBLIC_DEFIANCE != AUTOMATIC_ELITE_DEFECTION
```

## 6. Source notes

Primary/near-primary anchors used in research pass:

- Romanian MFA telegram to embassies, 19 Dec 1989, preserved via Making the History of 1989 / World History Commons.
- Romanian Ministry of Defence order of 17 Dec 1989 reproduced in Romanian documentary collections.
- Radio Free Europe archival reconstruction for 17–21 Dec 1989.
- Contemporary international reporting from 22 Dec 1989 describing army alignment shift in Bucharest.

These support the threshold distinction above; they do not justify stronger claims about every unit, every commander, or a single causal mechanism.

## 7. Status

```text
ROMANIA_THRESHOLD_EXTRACTION_001 = COMPLETE
PRE_THRESHOLD_SNAPSHOTS = READY
COMMAND_EXECUTABILITY_LAYER = SOURCE_SUPPORTED
WHOLE_ARMY_DEFECTION = NOT_CLAIMED
NEXT = HISTORICAL_PRE_THRESHOLD_BLIND_PACKET_001
```
