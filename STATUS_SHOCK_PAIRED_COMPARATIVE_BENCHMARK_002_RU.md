# STATUS SHOCK PAIRED COMPARATIVE BENCHMARK 002

**Статус:** SOURCE_BACKED_COMPARATIVE_DESIGN / WORKING_BENCHMARK / NOT_CAUSAL_VALIDATION

## 1. Цель

Проверить не просто наличие статусного шока, а развилку ответа системы при сравнительно похожих потерях.

Ключевой вопрос:

`SIMILAR_STATUS_SHOCK -> DIFFERENT_POLITICAL_TRANSLATION ?`

Главный guard:

`IMPERIAL_STRATEGY != IMPERIAL_NEED`

Дополнительные guards:

`OBJECTIVE_LOSS != PERCEIVED_LOSS`

`LOSS_MEMORY != RESTORATION_NARRATIVE`

`RESTORATION_NARRATIVE != REVISIONIST_POLICY`

`EXTERNAL_CONSTRAINT != INTERNAL_VALUE_CHANGE`

`DECLARED_REFORM != ROBUST_STRATEGY_SWITCH`

## 2. Парный дизайн

### PAIR-1: Denmark 1864 vs France 1871

Общее:
- крупное военное поражение;
- территориальная потеря;
- сильный национальный статусный шок;
- память о потере сохраняется.

Различие, которое тестируем:
- Denmark: постфактум устойчивый национальный нарратив «выиграть внутри то, что потеряно вовне», внутреннее развитие/социальная консолидация;
- France: сильная память об Alsace-Lorraine и эпизоды реваншистской мобилизации, но память не равна непрерывной государственной политике немедленного реванша.

Важная оговорка: датская формула о прямой причинной цепочке `1864 defeat -> cooperatives/welfare/internal development` является сильным национальным нарративом, но современная историография оспаривает её как слишком простую причинность. Поэтому в benchmark кодируется observed political translation, а не доказанная монопричина.

### PAIR-2: Spain 1898 vs Italy 1919-1920

Общее:
- сильная статусная фрустрация вокруг результата войны/имперского положения;
- публичный кризис национального достоинства;
- поиск новой стратегии.

Различие:
- Spain: Regenerationism предлагает модернизацию и внутреннее обновление, но политическая и социальная фрагментация блокирует устойчивую общенациональную стратегию;
- Italy: «mutilated victory» становится каналом националистической мобилизации; Fiume даёт наблюдаемый переход от нарратива к территориально-ревизионистскому действию.

### PAIR-3: Austria 1918 vs Turkey 1918-1923

Общее:
- системный распад многонациональной империи;
- потеря старого центра легитимности;
- тяжёлый кризис идентичности.

Различие:
- Austria: поиск новой civic/national identity остаётся конфликтным и незавершённым;
- Turkey: national movement переводит статусный и суверенный кризис в строительство новой национальной политико-правовой формы вместо восстановления прежней имперской архитектуры.

### PAIR-4: Netherlands-Indonesia 1949-1962 vs France-Algeria 1958-1962

Общее:
- болезненная потеря крупной колониальной территории;
- необходимость заменить прямой политический контроль новой формой отношений;
- сильная память и остаточные конфликты.

Различие:
- Netherlands-Indonesia: formal sovereignty transfer не завершает колониальный/постколониальный конфликт; спор о New Guinea и экономических связях задерживает нормализацию;
- France-Algeria: de Gaulle постепенно переводит систему к negotiated decolonization; Evian Accords одновременно фиксируют независимость и новую рамку сотрудничества.

Этот pair нужен, чтобы не превращать `RELATIONSHIP_SUBSTITUTION` в бинарный yes/no: она может быть быстрой, конфликтной, неполной или отложенной.

## 3. Новая схема причинной дисциплины

Разводим четыре уровня:

1. `status_shock_source` — что произошло объективно;
2. `perceived_status_injury` — насколько это переживается как унижение/утрата;
3. `translation_mechanism` — политический перевод запроса;
4. `operational_strategy` — что реально делает государство/движение.

Нельзя переходить напрямую:

`LOSS -> NEED -> POLICY`

без наблюдаемого промежуточного механизма.

## 4. Основные переменные

- observed_loss_state
- perceived_loss_state
- status_frustration_signal
- switch_pressure_source
- switch_trigger
- translation_mechanism
- replacement_status_channel
- loss_memory_strength
- restoration_narrative_strength
- revisionist_policy_signal
- operational_strategy_state
- robust_switch_state

## 5. Предварительные ожидаемые контрасты — только для evaluator, не для blind packet

- Denmark: INWARD_RECONSTRUCTION / causal attribution guarded
- France: MEMORY_WITHOUT_CONTINUOUS_REVISION
- Spain: BLOCKED_RECONSTRUCTION
- Italy: REVISIONIST_TRANSLATION
- Austria: IDENTITY_REALIGNMENT
- Turkey: NATIONAL_REFOUNDATION
- Netherlands-Indonesia: DELAYED_RELATIONSHIP_SUBSTITUTION
- France-Algeria: NEGOTIATED_RELATIONSHIP_SUBSTITUTION

## 6. Критерий ценности теста

Гипотеза усиливается, если независимые кодировщики при скрытых странах:
- сходятся на силе статусного шока;
- но устойчиво различают translation path;
- не превращают память о потере в автоматический ревизионизм;
- не превращают внешнее ограничение в доказательство внутренней смены ценностей.

Если кодировщики не различают пары без знания исхода, механизм считается недостаточно операционализированным и rubric должен быть пересобран.
