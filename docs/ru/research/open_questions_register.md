# OPEN QUESTIONS REGISTER

Эти пункты нельзя решать самостоятельно без автора/ревьюера.

| File | Line | Item |
|---|---:|---|
| `00_READ_ME_FIRST_FOR_DEVELOPER.md` | 29 | - Нельзя решать `[OPEN_QUESTION]` самостоятельно. |
| `architecture/objective_layer_design_v1.md` | 625 | [OPEN_QUESTION] Нужен ли `objective_confidence` уже в M3.1, или достаточно confidence на уровне компонент до M3.6? |
| `architecture/objective_layer_design_v1.md` | 681 | [OPEN_QUESTION] Нужно ли в M3.6 переименовать M1.4 `universal_risk`, если он уже включает trust adjustment? |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 54 | Все непокрытые имена добавить в отдельный список с пометкой `[OPEN_QUESTION]`. |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 656 | Да. Конвертер нужен, потому что нужно сохранить row count, значения строк, unknown columns и воспроизводимость миграции. Конвертер должен читать старые CSV, переименовывать известные колонки, сохранять неизвестные колонки, писать отчёт о `[OPEN_QUESTION]` колонках и делать backup. |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 910 | \| `domain_model` \| marketplace или отсутствует \| `domain-neutral` \| Опционально. [OPEN_QUESTION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 1185 | Как откатить: вернуть old `trust` в legacy block; в canonical block использовать `trust_penalty = 1 - trust`, только если old trust confirmed positive. Если знак неясен — `[OPEN_QUESTION]`. |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 1284 | 2. Все места с `[OPEN_QUESTION]` нельзя решать автоматически в коде. |
| `patches_M1/M1.2_domain_rename_patch.md` | 28 | \| `[REQUIRES_VERIFICATION]` \| `[REQUIRES_VERIFICATION]` \| `[OPEN_QUESTION]` \| `[OPEN_QUESTION]` \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 34 | \| `seller_name` \| CSV/API/dashboard \| `actor_name` \| [OPEN_QUESTION] \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 35 | \| `listing_title` \| CSV/dashboard \| `event_title` или `title` \| [OPEN_QUESTION] \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 36 | \| `listing_description` \| CSV/dashboard \| `event_description` или `description` \| [OPEN_QUESTION] \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 37 | \| `seller_profile` \| docs/code \| `actor_profile` \| [OPEN_QUESTION] \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 38 | \| `marketplace` \| README/docs \| `reference domain` \| [OPEN_QUESTION] \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 1269 | \| `seller_name` \| `actor_name` \| optional [OPEN_QUESTION] \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 1279 | \| `trusted_seller` \| `trusted_actor` \| optional [OPEN_QUESTION] \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 1280 | \| `anchor_seller` \| `anchor_actor` \| optional [OPEN_QUESTION] \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 1306 | \| `price` \| `value` \| optional [OPEN_QUESTION] \| |
| `patches_M3/M3.1_temporal_persistence_patch.md` | 340 | [OPEN_QUESTION] Если в текущем проекте уже используется Pydantic для схем, можно заменить dataclasses на `BaseModel`, но не менять поля. |
| `patches_M3/M3.1_temporal_persistence_patch.md` | 1200 | Примечание: тест `shadow_signal_high_temporal_persistence` из задания ожидает `partial=False` для 6 точек по `1d`. Но согласно решению M3.1 `partial_aggregated=True`, если часть масштабов отсутствует. Поэтому правильное ожидание в patch-документе: `partial=True`, если есть только `1d`. Если автор хочет считать single-scale 3+ точек как full, нужно изменить решение 6. [OPEN_QUESTION] |
| `patches_M3/M3.1_temporal_persistence_patch.md` | 1511 | - В future M3.6 можно добавить `confidence_by_window` в debug output. [OPEN_QUESTION] |
| `patches_M3/M3.1_temporal_persistence_patch.md` | 1543 | - M3.1 не делает I/O, но может ограничивать обработку разумным max length. [OPEN_QUESTION] |
| `patches_M3/M3.1_temporal_persistence_patch.md` | 1574 | - Если автор хочет иначе, изменить решение M3.1 до реализации. [OPEN_QUESTION] |
| `patches_M3/M3.2_observer_agreement_patch.md` | 509 | - В M3.2 не добавляется reason для invalid timestamp, потому что timestamp не влияет на value. [OPEN_QUESTION] Можно добавить `invalid_observer_timestamp` reason, если это нужно для audit. |
| `patches_M3/M3.2_observer_agreement_patch.md` | 643 | M3.2 может позволить `confidence` и `reliability` вне `[0, 1]`, потому что compute layer clips значения. Если API-level validation уже строгая, можно ограничить их `ge=0, le=1`. [OPEN_QUESTION] |
| `patches_M3/M3.2_observer_agreement_patch.md` | 1343 | - Добавить future test `duplicate_observer_id`. [OPEN_QUESTION] |
| `patches_M3/M3.2_observer_agreement_patch.md` | 1344 | - Log reason when duplicate observer_id detected. [OPEN_QUESTION] |
| `patches_M3/M3.2_observer_agreement_patch.md` | 1349 | - Рекомендуемое решение для M3.3+: deduplicate by latest timestamp per observer_id или require ENRA to pre-aggregate observers. [OPEN_QUESTION] |
| `patches_M3/M3.2_observer_agreement_patch.md` | 1376 | - monitor observer weights in debug output. [OPEN_QUESTION] |
| `patches_M3/M3.2_observer_agreement_patch.md` | 1398 | - В production можно добавить config: reject_unknown_observer_types. [OPEN_QUESTION] |
| `patches_M3/M3.3_source_redundancy_patch.md` | 192 | [OPEN_QUESTION] Если ENRA добавит `last_seen` на cluster level, truncation should use latest clusters by last_seen. В M3.3 `claim_clusters` — это `dict[str, list[str]]`, поэтому timestamp у cluster отсутствует. |
| `patches_M3/M3.3_source_redundancy_patch.md` | 717 | M3.3 может позволить `reliability_score` вне `[0, 1]`, потому compute layer clips. Если API-level validation уже строгая, можно ставить `ge=0, le=1`. [OPEN_QUESTION] |
| `patches_M3/M3.3_source_redundancy_patch.md` | 1059 | Detection: test with zero reliability mixed sources. [OPEN_QUESTION] |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 1495 | 6. `[OPEN_QUESTION]` Whether to expose `objective_risk_result.reasons` as separate response field, e.g. `objective_layer_reasons`. Recommended: add it in M3.6.2, not M3.6.1, to keep math patch minimal. |
| `patches_M3/M3.6.2_objective_layer_operational_patch.md` | 1398 | [OPEN_QUESTION] Whether component scores should be omitted when layer is disabled. Recommendation: keep them for observability, but mark layer inactive. |
