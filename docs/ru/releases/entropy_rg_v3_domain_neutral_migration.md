# Entropy-RG v3.0 Domain-Neutral Migration

## 1. Сводка изменений

Этот документ описывает миграцию `Entropy-RG Confinement Anomaly Detector v2.2` из маркетплейсного домена в доменно-нейтральное алгоритмическое ядро `Entropy-RG v3.0-domain-neutral` для проекта «Футуролог». Миграция не меняет математику, веса, пороги, HMAC-логику, decay-логику, confluence-логику и calibration-логику. Изменяются только имена сущностей, полей, переменных, CSV-колонок, API-маршрутов, комментариев и документации: `seller/listing/category/region` переводятся в `actor/event/topic/location`. Маркетплейс остаётся reference-доменом для тестов и примеров, но основной код и документация должны читаться как доменно-нейтральное scoring-ядро.

Важно: документ подготовлен как review patch по известной структуре и заданному списку файлов. Перед применением к архиву `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` нужно сверить реальные строки файлов. Если фактические имена функций отличаются от указанных ниже, применяется тот же принцип переименования без изменения формул и числовых значений.

## 2. Полная таблица переименований

| Старое имя | Новое имя | Файлы | Тип изменения |
|---|---|---|---|
| `seller` | `actor` | `app/scoring.py`, `app/confinement.py`, `app/sequential.py`, `app/trusted_baseline.py`, `app/explanations.py`, `app/calibration.py`, `app/api.py`, `app/main.py`, `app/dashboard.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_var / update_comment / update_docstring |
| `Seller` | `Actor` | `app/api.py`, `app/main.py`, `app/dashboard.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_class / update_docstring |
| `seller_id` | `actor_id` | `app/scoring.py`, `app/confinement.py`, `app/sequential.py`, `app/large_deviation.py`, `app/trusted_baseline.py`, `app/security.py`, `app/explanations.py`, `app/calibration.py`, `app/api.py`, `app/main.py`, `app/dashboard.py`, `data/sellers.csv`, `docs/TECHNICAL_SPECIFICATION.md` | rename_field / rename_var / rename_csv_column |
| `listing` | `event` | `app/scoring.py`, `app/confinement.py`, `app/sequential.py`, `app/large_deviation.py`, `app/explanations.py`, `app/calibration.py`, `app/api.py`, `app/dashboard.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_var / update_comment / update_docstring |
| `Listing` | `Event` | `app/api.py`, `app/main.py`, `app/dashboard.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_class / update_docstring |
| `listing_id` | `event_id` | `app/scoring.py`, `app/confinement.py`, `app/sequential.py`, `app/large_deviation.py`, `app/security.py`, `app/explanations.py`, `app/api.py`, `app/dashboard.py`, `data/listings.csv`, `docs/TECHNICAL_SPECIFICATION.md` | rename_field / rename_var / rename_csv_column |
| `category` | `topic` | `app/scoring.py`, `app/confinement.py`, `app/large_deviation.py`, `app/trusted_baseline.py`, `app/explanations.py`, `app/calibration.py`, `app/api.py`, `app/main.py`, `app/dashboard.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_var / update_comment / update_docstring |
| `category_id` | `topic_id` | `app/scoring.py`, `app/confinement.py`, `app/large_deviation.py`, `app/trusted_baseline.py`, `app/api.py`, `data/listings.csv`, `docs/TECHNICAL_SPECIFICATION.md` | rename_field / rename_var / rename_csv_column |
| `region` | `location` | `app/scoring.py`, `app/confinement.py`, `app/large_deviation.py`, `app/explanations.py`, `app/calibration.py`, `app/api.py`, `app/dashboard.py`, `data/sellers.csv`, `data/listings.csv`, `README.md` | rename_field / rename_var / rename_csv_column |
| `reviews_count` | `endorsement_count` | `app/scoring.py`, `app/trusted_baseline.py`, `app/calibration.py`, `app/dashboard.py`, `data/sellers.csv`, `README.md` | rename_field / rename_csv_column |
| `rating` | `reputation_score` | `app/scoring.py`, `app/trusted_baseline.py`, `app/calibration.py`, `app/dashboard.py`, `data/sellers.csv`, `README.md` | rename_field / rename_csv_column |
| `account_age_days` | `actor_age_days` | `app/scoring.py`, `app/trusted_baseline.py`, `app/calibration.py`, `app/dashboard.py`, `data/sellers.csv`, `README.md` | rename_field / rename_csv_column |
| `verified` | `verified_actor` | `app/scoring.py`, `app/trusted_baseline.py`, `app/calibration.py`, `app/dashboard.py`, `data/sellers.csv`, `README.md` | rename_field / rename_csv_column |
| `anchor_sellers` | `anchor_actors` | `app/trusted_baseline.py`, `app/calibration.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_var / update_docstring |
| `trusted_sellers` | `trusted_actors` | `app/trusted_baseline.py`, `app/calibration.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_var / update_docstring |
| `avg_price_deviation` | `avg_value_deviation` | `app/scoring.py`, `app/large_deviation.py`, `app/explanations.py`, `app/calibration.py`, `app/dashboard.py`, `data/listings.csv`, `README.md` | rename_field / rename_csv_column |
| `posting_frequency` | `emission_frequency` | `app/scoring.py`, `app/sequential.py`, `app/explanations.py`, `app/calibration.py`, `app/dashboard.py`, `data/sellers.csv`, `README.md` | rename_field / rename_csv_column |
| `duplicate_text_ratio` | `duplicate_text_ratio` | `app/scoring.py`, `app/confinement.py`, `app/explanations.py`, `app/calibration.py`, `app/dashboard.py`, `data/listings.csv` | no_change |
| `duplicate_image_ratio` | `duplicate_media_ratio` | `app/scoring.py`, `app/confinement.py`, `app/explanations.py`, `app/calibration.py`, `app/dashboard.py`, `data/listings.csv`, `README.md` | rename_field / rename_csv_column |
| `unique_regions` | `unique_locations` | `app/scoring.py`, `app/confinement.py`, `app/calibration.py`, `app/dashboard.py`, `README.md` | rename_field / rename_var |
| `unique_categories` | `unique_topics` | `app/scoring.py`, `app/confinement.py`, `app/calibration.py`, `app/dashboard.py`, `README.md` | rename_field / rename_var |
| `contact_reuse_score` | `identity_reuse_score` | `app/scoring.py`, `app/confinement.py`, `app/explanations.py`, `app/calibration.py`, `app/dashboard.py`, `data/sellers.csv`, `README.md` | rename_field / rename_csv_column |
| `account_age_risk` | `actor_age_risk` | `app/scoring.py`, `app/explanations.py`, `app/calibration.py`, `app/dashboard.py` | rename_field / rename_var |
| `rating_risk` | `reputation_risk` | `app/scoring.py`, `app/explanations.py`, `app/calibration.py`, `app/dashboard.py` | rename_field / rename_var |
| `reviews_risk` | `endorsement_risk` | `app/scoring.py`, `app/explanations.py`, `app/calibration.py`, `app/dashboard.py` | rename_field / rename_var |
| `CATEGORY_COUPLING` | `TOPIC_COUPLING` | `app/confinement.py`, `app/scoring.py`, `app/calibration.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_var |
| `score_seller` | `score_actor` | `app/scoring.py`, `app/api.py`, `app/main.py`, `app/dashboard.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_function |
| `score_listing` | `score_event` | `app/scoring.py`, `app/api.py`, `app/dashboard.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_function |
| `/seller/{id}` | `/actor/{id}` | `app/api.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_api_route |
| `/listing/{id}` | `/event/{id}` | `app/api.py`, `README.md`, `docs/TECHNICAL_SPECIFICATION.md` | rename_api_route |
| `data/sellers.csv` | `data/actors.csv` | `data/`, `app/main.py`, `app/dashboard.py`, `app/calibration.py`, `README.md` | rename_file |
| `data/listings.csv` | `data/events.csv` | `data/`, `app/main.py`, `app/dashboard.py`, `app/calibration.py`, `README.md` | rename_file |
| `SYSTEM_META.model_version` | `"entropy-rg-v3.0-domain-neutral"` | `app/security.py` или файл, где определён `SYSTEM_META` | rename_value |

Термины `gibbs`, `residue`, `sequential`, `surprise`, `graph`, `trust_score`, `trust_penalty`, `robustness_discount`, `confluence_bonus` не переименовываются.

## 3. Изменения по файлам

## app/scoring.py

Что меняется: файл переводится с marketplace-сущностей на нейтральные `actor/event/topic`. Функции `score_seller` и `score_listing`, если они есть, переименовываются в `score_actor` и `score_event`. Все математические формулы, веса `DEFAULT_WEIGHTS`, пороги risk levels и confluence-логика остаются без изменений.

### Unified diff

```diff
--- a/app/scoring.py
+++ b/app/scoring.py
@@
-# Marketplace scoring for sellers and listings
+# Domain-neutral scoring for actors and events

