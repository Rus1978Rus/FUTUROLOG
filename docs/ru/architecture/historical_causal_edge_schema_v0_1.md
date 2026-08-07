# HISTORICAL_CAUSAL_EDGE_SCHEMA v0.1
## Схема связей между историческими узлами FUTUROLOG

**Статус:** `WORKING_SCHEMA / NOT_CAUSAL_PROOF / REVIEW_REQUIRED_FOR_STRONG_EDGES`

Цель: превратить исторический слой из хронологического списка в граф, где каждая связь между узлами имеет собственное утверждение, доказательную опору, альтернативные объяснения и уровень уверенности.

## 1. Главный инвариант

```text
EARLIER_THAN != CAUSED
COEXISTED_WITH != CAUSED
CORRELATED_WITH != CAUSED
EDGE_CLAIM != CAUSAL_PROOF
```

Наличие ребра означает только: существует проверяемая гипотеза о конкретном отношении между двумя узлами.

## 2. Базовые типы ребер

```text
ENABLES
AMPLIFIES
CONSTRAINS
CHANNELS
RESOURCE_LINK
SECURITY_LINK
INSTITUTIONAL_INHERITANCE
PATH_DEPENDENCE
LEGITIMACY_LINK
CONFLICT_MANAGEMENT_LINK
TRIGGER_CONTEXT
COUNTERACTS
```

### ENABLES
A создаёт возможность или среду для B, но не делает B неизбежным.

### AMPLIFIES
A усиливает интенсивность, устойчивость или вероятность продолжения B.

### CONSTRAINS
A ограничивает диапазон доступных действий или траекторий B.

### CHANNELS
A задаёт канал, через который влияние/ресурс/политическое давление достигает B.

### RESOURCE_LINK
A связан с ресурсной способностью B. Не означает автоматически финансирование войны.

### SECURITY_LINK
A изменяет стратегическую или силовую среду B.

### INSTITUTIONAL_INHERITANCE
Институт, правило, организация или структура из A продолжают влиять на B.

### PATH_DEPENDENCE
A делает некоторые последующие варианты проще/дешевле/вероятнее, чем альтернативы, без утверждения неизбежности.

### LEGITIMACY_LINK
A влияет на политическую легитимность, идентичность или признание, относящиеся к B.

### CONFLICT_MANAGEMENT_LINK
A создаёт, поддерживает или ограничивает механизм управления конфликтом B.

### TRIGGER_CONTEXT
A является непосредственным контекстом/условием перехода к B, но не root cause.

### COUNTERACTS
A ослабляет, компенсирует или тормозит механизм, представленный B.

## 3. CSV-контракт

```text
edge_id
case_id
from_node_id
to_node_id
edge_type
edge_claim
mechanism
source_class
source_ref
confidence
alternative_interpretations
counterevidence_or_limitations
status
```

## 4. Confidence

```text
LOW
LOW_MEDIUM
MEDIUM
MEDIUM_HIGH
HIGH
```

Высокая уверенность в историческом факте не даёт автоматически высокую уверенность в причинной связи.

Пример:

```text
NODE_A factual confidence = HIGH
NODE_B factual confidence = HIGH
EDGE A -> B causal confidence = MEDIUM
```

## 5. Статусы

```text
WORKING
REVIEW_REQUIRED
REJECTED
SUPERSEDED
```

Сильные или политически спорные causal claims по умолчанию должны быть `REVIEW_REQUIRED`, пока не выполнен отдельный multi-source review.

## 6. Запрещённые сокращения

```text
ONE_EDGE == ROOT_CAUSE          # запрещено
LONG_HISTORY == INEVITABILITY  # запрещено
RESOURCE_LINK == MOTIVE        # запрещено
SECURITY_LINK == AGGRESSION_CAUSE # запрещено
COLONIAL_LEGACY == COMPLETE_EXPLANATION # запрещено
```

## 7. Направление графа

Ребро направлено `from_node_id -> to_node_id` и означает только заявленное отношение в поле `edge_type`.

Направление не обязано совпадать с простой хронологией: исторический институт может продолжать ограничивать более поздний процесс, но связь должна быть описана механизмом, а не словом «влиял» без расшифровки.

## 8. Связь с Resource Sustainment Layer

Позже допускаются cross-layer edges:

```text
HISTORICAL_NODE -> RESOURCE_FLOW
RESOURCE_STRUCTURE -> HISTORICAL_CONFLICT_NODE
```

Но такие ребра должны иметь отдельный namespace и не смешиваться с historical-only CSV до появления стабильных resource node IDs.

## 9. Правило ревью

Для каждого ребра reviewer обязан спросить:

1. Что именно передаётся от A к B?
2. Какой наблюдаемый механизм связывает узлы?
3. Может ли B возникнуть без A?
4. Есть ли альтернативное объяснение?
5. Есть ли контрпример или период, когда A существовал, но B не наступал?
6. Не является ли связь просто хронологической близостью?

## 10. Назначение

Граф нужен не для построения единственного нарратива, а для хранения конкурирующих причинных гипотез и проверки того, какие механизмы повторяются в разных исторических кейсах.
