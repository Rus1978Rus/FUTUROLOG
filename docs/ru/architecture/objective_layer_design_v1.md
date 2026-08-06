# Objective Layer Design v1

# Дизайн-документ Objective Layer для Entropy-RG

Статус: M3.0, рамочный дизайн до реализации компонент  
Проект: «Футуролог»  
Пакет: Entropy-RG v3.x  
Основание: `futurolog_architecture_v1.1.md`, `canonical_scoring_mapping_v1.md`, ERG-CAD, M1.1–M1.5  
Цель: спроектировать Objective Layer как единый слой до проектирования отдельных компонент M3.1–M3.5

## 1. Сводка и цель документа

Objective Layer — второй слой scoring-модели ERG-CAD, отвечающий не за интенсивность риска, а за устойчивость и проверяемость риск-сигнала. Universal Layer отвечает на вопрос «насколько сигнал рискованный или аномальный», Objective Layer отвечает на вопрос «насколько этот риск подтверждён временем, независимыми источниками, наблюдателями, масштабами и отделён от шума». Этот документ фиксирует интерфейсы, контекст, правила агрегации, поведение при missing/partial данных, стратегию тестирования и план M3.1–M3.6. Он не реализует формулы отдельных компонент, не задаёт числовые пороги и не меняет решения M1: `gamma = 0.07`, `alpha = 0.3` как metadata до активации слоя, dual output и `objective_risk = null` до M3.6.

## 2. Семантика и форма компонент

Каждая objective-компонента возвращает значение в диапазоне `[0, 1]`.

Семантика:

```text
1 = сигнал максимально объективен по этому измерению
0 = сигнал не подтверждён этим измерением
```

Это отличается от Universal Layer, где высокое значение означает высокую интенсивность риска. Objective Layer не усиливает риск сам по себе. Он проверяет, насколько риск-сигнал заслуживает доверия как устойчивый и проверяемый объект.

Общий шаблон функции:

```python
def compute_<component>(
    context: ObjectiveLayerContext,
) -> ObjectiveComponentResult:
    ...
```

Общая pydantic-like структура результата:

```python
class ObjectiveComponentResult:
    value: float  # in [0, 1]
    confidence: float  # in [0, 1], насколько компонента уверена в самой себе
    missing_inputs: list[str]  # каких входов не хватило для полноценного расчёта
    reasons: list[str]  # человекочитаемые объяснения
    partial: bool  # True, если расчёт выполнен с компромиссами
```

### 2.1 value

`value` — численное значение objective-компоненты.

Примеры интерпретации:

- `temporal_persistence.value = 0.9`: сигнал устойчиво сохранялся во временных окнах.
- `source_redundancy.value = 0.1`: сигнал поддержан почти не независимыми источниками.
- `scale_stability.value = 0.8`: риск стабилен при переходе между масштабами.

`value` всегда должен быть clipped в `[0, 1]`. Если компонента не может быть рассчитана вообще, она должна вернуть `None` на уровне aggregator или специальный result с `value = None` в реализации. В публичном дизайне M3.0 предпочтительно, чтобы compute-функции возвращали `ObjectiveComponentResult | None`, где `None` означает missing component.

### 2.2 confidence

`confidence` — не то же самое, что `value`.

`value` отвечает:

```text
Насколько сигнал объективен по данному измерению?
```

`confidence` отвечает:

```text
Насколько сама компонента уверена в своём расчёте при имеющихся данных?
```

Пример:

```text
source_redundancy.value = 0.8
source_redundancy.confidence = 0.3
```

Это означает: доступные источники выглядят независимыми, но данных мало, source registry неполный или часть источников имеет unknown status.

Другой пример:

```text
temporal_persistence.value = 0.2
temporal_persistence.confidence = 0.9
```

Это означает: история достаточно длинная, и компонент уверенно видит, что сигнал не сохраняется во времени.

Разделение `value` и `confidence` нужно, чтобы не смешивать качество сигнала с качеством измерения. Низкий `value` может быть уверенным результатом, а высокий `value` может быть слабым предположением.

### 2.3 missing_inputs

`missing_inputs` перечисляет данные, которых не хватило для полноценного расчёта.

Примеры:

