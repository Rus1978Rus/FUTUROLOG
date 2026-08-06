# REQUIRES VERIFICATION REGISTER

Перед реализацией разработчик должен закрыть эти пункты по фактическому коду.

| File | Line | Item |
|---|---:|---|
| `00_READ_ME_FIRST_FOR_DEVELOPER.md` | 30 | - Нельзя игнорировать `[REQUIRES_VERIFICATION]`. |
| `01_IMPLEMENTATION_ORDER.md` | 7 | 3. Закрыть все `[REQUIRES_VERIFICATION]` в M1.1. |
| `architecture/objective_layer_design_v1.md` | 672 | Это соответствует M1.4 по смыслу, если `universal_risk` трактуется как риск до применения trust adjustment. Если в конкретной реализации M1.4 `universal_risk` уже включает вычитание `gamma × trust_adjustment`, то M3.6 должен сначала нормализовать терминологию, чтобы не вычесть trust adjustment дважды. [REQUIRES_VERIFICATION] |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 9 | Ограничение: архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` не был открыт при подготовке этого плана. Все предположения о фактических файлах архива помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 21 | \| `app/scoring.py` \| BOTH \| Доменное переименование, canonical scoring rename, dual output, `trust_adjustment`, `alpha`, `gamma`. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 22 | \| `app/confinement.py` \| BOTH \| `category` → `topic`, `CATEGORY_COUPLING` → `TOPIC_COUPLING`, public `residue` → `rg_persistence_score`. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 23 | \| `app/sequential.py` \| BOTH \| `seller_id/listing_id` → `actor_id/event_id`; public `sequential` → `sequential_anomaly_score`. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 24 | \| `app/large_deviation.py` \| RENAME_DOMAIN \| `avg_price_deviation` → `avg_value_deviation`; `surprise` остаётся legacy building block. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 25 | \| `app/trusted_baseline.py` \| RENAME_DOMAIN \| `trusted_sellers/anchor_sellers` → `trusted_actors/anchor_actors`. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 26 | \| `app/security.py` \| BOTH \| Payload поля и `SYSTEM_META`; HMAC не менять. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 27 | \| `app/explanations.py` \| BOTH \| Доменные тексты, canonical labels, deprecated aliases. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 28 | \| `app/calibration.py` \| BOTH \| CSV paths, column names, scoring labels, metadata. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 29 | \| `app/api.py` \| BOTH \| Request/response схемы, endpoints, deprecated aliases, dual output. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 30 | \| `app/main.py` \| BOTH \| CLI/demo paths, scoring calls, output metadata. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 31 | \| `app/dashboard.py` \| BOTH \| Streamlit labels, CSV paths, dual scores. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 32 | \| `app/state_store.py` \| DATA_MIGRATION \| SQLite/state columns `seller_id` → `actor_id`, если файл есть. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 34 | \| `data/sellers.csv` \| DATA_MIGRATION \| Rename to `data/actors.csv`, column migration. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 35 | \| `data/listings.csv` \| DATA_MIGRATION \| Rename to `data/events.csv`, column migration. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 36 | \| `schema.sql` \| DATA_MIGRATION \| Если есть PostgreSQL schema. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 37 | \| `README.md` \| BOTH \| Domain-neutral description, compatibility notes. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 38 | \| `docs/TECHNICAL_SPECIFICATION.md` \| BOTH \| Domain model, canonical output, M1 boundaries. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 39 | \| `healthcheck.py` \| RENAME_SCORING \| Проверка `SYSTEM_META` и dual output status. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 40 | \| `tests/` \| BOTH \| Fixtures, API tests, score regression, deprecated aliases. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 41 | \| `requirements.txt` \| NO_CHANGE \| Dependencies не меняются в M1. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 42 | \| `pyproject.toml` / `setup.py` \| NO_CHANGE \| Не менять packaging, кроме версии при необходимости. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 43 | \| `.env.example` \| NO_CHANGE / DATA_MIGRATION \| Не трогать, если нет old CSV paths. Если есть `SELLERS_CSV`, заменить. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 44 | \| `scripts/` \| BOTH \| Если есть demo/CSV scripts, обновить paths и поля. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 60 | \| `seller` \| `actor` \| entity / docstring / comment / test_fixture \| `app/*.py`, `README.md`, `docs/*`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 61 | \| `seller_id` \| `actor_id` \| api_field / csv_column / test_fixture \| `app/scoring.py`, `app/api.py`, `app/state_store.py`, `data/actors.csv`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 62 | \| `listing` \| `event` \| entity / docstring / comment / test_fixture \| `app/*.py`, `README.md`, `docs/*`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 63 | \| `listing_id` \| `event_id` \| api_field / csv_column / test_fixture \| `app/scoring.py`, `app/api.py`, `data/events.csv`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 64 | \| `category` \| `topic` \| entity / feature / docstring / comment \| `app/confinement.py`, `app/scoring.py`, `app/api.py`, `README.md`, `docs/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 65 | \| `category_id` \| `topic_id` \| api_field / csv_column \| `app/api.py`, `app/scoring.py`, `data/events.csv`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 66 | \| `region` \| `location` \| feature / csv_column / api_field \| `app/*.py`, `data/actors.csv`, `data/events.csv`, `dashboard.py` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 67 | \| `reviews_count` \| `endorsement_count` \| feature / csv_column \| `app/scoring.py`, `app/trusted_baseline.py`, `app/calibration.py`, `data/actors.csv` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 68 | \| `rating` \| `reputation_score` \| feature / csv_column \| `app/scoring.py`, `app/trusted_baseline.py`, `app/calibration.py`, `data/actors.csv` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 69 | \| `account_age_days` \| `actor_age_days` \| feature / csv_column \| `app/scoring.py`, `app/calibration.py`, `data/actors.csv`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 70 | \| `verified` \| `verified_actor` \| feature / csv_column \| `app/scoring.py`, `app/trusted_baseline.py`, `data/actors.csv` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 71 | \| `anchor_sellers` \| `anchor_actors` \| feature / docstring / comment \| `app/trusted_baseline.py`, `app/calibration.py`, `README.md`, `docs/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 72 | \| `trusted_sellers` \| `trusted_actors` \| feature / docstring / comment \| `app/trusted_baseline.py`, `app/calibration.py`, `README.md`, `docs/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 73 | \| `avg_price_deviation` \| `avg_value_deviation` \| feature / csv_column \| `app/scoring.py`, `app/large_deviation.py`, `data/events.csv`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 74 | \| `posting_frequency` \| `emission_frequency` \| feature / csv_column \| `app/scoring.py`, `app/sequential.py`, `data/actors.csv`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 75 | \| `duplicate_image_ratio` \| `duplicate_media_ratio` \| feature / csv_column \| `app/scoring.py`, `app/confinement.py`, `data/events.csv`, `dashboard.py` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 76 | \| `unique_regions` \| `unique_locations` \| feature \| `app/confinement.py`, `app/scoring.py`, `app/calibration.py` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 77 | \| `unique_categories` \| `unique_topics` \| feature \| `app/confinement.py`, `app/scoring.py`, `app/calibration.py` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 78 | \| `contact_reuse_score` \| `identity_reuse_score` \| feature / csv_column \| `app/scoring.py`, `app/confinement.py`, `data/actors.csv`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 79 | \| `account_age_risk` \| `actor_age_risk` \| feature \| `app/scoring.py`, `app/explanations.py`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 80 | \| `rating_risk` \| `reputation_risk` \| feature \| `app/scoring.py`, `app/explanations.py`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 81 | \| `reviews_risk` \| `endorsement_risk` \| feature \| `app/scoring.py`, `app/explanations.py`, `tests/*` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 83 | \| `data/sellers.csv` \| `data/actors.csv` \| data file \| `data/`, `app/main.py`, `app/dashboard.py`, `app/calibration.py` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 84 | \| `data/listings.csv` \| `data/events.csv` \| data file \| `data/`, `app/main.py`, `app/dashboard.py`, `app/calibration.py` [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 85 | \| `GET /seller/{id}` \| `GET /actor/{id}` \| api_endpoint \| `app/api.py`, `README.md`, API tests [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 86 | \| `GET /listing/{id}` \| `GET /event/{id}` \| api_endpoint \| `app/api.py`, `README.md`, API tests [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 92 | \| `trust` \| `trust_penalty` \| `app/scoring.py`, `app/canonical_mapping.py`, `app/api.py`, `app/explanations.py`, tests [REQUIRES_VERIFICATION] \| Canonical rename. Перед применением проверить знак: значение должно быть penalty. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 93 | \| `residue` \| `rg_persistence_score` \| `app/scoring.py`, `app/confinement.py`, `app/canonical_mapping.py`, `app/api.py`, `dashboard.py`, tests [REQUIRES_VERIFICATION] \| Public canonical key. Legacy key остаётся в `legacy_component_scores` до v3.2. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 94 | \| `sequential` \| `sequential_anomaly_score` \| `app/scoring.py`, `app/sequential.py`, `app/canonical_mapping.py`, API/tests [REQUIRES_VERIFICATION] \| Public canonical key. Sequential formula не менять. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 95 | \| `graph` \| `graph_risk` \| `app/scoring.py`, `app/canonical_mapping.py`, `dashboard.py`, docs/tests [REQUIRES_VERIFICATION] \| Public canonical key. Graph logic не менять. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 96 | \| `gibbs` \| `gibbs` \| `app/scoring.py`, `app/canonical_mapping.py` [REQUIRES_VERIFICATION] \| Оставить legacy building block. Не делать canonical-компонентой. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 97 | \| `surprise` \| `surprise` \| `app/scoring.py`, `app/large_deviation.py`, `app/canonical_mapping.py` [REQUIRES_VERIFICATION] \| Оставить legacy building block. Не делать canonical-компонентой. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 98 | \| `robustness` \| `trust_adjustment` \| `app/scoring.py`, `app/canonical_mapping.py`, `app/api.py`, `dashboard.py`, tests [REQUIRES_VERIFICATION] \| Убирается из `DEFAULT_WEIGHTS`; добавляется как отдельный modifier; применяется со знаком минус `− gamma × trust_adjustment`. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 99 | \| `DEFAULT_WEIGHTS["trust"]` \| `DEFAULT_WEIGHTS["trust_penalty"]` \| `app/scoring.py` [REQUIRES_VERIFICATION] \| Вес 0.10 сохранить; проверить знак. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 100 | \| `DEFAULT_WEIGHTS["residue"]` \| `DEFAULT_WEIGHTS["rg_persistence_score"]` \| `app/scoring.py` [REQUIRES_VERIFICATION] \| Вес 0.22 сохраняется для regression, если M1 не меняет математику. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 101 | \| `DEFAULT_WEIGHTS["sequential"]` \| `DEFAULT_WEIGHTS["sequential_anomaly_score"]` \| `app/scoring.py` [REQUIRES_VERIFICATION] \| Вес 0.18 сохраняется для regression. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 102 | \| `DEFAULT_WEIGHTS["graph"]` \| `DEFAULT_WEIGHTS["graph_risk"]` \| `app/scoring.py` [REQUIRES_VERIFICATION] \| Вес 0.12 сохраняется для regression. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 103 | \| `DEFAULT_WEIGHTS["robustness"]` \| removed from `DEFAULT_WEIGHTS` \| `app/scoring.py` [REQUIRES_VERIFICATION] \| Не участвует как весовая компонента; переносится в `trust_adjustment`. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 104 | \| `component_scores` \| `legacy_component_scores` + `canonical_component_scores` \| `app/scoring.py`, `app/api.py`, `dashboard.py`, tests [REQUIRES_VERIFICATION] \| На v3.0 вернуть оба блока. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 105 | \| None \| `weights_version = "preprint-v1-uncalibrated"` \| `app/security.py`, `app/scoring.py`, API output [REQUIRES_VERIFICATION] \| Новое metadata поле. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 106 | \| None \| `calibration_status = "uncalibrated"` \| `app/security.py`, `app/scoring.py`, API output [REQUIRES_VERIFICATION] \| Новое metadata поле. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 107 | \| None \| `alpha = 0.3` \| `app/scoring.py`, `app/canonical_mapping.py`, API output [REQUIRES_VERIFICATION] \| Стартовое значение soft-objective formula. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 108 | \| None \| `gamma = 0.07` \| `app/scoring.py`, `app/canonical_mapping.py`, API output [REQUIRES_VERIFICATION] \| Стартовое значение из диапазона 0.05–0.10. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 109 | \| old model version \| `entropy-rg-v3.0-domain-neutral` \| `app/security.py`, `healthcheck.py`, API output [REQUIRES_VERIFICATION] \| Обновить `SYSTEM_META`. \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 604 | \| `seller_name` \| `actor_name` \| optional \| Если есть. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 614 | \| `trusted_seller` \| `trusted_actor` \| optional \| Если есть. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 615 | \| `anchor_seller` \| `anchor_actor` \| optional \| Если есть. [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 660 | [REQUIRES_VERIFICATION] Ожидаемые таблицы: |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 673 | [REQUIRES_VERIFICATION] |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 697 | \| `GET /metrics` \| `GET /metrics` \| unchanged [REQUIRES_VERIFICATION] \| |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 900 | Ожидаемое расположение: `app/security.py`, `app/scoring.py`, `healthcheck.py` или отдельный config module. [REQUIRES_VERIFICATION] |
| `patches_M1/M1.1_migration_plan_v3_0.md` | 1283 | 1. Все места с `[REQUIRES_VERIFICATION]` должны быть проверены после распаковки архива. |
| `patches_M1/M1.2_domain_rename_patch.md` | 10 | Важно: этот patch-документ подготовлен по согласованному плану M1.1 и заданной таблице переименований. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M1/M1.2_domain_rename_patch.md` | 14 | M1.2 выполняет только доменное переименование Entropy-RG: `seller/listing/category/region` и связанные feature-поля переводятся в `actor/event/topic/location`. Также переименовываются CSV-файлы `data/sellers.csv → data/actors.csv` и `data/listings.csv → data/events.csv`, добавляются новые API endpoints `GET /actor/{id}` и `GET /event/{id}`, а старые endpoints сохраняются как deprecated aliases до v3.2. Scoring keys, `DEFAULT_WEIGHTS`, формулы, пороги, confluence-логика, HMAC-логика, `SYSTEM_META`, `model_version`, `weights_version`, dual output и canonical scoring rename в M1.2 не изменяются. Ожидаемо затрагиваются файлы `app/scoring.py`, `app/confinement.py`, `app/sequential.py`, `app/large_deviation.py`, `app/trusted_baseline.py`, `app/security.py`, `app/explanations.py`, `app/calibration.py`, `app/api.py`, `app/main.py`, `app/dashboard.py`, `app/state_store.py`, CSV-файлы, тесты и документация. Точный список должен быть сверён после распаковки архива. [REQUIRES_VERIFICATION] |
| `patches_M1/M1.2_domain_rename_patch.md` | 28 | \| `[REQUIRES_VERIFICATION]` \| `[REQUIRES_VERIFICATION]` \| `[OPEN_QUESTION]` \| `[OPEN_QUESTION]` \| |
| `patches_M1/M1.2_domain_rename_patch.md` | 339 | compute_seller_residue = compute_observed_residue  # [REQUIRES_VERIFICATION] |
| `patches_M1/M1.2_domain_rename_patch.md` | 342 | Если фактическое имя старой публичной функции отличается, alias должен сохранять именно старое имя. [REQUIRES_VERIFICATION] |
| `patches_M1/M1.2_domain_rename_patch.md` | 572 | canonicalize_seller_score_payload = canonicalize_score_payload  # [REQUIRES_VERIFICATION] |
| `patches_M1/M1.2_domain_rename_patch.md` | 575 | Если старая функция называлась иначе, deprecated alias должен соответствовать фактическому старому имени. [REQUIRES_VERIFICATION] |
| `patches_M1/M1.2_domain_rename_patch.md` | 880 | repository.get_seller = repository.get_actor  # [REQUIRES_VERIFICATION] |
| `patches_M1/M1.2_domain_rename_patch.md` | 881 | repository.get_listing = repository.get_event  # [REQUIRES_VERIFICATION] |
| `patches_M1/M1.2_domain_rename_patch.md` | 1255 | [REQUIRES_VERIFICATION] If alias is implemented as wrapper instead of direct assignment, compare outputs instead of identity. |
| `patches_M1/M1.2_domain_rename_patch.md` | 1694 | Примечание: `trust_penalty` как внутренняя переменная уже может существовать по ревью, но M1.2 не должен менять её статус. [REQUIRES_VERIFICATION] |
| `patches_M1/M1.3_scoring_rename_patch.md` | 10 | Важно: этот patch-документ подготовлен по согласованным решениям M1.1/M1.2 и заданию M1.3. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M1/M1.3_scoring_rename_patch.md` | 200 | [REQUIRES_VERIFICATION] Реальные reason codes нужно сверить с `app/scoring.py` и `app/explanations.py`. |
| `patches_M1/M1.3_scoring_rename_patch.md` | 277 | [REQUIRES_VERIFICATION] Если старое имя `integrate_scores` должно сохраниться для API, можно оставить имя функции прежним и переименовать только аргументы. В этом случае deprecated wrapper не нужен, но старые keyword arguments должны поддерживаться через compatibility adapter. Решение зависит от фактических вызовов. |
| `patches_M1/M1.3_scoring_rename_patch.md` | 555 | [REQUIRES_VERIFICATION] Реальные reason codes и thresholds нужно сверить с фактическим файлом. |
| `patches_M1/M1.3_scoring_rename_patch.md` | 682 | Если после M1.2 в request schemas есть поле `robustness` или `robustness_discount`, переименовать в `trust_adjustment`. [REQUIRES_VERIFICATION] |
| `patches_M1/M1.3_scoring_rename_patch.md` | 908 | [REQUIRES_VERIFICATION] Если CI не имеет доступа к `/tmp`, этот тест должен быть переведён на fixtures in repo, например `tests/fixtures/v3_0_m1_2_scores.jsonl`. |
| `patches_M1/M1.3_scoring_rename_patch.md` | 966 | [REQUIRES_VERIFICATION] Threshold values and reason conditions must be adapted to actual `compute_confluence_bonus`. |
| `patches_M1/M1.4_dual_output_patch.md` | 10 | Важно: этот patch-документ подготовлен по согласованным решениям M1.1–M1.3. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M1/M1.4_dual_output_patch.md` | 342 | или M1.3-вариант без metadata. [REQUIRES_VERIFICATION] |
| `patches_M1/M1.4_dual_output_patch.md` | 383 | [REQUIRES_VERIFICATION] Фактическая структура security payload может отличаться. |
| `patches_M1/M1.4_dual_output_patch.md` | 502 | [REQUIRES_VERIFICATION] Если deprecated endpoint называется иначе, применить тот же принцип. |
| `patches_M1/M1.4_dual_output_patch.md` | 768 | [REQUIRES_VERIFICATION] Если healthcheck function называется иначе, адаптировать import. |
| `patches_M1/M1.4_dual_output_patch.md` | 831 | [REQUIRES_VERIFICATION] If some fixtures have `trust_adjustment = 0`, scores may not differ. In that case add at least one fixture with non-zero trust_adjustment. |
| `patches_M1/M1.5_documentation_release.md` | 710 | [REQUIRES_VERIFICATION] Имена SQLite/PostgreSQL файлов и переменных окружения зависят от фактической реализации. |
| `patches_M3/M3.1_temporal_persistence_patch.md` | 11 | Важно: этот patch-документ подготовлен по архитектурным решениям M3.0/M3.1. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M3/M3.1_temporal_persistence_patch.md` | 653 | [REQUIRES_VERIFICATION] Фактическая сигнатура `integrate_scores` после M1.4 может отличаться. Ниже — целевой паттерн. |
| `patches_M3/M3.1_temporal_persistence_patch.md` | 1363 | [REQUIRES_VERIFICATION] `score_actor_with_history_fixture`, `score_actor_without_history_fixture`, `load_jsonl` должны быть адаптированы под существующую test infrastructure. |
| `patches_M3/M3.2_observer_agreement_patch.md` | 11 | Важно: этот patch-документ подготовлен по архитектурным решениям M3.0–M3.2. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M3/M3.2_observer_agreement_patch.md` | 530 | [REQUIRES_VERIFICATION] Фактическая сигнатура scoring pipeline после M3.1 может отличаться. Ниже целевой паттерн. |
| `patches_M3/M3.2_observer_agreement_patch.md` | 1182 | [REQUIRES_VERIFICATION] Fixture helpers must be adapted to actual test infrastructure. |
| `patches_M3/M3.3_source_redundancy_patch.md` | 11 | Важно: этот patch-документ подготовлен по архитектурным решениям M3.0–M3.3. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M3/M3.3_source_redundancy_patch.md` | 665 | [REQUIRES_VERIFICATION] Фактический scoring pipeline после M3.2 может отличаться. Целевой паттерн: |
| `patches_M3/M3.3_source_redundancy_patch.md` | 952 | [REQUIRES_VERIFICATION] Fixture helper names must be adapted to the actual test infrastructure. |
| `patches_M3/M3.3_source_redundancy_patch.md` | 1044 | Detection: test with unknown source_id in cluster. [REQUIRES_VERIFICATION] |
| `patches_M3/M3.3_source_redundancy_patch.md` | 1064 | Detection: clustering tests with duplicate source ids. [REQUIRES_VERIFICATION] |
| `patches_M3/M3.4_noise_separation_patch.md` | 11 | Важно: исходное задание в текущем сообщении обрывается на фразе `distribution содержит p95...`. Поэтому часть граничных случаев ниже восстановлена по уже заданным решениям M3.4 и помечена `[REQUIRES_VERIFICATION]`, если требует подтверждения автора. |
| `patches_M3/M3.4_noise_separation_patch.md` | 197 | Решение M3.4: clipped для safety, но добавить reason `noise_quantile_clipped_to_unit_range`. [REQUIRES_VERIFICATION] |
| `patches_M3/M3.4_noise_separation_patch.md` | 489 | [REQUIRES_VERIFICATION] Фактический scoring pipeline после M3.3 может отличаться. Целевой паттерн: |
| `patches_M3/M3.5_scale_stability_patch.md` | 11 | Важно: этот patch-документ подготовлен как целевой patch. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M3/M3.5_scale_stability_patch.md` | 560 | [REQUIRES_VERIFICATION] Фактический scoring pipeline после M3.4 может отличаться. Целевой паттерн: |
| `patches_M3/M3.5_scale_stability_patch.md` | 751 | [REQUIRES_VERIFICATION] Because pair weights are low for event→actor due to event sample_count=1, the test must ensure later transitions also dissolve enough to keep value low. If value is borderline, adjust fixture to `event=0.95, actor=0.25, topic=0.1, global=0.02`. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 11 | Важно: этот patch-документ подготовлен как целевой patch. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 476 | [REQUIRES_VERIFICATION] В текущем коде после M3.5 objective results могут уже быть converted to dict через `.to_dict()`. Для aggregator нужны исходные `ObjectiveComponentResult`, не dict. Если pipeline сейчас хранит только dict, нужно сохранить параллельный `objective_component_results_raw`. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 617 | [REQUIRES_VERIFICATION] Если snapshots include `model_version`, HMAC fixtures must be updated. Это ожидаемое изменение M3.6.1. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 787 | [REQUIRES_VERIFICATION] JSON example above must be updated to exact arithmetic if used as fixture. The intended value is `0.546905`, not `0.546405`. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 1486 | [REQUIRES_VERIFICATION] CLI argument `--objective-context` may not exist. If unavailable, use the project’s test helper or API fixture runner. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 1490 | 1. `[REQUIRES_VERIFICATION]` Whether current `integrate_scores` keeps raw `ObjectiveComponentResult` objects or only dicts. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 1491 | 2. `[REQUIRES_VERIFICATION]` Exact location of `DEFAULT_ALPHA`, `DEFAULT_GAMMA`, and `SYSTEM_META`. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 1492 | 3. `[REQUIRES_VERIFICATION]` Whether `build_dual_output` can import `ObjectiveRiskResult` without circular imports. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 1493 | 4. `[REQUIRES_VERIFICATION]` Whether HMAC payload includes new fields and requires fixture updates. |
| `patches_M3/M3.6.1_objective_layer_activation_patch.md` | 1494 | 5. `[REQUIRES_VERIFICATION]` Exact runner for full objective baseline fixtures. |
| `patches_M3/M3.6.2_objective_layer_operational_patch.md` | 11 | Важно: этот patch-документ подготовлен как целевой patch. Фактический архив `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в текущем контексте не открыт, поэтому места, где требуется сверка с реальным кодом, помечены `[REQUIRES_VERIFICATION]`. |
| `patches_M3/M3.6.2_objective_layer_operational_patch.md` | 21 | [REQUIRES_VERIFICATION] Если в проекте уже есть `app/config.py`, его нужно расширить, а не создавать второй конкурирующий config module. |
| `patches_M3/M3.6.2_objective_layer_operational_patch.md` | 294 | [REQUIRES_VERIFICATION] If HMAC payload includes `weights_version`, test fixtures must be updated because the schema changes from string to object. |
