# OBJECTIVE_COVERAGE_DESIGN v0.1
## Проект нового слоя Objective / Coverage для универсального FUTUROLOG

**Статус:** `DESIGN_DRAFT / PRE-IMPLEMENTATION / NOT_VALIDATED`

Цель — исправить слабое место старого Objective Risk: высокий результат не должен возникать только потому, что система увидела малую часть данных и пересчитала веса по доступным компонентам.

## Главный инвариант

```text
HIGH_MEASURED_SCORE + LOW_COVERAGE
!=
HIGH_EFFECTIVE_CONFIDENCE
```

## Разделяем то, что раньше смешивалось

Новый слой должен выдавать минимум семь независимых величин:

```text
measured_score
evidence_coverage
source_independence
freshness
pipeline_completeness
observed_noise
effective_confidence
```

- `measured_score` — что показали реально доступные измерения.
- `evidence_coverage` — какую долю требуемой доказательной картины система реально наблюдает.
- `source_independence` — насколько подтверждения действительно независимы.
- `freshness` — насколько данные свежи относительно задачи.
- `pipeline_completeness` — прошёл ли сигнал обязательный маршрут обработки.
- `observed_noise` — насколько наблюдаемая картина нестабильна/шумна.
- `effective_confidence` — насколько уверенно система поддерживает текущий аналитический вывод с учётом ограниченности наблюдения.

## Missing data policy

Запрещено:

```text
missing component
→ удалить его
→ перенормировать веса оставшихся
→ выдать score как будто покрытие полное
```

Разрешено отдельно показывать:

```text
measured_score = результат по реально измеренным компонентам
coverage       = доля доступной необходимой информации
```

Инварианты:

```text
NO_DATA != NEGATIVE_EVIDENCE
NO_DATA != NO_RISK
```

## Минимальный контракт компонента

Для каждого компонента `i`:

```text
value_i
quality_i
availability_i
freshness_i
independence_group_i
pipeline_ok_i
noise_i
```

Точная формула объединения на v0.1 намеренно не фиксируется.

## Семейства формул для сравнительного прогона

Нужно сравнить минимум три семейства:

1. **Linear with explicit coverage** — линейное взвешивание с отдельным штрафом за покрытие.
2. **Weighted geometric mean** — геометрическое объединение, сильнее наказывающее слабые компоненты.
3. **Hybrid / min-cap** — обычный основной score с верхним ограничителем по критически низкому coverage/freshness/pipeline completeness.

Финальная формула выбирается только после одинакового тестового прогона.

## Заимствования из доноров

- **ACDM-KERNEL:** observability horizon (горизонт наблюдаемости), нейтральные signal/score contracts, явная деградация при потере наблюдаемости. Не переносить буквально правило «один старый сигнал → confidence=0».
- **Notarius:** provenance (происхождение), mandatory route (обязательный маршрут), missing-step detection (обнаружение пропущенного шага).
- **Vakhter:** ошибка компонента не должна превращаться в ложный `CLEAN`; сбой локализуется и явно снижает доверие.
- **Foundation Layer:** `CLAIM != PROOF`, `CONSENSUS != PROOF`, `TRACE != ACTOR`, наблюдаемое поведение важнее заявленного.
- **MSL/MIP:** pinned data versions (зафиксированные версии данных) и видимая деградация оси.
- **QuditEngine / CONVEYOR:** пререгистрация, воспроизводимость, сохранение отрицательных результатов, `PROPOSED_FORMULA != ACCEPTED_FORMULA`.

## Предлагаемый выход API

```json
{
  "measured_score": 0.78,
  "evidence_coverage": 0.46,
  "source_independence": 0.61,
  "freshness": 0.88,
  "pipeline_completeness": 0.92,
  "observed_noise": 0.24,
  "effective_confidence": 0.41,
  "status": "DEGRADED_EVIDENCE",
  "missing_components": ["observer_agreement", "source_redundancy"],
  "degraded_components": ["temporal_persistence"],
  "reasons": []
}
```

Числа здесь только пример структуры, не утверждённые пороги.

## Минимальные статусы

```text
FULL_EVIDENCE
PARTIAL_EVIDENCE
DEGRADED_EVIDENCE
INSUFFICIENT_EVIDENCE
UNVERIFIABLE_COMPONENT
PIPELINE_INCOMPLETE
STALE_EVIDENCE
```

## Boundary tests (граничные тесты)

1. Один идеальный компонент из пяти: measured высокий, effective confidence не высокий.
2. Пять средних независимых компонентов: coverage высокий, confidence зависит от качества.
3. Десять копий одного источника: source count высокий, source independence низкий.
4. Свежие данные + один старый компонент: старость локализована, вся система не обнуляется автоматически.
5. Пропущен обязательный pipeline step: completeness падает, причина видима.
6. Модуль упал: не `PASS` и не искусственный ноль, а `UNKNOWN/DEGRADED`.
7. Полный coverage, но сильный шум: confidence ограничена шумом.
8. Низкий coverage, но очень сильный сигнал: допустим `EARLY_SIGNAL`, но не `HIGH_CONFIDENCE_FACT`.

## Два разных результата

FUTUROLOG должен различать:

```text
SIGNAL_STRENGTH
EVIDENCE_CONFIDENCE
```

Состояние `signal_strength = HIGH` и `evidence_confidence = LOW` допустимо и важно для раннего предупреждения.

## Семантическая граница

```text
CONFIDENCE_IN_ANALYSIS
!=
PROBABILITY_OF_FUTURE_EVENT
```

`effective_confidence` — это уверенность в аналитическом выводе на основании наблюдаемой доказательной картины. Это не автоматически вероятность будущего события.

## Решение v0.1

Фиксируется архитектурное разделение:

```text
MEASURED
COVERAGE
INDEPENDENCE
FRESHNESS
PIPELINE
NOISE
CONFIDENCE
```

Статус:

```text
DESIGN_ACCEPTABLE_FOR_COMPARATIVE_PROTOTYPING
NOT_IMPLEMENTED
NOT_CALIBRATED
NOT_VALIDATED
```

Следующий шаг: `OBJECTIVE_COVERAGE_FORMULA_BAKEOFF_v0_1` — реализовать несколько семейства формул, прогнать одинаковые synthetic boundary fixtures (синтетические граничные примеры), сохранить провальные варианты и выбрать только кандидата для дальнейшей исторической оценки.