```python
missing_inputs = ["score_history"]
missing_inputs = ["source_registry.independence_graph"]
missing_inputs = ["scale_aggregates.levels[community]"]
missing_inputs = ["noise_baseline.sample_size"]
```

Если входы частично отсутствуют, компонент может всё равно вернуть `value`, но должен:

- снизить `confidence`;
- добавить `missing_inputs`;
- поставить `partial = True`;
- добавить reason.

Пример:

```python
ObjectiveComponentResult(
    value=0.55,
    confidence=0.4,
    missing_inputs=["source_registry.independence_graph"],
    reasons=[
        "source_redundancy_estimated_from_unique_source_count",
        "independence_graph_missing",
    ],
    partial=True,
)
```

### 2.4 reasons

`reasons` — человекочитаемые и/или machine-readable объяснения.

Рекомендация:

- reason code должен быть коротким и стабильным;
- человекочитаемый текст может генерироваться отдельно в `app/explanations.py`;
- reason code не должен содержать случайные значения;
- reason code должен помогать audit и dashboard.

Примеры:

```python
"temporal_persistence_high_across_windows"
"observer_agreement_low_detector_conflict"
"source_redundancy_single_origin_cascade"
"noise_separation_close_to_noise_baseline"
"scale_stability_missing_global_level"
```

### 2.5 partial

`partial` — отдельное поле, а не просто `confidence < 1`, потому что оно отвечает на другой вопрос.

`confidence` является числом. `partial` является флагом режима расчёта.

Пример:

```text
partial = True
confidence = 0.8
```

Это возможно, если компонент использовал fallback-алгоритм, но fallback хорошо применим к текущему кейсу.

Пример:

```text
partial = False
confidence = 0.6
```

Это возможно, если все нужные входы есть, но данные сами по себе шумные или малочисленные.

`partial` нужен для response-level флага:

```text
objective_layer_partial = true
```

Если хотя бы одна активная компонента partial, весь слой должен явно показывать ограничение результата.

## 3. ObjectiveLayerContext — расширение ScoringInput

Objective Layer не делает I/O и не обращается к state_store. ENRA собирает весь контекст и передаёт его в Entropy-RG за один вызов. Это push-модель.

Текущий M1 ScoringInput расширяется до `ObjectiveLayerContext`.

```python
class ObjectiveLayerContext:
    # унаследовано от M1 ScoringInput
    event_id: str
    actor_id: str | None
    topic_id: str
    timestamp: str
    features: dict
    history_window: dict
    graph_context: dict
    baseline_context: dict

    # новые поля M3
    score_history: list[ScoreHistoryPoint]
    observer_results: list[ObserverResult]
    source_registry: SourceRegistrySnapshot
    noise_baseline: NoiseBaselineSnapshot
    scale_aggregates: ScaleAggregatesSnapshot
```

### 3.1 score_history

Используется компонентой:

```text
temporal_persistence
```

Структура:

```python
class ScoreHistoryPoint:
    timestamp: str
    universal_risk: float
    window: str  # "1h", "1d", "1w" или другой aggregation level
    decay_applied: bool
```

Семантика:

- `timestamp`: время расчёта или конец окна.
- `universal_risk`: universal score на этом окне.
- `window`: агрегационный уровень.
- `decay_applied`: был ли применён decay к старым наблюдениям.

Минимальные требования:

- список может быть пустым;
- порядок элементов не должен влиять на итог после сортировки по timestamp;
- компонент temporal_persistence обязан корректно обрабатывать длину 0 и 1.

Пример:

```python
score_history = [
    ScoreHistoryPoint(
        timestamp="2026-05-01T10:00:00Z",
        universal_risk=0.62,
        window="1h",
        decay_applied=True,
    ),
    ScoreHistoryPoint(
        timestamp="2026-05-01T11:00:00Z",
        universal_risk=0.66,
        window="1h",
        decay_applied=True,
    ),
]
```

### 3.2 observer_results

Используется компонентой:

```text
observer_agreement
```

Структура:

```python
class ObserverResult:
    observer_id: str
    observer_type: str  # "rule_detector", "graph_detector",
                        # "sequence_detector", "baseline_detector",
                        # "human_review"
    flagged: bool
    confidence: float
    timestamp: str
```

Семантика:

