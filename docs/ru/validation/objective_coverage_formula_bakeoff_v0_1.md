# OBJECTIVE_COVERAGE_FORMULA_BAKEOFF v0.1
## Сравнительный эксперимент формул Objective / Coverage

**Статус:** `EXPERIMENTAL / NOT_CALIBRATED / NOT_VALIDATED / NO_PRODUCTION_FORMULA_SELECTED`

Цель — отсеять варианты, которые плохо ведут себя на заранее заданных граничных случаях. Это не доказательство финальной формулы.

## Кандидаты

- **A_LINEAR_COVERAGE** — `measured × coverage × arithmetic_quality`.
- **B_GEOMETRIC** — `measured × geometric_mean(coverage, independence, freshness, pipeline, low_noise)`.
- **C_HYBRID_MIN_CAP** — quality × `sqrt(coverage × pipeline)` с временным потолком по слабейшему из `coverage / independence / pipeline`.

Все коэффициенты и потолок C — **экспериментальные, не откалиброванные**.

## Результаты 8 boundary fixtures (граничных сценариев)

| Fixture | A_LINEAR_COVERAGE | B_GEOMETRIC | C_HYBRID_MIN_CAP |
|---|---:|---:|---:|
| T1_ONE_STRONG_COMPONENT_LOW_COVERAGE | 0.172 PASS | 0.631 FAIL | 0.320 PASS |
| T2_FULL_MULTI_COMPONENT | 0.620 PASS | 0.627 PASS | 0.620 PASS |
| T3_MANY_COPIES_ONE_SOURCE | 0.601 FAIL | 0.539 FAIL | 0.235 PASS |
| T4_MIXED_FRESHNESS | 0.499 PASS | 0.586 PASS | 0.527 PASS |
| T5_MANDATORY_PIPELINE_STEP_MISSING | 0.490 FAIL | 0.000 PASS | 0.000 PASS |
| T6_COMPONENT_FAILURE_DEGRADED | 0.394 PASS | 0.589 PASS | 0.409 PASS |
| T7_FULL_COVERAGE_HIGH_NOISE | 0.633 PASS | 0.502 PASS | 0.633 PASS |
| T8_STRONG_EARLY_SIGNAL_LOW_COVERAGE | 0.221 PASS | 0.682 FAIL | 0.362 PASS |

Итог:
- A: **6/8**
- B: **5/8**
- C: **8/8**

## Проверка монотонности

5000 случайных состояний, `seed=42`.

Нарушения:
- A: `0`
- B: `0`
- C: `0`

Все три кандидата прошли проверку монотонности.

## Интерпретация

**A** — хороший простой baseline (базовый кандидат). Низкое coverage явно штрафует confidence, но арифметическая quality допускает компенсацию слабых компонентов сильными.

**B** — конъюнктивнее обычной линейной свёртки, но на тестах низкого coverage / independence может оставлять confidence выше желаемой.

**C** — лучше всего соблюдает наш защитный принцип на синтетических тестах, потому что слабый критический компонент ограничивает потолок confidence. Но сам cap пока является инженерной гипотезой.

## Решение v0.1

```text
A_LINEAR_COVERAGE:
    KEEP_AS_BASELINE_CANDIDATE

B_GEOMETRIC:
    KEEP_FOR_COMPARISON

C_HYBRID_MIN_CAP:
    PROMOTE_TO_HISTORICAL_EVALUATION_CANDIDATE
    NOT_ACCEPTED_AS_FINAL
```

Инварианты:

```text
SYNTHETIC_PASS != REAL_WORLD_VALIDATION
BEST_IN_BAKEOFF != FINAL_FORMULA
CONFIDENCE_IN_ANALYSIS != PROBABILITY_OF_FUTURE_EVENT
```

## Следующий gate (этап допуска)

`OBJECTIVE_COVERAGE_HISTORICAL_EVALUATION_v0_1`

Там формулы и коэффициенты должны быть заморожены до просмотра будущего участка данных. Только историческая проверка может решить, какой кандидат продолжает путь.
