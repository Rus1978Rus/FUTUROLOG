# DOMAIN_NEUTRAL_EVIDENCESTATE_ADAPTER v0.2 DRAFT

**Статус:** `REVISED_DRAFT_AFTER_MULTI_MODEL_AUDIT / CROSS_CASE_REPAIR_CANDIDATE / NOT_ACTIVE / NOT_CALIBRATED / NOT_VALIDATED`

## 1. Почему нужен v0.2

`EVIDENCE_STATE_ADAPTER_SPEC v0.1` остаётся неизменённым историческим артефактом. Он хорошо подходит к Russia–Ukraine pilot, но его primary classes:

```text
MILITARY_BUILDUP
DIPLOMATIC_COERCION_OR_WARNING
ECONOMIC_ENERGY_STRESS
```

не являются нейтральными для Мьянмы.

Поэтому v0.2 не заменяет v0.1 тихо, а создаётся как отдельный draft.

Guard:

```text
OLD_ADAPTER_LIMIT != PERMISSION_TO_REWRITE_HISTORY
```

## 2. Основной принцип

Вместо событийно-специфических primary classes используются domain-neutral pressure channels:

```text
P1 SECURITY_COERCION_AND_VIOLENCE
P2 INSTITUTIONAL_AND_POLITICAL_PRESSURE
P3 ECONOMIC_RESOURCE_AND_BASIC_NEEDS_STRESS
P4 SOCIAL_GROUP_MOBILIZATION_AND_FRAGMENTATION
P5 SERVICE_INFRASTRUCTURE_AND_HUMAN_SECURITY_DEGRADATION
P6 INFORMATION_ENVIRONMENT_AND_OBSERVATION_DISTORTION
```

Это adapter layer поверх уже собранных evidence domains, а не новая historical schema.

## 3. Atomic evidence rule

После `AGREEMENT_REPORT_001` обязательна атомизация mixed claims.

Одна evidence row должна выражать один основной тип утверждения. Если исходная публикация одновременно содержит:

- observed fact;
- projection;
- stabilizer/countermeasure;
- threat-perception signal;
- sensor-existence claim;
- retrospective synthesis;

они разделяются на отдельные atomic rows с общей provenance-ссылкой.

```text
MIXED_CLAIM => ATOMIZE_BEFORE_CODING
```

Пример: `observed skipped meals` и `3.4M projected hunger` не должны получать один общий strength.

## 4. Cutoff gate — механическое правило

Каждая atomic row сначала проходит cutoff gate:

```text
cutoff_admissibility = PASS | FAIL | CONDITIONAL
```

`PASS` — original publication time не позже конкретного snapshot cutoff.

`FAIL` — публикация/синтез позже cutoff или иначе запрещена frozen protocol.

`CONDITIONAL` — дата/публичная наблюдаемость ещё не доказана достаточно точно.

Для directional contribution действует жёсткое правило:

```text
CUTOFF_FAIL => pressure_signal = 0
CUTOFF_FAIL => stabilizer_signal = 0
CUTOFF_FAIL => event_strength = 0
CUTOFF_CONDITIONAL => NO_NUMERIC_CONTRIBUTION
```

При этом исходный claim не удаляется: он сохраняется в audit trail как excluded/conditional evidence.

## 5. Два независимых направления вместо одного знака

`AGREEMENT_REPORT_001` показал, что один scalar direction `+1/0/-1` теряет dual-use evidence.

Поэтому каждая admissible atomic row хранит отдельно:

```text
pressure_signal ∈ {0,1}
stabilizer_signal ∈ {0,1}
```

Оба могут быть `1`, если один и тот же observed fact legitimately содержит два разных аспекта, но предпочтительный путь — атомизация на две rows.

Примеры:

- создание продовольственного резерва: stabilizer signal;
- сам факт экстренной подготовки может отдельно быть threat-perception signal, но НЕ автоматически pressure event;
- заявление о защитных мерах: stabilizer/countermeasure;
- указание в том же заявлении на серьёзную угрозу: отдельный threat-perception claim.

Guards:

```text
COUNTERMEASURE_EXISTS != THREAT_REDUCTION
THREAT_PERCEPTION_SIGNAL != PRESSURE_EVENT
PRESSURE - STABILIZER != AUTOMATIC_RISK_SCORE
```

## 6. Message direction vs system direction

Для информационных claims отдельно хранятся:

```text
message_content_direction
system_pressure_role
```

Например, нарратив «угроза выдумана» по содержанию выглядит деэскалационным, но его роль в информационной операции может быть pressure/manipulation signal.

```text
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_DIRECTION
```

Нельзя кодировать system pressure только по буквальному тону сообщения.

## 7. Event strength отдельно от scale и quality

Главный patch v0.2:

```text
event_strength != coverage_scale
event_strength != evidence_quality
event_strength != confidence
```

Хранятся четыре разные оси:

```text
event_strength = 0 NONE | 1 WEAK | 2 SUBSTANTIAL | 3 SEVERE
coverage_scale = LOCAL | MULTI_LOCAL | REGIONAL | NATIONAL | CROSS_BORDER | UNKNOWN
evidence_quality = LOW | MEDIUM | HIGH
confidence = LOW | MEDIUM | HIGH
```

`event_strength` отвечает только на вопрос: насколько сильное изменение утверждает admissible evidence в своей наблюдаемой области.

`coverage_scale` отвечает: насколько широко эта область охвачена.

`evidence_quality` отвечает: насколько надёжен сам evidence item.

`confidence` отвечает: насколько уверенно выполнена кодировка с учётом ambiguities/limitations.

## 8. Severity anchors

Для admissible atomic rows:

### 0 NONE / NON-DIRECTIONAL
Нет directional event contribution; sensor-only, metadata-only, excluded, neutral descriptive record.

### 1 WEAK
Локальный/ограниченный или ранний directional signal без доказанного существенного system change.

### 2 SUBSTANTIAL
Явное и материальное изменение внутри наблюдаемого сегмента; устойчивое, повторяющееся или затрагивающее ключевую функцию, но без достаточной основы для `SEVERE`.

### 3 SEVERE
Операционно/системно тяжёлое изменение внутри заявленного scope: near-paralysis, large-scale coercive change, severe service breakdown или сопоставимый эффект. `SEVERE` не требует national coverage, но coverage_scale должен храниться отдельно.

Если coder не может отделить 2 от 3 из текста evidence, `ambiguity_status = HIGH` и item не используется для финальной calibration без review.

## 9. Sensor-only rule

Подтверждение существования сенсора/документа само по себе не является event strength:

```text
SENSOR_EXISTENCE != EVENT_STRENGTH
```

Для `SENSOR_ONLY`:

```text
event_strength = 0
pressure_signal = 0
stabilizer_signal = 0
sensor_status = PRESENT_VALUE_NOT_IMPORTED
```

Когда значение извлечено и валидировано, создаётся отдельная atomic evidence row.

## 10. Projection rule

Projection и observed fact разделяются:

```text
PROJECTION != OBSERVED_COUNT
```

Projection row получает:

```text
claim_mode = PROJECTED
```

Observed row:

```text
claim_mode = OBSERVED
```

Projection может быть evidence ожиданий/модели, но не повышает observed event strength как будто результат уже реализован.

## 11. Domain-neutral pressure channels

### P1 SECURITY_COERCION_AND_VIOLENCE
military buildup, coup coercion, conflict escalation, armed-group formation, direct security warnings.

### P2 INSTITUTIONAL_AND_POLITICAL_PRESSURE
diplomatic coercion, institutional breakdown, legitimacy pressure, repression, governance shock.

### P3 ECONOMIC_RESOURCE_AND_BASIC_NEEDS_STRESS
macro/energy stress, food/fuel prices, banking/payment disruption, affordability, resource capacity.

### P4 SOCIAL_GROUP_MOBILIZATION_AND_FRAGMENTATION
professional mobilization, protest/CDM, local defense emergence, coalescence/fragmentation, small-group shifts.

### P5 SERVICE_INFRASTRUCTURE_AND_HUMAN_SECURITY_DEGRADATION
displacement, health/education/water disruption, humanitarian access deterioration.

### P6 INFORMATION_ENVIRONMENT_AND_OBSERVATION_DISTORTION
disinformation, media repression, internet shutdown, sensor collapse, agenda amplification, representation–reality gap.

## 12. Channel availability

Channel AVAILABLE only if есть минимум один atomic item:

```text
cutoff_admissibility = PASS
source_family verified
original_publication_time verified
pipeline >= QUALITY_CHECKED
not RETROSPECTIVE_ONLY
not SENSOR_ONLY without imported event value
```

Missing channel не становится severity 0; он уменьшает coverage.

## 13. Channel aggregation — draft rule

Пока до calibration канал не получает один итоговый severity автоматически из максимума.

Запрещено:

```text
CHANNEL_SEVERITY = MAX(ITEM_STRENGTH)
```

по умолчанию, потому что один яркий локальный item может захватить весь канал.

До calibration channel summary хранит:

```text
max_item_strength
median_item_strength
number_of_atomic_items
source_family_count
coverage_scale_distribution
pressure_item_count
stabilizer_item_count
```

Финальная aggregation formula остаётся `REVIEW_REQUIRED`.

## 14. Evidence coverage и topology

Scalar coverage сохраняется только как служебная величина:

```text
evidence_coverage = available_channels / 6
```

и обязательно сопровождается topology matrix.