- `observer_id`: стабильный идентификатор наблюдателя/детектора.
- `observer_type`: тип наблюдателя.
- `flagged`: считает ли observer, что сигнал значим.
- `confidence`: уверенность observer в собственном выводе.
- `timestamp`: время вывода.

В M3 MVP observer может быть простым детектором, а не ML-моделью.

Пример observer set:

```python
observer_results = [
    ObserverResult(
        observer_id="rule_detector_v1",
        observer_type="rule_detector",
        flagged=True,
        confidence=0.7,
        timestamp="2026-05-01T10:00:00Z",
    ),
    ObserverResult(
        observer_id="graph_detector_v1",
        observer_type="graph_detector",
        flagged=False,
        confidence=0.6,
        timestamp="2026-05-01T10:00:00Z",
    ),
]
```

### 3.3 source_registry

Используется компонентой:

```text
source_redundancy
```

Структуры:

```python
class SourceRegistrySnapshot:
    sources: list[SourceMetadata]
    independence_graph: dict  # source_id -> list of correlated source_ids
    claim_clusters: dict  # claim_hash -> list of source_ids
```

```python
class SourceMetadata:
    source_id: str
    reliability_score: float
    first_seen: str
    original_or_derivative: str  # "original" / "derivative" / "unknown"
```

Семантика:

- `sources`: список источников, связанных с текущим сигналом.
- `independence_graph`: граф зависимостей источников.
- `claim_clusters`: группировка claim по hash/semantic cluster.
- `original_or_derivative`: признак первичности или производности источника.

Важно: большое количество источников не равно независимости. Если 30 источников перепечатали один первоисточник, redundancy должна быть низкой.

Минимальная структура для MVP может содержать только `sources` и пустой `independence_graph`, но в этом случае component result должен быть `partial=True`.

### 3.4 noise_baseline

Используется компонентой:

```text
noise_separation
```

Структура:

```python
class NoiseBaselineSnapshot:
    noise_score_distribution: dict  # quantiles или histogram
    sample_size: int
    window: str
```

Семантика:

- `noise_score_distribution`: baseline-распределение шумовых событий.
- `sample_size`: число наблюдений в baseline.
- `window`: период, на котором baseline собран.

Пример:

```python
noise_baseline = NoiseBaselineSnapshot(
    noise_score_distribution={
        "p50": 0.21,
        "p75": 0.33,
        "p90": 0.48,
        "p95": 0.57,
    },
    sample_size=5000,
    window="30d",
)
```

В M3.0 не задаётся конкретная формула separation. Компонента M3.4 должна использовать эту структуру, не делая I/O.

### 3.5 scale_aggregates

Используется компонентой:

```text
scale_stability
```

Структуры:

```python
class ScaleAggregatesSnapshot:
    levels: list[ScaleLevel]
```

```python
class ScaleLevel:
    level_name: str  # "event", "actor", "topic", "macro_topic",
                     # "community", "global"
    aggregated_risk: float
    sample_count: int
```

Семантика:

- `level_name`: масштаб.
- `aggregated_risk`: риск, агрегированный на этом уровне.
- `sample_count`: сколько наблюдений вошло в агрегат.

Пример:

```python
scale_aggregates = ScaleAggregatesSnapshot(
    levels=[
        ScaleLevel(level_name="event", aggregated_risk=0.74, sample_count=1),
        ScaleLevel(level_name="actor", aggregated_risk=0.70, sample_count=14),
        ScaleLevel(level_name="topic", aggregated_risk=0.68, sample_count=120),
        ScaleLevel(level_name="community", aggregated_risk=0.66, sample_count=800),
    ]
)
```

Scale stability должна корректно обрабатывать отсутствие некоторых уровней и малые `sample_count`.

## 4. Интеграция компонент в objective_risk

Objective Risk Score вычисляется как взвешенная сумма пяти компонент:

```text
objective_risk =
    0.25 * scale_stability.value
  + 0.20 * temporal_persistence.value
  + 0.20 * source_redundancy.value
  + 0.20 * observer_agreement.value
  + 0.15 * noise_separation.value
```

Веса:

| Компонента | Вес |
|---|---:|
| `scale_stability` | 0.25 |
| `temporal_persistence` | 0.20 |
| `source_redundancy` | 0.20 |
| `observer_agreement` | 0.20 |
| `noise_separation` | 0.15 |

