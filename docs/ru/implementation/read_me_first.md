# READ ME FIRST FOR DEVELOPER

Это handoff-pack проекта «Футуролог» для инженерной реализации Entropy-RG / Objective Layer.

## Статус

- Paper architecture: complete.
- Engineering implementation: not complete.
- Calibration status: `uncalibrated`.
- Default rollout: `objective_layer_enabled=false`.

## Главное правило

Не начинать с M3. Сначала реализовать M1 полностью и добиться зелёных тестов.

## Порядок работы

1. Открыть исходный архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` у автора проекта.
2. Сверить фактическую структуру кода с `patches_M1/M1.1_migration_plan_v3_0.md`.
3. Реализовать M1.2.
4. Прогнать тесты и regression baseline.
5. Прислать diff на ревью.
6. Не переходить к M1.3 до принятия M1.2.
7. После закрытия M1 переходить к M3.1 → M3.6.2 строго по порядку.

## Нельзя

- Нельзя менять формулы «по дороге».
- Нельзя решать `[OPEN_QUESTION]` самостоятельно.
- Нельзя игнорировать `[REQUIRES_VERIFICATION]`.
- Нельзя активировать Objective Layer без config flag.
- Нельзя считать `final_score` вероятностью события.

## Главный invariant

```text
trust_adjustment вычитается ровно один раз.
```

Правильная формула после M3.6.1:

```text
final_score =
    universal_raw × (alpha + (1 - alpha) × objective_risk_or_1)
    - gamma × trust_adjustment
```

## Safe rollout

По умолчанию:

```text
objective_layer_enabled = false
```

Это означает:

```text
objective_layer_active = false
alpha_active = false
final_score = universal_risk
```
