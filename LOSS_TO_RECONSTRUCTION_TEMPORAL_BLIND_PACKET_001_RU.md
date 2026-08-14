# LOSS TO RECONSTRUCTION — TEMPORAL BLIND PACKET 001

PACKET_SCHEMA_ID: `LTR-TB-001-V1`

Статус: `READY_FOR_EXTERNAL_MULTI_MODEL_TEST / COUNTRY_LABELS_HIDDEN / TEMPORAL_ORDER_VISIBLE / OUTCOMES_HIDDEN`

## Цель

Определить, когда после крупной потери статуса, территории или прежней внешней роли система продолжает старую стратегию, переключается на внутреннюю реконструкцию, получает внешний запрет старой стратегии, переводит статусный запрос в ревизионизм либо переходит к controlled contraction.

## Guards

`IMPERIAL_STRATEGY != IMPERIAL_NEED`

`LOSS != REVISIONISM`

`STATUS_NEED != TERRITORIAL_NEED`

`MILITARY_FAILURE != AUTOMATIC_INTERNAL_RECONSTRUCTION`

`EXTERNAL_CONSTRAINT != INTERNAL_VALUE_CHANGE`

`ECONOMIC_SUCCESS_AFTER_LOSS != PROOF_OF_POLICY_CAUSATION`

`RESTORATION_NARRATIVE != POPULATION_WIDE_PRIMARY_NEED`

`MIXED_TRAJECTORY != CLASSIFICATION_FAILURE`

## Серии

### A
A-T0: длительная внешняя война и сохранение старой стратегии.

A-T1: после почти двух десятилетий войны начинается частичный дефолт по чрезвычайным инструментам военного финансирования.

A-T2: война завершается без восстановления прежнего масштаба внешнего доминирования; последствия финансирования продолжаются.

A-T3: длительная внутренняя политико-финансовая перестройка; отдельные военные авантюры всё ещё возможны.

### B
B-T0: полное военное поражение; военная база подлежит ликвидации/контролю; центр временно не полностью суверенен.

B-T1: внешние управляющие силы запрещают восстановление военного потенциала; мирная экономика становится допустимым каналом восстановления.

B-T2: крупная валютная/экономическая реформа институционализирует реконструкцию.

B-T3: статус восстанавливается через экономическую производительность и интеграцию, а не немедленное военное восстановление.

### C
C-T0: полное поражение; разоружение; крупная потеря внешних территорий.

C-T1: внешний режим демилитаризует промышленность и допускает мирную конверсию части мощностей.

C-T2: экономическая реконструкция развивается внутри сильного внешнего ограничения старой стратегии.

### D
D-T0: после большой войны центр сохраняет значительную внешнюю систему владений и говорит о постепенном самоуправлении периферии.

D-T1: часть переходов переговорная, часть движений подавляется силой.

D-T2: внешняя силовая операция прекращается под давлением более мощного союзника; предел старой внешней роли становится видимым.

D-T3: независимость периферий ускоряется; центр публично признаёт более быстрый демонтаж старой системы.

### E
E-T0: начинается длительный вооружённый конфликт за сохранение ключевой периферии.

E-T1: растут военная стоимость и внутренний политический кризис.

E-T2: внутри центра усиливается переход от «военного решения» к политическому самоопределению/переговорам.

E-T3: переговорная линия приводит к соглашению, прекращающему прежний формат контроля.

### F
F-T0: мирный договор фиксирует крупную территориальную и статусную потерю.

F-T1: пересмотр границ становится устойчивой политической темой.

F-T2: ревизионистская политика сохраняет высокую политическую значимость и территориальные требования.

F-T3: после нового потрясения ревизионистская тенденция остаётся наблюдаемой.

### G
G-T0: государство формально победитель, но часть националистов описывает результат как унизительно неполный.

G-T1: территориальные требования вызывают массовую националистическую мобилизацию; вооружённая группа самовольно занимает спорную территорию.

G-T2: нарратив «урезанной победы» усиливает чувство унижения несмотря на реальные приобретения.

G-T3: радикальный национализм становится одним из каналов политической мобилизации; не считать его единственной причиной последующего режима.

## Coding values

`observed_loss_state = NONE | LIMITED | MAJOR | SYSTEMIC | UNKNOWN`

`old_strategy_cost_visibility = LOW | RISING | HIGH | CRITICAL | UNKNOWN`

`status_frustration_signal = ABSENT | WEAK | SUBSTANTIAL | HIGH | UNKNOWN`

`internal_reconstruction_channel = ABSENT | EMERGING | ACTIVE | DOMINANT | UNKNOWN`

`external_constraint_strength = NONE | LIMITED | STRONG | DOMINANT | UNKNOWN`

`alternative_status_channel = ABSENT | EMERGING | ACTIVE | DOMINANT | UNKNOWN`

`restoration_narrative_strength = ABSENT | WEAK | SUBSTANTIAL | DOMINANT | UNKNOWN`

`revisionist_policy_signal = ABSENT | PRESENT_WEAK | PRESENT_STRONG | ACTIVE | UNKNOWN`

`strategy_translation_state = OLD_STRATEGY_CONTINUES | MIXED | INTERNAL_RECONSTRUCTION | CONTROLLED_CONTRACTION | REVISIONIST_TRANSLATION | EXTERNALLY_REDIRECTED | UNKNOWN`

`strategy_switch_evidence = NONE | EARLY | ROBUST | DIRECT | UNKNOWN`

`confidence = LOW | MEDIUM | HIGH`

## Series summary fields

- `first_old_strategy_cost_visible_step`
- `first_alternative_status_channel_step`
- `first_revisionist_translation_step`
- `first_robust_strategy_switch_step`
- `dominant_translation_path`

`dominant_translation_path = INTERNAL_RECONSTRUCTION | ECONOMIC_STATUS_SUBSTITUTION | CONTROLLED_CONTRACTION | REVISIONISM | RESTORATION_ATTEMPT | EXTERNALLY_REDIRECTED | MIXED | UNKNOWN`

## Protocol gate

Reject before scoring if real countries/events are named, later events are imported into earlier steps, external constraint is converted into internal value change, loss is automatically converted into revisionism, or economic success is treated as proof of causation.

External coder should receive only the DOCX/packet and return two CSV blocks according to schema `LTR-TB-001-V1`.