Confluence bonus к `objective_risk` не применяется. Объективность трактуется как линейная свёртка независимых измерений.

### 4.1 Objective layer result

Рекомендуемая структура результата слоя:

```python
class ObjectiveLayerResult:
    objective_component_scores: dict[str, ObjectiveComponentResult]
    objective_risk: float | None
    objective_layer_active: bool
    objective_layer_partial: bool
    missing_components: list[str]
    active_components: list[str]
    normalized_weights: dict[str, float]
    reasons: list[str]
```

### 4.2 Поведение при missing компонентах

Компонента считается missing, если:

- функция вернула `None`;
- нет ключевых входов;
- компонент явно `not_implemented`;
- result имеет `value = None`;
- result не прошёл валидацию диапазона `[0, 1]`.

Если компонента missing, её вес временно перераспределяется на оставшиеся компоненты пропорционально их исходным весам.

Алгоритм:

```python
BASE_OBJECTIVE_WEIGHTS = {
    "scale_stability": 0.25,
    "temporal_persistence": 0.20,
    "source_redundancy": 0.20,
    "observer_agreement": 0.20,
    "noise_separation": 0.15,
}


def normalize_available_weights(
    available_components: list[str],
) -> dict[str, float]:
    total = sum(BASE_OBJECTIVE_WEIGHTS[name] for name in available_components)
    if total == 0:
        return {}
    return {
        name: BASE_OBJECTIVE_WEIGHTS[name] / total
        for name in available_components
    }
```

Если все компоненты missing:

```text
objective_risk = None
objective_layer_active = false
objective_layer_partial = true
```

Даже если слой был включён конфигурационно, он должен безопасно деактивироваться на конкретном response, если нет данных.

Если хотя бы одна компонента partial:

```text
objective_layer_partial = true
```

Если все активные компоненты full:

```text
objective_layer_partial = false
```

### 4.3 Пример нормализации весов

#### Пример 1: отсутствует scale_stability

Доступны:

- temporal_persistence: base 0.20;
- source_redundancy: base 0.20;
- observer_agreement: base 0.20;
- noise_separation: base 0.15.

Сумма доступных весов:

```text
0.20 + 0.20 + 0.20 + 0.15 = 0.75
```

Нормализованные веса:

```text
temporal_persistence = 0.20 / 0.75 = 0.2667
source_redundancy = 0.20 / 0.75 = 0.2667
observer_agreement = 0.20 / 0.75 = 0.2667
noise_separation = 0.15 / 0.75 = 0.2000
```

Если значения:

```text
temporal_persistence.value = 0.7
source_redundancy.value = 0.5
observer_agreement.value = 0.6
noise_separation.value = 0.4
```

то:

```text
objective_risk =
    0.2667 * 0.7
  + 0.2667 * 0.5
  + 0.2667 * 0.6
  + 0.2000 * 0.4
  = 0.56 примерно
```

#### Пример 2: доступны только temporal_persistence и observer_agreement

Сумма доступных весов:

```text
0.20 + 0.20 = 0.40
```

Нормализованные веса:

```text
temporal_persistence = 0.5
observer_agreement = 0.5
```

Если оба результата partial, слой может вернуть `objective_risk`, но response должен содержать:

```text
objective_layer_partial = true
missing_components = ["scale_stability", "source_redundancy", "noise_separation"]
```

#### Пример 3: отсутствуют все компоненты

```text
available_components = []
normalized_weights = {}
objective_risk = None
objective_layer_active = false
objective_layer_partial = true
```

Финальная формула должна перейти в fallback без Objective Layer.

### 4.4 Confidence на уровне слоя

M3.0 не фиксирует обязательную формулу layer confidence, но рекомендует добавить поле в M3.6:

```python
objective_confidence: float
```

Возможная будущая логика:

```text
objective_confidence = weighted average of component confidence
```

[OPEN_QUESTION] Нужен ли `objective_confidence` уже в M3.1, или достаточно confidence на уровне компонент до M3.6?

## 5. Финальная формула после активации

Формула, которая активируется в M3.6:

```text
final_score =
    universal_risk × (alpha + (1 - alpha) × objective_risk)
    - gamma × trust_adjustment
```

Значения из M1:

```text
alpha = 0.3
gamma = 0.07
```

