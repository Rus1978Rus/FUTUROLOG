# STATUS SHOCK TRANSLATION SCHEMA v0.2 — PATCH

DATE: 2026-08-16
STATUS: SCHEMA_PATCH / READY_FOR_NEXT_BENCHMARK / NOT_RUNTIME_RULE
SOURCE: multi-model review of `SSTB-001-V1`

## 1. Причина патча

`SSTB-001-V1` показал высокое согласие по итоговым траекториям, но несколько полей смешивают разные причинные уровни и провоцируют ложные межмодельные расхождения.

## 2. Новые раздельные оси

### 2.1 Память о потере

`loss_memory_strength = ABSENT | WEAK | SUBSTANTIAL | DOMINANT | UNKNOWN`

Это культурная/символическая память о потере.

Guard:

`LOSS_MEMORY != RESTORATION_NARRATIVE`

### 2.2 Реставрационный нарратив

`restoration_narrative_strength = ABSENT | WEAK | SUBSTANTIAL | DOMINANT | UNKNOWN`

Требует явного утверждения, что прежнее состояние/территория/иерархия должна быть восстановлена.

Guard:

`MEMORY_OF_LOSS != CLAIM_OF_REQUIRED_RESTORATION`

### 2.3 Давление на старую стратегию

`switch_pressure_source = NONE | INTERNAL_COST | EXTERNAL_CONSTRAINT | IDENTITY_CRISIS | LEGITIMACY_CRISIS | MILITARY_FAILURE | MIXED | UNKNOWN`

Это источник давления, а не сам момент переключения.

### 2.4 Триггер переключения

`switch_trigger = NONE | POLICY_DECISION | MATERIAL_FAILURE | EXTERNAL_BLOCK | ELITE_REALIGNMENT | INSTITUTIONAL_BREAK | NEGOTIATED_SETTLEMENT | MIXED | UNKNOWN`

Это наблюдаемый ближайший механизм перехода.

### 2.5 Политический перевод

`switch_translation_mechanism = NONE | POLITICAL_REFRAMING | ECONOMIC_REORIENTATION | NATIONAL_REFOUNDATION | INSTITUTIONAL_CONSOLIDATION | RELATIONSHIP_SUBSTITUTION | EXTERNAL_REDIRECTION | REVISIONIST_TRANSLATION | MIXED | UNKNOWN`

Это способ, которым новый курс был оформлен.

### 2.6 Направление идентичности

`identity_destination = OLD_SYSTEM_CONTINUITY | NEW_NATIONAL_IDENTITY | BROADER_EXTERNAL_IDENTITY | POST_IMPERIAL_IDENTITY | CONTESTED | UNKNOWN`

Это не то же самое, что replacement status channel.

Guard:

`IDENTITY_DESTINATION != STATUS_CHANNEL`

### 2.7 Канал замещения статуса

`replacement_status_channel = ABSENT | INTERNAL_DEVELOPMENT | ECONOMIC_PERFORMANCE | EXTERNAL_INTEGRATION | INSTITUTIONAL_PERFORMANCE | RELATIONSHIP_NETWORK | CULTURAL_STATUS | UNKNOWN`

### 2.8 Операционное состояние стратегии

`operational_strategy_state = OLD_STRATEGY_CONTINUES | SEARCHING | MIXED | SWITCHING | NEW_STRATEGY_ACTIVE | UNKNOWN`

### 2.9 Итоговая траектория

`dominant_translation_path = INWARD_RECONSTRUCTION | BLOCKED_RECONSTRUCTION | IDENTITY_REALIGNMENT | NATIONAL_REFOUNDATION | MEMORY_WITHOUT_REVISION | RELATIONSHIP_SUBSTITUTION | REVISIONISM | RESTORATION | EXTERNALLY_REDIRECTED | MIXED | UNKNOWN`

Step-level operational state не обязан совпадать по словарю с series-level dominant path.

## 3. Новые guards

`OBJECTIVE_LOSS != PERCEIVED_LOSS`

`PERCEIVED_LOSS != STATUS_FRUSTRATION`

`STATUS_FRUSTRATION != TERRITORIAL_NEED`

`LOSS_MEMORY != RESTORATION_NARRATIVE`

`RESTORATION_NARRATIVE != REVISIONIST_POLICY`

`ARMED_RESISTANCE_TO_SETTLEMENT != REVISIONIST_STATE_POLICY`

`FAILED_OR_TRANSIENT_RESTORATION_ATTEMPT != SUSTAINED_REVISIONIST_POLICY`

`EXTERNAL_CONSTRAINT != INTERNAL_VALUE_CHANGE`

`IDENTITY_DESTINATION != STATUS_CHANNEL`

`DECLARED_REFORM != ROBUST_STRATEGY_SWITCH`

`OPERATIONAL_STATE != DOMINANT_TRANSLATION_PATH`

## 4. Минимальная логика robust switch

`strategy_switch_evidence = NONE | EARLY | ROBUST | DIRECT | UNKNOWN`

ROBUST допускается только если наблюдается как минимум одно из:
- устойчивое институциональное перераспределение ресурсов;
- новая политика реализуется, а не только декларируется;
- новый канал статуса получает материальное или организационное выражение;
- прежний канал систематически теряет приоритет;
- изменение переживает минимум один последующий временной срез без возврата к исходной стратегии.

Guard:

`DECLARATION != ROBUST_SWITCH`

## 5. Следующий benchmark

Следующий тест должен специально содержать пары с похожим `perceived_loss_state/status_frustration_signal`, но разными:
- `switch_pressure_source`;
- `switch_trigger`;
- `identity_destination`;
- `replacement_status_channel`;
- `dominant_translation_path`.

Цель — проверить не угадывание истории, а способность различать механизм политического перевода сходного социального запроса.