@@
-def score_seller(seller, listings, baseline=None):
+def score_actor(actor, events, baseline=None):
@@
-    seller_id = seller.get("seller_id")
-    category = seller.get("category")
-    region = seller.get("region")
+    actor_id = actor.get("actor_id")
+    topic = actor.get("topic")
+    location = actor.get("location")

@@
-    account_age_risk = compute_account_age_risk(seller.get("account_age_days"))
-    rating_risk = compute_rating_risk(seller.get("rating"))
-    reviews_risk = compute_reviews_risk(seller.get("reviews_count"))
+    actor_age_risk = compute_actor_age_risk(actor.get("actor_age_days"))
+    reputation_risk = compute_reputation_risk(actor.get("reputation_score"))
+    endorsement_risk = compute_endorsement_risk(actor.get("endorsement_count"))

@@
-    feature_scores = {
-        "account_age_risk": account_age_risk,
-        "rating_risk": rating_risk,
-        "reviews_risk": reviews_risk,
-        "contact_reuse_score": seller.get("contact_reuse_score", 0.0),
-        "posting_frequency": seller.get("posting_frequency", 0.0),
-    }
+    feature_scores = {
+        "actor_age_risk": actor_age_risk,
+        "reputation_risk": reputation_risk,
+        "endorsement_risk": endorsement_risk,
+        "identity_reuse_score": actor.get("identity_reuse_score", 0.0),
+        "emission_frequency": actor.get("emission_frequency", 0.0),
+    }

@@
-    duplicate_image_ratio = aggregate_duplicate_image_ratio(listings)
-    unique_regions = count_unique_regions(listings)
-    unique_categories = count_unique_categories(listings)
+    duplicate_media_ratio = aggregate_duplicate_media_ratio(events)
+    unique_locations = count_unique_locations(events)
+    unique_topics = count_unique_topics(events)