```text
SAME_COVERAGE_PERCENT != SAME_COVERAGE_TOPOLOGY
```

Каждый snapshot хранит:

```text
coverage_strength_by_segment
known_blind_spots
access_degradation
retrospective_only_segments
sensor_only_segments
underrepresented_groups
underrepresented_regions
underrepresented_platforms
```

## 15. Source independence

Сохраняется family-diversity heuristic как отдельная характеристика наблюдаемого набора, не как доказательство causal independence:

```text
HHI = sum(p_i^2)
raw_diversity = 1 - HHI
max_diversity = 1 - 1/n_families
source_independence = raw_diversity / max_diversity, if n_families > 1
source_independence = 0, if n_families = 1
```

```text
FAMILY_DIVERSITY != PROVEN_CAUSAL_INDEPENDENCE
```

## 16. Freshness

30-day pilot decay сохраняется только как историческая эвристика и помечается `REVIEW_REQUIRED`:

```text
item_freshness = max(0, 1 - age_days / 30)
```

Разные channels могут иметь разные естественные time constants; до calibration это не меняется тихо.

## 17. Pipeline completeness

Сохраняются 7 этапов:

```text
FETCHED
SOURCE_IDENTIFIED
ORIGINAL_PUBLICATION_TIME_VERIFIED
PARSED
NORMALIZED
QUALITY_CHECKED
SCORED
```

## 18. Counter-signals и observed noise

Stabilizer не вычитается автоматически из pressure.

Старую формулу `observed_noise` нельзя применять к dual-use/mixed items до атомизации и systematic negative-control search.

Поэтому:

```text
observed_noise = BLOCKED
```

до отдельного `NOISE_MODEL_REVIEW`.

## 19. Representation–Reality Gap

Для information/social claims хранятся независимо:

```text
AGENDA_VISIBILITY
AGENDA_SOCIAL_PREVALENCE
AGENDA_BEHAVIORAL_IMPACT
```

Неизвестные уровни остаются `UNKNOWN`.

## 20. Cross-case rule

Russia–Ukraine и Myanmar используют один набор domain-neutral channels, но numeric comparison не разрешается без topology annotation и одинаковой coding protocol version.

```text
SAME_ADAPTER != SAME_OBSERVABILITY
SAME_SCHEMA != SAME_MEASUREMENT_QUALITY
```

## 21. Multi-model audit lessons

`AGREEMENT_REPORT_001` показал:

- direction disagreement на dual-use evidence;
- strength disagreement на system scope;
- leakage risk, если `FAIL` item сохраняет ненулевой score;
- ambiguity из-за неявных cutoff boundaries;
- sensor-only confusion;
- projection/observation mixing.

Обязательные guards v0.2:

```text
CUTOFF_FAIL => DIRECTIONAL_CONTRIBUTION_ZERO
CUTOFF_FAIL => STRENGTH_CONTRIBUTION_ZERO
SIGNAL_STRENGTH != COVERAGE_SCALE
SIGNAL_STRENGTH != EVIDENCE_QUALITY
COUNTERMEASURE_EXISTS != THREAT_REDUCTION
THREAT_PERCEPTION_SIGNAL != PRESSURE_EVENT
SENSOR_EXISTENCE != EVENT_STRENGTH
MIXED_CLAIM => ATOMIZE_BEFORE_CODING
MESSAGE_CONTENT_DIRECTION != SYSTEM_PRESSURE_DIRECTION
```

## 22. Gate до активации

Перед переводом из DRAFT в `ACTIVE_CANDIDATE` нужно:

```text
1 FIRST_CODING_LEDGER_001 preserved
2 AGREEMENT_REPORT_001 preserved
3 ATOMIC_RECODE_PACKET_002 generated
4 multi-model recode on v0.2 completed
5 cutoff dates explicit for every packet item
6 negative-control targeted backfill materially improved
7 leakage audit passed
8 coverage topology attached
9 aggregation formula separately reviewed
10 true outcome-blind validation status explicitly resolved
```

Машинный multi-model recode может проверить rubric consistency, но не доказывает outcome-blind validation.

## 23. Статус

```text
DOMAIN_NEUTRAL_ADAPTER_v0_2_REVISED_DRAFT
MULTI_MODEL_AUDIT_PATCHES_APPLIED
ATOMICIZATION_REQUIRED
CUTOFF_ZEROING_RULE_ACTIVE_IN_DRAFT
DUAL_SIGNAL_MODEL_INTRODUCED
STRENGTH_SCALE_QUALITY_SEPARATED
CHANNEL_AGGREGATION_NOT_YET_CALIBRATED
NOT_ACTIVE
NOT_CALIBRATED
NOT_VALIDATED
NUMERIC_EVIDENCESTATE_STILL_BLOCKED
```