До M3.6:

```text
objective_layer_active = false
alpha_active = false
objective_risk = None
```

### 5.1 Поведение при неактивном Objective Layer

Если:

```text
objective_risk = None
```

или:

```text
objective_layer_active = false
```

то:

```text
final_score = universal_risk - gamma × trust_adjustment
```

Это соответствует M1.4 по смыслу, если `universal_risk` трактуется как риск до применения trust adjustment. Если в конкретной реализации M1.4 `universal_risk` уже включает вычитание `gamma × trust_adjustment`, то M3.6 должен сначала нормализовать терминологию, чтобы не вычесть trust adjustment дважды. [REQUIRES_VERIFICATION]

Рекомендуемая M3 терминология:

```text
universal_raw = sum(weights × component_scores) + confluence_bonus
final_score_without_objective = universal_raw - gamma × trust_adjustment
```

[OPEN_QUESTION] Нужно ли в M3.6 переименовать M1.4 `universal_risk`, если он уже включает trust adjustment?

### 5.2 Поведение при активном Objective Layer

Если:

```text
objective_layer_active = true
objective_risk is not None
```

то:

```text
alpha_active = true
final_score =
    universal_risk × (alpha + (1 - alpha) × objective_risk)
    - gamma × trust_adjustment
```

`objective_risk` должен быть в `[0, 1]`.

### 5.3 Граничные случаи

#### objective_risk = 0

```text
final_score =
    universal_risk × alpha
    - gamma × trust_adjustment
```

При `alpha = 0.3` это означает: Universal signal не исчезает полностью, но остаётся только минимальный corridor. Это защищает Hot Path от полного обнуления сигналов на раннем этапе.

#### objective_risk = 1

```text
final_score =
    universal_risk
    - gamma × trust_adjustment
```

Objective Layer полностью подтверждает риск. Эффект alpha исчезает.

#### alpha = 0

```text
final_score =
    universal_risk × objective_risk
    - gamma × trust_adjustment
```

Это строгая ERG-CAD-форма. Она подходит только после зрелой реализации Objective Layer и калибровки.

#### alpha = 1

```text
final_score =
    universal_risk
    - gamma × trust_adjustment
```

Objective Layer не влияет. Это degenerate mode, эквивалент fallback без objective множителя.

#### objective_risk missing при active=true

Если слой включён, но на конкретном response все компоненты missing:

```text
objective_risk = None
objective_layer_active = false
objective_layer_partial = true
alpha_active = false
final_score = universal_risk - gamma × trust_adjustment
```

Response должен содержать reason:

```text
"objective_layer_deactivated_all_components_missing"
```

## 6. Вспомогательные структуры

Главное правило M3.0:

```text
ObserverRegistry, SourceIndependenceGraph, NoiseBaseline, ScaleAggregator и ScoreHistory — зона ответственности ENRA, не Entropy-RG.
```

Entropy-RG получает snapshot-контекст и считает objective components. Он не знает, как этот контекст собран, не делает callbacks, не читает базы и не вызывает внешние сервисы.

### 6.1 ObserverRegistry

`ObserverRegistry` — сервис на стороне ENRA, который запускает независимые detectors и собирает результаты в `ObserverResult[]`.

MVP-набор:

- rule-based detector;
- graph-only detector;
- sequence-only detector;
- baseline-only detector;
- optional human_review later.

Entropy-RG получает:

```python
observer_results: list[ObserverResult]
```

Entropy-RG не запускает observers самостоятельно.

### 6.2 SourceIndependenceGraph

`SourceIndependenceGraph` хранится в SourceRegistry на стороне ENRA. Он описывает зависимость источников:

- кто кого цитирует;
- кто перепечатывает;
- какие источники принадлежат одному owner;
- какие источники часто синхронно публикуют один claim;
- какие источники считаются derivative.

Для MVP достаточно экспертного графа на 10–50 источников.

Entropy-RG получает snapshot:

```python
source_registry: SourceRegistrySnapshot
```

### 6.3 NoiseBaseline

`NoiseBaseline` хранится в state_store или offline artifact на стороне ENRA.

Содержит распределение universal scores для событий, считающихся шумом по rule-based heuristics:

- одиночные events;
- отсутствие upstream-сигналов;
- фоновый поток;
- events, не сохранившиеся во времени;
- events без независимых источников.

Entropy-RG получает:

```python
noise_baseline: NoiseBaselineSnapshot
```

NoiseBaseline обновляется offline. Entropy-RG не пересчитывает baseline во время scoring-вызова.

### 6.4 ScaleAggregator

`ScaleAggregator` — часть ENRA pipeline. Он считает aggregated risk на уровнях:

```text
event → actor → topic → macro_topic → community → global
```

Entropy-RG получает:

```python
scale_aggregates: ScaleAggregatesSnapshot
```

Entropy-RG не строит иерархию масштабов. Он только проверяет устойчивость переданных агрегатов.

### 6.5 ScoreHistory

`ScoreHistory` — часть state_store ENRA. Он хранит universal scores по:

- event_id;
- actor_id;
- topic_id;
- rolling windows;
- timestamps;
- decay status.

Entropy-RG получает:

```python
score_history: list[ScoreHistoryPoint]
```

Он не читает state_store напрямую.

## 7. Стратегия MVP реализации

Каждая компонента имеет три уровня реализации:

- `minimal`: простейшая формула или эвристика для smoke tests;
- `mvp`: рекомендуемая первая версия для M3.1–M3.5;
- `full`: целевой уровень после калибровки и накопления данных.

| Компонента | minimal | mvp | full |
|---|---|---|---|
| `temporal_persistence` | Доля окон, где universal score выше threshold | Rolling window + decay-aware persistence по нескольким окнам | Survival analysis / persistence modeling с domain-calibrated thresholds |
| `observer_agreement` | Majority vote по `flagged` | Weighted vote с reliability/confidence observer weights | Inter-rater agreement coefficient, calibration per observer type |
| `source_redundancy` | Count unique sources, capped/clipped | Count independent source clusters через independence graph и claim clusters | Bayesian belief propagation или графовая модель зависимости источников |
| `noise_separation` | Разница universal_risk и noise median | Separation margin относительно quantiles/histogram noise baseline | RiskGap-style model с calibrated noise-vs-signal distributions |
| `scale_stability` | Низкое std/variance across scale levels | Gradient между соседними уровнями + penalty за missing/low sample levels | Full scale-by-scale stability check с threshold η и scale hierarchy calibration |

M3.1–M3.5 должны реализовать MVP-уровень, не full-уровень.

### 7.1 Статусы реализации

Каждая компонента должна иметь статус:

```text
not_implemented
partial
ready
```

Слой активируется только когда минимум 3 из 5 компонент имеют статус не ниже `partial`.

До активации:

```text
objective_layer_active = false
alpha_active = false
```

После активации в M3.6:

```text
objective_layer_active = true
alpha_active = true
```

если минимум 3 компоненты доступны на конкретном request.

### 7.2 Response после частичной реализации

Даже до M3.6 компоненты могут возвращаться в response:

```json
{
  "objective_component_scores": {
    "temporal_persistence": {
      "value": 0.7,
      "confidence": 0.6,
      "missing_inputs": [],
      "reasons": ["temporal_persistence_present_in_3_windows"],
      "partial": true
    }
  },
  "objective_risk": null,
  "objective_layer_active": false,
  "alpha_active": false
}
```

Это позволяет тестировать компоненты без изменения final_score.

## 8. Тест-стратегия Objective Layer

У Objective Layer нет прямого ground truth на старте. Поэтому валидация строится через property-based tests, behavioral assertions и synthetic scenarios.

### 8.1 Монотонность

Если в контексте увеличить количество подтверждающих наблюдений, objective_risk не должен уменьшиться.

Примеры:

- больше observer_results с `flagged=True`;
- больше независимых source clusters;
- больше временных окон выше threshold;
- больше scale levels со стабильным risk;
- signal дальше от noise baseline.

Псевдотест:

```python
assert objective_risk(context_with_more_independent_sources) >= objective_risk(base_context)
```

### 8.2 Инвариантность к перестановкам

Перестановка элементов не должна менять результат:

- `observer_results`;
- `source_registry.sources`;
- `scale_aggregates.levels`;
- `score_history`, если функция сортирует по timestamp.

Псевдотест:

```python
assert compute_objective(context_a) == compute_objective(shuffled_context_a)
```