@@
-    return {
-        "seller_id": seller_id,
+    return {
+        "actor_id": actor_id,
         "component_scores": component_scores,
         "confluence_bonus": confluence_bonus,
         "final_score": final_score,
         "risk_level": risk_level,
         "reasons": reasons,
     }

@@
-def score_listing(listing, seller_context, baseline=None):
+def score_event(event, actor_context, baseline=None):
@@
-    listing_id = listing.get("listing_id")
-    seller_id = listing.get("seller_id")
-    category_id = listing.get("category_id")
-    region = listing.get("region")
+    event_id = event.get("event_id")
+    actor_id = event.get("actor_id")
+    topic_id = event.get("topic_id")
+    location = event.get("location")

@@
-    avg_price_deviation = listing.get("avg_price_deviation", 0.0)
-    duplicate_image_ratio = listing.get("duplicate_image_ratio", 0.0)
+    avg_value_deviation = event.get("avg_value_deviation", 0.0)
+    duplicate_media_ratio = event.get("duplicate_media_ratio", 0.0)

@@
-    return {
-        "listing_id": listing_id,
-        "seller_id": seller_id,
-        "category_id": category_id,
+    return {
+        "event_id": event_id,
+        "actor_id": actor_id,
+        "topic_id": topic_id,
         "component_scores": component_scores,
         "confluence_bonus": confluence_bonus,
         "final_score": final_score,
     }
```

### Переименование helper-функций

Если в файле есть helper-функции с доменными именами, переименовать только имена, не тело формул:

```diff
--- a/app/scoring.py
+++ b/app/scoring.py
@@
-def compute_account_age_risk(account_age_days):
+def compute_actor_age_risk(actor_age_days):
@@
-    return formula_without_changes(account_age_days)
+    return formula_without_changes(actor_age_days)

@@
-def compute_rating_risk(rating):
+def compute_reputation_risk(reputation_score):
@@
-    return formula_without_changes(rating)
+    return formula_without_changes(reputation_score)

@@
-def compute_reviews_risk(reviews_count):
+def compute_endorsement_risk(endorsement_count):
@@
-    return formula_without_changes(reviews_count)
+    return formula_without_changes(endorsement_count)
```

Если фактические функции называются иначе, применить тот же mapping к параметрам и ключам словарей.

## app/confinement.py

Что меняется: `category` становится `topic`, `CATEGORY_COUPLING` становится `TOPIC_COUPLING`, `listing/seller` становятся `event/actor`. Формула exponential decay и category/topic coupling не меняется.

### Unified diff

```diff
--- a/app/confinement.py
+++ b/app/confinement.py
@@
-CATEGORY_COUPLING = {
+TOPIC_COUPLING = {
     "electronics": 1.00,
     "phones": 1.10,
     "cars": 1.25,
     "real_estate": 1.35,
 }
+# Example topic coupling profile. These keys are a reference domain profile
+# and should be replaced by the user for their target domain.

@@
-def compute_expected_decay(scale_distance, category):
-    coupling = CATEGORY_COUPLING.get(category, 1.0)
+def compute_expected_decay(scale_distance, topic):
+    coupling = TOPIC_COUPLING.get(topic, 1.0)
     return math.exp(-coupling * scale_distance)

@@
-def check_information_residue(listings, seller, category):
+def check_information_residue(events, actor, topic):
@@
-    observed = compute_observed_residue(listings, seller)
-    expected = compute_expected_decay(scale_distance, category)
+    observed = compute_observed_residue(events, actor)
+    expected = compute_expected_decay(scale_distance, topic)
@@
-        "seller_id": seller.get("seller_id"),
-        "category": category,
+        "actor_id": actor.get("actor_id"),
+        "topic": topic,
         "observed": observed,
         "expected": expected,
         "residue": residue,
     }

@@
-def count_unique_regions(listings):
-    return len({row.get("region") for row in listings if row.get("region")})
+def count_unique_locations(events):
+    return len({row.get("location") for row in events if row.get("location")})

@@
-def count_unique_categories(listings):
-    return len({row.get("category") for row in listings if row.get("category")})
+def count_unique_topics(events):
+    return len({row.get("topic") for row in events if row.get("topic")})
```

## app/sequential.py

Что меняется: последовательное накопление evidence переводится с `seller_id/listing_id` на `actor_id/event_id`. Формулы decay, update и accumulation не меняются.

### Unified diff

```diff
--- a/app/sequential.py
+++ b/app/sequential.py
@@
-def update_seller_sequence(seller_id, listing_id, score, timestamp, state_store):
+def update_actor_sequence(actor_id, event_id, score, timestamp, state_store):
@@
-    previous_state = state_store.get_sequence_state(seller_id)
+    previous_state = state_store.get_sequence_state(actor_id)
@@
-        "seller_id": seller_id,
-        "listing_id": listing_id,
+        "actor_id": actor_id,
+        "event_id": event_id,
         "score": updated_score,
         "timestamp": timestamp,
     }
@@
-    state_store.save_sequence_state(seller_id, new_state)
+    state_store.save_sequence_state(actor_id, new_state)
     return new_state

@@
-def compute_sequential_evidence(seller_events, decay):
+def compute_sequential_evidence(actor_events, decay):
@@
-    for event in seller_events:
+    for event in actor_events:
         # Formula unchanged.
         ...
```

Если в файле есть class или dataclass вроде `SellerSequenceState`, переименовать в `ActorSequenceState`, не меняя поля, кроме `seller_id -> actor_id`.

## app/large_deviation.py

Что меняется: marketplace-поля переводятся в нейтральные features. `robust_z_score`, `gaussian_tail_probability`, MAD и tail probability не изменяются.

### Unified diff

```diff
--- a/app/large_deviation.py
+++ b/app/large_deviation.py
@@
-def compute_price_surprise(avg_price_deviation, baseline_window):
-    z = robust_z_score(avg_price_deviation, baseline_window)
+def compute_value_surprise(avg_value_deviation, baseline_window):
+    z = robust_z_score(avg_value_deviation, baseline_window)
     return gaussian_tail_probability(z)

@@
-def compute_listing_surprise(listing, baseline):
-    avg_price_deviation = listing.get("avg_price_deviation", 0.0)
-    category_id = listing.get("category_id")
-    region = listing.get("region")
+def compute_event_surprise(event, baseline):
+    avg_value_deviation = event.get("avg_value_deviation", 0.0)
+    topic_id = event.get("topic_id")
+    location = event.get("location")
@@
-    baseline_window = baseline.get_window(category_id, region)
-    return compute_price_surprise(avg_price_deviation, baseline_window)
+    baseline_window = baseline.get_window(topic_id, location)
+    return compute_value_surprise(avg_value_deviation, baseline_window)
```

Примечание: если `price` как поле используется в тестовом marketplace profile, оно может остаться в example-data only. В scoring-core использовать `value`.

## app/trusted_baseline.py

Что меняется: trusted/anchor sellers становятся trusted/anchor actors. Логика trusted baseline и poisoning protection не меняется.

### Unified diff

```diff
--- a/app/trusted_baseline.py
+++ b/app/trusted_baseline.py
@@
-class TrustedSellerBaseline:
+class TrustedActorBaseline:
@@
-    def __init__(self, anchor_sellers):
-        self.anchor_sellers = anchor_sellers
+    def __init__(self, anchor_actors):
+        self.anchor_actors = anchor_actors

@@
-    def build_from_trusted_sellers(self, trusted_sellers):
+    def build_from_trusted_actors(self, trusted_actors):
@@
-        for seller in trusted_sellers:
-            seller_id = seller["seller_id"]
-            category = seller.get("category")
+        for actor in trusted_actors:
+            actor_id = actor["actor_id"]
+            topic = actor.get("topic")
             # Baseline formula unchanged.
             ...

@@
-    def is_anchor_seller(self, seller_id):
-        return seller_id in self.anchor_sellers
+    def is_anchor_actor(self, actor_id):
+        return actor_id in self.anchor_actors
```

Если class name используется в импортах, обновить импорты во всех файлах:

```diff
-from app.trusted_baseline import TrustedSellerBaseline
+from app.trusted_baseline import TrustedActorBaseline
```

## app/security.py

Что меняется: HMAC-логика не меняется. Переименовываются только payload-поля `seller_id/listing_id` в `actor_id/event_id`, а `SYSTEM_META.model_version` меняется на `"entropy-rg-v3.0-domain-neutral"`.

### Unified diff

```diff
--- a/app/security.py
+++ b/app/security.py
@@
 SYSTEM_META = {
-    "model_version": "entropy-rg-v2.2-final",
+    "model_version": "entropy-rg-v3.0-domain-neutral",
 }

@@
-def canonicalize_score_payload(seller_id, listing_id, score_payload):
+def canonicalize_score_payload(actor_id, event_id, score_payload):
@@
     payload = {
-        "seller_id": seller_id,
-        "listing_id": listing_id,
+        "actor_id": actor_id,
+        "event_id": event_id,
         "score_payload": score_payload,
         "model_version": SYSTEM_META["model_version"],
     }
     return canonical_json(payload)

@@
-# HMAC sealing for seller/listing scoring payloads.
+# HMAC sealing for actor/event scoring payloads.
```

Запрещено менять:

```python
hmac.new(...)
hashlib.sha256(...)
canonical_json(...)
```

Если в файле есть CSV injection protection, оставить логику без изменений, заменить только комментарии `seller/listing` на `actor/event`.

## app/explanations.py

Что меняется: человекочитаемые explanations переводятся на нейтральные формулировки. Коды причин по возможности сохранить, если они уже используются тестами; если коды содержат seller/listing, добавить alias-map на одну версию.

### Unified diff

```diff
--- a/app/explanations.py
+++ b/app/explanations.py
@@
-REASON_TEXT = {
-    "new_seller_high_activity": "New seller has unusually high posting activity.",
-    "price_deviation": "Listing price deviates from category baseline.",
-    "contact_reuse": "Seller contact identity is reused across multiple accounts.",
-}
+REASON_TEXT = {
+    "new_actor_high_activity": "New actor has unusually high event emission activity.",
+    "value_deviation": "Event value deviates from topic baseline.",
+    "identity_reuse": "Actor identity is reused across multiple entities or contexts.",
+}

@@
+# Deprecated reason aliases retained for one version.
+DEPRECATED_REASON_ALIASES = {
+    "new_seller_high_activity": "new_actor_high_activity",
+    "price_deviation": "value_deviation",
+    "contact_reuse": "identity_reuse",
+}

@@
-def explain_seller_score(score_payload):
+def explain_actor_score(score_payload):
@@
-    seller_id = score_payload.get("seller_id")
+    actor_id = score_payload.get("actor_id")
@@
-    return f"Seller {seller_id}: {summary}"
+    return f"Actor {actor_id}: {summary}"
```

Если в коде используются старые reason codes как внешняя часть API, оставить старые коды как deprecated aliases до v4.0.

## app/calibration.py

Что меняется: calibration-логика не меняется. Меняются имена входных файлов, колонок, переменных и отчётных подписей.

### Unified diff

```diff
--- a/app/calibration.py
+++ b/app/calibration.py
@@
-SELLERS_CSV = "data/sellers.csv"
-LISTINGS_CSV = "data/listings.csv"
+ACTORS_CSV = "data/actors.csv"
+EVENTS_CSV = "data/events.csv"

@@
-def load_sellers(path=SELLERS_CSV):
+def load_actors(path=ACTORS_CSV):
     return pd.read_csv(path)

@@
-def load_listings(path=LISTINGS_CSV):
+def load_events(path=EVENTS_CSV):
     return pd.read_csv(path)

@@
-def calibrate_seller_scores(sellers, listings):
+def calibrate_actor_scores(actors, events):
@@
-    for _, seller in sellers.iterrows():
-        seller_listings = listings[listings["seller_id"] == seller["seller_id"]]
-        score = score_seller(seller.to_dict(), seller_listings.to_dict("records"))
+    for _, actor in actors.iterrows():
+        actor_events = events[events["actor_id"] == actor["actor_id"]]
+        score = score_actor(actor.to_dict(), actor_events.to_dict("records"))
         scores.append(score["final_score"])
     return scores
```

Если графики имеют названия вроде `"Seller score distribution"`, заменить на `"Actor score distribution"`.

## app/api.py

Что меняется: API принимает `actor_id/event_id/topic_id`. Добавляются новые route. Старые route сохраняются как deprecated aliases на одну версию и вызывают новые handlers.

### Unified diff

```diff
--- a/app/api.py
+++ b/app/api.py
@@
-class ScoreRequest(BaseModel):
-    seller_id: str
-    listing_id: str | None = None
-    category_id: str | None = None
+class ScoreRequest(BaseModel):
+    actor_id: str
+    event_id: str | None = None
+    topic_id: str | None = None
     features: dict

@@
-@app.post("/score")
-def score(request: ScoreRequest):
-    result = score_seller_by_id(
-        seller_id=request.seller_id,
-        listing_id=request.listing_id,
-        features=request.features,
-    )
+@app.post("/score")
+def score(request: ScoreRequest):
+    result = score_actor_by_id(
+        actor_id=request.actor_id,
+        event_id=request.event_id,
+        features=request.features,
+    )
     return result

@@
-@app.get("/seller/{seller_id}")
-def get_seller(seller_id: str):
-    return repository.get_seller(seller_id)
+@app.get("/actor/{actor_id}")
+def get_actor(actor_id: str):
+    return repository.get_actor(actor_id)

@@
-@app.get("/listing/{listing_id}")
-def get_listing(listing_id: str):
-    return repository.get_listing(listing_id)
+@app.get("/event/{event_id}")
+def get_event(event_id: str):
+    return repository.get_event(event_id)
```

### Deprecated aliases for one version

```diff
--- a/app/api.py
+++ b/app/api.py
@@
+class DeprecatedScoreRequest(BaseModel):
+    seller_id: str
+    listing_id: str | None = None
+    category_id: str | None = None
+    features: dict
+
+
+@app.post("/score-seller", deprecated=True)
+def score_seller_deprecated(request: DeprecatedScoreRequest):
+    migrated = ScoreRequest(
+        actor_id=request.seller_id,
+        event_id=request.listing_id,
+        topic_id=request.category_id,
+        features=request.features,
+    )
+    return score(migrated)
+
+
+@app.get("/seller/{seller_id}", deprecated=True)
+def get_seller_deprecated(seller_id: str):
+    return get_actor(seller_id)
+
+
+@app.get("/listing/{listing_id}", deprecated=True)
+def get_listing_deprecated(listing_id: str):
+    return get_event(listing_id)
```

### Пример нового POST /score

```json
{
  "actor_id": "actor_001",
  "event_id": "event_1001",
  "topic_id": "electronics",
  "features": {
    "avg_value_deviation": 0.72,
    "emission_frequency": 0.61,
    "duplicate_text_ratio": 0.18,
    "duplicate_media_ratio": 0.22,
    "identity_reuse_score": 0.44,
    "actor_age_days": 19,
    "reputation_score": 4.2,
    "endorsement_count": 18
  }
}
```

Старый формат с `seller_id/listing_id/category_id` поддерживается только через deprecated endpoint или через compatibility adapter, но основной `/score` должен принимать `actor_id/event_id/topic_id`.

## app/main.py

Что меняется: точки входа, загрузка CSV и CLI-команды переводятся на `actor/event`.

### Unified diff

```diff
--- a/app/main.py
+++ b/app/main.py
@@
-from app.scoring import score_seller
+from app.scoring import score_actor

@@
-def run_demo(sellers_path="data/sellers.csv", listings_path="data/listings.csv"):
-    sellers = load_csv(sellers_path)
-    listings = load_csv(listings_path)
-    for seller in sellers:
-        seller_listings = [row for row in listings if row["seller_id"] == seller["seller_id"]]
-        print(score_seller(seller, seller_listings))
+def run_demo(actors_path="data/actors.csv", events_path="data/events.csv"):
+    actors = load_csv(actors_path)
+    events = load_csv(events_path)
+    for actor in actors:
+        actor_events = [row for row in events if row["actor_id"] == actor["actor_id"]]
+        print(score_actor(actor, actor_events))
```

Если есть argparse-опции:

```diff
--- a/app/main.py
+++ b/app/main.py
@@
-parser.add_argument("--sellers", default="data/sellers.csv")
-parser.add_argument("--listings", default="data/listings.csv")
+parser.add_argument("--actors", default="data/actors.csv")
+parser.add_argument("--events", default="data/events.csv")
```

Deprecated CLI aliases можно оставить на одну версию, если это уже используется в скриптах:

```python
parser.add_argument("--sellers", default=None, help="Deprecated alias for --actors")
parser.add_argument("--listings", default=None, help="Deprecated alias for --events")
```

## app/dashboard.py

Что меняется: Streamlit dashboard должен показывать `actors/events/topics`, но scoring-графики и значения остаются теми же.

### Unified diff

```diff
--- a/app/dashboard.py
+++ b/app/dashboard.py
@@
-st.title("Entropy-RG Seller Anomaly Detector")
+st.title("Entropy-RG Domain-Neutral Anomaly Detector")

@@
-sellers = pd.read_csv("data/sellers.csv")
-listings = pd.read_csv("data/listings.csv")
+actors = pd.read_csv("data/actors.csv")
+events = pd.read_csv("data/events.csv")

@@
-selected_seller = st.selectbox("Seller", sellers["seller_id"].tolist())
-seller = sellers[sellers["seller_id"] == selected_seller].iloc[0].to_dict()
-seller_listings = listings[listings["seller_id"] == selected_seller].to_dict("records")
-result = score_seller(seller, seller_listings)
+selected_actor = st.selectbox("Actor", actors["actor_id"].tolist())
+actor = actors[actors["actor_id"] == selected_actor].iloc[0].to_dict()
+actor_events = events[events["actor_id"] == selected_actor].to_dict("records")
+result = score_actor(actor, actor_events)

@@
-st.metric("Seller risk score", result["final_score"])
+st.metric("Actor anomaly score", result["final_score"])

@@
-st.dataframe(seller_listings)
+st.dataframe(actor_events)
```

Старый dashboard-текст вроде `fraud seller`, `marketplace moderation`, `listing anomaly` заменить на `actor anomaly`, `event anomaly`, `domain-neutral scoring`. Marketplace можно оставить только в отдельном блоке `Reference marketplace demo`.

## state_store.py, если файл существует

В задании state_store.py не указан в списке затрагиваемых файлов, но отдельно сказано: структуру `state_store.py` не менять, только переименовать поля `seller_id -> actor_id`. Если файл есть в архиве, применить следующий патч.

### Unified diff

```diff
--- a/app/state_store.py
+++ b/app/state_store.py
@@
-def get_sequence_state(self, seller_id):
+def get_sequence_state(self, actor_id):
@@
-    return self.conn.execute("SELECT * FROM sequence_state WHERE seller_id = ?", (seller_id,))
+    return self.conn.execute("SELECT * FROM sequence_state WHERE actor_id = ?", (actor_id,))

@@
-def save_sequence_state(self, seller_id, state):
+def save_sequence_state(self, actor_id, state):
@@
-    state["seller_id"] = seller_id
+    state["actor_id"] = actor_id
```

SQLite-структура не должна усложняться и не должна получать новые таблицы. Если уже есть миграционный скрипт, добавить только rename column. Если SQLite-таблица создаётся с нуля, заменить `seller_id` на `actor_id` в DDL.

## data/sellers.csv и data/listings.csv

Что меняется: файлы переименовываются в `data/actors.csv` и `data/events.csv`. Колонки переводятся согласно mapping ниже. Значения строк не меняются.

Подробнее см. раздел 4.

## README.md

Что меняется: основной текст становится доменно-нейтральным. Marketplace остаётся только как reference-домен для тестирования.

### Блок «Было / Стало»

Было:

```markdown
# Entropy-RG Confinement Anomaly Detector

Detector of suspicious sellers and listings on a marketplace.
```

Стало:

```markdown
# Entropy-RG Domain-Neutral Anomaly Detector

Domain-neutral anomaly scoring core for actors and events across data platforms.
The package computes multi-component anomaly scores using confinement/residue,
sequential evidence, large-deviation surprise, graph/context features and
confluence logic.

This package is the algorithmic scoring core of the Futurolog project.
Marketplace examples remain as a reference domain and can be used for testing.
```

Было:

```markdown
The system scores sellers using listings, categories, regions and price deviations.
```

Стало:

```markdown
The system scores actors using events, topics, locations and value deviations.
A marketplace can still be represented as one reference domain:
seller -> actor, listing -> event, category -> topic, region -> location.
```

Добавить раздел:

```markdown
## Domain model

- actor: entity that emits or participates in events.
- event: atomic observation received from a source.
- topic: thematic grouping used for baselines and coupling profiles.
- location: spatial or logical context.
- evidence: selected event or artifact used to support or refute a score.
```

Yang-Mills/research inspiration section оставить без изменения смысла. Если там говорится `seller/listing`, заменить только примеры на `actor/event`.

## docs/TECHNICAL_SPECIFICATION.md

Что меняется: спецификация должна описывать Entropy-RG как algorithmic core, а не marketplace-only detector.

### Блок «Было / Стало»

Было:

```markdown
Entropy-RG detects suspicious marketplace sellers by evaluating their listings,
categories, price deviations and contact reuse.
```

Стало:

```markdown
Entropy-RG detects structurally persistent anomalies in domain-neutral data
streams by evaluating actors, events, topics, value deviations and identity reuse.
Marketplace detection remains a reference profile, not the core domain.
```

Добавить параграф:

```markdown
## Role in Futurolog

Entropy-RG v3.0-domain-neutral is the algorithmic scoring core of the Futurolog
project. ENRA provides orchestration, priority lanes, audit path and compensation
events. Entropy-RG provides component scores, confluence logic and explanations.
The integration boundary is the ScoringInput -> ScoringOutput contract.
```

Добавить contract:

```python
class ScoringInput:
    actor_id: str
    event_id: str | None
    topic_id: str | None
    features: dict
    history_window: dict | None
    graph_context: dict | None
    baseline_context: dict | None

class ScoringOutput:
    component_scores: dict
    confluence_bonus: float
    final_score: float
    risk_level: str
    reasons: list[str]
    model_version: str
```

Не добавлять новые scoring-компоненты. Если в спецификации упоминается `gibbs` как уже существующий термин, оставить. Если `gibbs` не реализован в коде v2.2, не добавлять его в код в рамках этой миграции.

## 4. Изменения в данных

### Новые имена CSV

```text
data/sellers.csv  -> data/actors.csv
data/listings.csv -> data/events.csv
```

### Маппинг колонок sellers.csv -> actors.csv

| Старый CSV | Новый CSV | Комментарий |
|---|---|---|
| `seller_id` | `actor_id` | Идентификатор субъекта |
| `seller_name` | `actor_name` | Если колонка есть |
| `category` | `topic` | Если actor имеет primary category |
| `category_id` | `topic_id` | Если actor имеет primary category_id |
| `region` | `location` | География или логический контекст |
| `reviews_count` | `endorsement_count` | Количество подтверждений/оценок |
| `rating` | `reputation_score` | Репутационная оценка |
| `account_age_days` | `actor_age_days` | Возраст actor |
| `verified` | `verified_actor` | Признак верификации |
| `posting_frequency` | `emission_frequency` | Частота генерации событий |
| `contact_reuse_score` | `identity_reuse_score` | Переиспользование идентичности |
| `trusted_seller` | `trusted_actor` | Если колонка есть |
| `anchor_seller` | `anchor_actor` | Если колонка есть |

Если в фактическом `sellers.csv` есть дополнительные колонки, не удалять их автоматически. Применить правило:

```text
seller_* -> actor_*
*_seller_* -> *_actor_*
marketplace-only field -> оставить только в reference profile или вынести в features
```

Колонки без очевидного mapping пометить `REVIEW_REQUIRED`.

### Маппинг колонок listings.csv -> events.csv

| Старый CSV | Новый CSV | Комментарий |
|---|---|---|
| `listing_id` | `event_id` | Идентификатор события |
| `seller_id` | `actor_id` | Связь с actor |
| `category` | `topic` | Тематический контейнер |
| `category_id` | `topic_id` | Идентификатор темы |
| `region` | `location` | География или логический контекст |
| `price` | `value` | Если используется как generic numeric value |
| `avg_price_deviation` | `avg_value_deviation` | Универсальное отклонение значения |
| `posting_frequency` | `emission_frequency` | Если есть на уровне event |
| `duplicate_text_ratio` | `duplicate_text_ratio` | Без изменений |
| `duplicate_image_ratio` | `duplicate_media_ratio` | Медиа шире изображения |
| `created_at` | `created_at` | Без изменений |
| `updated_at` | `updated_at` | Без изменений |
| `title` | `title` | Без изменений |
| `description` | `description` | Без изменений |

Если в фактическом `listings.csv` есть marketplace-specific поля вроде `shipping_price`, `brand`, `condition`, не удалять их. Для domain-neutral core они должны оставаться в `features` или в `reference_marketplace_profile`.

### Пример actors.csv

```csv
actor_id,actor_name,topic,location,endorsement_count,reputation_score,actor_age_days,verified_actor,emission_frequency,identity_reuse_score
actor_001,Reference Actor A,electronics,UA-KYIV,128,4.8,940,true,0.18,0.02
actor_002,Reference Actor B,phones,UA-LVIV,12,3.9,21,false,0.76,0.41
actor_003,Reference Actor C,cars,UA-ODESA,43,4.2,180,true,0.33,0.10
```

### Пример events.csv

```csv
event_id,actor_id,topic_id,topic,location,value,avg_value_deviation,duplicate_text_ratio,duplicate_media_ratio,created_at
event_1001,actor_001,topic_electronics,electronics,UA-KYIV,1200,0.14,0.03,0.01,2026-05-01T10:00:00Z
event_1002,actor_002,topic_phones,phones,UA-LVIV,220,0.71,0.18,0.22,2026-05-01T10:05:00Z
event_1003,actor_003,topic_cars,cars,UA-ODESA,8500,0.39,0.07,0.05,2026-05-01T10:10:00Z
```

### CSV migration script

Рекомендуемый одноразовый скрипт:

```python
from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")

SELLER_TO_ACTOR = {
    "seller_id": "actor_id",
    "seller_name": "actor_name",
    "category": "topic",
    "category_id": "topic_id",
    "region": "location",
    "reviews_count": "endorsement_count",
    "rating": "reputation_score",
    "account_age_days": "actor_age_days",
    "verified": "verified_actor",
    "posting_frequency": "emission_frequency",
    "contact_reuse_score": "identity_reuse_score",
    "trusted_seller": "trusted_actor",
    "anchor_seller": "anchor_actor",
}

LISTING_TO_EVENT = {
    "listing_id": "event_id",
    "seller_id": "actor_id",
    "category": "topic",
    "category_id": "topic_id",
    "region": "location",
    "price": "value",
    "avg_price_deviation": "avg_value_deviation",
    "posting_frequency": "emission_frequency",
    "duplicate_text_ratio": "duplicate_text_ratio",
    "duplicate_image_ratio": "duplicate_media_ratio",
}

def rename_columns(input_file: str, output_file: str, mapping: dict) -> None:
    df = pd.read_csv(DATA_DIR / input_file)
    df = df.rename(columns={k: v for k, v in mapping.items() if k in df.columns})
    df.to_csv(DATA_DIR / output_file, index=False)

rename_columns("sellers.csv", "actors.csv", SELLER_TO_ACTOR)
rename_columns("listings.csv", "events.csv", LISTING_TO_EVENT)
```

## 5. Изменения в API

### Основной endpoint

`POST /score` теперь принимает `actor_id` вместо `seller_id`, `event_id` вместо `listing_id`, `topic_id` вместо `category_id`.

Новый request:

```json
{
  "actor_id": "actor_002",
  "event_id": "event_1002",
  "topic_id": "topic_phones",
  "features": {
    "avg_value_deviation": 0.71,
    "emission_frequency": 0.76,
    "duplicate_text_ratio": 0.18,
    "duplicate_media_ratio": 0.22,
    "identity_reuse_score": 0.41,
    "actor_age_days": 21,
    "reputation_score": 3.9,
    "endorsement_count": 12
  }
}
```

Новый response:

```json
{
  "actor_id": "actor_002",
  "event_id": "event_1002",
  "topic_id": "topic_phones",
  "component_scores": {
    "residue": 0.0,
    "sequential": 0.0,
    "surprise": 0.0,
    "graph": 0.0
  },
  "confluence_bonus": 0.0,
  "final_score": 0.0,
  "risk_level": "low",
  "reasons": [],
  "model_version": "entropy-rg-v3.0-domain-neutral"
}
```

Значения `0.0` здесь демонстрационные. Реальный response должен возвращать те же score, что v2.2 на эквивалентных данных.

### Новый GET endpoint

```text
GET /actor/{id}
```

Заменяет:

```text
GET /seller/{id}
```

### Дополнительный endpoint

```text
GET /event/{id}
```

Заменяет:

```text
GET /listing/{id}
```

### Deprecated aliases на одну версию

Сохранить на один релиз:

```text
POST /score-seller
GET /seller/{id}
GET /listing/{id}
```

Правила:

- aliases должны быть помечены `deprecated=True`, если используется FastAPI;
- aliases не должны содержать отдельную логику;
- aliases должны маппить старые поля на новые и вызывать новые handlers;
- в README указать срок удаления: `will be removed in v4.0`.

### Compatibility adapter

Для внутреннего использования можно добавить функцию:

```python
def migrate_legacy_score_request(payload: dict) -> dict:
    migrated = dict(payload)

    if "seller_id" in migrated and "actor_id" not in migrated:
        migrated["actor_id"] = migrated.pop("seller_id")

    if "listing_id" in migrated and "event_id" not in migrated:
        migrated["event_id"] = migrated.pop("listing_id")

    if "category_id" in migrated and "topic_id" not in migrated:
        migrated["topic_id"] = migrated.pop("category_id")

    features = migrated.get("features", {})
    feature_mapping = {
        "avg_price_deviation": "avg_value_deviation",
        "posting_frequency": "emission_frequency",
        "duplicate_image_ratio": "duplicate_media_ratio",
        "contact_reuse_score": "identity_reuse_score",
        "account_age_risk": "actor_age_risk",
        "rating_risk": "reputation_risk",
        "reviews_risk": "endorsement_risk",
    }

    for old, new in feature_mapping.items():
        if old in features and new not in features:
            features[new] = features.pop(old)

    migrated["features"] = features
    return migrated
```

Эта функция не должна менять score. Она только переименовывает ключи.

## 6. Изменения в README и TECHNICAL_SPECIFICATION

### README.md: обязательные изменения

Основная формулировка:

```markdown
Entropy-RG v3.0-domain-neutral is a domain-neutral anomaly scoring core.
It evaluates actors and events across topics using multi-component scoring:
residue, sequential evidence, large-deviation surprise, graph/context features
and confluence logic.
```

Добавить:

```markdown
## Role in Futurolog

This package is the algorithmic core of the Futurolog project. ENRA provides
orchestration, priority queues, audit path, safety lane and compensation events.
Entropy-RG provides scoring functions, calibration, trusted baseline logic and
explanations.

Marketplace examples remain as a reference domain and can be used for testing.
They are not the core domain model.
```

Заменить терминологию:

```text
seller -> actor
listing -> event
category -> topic
region -> location
price deviation -> value deviation
contact reuse -> identity reuse
```

Оставить Yang-Mills context:

```markdown
The Yang-Mills/confinement language is used as research inspiration for
multi-scale persistence and information residue. It is not a runtime dependency
and should not be interpreted as a physical proof of model accuracy.
```

### TECHNICAL_SPECIFICATION.md: обязательные изменения

Добавить раздел:

```markdown
## Domain-neutral migration

v3.0-domain-neutral removes marketplace-specific naming from the core package.
The mathematical logic is unchanged. The migration only renames entities,
fields, variables, comments, docs and API routes.

Mapping:
- seller -> actor
- listing -> event
- category -> topic
- region -> location
```

Добавить integration boundary:

```markdown
## Integration boundary with ENRA

ENRA calls Entropy-RG through a stable scoring contract.

Input:
- actor_id
- event_id
- topic_id
- features
- history_window
- graph_context
- baseline_context

Output:
- component_scores
- confluence_bonus
- final_score
- risk_level
- reasons
- model_version
```

Уточнить:

```markdown
Entropy-RG does not own priority lanes, compensation workflows or audit
orchestration. Those belong to ENRA. Entropy-RG only computes scores and
explanations.
```

### Запрещённые изменения в документации

Не писать:

```text
The system predicts the future.
The system guarantees early detection.
The system proves real-world causality.
The system uses Yang-Mills equations to calculate risk.
```

Писать:

```text
The system scores structurally persistent anomalies and weak signals.
The system supports auditable early-warning workflows.
The system uses Yang-Mills/confinement as research inspiration only.
```

## 7. Тест-чеклист после миграции

### 7.1. Статический поиск старых терминов

Команды:

```bash
grep -R "seller" -n app README.md docs || true
grep -R "listing" -n app README.md docs || true
grep -R "category" -n app README.md docs || true
grep -R "region" -n app README.md docs || true
grep -R "avg_price_deviation" -n app README.md docs data || true
grep -R "posting_frequency" -n app README.md docs data || true
grep -R "duplicate_image_ratio" -n app README.md docs data || true
grep -R "contact_reuse_score" -n app README.md docs data || true
```

Ожидание:

- в основном коде старые термины отсутствуют;
- допускаются только deprecated aliases и reference marketplace examples;
- все допустимые старые термины должны быть явно помечены `deprecated` или `reference`.

### 7.2. Проверка model_version

Команда:

```bash
grep -R "model_version" -n app
```

Ожидание:

```text
SYSTEM_META.model_version = "entropy-rg-v3.0-domain-neutral"
```

или эквивалент в словаре:

```python
SYSTEM_META = {"model_version": "entropy-rg-v3.0-domain-neutral"}
```

### 7.3. Pytest

Если в проекте есть тесты:

```bash
pytest -q
```

Ожидание:

```text
all tests passed
```

Если тестов нет, создать минимальный smoke test для scoring contract:

```python
def test_score_actor_contract():
    actor = {
        "actor_id": "actor_001",
        "actor_age_days": 100,
        "reputation_score": 4.5,
        "endorsement_count": 20,
        "emission_frequency": 0.2,
        "identity_reuse_score": 0.0,
    }
    events = [
        {
            "event_id": "event_001",
            "actor_id": "actor_001",
            "topic": "electronics",
            "location": "UA-KYIV",
            "avg_value_deviation": 0.1,
            "duplicate_text_ratio": 0.0,
            "duplicate_media_ratio": 0.0,
        }
    ]

    result = score_actor(actor, events)

    assert "actor_id" in result
    assert "final_score" in result
    assert "component_scores" in result
```

### 7.4. Healthcheck

Если есть `healthcheck.py`:

```bash
python healthcheck.py
```

Ожидание:

```text
OK
```

Если healthcheck принимает endpoint:

```bash
python healthcheck.py --url http://localhost:8000
```

### 7.5. API smoke test

Запуск API:

```bash
uvicorn app.api:app --reload --port 8000
```

Проверка нового `/score`:

```bash
curl -s -X POST http://localhost:8000/score \
  -H "Content-Type: application/json" \
  -d '{
    "actor_id": "actor_002",
    "event_id": "event_1002",
    "topic_id": "topic_phones",
    "features": {
      "avg_value_deviation": 0.71,
      "emission_frequency": 0.76,
      "duplicate_text_ratio": 0.18,
      "duplicate_media_ratio": 0.22,
      "identity_reuse_score": 0.41,
      "actor_age_days": 21,
      "reputation_score": 3.9,
      "endorsement_count": 12
    }
  }'
