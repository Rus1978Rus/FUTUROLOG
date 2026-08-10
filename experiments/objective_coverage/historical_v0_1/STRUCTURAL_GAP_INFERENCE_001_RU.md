# STRUCTURAL_GAP_INFERENCE 001

**Статус:** `CONCEPTUAL_METHOD / SEARCH_TRIGGER_ONLY / NOT_RUNTIME_INFERENCE / NOT_PROOF_OF_HIDDEN_CAUSE`

## 1. Назначение

Этот механизм предназначен для обнаружения возможных недостающих элементов модели, когда несколько хорошо поддержанных наблюдений нельзя непротиворечиво объяснить текущей структурой FUTUROLOG.

Он не разрешает системе придумывать скрытую причину. Он разрешает только сформулировать проверяемую гипотезу о том, какого типа структура может отсутствовать, и породить целевой поиск различающих свидетельств.

## 2. Базовая цепочка

```text
KNOWN_FACT_A
+ KNOWN_FACT_B
+ KNOWN_FACT_C
+ CURRENT_MODEL
→ UNEXPLAINED_RESIDUAL / CONTRADICTION
→ MISSING_STRUCTURE_HYPOTHESIS_SET
→ DISCRIMINATING_EVIDENCE_PLAN
→ SEARCH / TEST
→ UPDATE_OR_REJECT
```

## 3. Жёсткие guards

```text
CONTRADICTION != ERROR_IN_REALITY
MODEL_RESIDUAL != PROOF_OF_HIDDEN_FACTOR
MISSING_FACTOR_HYPOTHESIS != OBSERVED_FACT
UNEXPLAINED_BEHAVIOR != ACTOR_IRRATIONALITY
INFERENCE MUST GENERATE A TESTABLE SEARCH TARGET
HYPOTHESIS_GENERATION != EVIDENCE
BEST_FIT != TRUTH
UNOBSERVED != NONEXISTENT
```

## 4. Типы residual

### R1 LOGICAL_INCONSISTENCY
Наблюдения и текущая модель требуют несовместимых выводов.

### R2 PERSISTENT_BEHAVIORAL_RESIDUAL
Поведение актора устойчиво отклоняется от того, что объясняет текущий набор факторов.

### R3 MISSING_LINK
Наблюдается A и затем C, но механизм перехода A→C отсутствует или не подтверждён.

### R4 SCALE_MISMATCH
Модель объясняет локальный эффект, но наблюдается иной масштаб — или наоборот.

### R5 TIMING_MISMATCH
Направление явления объяснимо, но его время/скорость не согласуются с моделью.

### R6 SIGN_MISMATCH
Модель ожидает стабилизацию, а наблюдается усиление давления, либо наоборот.

### R7 OBSERVABILITY_RESIDUAL
Противоречие может быть вызвано не скрытым механизмом, а дырой наблюдаемости, access failure, reporting bias или sensor collapse.

## 5. Иерархия проверки до hidden-factor hypothesis

Перед созданием гипотезы о скрытом факторе система обязана проверить более простые причины:

```text
1 DATA_ERROR?
2 CUTOFF_LEAKAGE?
3 DUPLICATE / NON_INDEPENDENT SOURCES?
4 OBSERVATION_GAP?
5 WRONG_SCALE OR WRONG_DENOMINATOR?
6 WRONG ACTOR / GROUP AGGREGATION?
7 TEMPORAL LAG?
8 KNOWN STABILIZER / PRESSURE OMITTED?
9 ONLY THEN: MISSING_STRUCTURE_HYPOTHESIS
```

## 6. Формат missing-structure hypothesis

Каждая гипотеза хранится как:

```text
hypothesis_id
residual_id
hypothesized_missing_factor_class
status = INFERRED_MISSING_FACTOR / NOT_OBSERVED
what_it_would_explain
what_it_does_not_explain
alternative_hypotheses
required_discriminating_evidence
possible_observation_bias_explanation
falsification_condition
confidence = LOW | MEDIUM | HIGH
```

По умолчанию confidence не может быть HIGH только из-за красивого fit.

## 7. Пример для actor force signaling

Наблюдение:

```text
HIGH_COST_PREPARATION
+ LARGE_EXPECTED_EXTERNAL_COSTS
+ DIPLOMATIC_OFFRAMPS_EXIST
+ ACTOR_CONTINUES_PREPARATION
```

Недопустимый вывод:

```text
ACTOR_IS_IRRATIONAL
```

Разрешённый hypothesis set:

```text
H1 domestic political cost of retreat is high
H2 leadership objective is non-economic / ideological
H3 actor estimates opponent resistance as low
H4 actor discounts sanctions/costs
H5 private commitment or internal deadline exists
H6 public data overstates true expected costs
H7 observed preparation has another purpose
```

Ни одна H не считается фактом.

Затем создаётся discriminating-evidence plan: какие наблюдения различат H1–H7.

## 8. Discriminating evidence principle

Поиск должен быть устроен не как confirmation search.

```text
SEARCH_FOR_WHAT_DISTINGUISHES_H1_FROM_H2_H3...
NOT SEARCH_ONLY_FOR_SUPPORT_OF_FAVORITE_HYPOTHESIS
```

Предпочтение получают свидетельства, которые:

- одновременно повышают одну гипотезу и понижают другую;
- доступны до cutoff;
- имеют независимое происхождение;
- не являются только риторикой;
- имеют явную provenance chain.

## 9. Residual ledger

FUTUROLOG должен хранить отдельный `RESIDUAL_LEDGER`, чтобы необъяснённые куски не исчезали после очередного пересказа.

Поля:

```text
residual_id
snapshot_id
observations_in_tension
model_component_in_tension
residual_type
severity = LOW | MEDIUM | HIGH
observability_check_status
hypothesis_set_status
search_plan_status
resolved_status
resolution_note
```

## 10. Связь с Observation & Coverage

Перед hidden inference обязательно проверяется:

```text
OBSERVABILITY_GAP_CAN_MIMIC_HIDDEN_CAUSE
```

Если система плохо видит закрытые мессенджеры, малые группы, неформальную экономику или удалённые регионы, residual сначала получает флаг `POSSIBLE_OBSERVATION_ARTIFACT`.

## 11. Связь с false-positive analogues

Гипотеза считается сильнее только если помогает объяснять различие между похожими кризисами, а не только один известный исход.

Например, скрытый фактор, придуманный для Russia–Ukraine, должен быть проверен на India–Pakistan и Greece–Turkey analogues. Если он одинаково "объясняет" всё задним числом, его discriminating value низок.

```text
EXPLAINS_ONE_CASE_POST_HOC != DISCRIMINATING_MECHANISM
```

## 12. Что этот механизм НЕ делает

- не читает мысли акторов;
- не превращает отсутствие данных в доказательство тайного плана;
- не создаёт causal fact без evidence;
- не заменяет OSINT;
- не позволяет LLM скрытно заполнять пробелы;
- не разрешает числовой вклад inferred factor в EvidenceState без отдельного validation gate.

## 13. Gate до runtime

Перед реализацией нужны:

```text
1 residual taxonomy review
2 blind test on historical cases
3 false-positive analogue test
4 hallucination/adversarial test
5 provenance schema for hypotheses
6 explicit hypothesis-expiry rule
7 human-review path for HIGH-severity residuals
```

## 14. Статус

```text
STRUCTURAL_GAP_INFERENCE_001_CREATED
SEARCH_TRIGGER_ONLY
HIDDEN_FACTOR_NOT_EQUAL_FACT
NUMERIC_USE_BLOCKED
READY_FOR_HISTORICAL_RESIDUAL_PILOT
```