### 8.3 Граничные случаи

Обязательные cases:

| Case | Ожидание |
|---|---|
| Пустой `observer_results` | `observer_agreement.partial = true`, confidence низкая или component missing |
| Одиночный source | `source_redundancy.value` низкий |
| `score_history` длиной 1 | `temporal_persistence.partial = true` |
| Все `scale_aggregates` равны | `scale_stability.value` высокий |
| `noise_baseline.sample_size = 0` | `noise_separation` missing или partial |
| Все компоненты missing | `objective_risk = None`, `objective_layer_active = false` |
| Только 2 компоненты partial | Слой не активируется, если activation rule требует минимум 3 |
| 3 компоненты partial | Слой может активироваться в M3.6, но `objective_layer_partial = true` |

### 8.4 Synthetic scenarios

Эти 5 сценариев являются обязательным регрессионным набором для M3.1–M3.5.

#### Scenario 1: shadow signal

Описание: слабый или средний universal signal, но повторяется через несколько временных окон и поддержан независимыми источниками.

Ожидание:

```text
universal_risk = medium
objective_risk = high
temporal_persistence = high
source_redundancy = high
observer_agreement = medium/high
```

Цель: убедиться, что Objective Layer не пропускает слабый, но устойчивый сигнал.

#### Scenario 2: media wave

Описание: громкий информационный каскад из одного первоисточника. Много публикаций, но все происходят из одного claim/source cluster.

Ожидание:

```text
universal_risk = high
source_redundancy = low
noise_separation = medium/low
objective_risk = low/medium
```

Цель: отделить независимые подтверждения от перепечаток.

#### Scenario 3: noise spike

Описание: одиночный выброс без истории, без независимых источников, без подтверждения observers.

Ожидание:

```text
universal_risk = high
temporal_persistence = low
source_redundancy = low
observer_agreement = low
objective_risk = low
```

Цель: показать, что высокий universal risk сам по себе не равен объективному сигналу.

#### Scenario 4: stable trend

Описание: сигнал устойчив во времени, виден на нескольких масштабах, поддержан разными sources и observers.

Ожидание:

```text
universal_risk = high
objective_risk = high
scale_stability = high
temporal_persistence = high
source_redundancy = high
observer_agreement = high
noise_separation = high
```

Цель: эталонный positive case.

#### Scenario 5: isolated anomaly

Описание: сильное отклонение на одном уровне, но отсутствует на actor/topic/community/global scales.

Ожидание:

```text
universal_risk = high
scale_stability = low
objective_risk = low/medium
```

Цель: проверить, что Objective Layer снижает значимость непереносимого между масштабами сигнала.

### 8.5 Smoke-тесты

Обязательные smoke tests:

- objective component value всегда в `[0, 1]`;
- confidence всегда в `[0, 1]`;
- objective_risk всегда в `[0, 1]` или `None`;
- objective_risk не зависит напрямую от universal_risk, кроме компонент, которые явно получают score history или noise separation inputs;
- missing weights перераспределяются корректно;
- objective_layer_partial корректно отражает хотя бы одну partial-компоненту;
- objective_layer_active не включается при 0–2 доступных компонентах;
- order invariance выполняется для списков;
- пустые списки не приводят к exception;
- component results содержат reasons.

## 9. План M3.1–M3.6

### M3.1 temporal_persistence

Содержание:

- rolling-window score history;
- доля окон выше threshold;
- decay-aware логика;
- missing behavior для короткой истории;
- tests for monotonicity and history length.

Output:

```text
temporal_persistence: ObjectiveComponentResult
```

### M3.2 observer_agreement

Содержание:

- набор простых detectors;
- majority vote;
- weighted vote через observer confidence/reliability;
- support for human_review later;
- tests for permutation invariance.

Output:

```text
observer_agreement: ObjectiveComponentResult
```

### M3.3 source_redundancy

Содержание:

- source independence graph;
- claim clusters;
- count independent source clusters;
- low score for derivative cascades;
- tests for media wave scenario.

Output:

```text
source_redundancy: ObjectiveComponentResult
```

### M3.4 noise_separation

Содержание:

- noise baseline distribution;
- separation margin between signal and noise;
- missing/low sample behavior;
- tests for noise spike scenario.

Output:

```text
noise_separation: ObjectiveComponentResult
```

### M3.5 scale_stability

Содержание:

- scale aggregates;
- gradient between levels;
- stability threshold design;
- missing scale behavior;
- tests for isolated anomaly and stable trend.

Output:

```text
scale_stability: ObjectiveComponentResult
```

### M3.6 activation

Содержание:

- activation rule: at least 3 of 5 components partial or ready;
- `objective_layer_active = true`;
- `alpha_active = true`;
- full final score formula;
- M3 baseline JSONL;
- metadata update;
- response schema update;
- dashboard update.

Formula after activation:

```text
final_score =
    universal_risk × (alpha + (1 - alpha) × objective_risk)
    - gamma × trust_adjustment
```

## 10. Открытые вопросы для решения автора

1. Какие observer types входят в MVP M3.2?  
   Рекомендация: `rule_detector`, `graph_detector`, `sequence_detector`, `baseline_detector`. `human_review` добавить позже.

2. Кто выбирает первые 10–50 источников для SourceRegistry MVP?  
   Это продуктово-доменное решение. Разработчик не должен выбирать источники сам.

3. Что считать одним claim cluster в M3.3?  
   Возможные варианты: exact hash, semantic hash, normalized text similarity, ручная разметка. Требуется решение автора.

4. Где брать noise baseline на ранней стадии?  
   Варианты: synthetic baseline, historical weak/noise events, rule-based filtered stream. Требуется решение, потому что от этого зависит M3.4.

5. Оставлять ли `alpha = 0.3` при активации M3.6 или временно повысить alpha для мягкого старта?  
   Рекомендация M1: `alpha = 0.3`, но автор может изменить после первых synthetic tests.

6. Нужен ли `objective_confidence` на уровне всего слоя уже в M3.1–M3.5?  
   Сейчас confidence есть на уровне компонент. Layer-level confidence может быть полезен для dashboard, но усложнит API.

7. Какой минимум данных считать достаточным для activation rule?  
   Правило «3 из 5 компонент partial/ready» зафиксировано, но нужно решить, достаточно ли partial-компонент с низким confidence.

8. Должны ли partial-компоненты с `confidence < 0.3` участвовать в objective_risk?  
   Возможные варианты: участвуют с нормализованным весом, не участвуют, участвуют с confidence-weighted value. Требуется решение.

9. Как версионировать Objective Layer weights?  
   Нужно ли отдельное `objective_weights_version`, или достаточно общего `weights_version`?

10. Какие synthetic scenarios приоритетнее для футурологии: geopolitical, market, technology, social manipulation, climate/health?  
   Текущие 5 сценариев универсальны, но примеры данных должны быть доменными.

## 11. Ограничения M3.0

Этот документ не проектирует:

- внутренние формулы каждой компоненты;
- числовые thresholds;
- decay parameters;
- конкретные source lists;
- конкретные observer implementations;
- UI dashboard for Objective Layer;
- интеграцию с внешними источниками;
- Hash-chain;
- calibration pipeline;
- production monitoring.

Этот документ фиксирует только:

- интерфейс `ObjectiveComponentResult`;
- интерфейс `ObjectiveLayerContext`;
- правила aggregation;
- missing/partial behavior;
- final formula activation rules;
- ответственность ENRA vs Entropy-RG;
- MVP/full roadmap;
- тестовую стратегию.

## 12. Согласованность с M1

M3.0 не нарушает решения M1:

| Решение M1 | Статус в M3.0 |
|---|---|
| `gamma = 0.07` | сохраняется |
| `alpha = 0.3` | сохраняется как стартовое значение |
| dual output API | сохраняется |
| `objective_risk = null` до активации | сохраняется до M3.6 |
| `objective_layer_active = false` до активации | сохраняется до M3.6 |
| `alpha_active = false` до активации | сохраняется до M3.6 |
| `gibbs` и `surprise` не являются canonical ERG-CAD компонентами | сохраняется |
| Objective Layer не реализован в M1 | не меняется в M3.0 |
| Entropy-RG stateless относительно Objective Context | зафиксировано |

Research inspiration: RG-style coarse-graining и confinement-like язык остаются conceptual inspiration. M3.0 не использует Yang-Mills как физическое обоснование или зависимость реализации.