```

Ожидание:

- HTTP 200;
- response содержит `actor_id`;
- response содержит `final_score`;
- response содержит `model_version = "entropy-rg-v3.0-domain-neutral"`.

Проверка deprecated alias:

```bash
curl -s -X POST http://localhost:8000/score-seller \
  -H "Content-Type: application/json" \
  -d '{
    "seller_id": "actor_002",
    "listing_id": "event_1002",
    "category_id": "topic_phones",
    "features": {
      "avg_price_deviation": 0.71,
      "posting_frequency": 0.76,
      "duplicate_text_ratio": 0.18,
      "duplicate_image_ratio": 0.22,
      "contact_reuse_score": 0.41
    }
  }'
```

Ожидание:

- HTTP 200;
- response в новом формате;
- score совпадает с `/score` на эквивалентном payload.

### 7.6. Проверка неизменности score

Перед миграцией сохранить baseline output:

```bash
python app/main.py --sellers data/sellers.csv --listings data/listings.csv > /tmp/v2_scores.jsonl
```

После миграции:

```bash
python app/main.py --actors data/actors.csv --events data/events.csv > /tmp/v3_scores.jsonl
```

Сравнить `final_score`:

```python
import json
from pathlib import Path

def load_scores(path):
    rows = []
    for line in Path(path).read_text().splitlines():
        if not line.strip():
            continue
        rows.append(json.loads(line))
    return rows

