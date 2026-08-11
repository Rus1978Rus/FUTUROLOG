# STRUCTURAL_GAP INFERENCE v0.5 — SEMANTICS PATCH

**Статус:** `PATCH_CANDIDATE / SYNTHETIC_NOVEL_RESIDUAL_TEST_SUPPORTED / NOT_REAL_WORLD_VALIDATED / NUMERIC_USE_BLOCKED`

## 1. Причина патча

`NOVEL_RESIDUAL_DISCRIMINATION_SET_001` показал сильное различение true residual vs no-gap controls, но выявил две семантические неоднозначности:

1. `known_explanations_exhausted` допускает противоположные трактовки.
2. `observation_status=SUFFICIENT` иногда сохраняется даже когда сам structural decision признан `NOT_ASSESSABLE` из-за measurement discontinuity.

## 2. Переименование поля

Удалить:

```text
known_explanations_exhausted
```

Ввести:

```text
unresolved_after_known_explanations = YES | NO | NOT_ASSESSABLE
```

Смысл:

```text
YES = известные релевантные объяснения проверены, но residual сохраняется
NO = residual отсутствует либо разрешен известным объяснением
NOT_ASSESSABLE = данных недостаточно, чтобы решить
```

Жёсткие инварианты:

```text
NO_GAP => unresolved_after_known_explanations = NO
PERSISTS_AFTER_CHECKS => unresolved_after_known_explanations = YES
observation_status = INCOMPLETE => unresolved_after_known_explanations = NOT_ASSESSABLE
```

## 3. Observation sufficiency rule

`SUFFICIENT` означает не "данных вообще много", а:

```text
SUFFICIENT_FOR_THIS_STRUCTURAL_DECISION
```

Поэтому:

```text
MEASUREMENT_DISCONTINUITY
+ NO_BRIDGE_CALIBRATION
+ STRUCTURAL_CONCLUSION_DEPENDS_ON_COMPARABILITY
=> observation_status = INCOMPLETE
=> structural_gap_status = NOT_ASSESSABLE
=> observation_recovery_search = YES
=> hidden_factor_search_allowed = NO
```

Нельзя одновременно кодировать:

```text
observation_status = SUFFICIENT
AND
residual_persistence = NOT_ASSESSABLE
```

если причиной `NOT_ASSESSABLE` является отсутствие диагностически необходимой сопоставимости данных.

## 4. Unknown outcome vs temporal lag

`UNKNOWN_OUTCOME` и `TEMPORAL_LAG` остаются разными, но могут сосуществовать.

Если механизм имеет заранее ожидаемое окно эффекта и это окно ещё не завершено:

```text
temporal_status = WITHIN_EXPECTED_LAG
outcome_status = UNKNOWN
structural_gap_status = NO_GAP
```

Для следующей schema рекомендуется отделить:

```text
pre_hidden_resolution
```

на две оси:

```text
resolution_class
observation_or_time_status
```

Но до отдельного schema redesign это не блокирует текущий метод.

## 5. True residual gate

Hidden-factor search допускается только если одновременно:

```text
observation_status = SUFFICIENT
residual_persistence = PERSISTS_AFTER_CHECKS
unresolved_after_known_explanations = YES
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY
```

И даже тогда:

```text
STRUCTURAL_GAP != IDENTIFIED_HIDDEN_CAUSE
HYPOTHESIS_CLASS = NOT_OBSERVED
```

## 6. Anti-suppression guard

После усиления observation guards запрещено превращать любую неожиданность в `NOT_ASSESSABLE`.

```text
SUFFICIENT_OBSERVATIONS
+ MODEL_EXPECTATION_EXPLICIT
+ BOUNDARY_CONDITIONS_CONFIRMED
+ LAG_CHECKED
+ DATA_CONTINUITY_CONFIRMED
+ KNOWN_EXPLANATIONS_FAIL
+ OBSERVED_CONTRADICTION_PERSISTS
=> STRUCTURAL_RESIDUAL_SEARCH_TRIGGER_ALLOWED
```

Это защищает от противоположной ошибки: чрезмерной осторожности, которая никогда не признаёт неполноту модели.

## 7. Текущий evidence status

На synthetic novel residual set:

```text
true residual cases recognized = 9/9 model-decisions
canonical no-gap false gap = 0/15
incomplete hidden-factor false trigger = 0/6
hidden-cause overclaim = 0/30
```

Это `SUPPORTED_IN_SYNTHETIC_STRESS_TEST`, не real-world validation.

## 8. Следующий gate

Перед runtime:

1. real historical blind residual cases without evaluator-explicit contradiction wording;
2. adversarial near-miss cases;
3. cases with multiple weak residuals rather than one clean contradiction;
4. provenance requirements for each residual check;
5. expiry/reopen logic for residuals;
6. aggregation interaction with EvidenceState;
7. human review for HIGH-severity open gaps.

## 9. Status

```text
STRUCTURAL_GAP_INFERENCE_V0_5_SEMANTICS_PATCH = READY
SYNTHETIC_DISCRIMINATION = STRONG_SIGNAL
REAL_WORLD_VALIDATION = NOT_CLAIMED
HIDDEN_FACTOR_PROOF = FORBIDDEN
NUMERIC_USE = BLOCKED
NEXT = REAL_HISTORICAL_RESIDUAL_BLIND_SET_001
```