v2 = load_scores("/tmp/v2_scores.jsonl")
v3 = load_scores("/tmp/v3_scores.jsonl")

assert len(v2) == len(v3)

for old, new in zip(v2, v3):
    assert abs(old["final_score"] - new["final_score"]) < 1e-9
```

Если output не JSONL, адаптировать parser, но критерий остаётся тем же:

```text
score_seller на старых данных == score_actor на переименованных данных
```

### 7.7. Проверка Streamlit dashboard

Команда:

```bash
streamlit run app/dashboard.py
```

Ожидание:

- dashboard открывается;
- заголовки говорят `Actor`, `Event`, `Topic`;
- score components отображаются;
- загрузка `data/actors.csv` и `data/events.csv` проходит без ошибок.

### 7.8. Проверка CSV migration

Команды:

```bash
python scripts/migrate_csv_domain_neutral.py
python - <<'PY'
import pandas as pd

actors = pd.read_csv("data/actors.csv")
events = pd.read_csv("data/events.csv")

required_actor_cols = {
    "actor_id",
    "actor_age_days",
    "reputation_score",
    "endorsement_count",
}

required_event_cols = {
    "event_id",
    "actor_id",
    "topic",
    "location",
    "avg_value_deviation",
}

missing_actor = required_actor_cols - set(actors.columns)
missing_event = required_event_cols - set(events.columns)

assert not missing_actor, missing_actor
assert not missing_event, missing_event

print("CSV migration OK")
PY
```

### 7.9. Проверка HMAC/audit

Команда зависит от фактического интерфейса. Минимальная проверка:

```bash
python - <<'PY'
from app.security import SYSTEM_META

assert SYSTEM_META["model_version"] == "entropy-rg-v3.0-domain-neutral"
print("model_version OK")
PY
```

Если есть функция sealing:

```bash
python - <<'PY'
from app.security import canonicalize_score_payload, seal_payload

payload = canonicalize_score_payload(
    actor_id="actor_001",
    event_id="event_001",
    score_payload={"final_score": 0.42},
)

sealed = seal_payload(payload)

assert sealed
print("HMAC sealing OK")
PY
```

### 7.10. Проверка отсутствия изменений чисел

Команды:

```bash
grep -R "DEFAULT_WEIGHTS" -n app
grep -R "residue_threshold" -n app
grep -R "persistence_threshold" -n app
grep -R "30" -n app/scoring.py
grep -R "55" -n app/scoring.py
grep -R "75" -n app/scoring.py
grep -R "85" -n app/scoring.py
```

Ожидание:

- веса совпадают с v2.2;
- пороги совпадают с v2.2;
- risk levels 30/55/75/85 не изменены;
- diff не содержит изменения числовых значений в формулах.

## 8. Review notes и вопросы на ревью

### REVIEW_REQUIRED: фактические дополнительные CSV-колонки

В задании перечислены базовые поля, но фактические `sellers.csv` и `listings.csv` могут содержать дополнительные колонки. Для них правило такое:

- если колонка явно содержит `seller`, заменить на `actor`;
- если колонка явно содержит `listing`, заменить на `event`;
- если колонка явно содержит `category`, заменить на `topic`;
- если колонка явно содержит `region`, заменить на `location`;
- если колонка является marketplace-only, оставить в reference profile или в `features`;
- если нет уверенности, не выдумывать новое имя, пометить `REVIEW_REQUIRED`.

### REVIEW_REQUIRED: имена функций в реальном архиве

В этом документе используются ожидаемые имена вроде:

```text
score_seller
score_listing
compute_account_age_risk
compute_rating_risk
compute_reviews_risk
```

Если в архиве функции называются иначе, переименовать их по смыслу, но не менять тело формул.

### REVIEW_REQUIRED: наличие gibbs в коде

Архитектурный документ «Футуролога» упоминает `gibbs` как одну из компонент. В рамках этой миграции запрещено добавлять новую компоненту в код. Если `gibbs` уже есть в Entropy-RG v2.2, оставить. Если его нет, не добавлять и зафиксировать отдельную задачу.

### REVIEW_REQUIRED: SQLite column rename

Если существующие SQLite-таблицы уже созданы у пользователя, простой rename в коде может не совпасть со старой схемой. Для production-migration нужен отдельный миграционный скрипт:

```sql
ALTER TABLE sequence_state RENAME COLUMN seller_id TO actor_id;
```

Но если MVP пересоздаёт SQLite с нуля, достаточно поменять DDL.

## 9. Минимальный порядок применения патча

1. Создать ветку:

```bash
git checkout -b entropy-rg-v3-domain-neutral
```

2. Переименовать CSV:

```bash
mv data/sellers.csv data/actors.csv
mv data/listings.csv data/events.csv
```

3. Запустить CSV migration script.

4. Применить переименования в коде:

```bash
python - <<'PY'
from pathlib import Path

replacements = {
    "seller_id": "actor_id",
    "listing_id": "event_id",
    "category_id": "topic_id",
    "seller": "actor",
    "Seller": "Actor",
    "listing": "event",
    "Listing": "Event",
    "category": "topic",
    "Category": "Topic",
    "region": "location",
    "Region": "Location",
    "reviews_count": "endorsement_count",
    "rating": "reputation_score",
    "account_age_days": "actor_age_days",
    "verified": "verified_actor",
    "anchor_sellers": "anchor_actors",
    "trusted_sellers": "trusted_actors",
    "avg_price_deviation": "avg_value_deviation",
    "posting_frequency": "emission_frequency",
    "duplicate_image_ratio": "duplicate_media_ratio",
    "unique_regions": "unique_locations",
    "unique_categories": "unique_topics",
    "contact_reuse_score": "identity_reuse_score",
    "account_age_risk": "actor_age_risk",
    "rating_risk": "reputation_risk",
    "reviews_risk": "endorsement_risk",
    "CATEGORY_COUPLING": "TOPIC_COUPLING",
    "score_seller": "score_actor",
    "score_listing": "score_event",
}

paths = [
    Path("app"),
    Path("README.md"),
    Path("docs/TECHNICAL_SPECIFICATION.md"),
]

for root in paths:
    if root.is_file():
        files = [root]
    else:
        files = list(root.rglob("*.py")) + list(root.rglob("*.md"))

    for path in files:
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in replacements.items():
            new_text = new_text.replace(old, new)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
PY
```

Внимание: этот script делает механическое переименование. После него обязательно выполнить ручной review diff, потому что слова вроде `category` внутри example profile могут быть допустимы только в комментариях.

5. Вручную поправить API aliases.

6. Вручную проверить `SYSTEM_META.model_version`.

7. Запустить тест-чеклист.

8. Сравнить score до/после.

## 10. Критерии завершения миграции

Миграция считается завершённой, если:

- основной код использует `actor/event/topic/location`;
- старые `seller/listing/category/region` встречаются только в deprecated aliases или marketplace reference examples;
- `SYSTEM_META.model_version = "entropy-rg-v3.0-domain-neutral"`;
- `/score` принимает `actor_id`;
- `/actor/{id}` работает;
- deprecated `/seller/{id}` работает одну версию;
- `data/actors.csv` и `data/events.csv` загружаются;
- `final_score` на переименованных данных совпадает с v2.2;
- ни одна формула, константа, вес или порог не изменены;
- README и TECHNICAL_SPECIFICATION читаются как описание доменно-нейтрального scoring-core;
- marketplace описан только как reference-домен, а не как основная предметная область.
