# OBSERVATION & COVERAGE LAYER v0.1

**Статус:** `ARCHITECTURE_DRAFT / PRE-IMPLEMENTATION / NOT_VALIDATED`

## 1. Назначение

FUTUROLOG наблюдает не сам мир, а следы мира, прошедшие через СМИ, соцсети, мессенджеры, отчёты, статистику, архивы, датчики, ручные наблюдения и другие интерфейсы.

Поэтому система обязана моделировать не только объект наблюдения, но и сам процесс наблюдения.

Ключевой принцип:

```text
OBSERVABILITY != PREVALENCE
```

Наблюдаемость явления не равна его реальной распространённости.

## 2. Универсальные guards

```text
VISIBILITY != MAGNITUDE
REPORT_COUNT != EVENT_COUNT
EVENT_COUNT != POPULATION_RATE
VIRALITY != SOCIAL_PREVALENCE
VISIBLE_EXCEPTION != BASE_RATE
ABSENCE_OF_REPORTS != ABSENCE_OF_PHENOMENON
COLLECTABILITY != PREVALENCE
PLATFORM_VISIBILITY != SOCIAL_VISIBILITY
ACCESSIBLE_COMMUNITIES != REPRESENTATIVE_COMMUNITIES
INACCESSIBLE_SOURCE != IRRELEVANT_SOURCE
ACCESS_FAILURE_IS_DATA
NO_SINGLE_SOURCE_DEPENDENCY
```

## 3. Observation process

Для каждого сигнала хранить маршрут:

```text
REAL_PROCESS
→ EVENT_OR_STATE
→ TRACE
→ DETECTION
→ PUBLICATION
→ AMPLIFICATION
→ COLLECTION
→ NORMALIZATION
→ FUTUROLOG
```

Каждый переход может искажать картину.

## 4. Тип доступа к источнику

Минимальные значения:

- `DIRECT` — оригинальный разрешённо доступный источник;
- `OFFICIAL_API` — официальный API;
- `PUBLIC_WEB` — публичная страница/лента;
- `ARCHIVED` — архивная копия;
- `FORWARDED` — пересланный материал;
- `SECONDARY_REFERENCE` — пересказ другим источником;
- `HUMAN_IN_THE_LOOP` — материал получен человеком и передан системе;
- `PARTNER_DATA` — разрешённый партнёрский доступ;
- `INACCESSIBLE` — источник известен, но недоступен;
- `UNKNOWN_ACCESS_MODE` — способ получения не подтверждён.

## 5. Мессенджеры

FUTUROLOG не должен маскировать автоматический сборщик под человека ради обхода CAPTCHA, антибот-защиты, лимитов, блокировок или запретов платформ.

Разрешён режим `LOW_IMPACT_COLLECTION` — щадящий сбор через разрешённые интерфейсы: кэширование, отсутствие повторного скачивания, умеренная частота, официальные механизмы доступа.

Guards:

```text
ACCESS_DENIED != NO_ACTIVITY
BOT_BLOCKED != SOURCE_EMPTY
PRIVATE_CHANNEL != ZERO_SIGNAL
SAMPLE_OBSERVED != WHOLE_MESSENGER_SPACE
NEED_FOR_DATA != PERMISSION_TO_BYPASS_ACCESS_CONTROL
```

## 6. Coverage topology

Общий процент покрытия недостаточен.

Система должна хранить топологию покрытия по сегментам:

- государственные источники;
- оппозиционные источники;
- региональные сообщества;
- малые социальные группы;
- религиозные группы;
- профессиональные группы;
- диаспоры;
- традиционные СМИ;
- Telegram/другие мессенджеры;
- форумы;
- официальная статистика;
- локальные источники;
- международные источники.

Пример:

```text
coverage_total = 0.70
opposition_coverage = 0.28
regional_coverage = 0.74
small_group_coverage = 0.19
```

Это не одно и то же состояние системы.

## 7. Information operation / agenda distortion

Отдельно хранить:

- `AGENDA_VISIBILITY` — насколько тема заметна;
- `AGENDA_SOCIAL_PREVALENCE` — насколько она реально распространена;
- `AGENDA_BEHAVIORAL_IMPACT` — насколько тема влияет на поведение;
- `INFORMATION_AMPLIFICATION` — степень усиления;
- `COORDINATION_EVIDENCE` — свидетельства координации;
- `ATTRIBUTION_CONFIDENCE` — уверенность в источнике операции.

Guards:

```text
TRENDING != POPULATION_PREVALENCE
COORDINATION != STATE_OPERATION
BENEFITS_ACTOR_X != CAUSED_BY_ACTOR_X
FAKE_CLAIM != ZERO_REAL_WORLD_EFFECT
FOREIGN_ORIGIN != FOREIGN_CONTROL
ONLINE_MAJORITY != POPULATION_MAJORITY
INFORMATION_OPERATION != UNDERLYING_SOCIAL_PROCESS
```

Фейк может быть слабым свидетельством исходной реальности, но сильным свидетельством информационной активности и реального последующего поведенческого эффекта.

## 8. Representation-Reality Gap

Вводится отдельная диагностическая величина:

`REPRESENTATION_REALITY_GAP` — разрыв между информационной картиной и независимо наблюдаемой социальной/материальной реальностью.

Она не означает автоматически «СМИ врут».

## 9. Base-rate guard

Система обязана искать знаменатель.

Пример:

```text
10 нападений
```

без данных о размере группы, числе контактов, общей частоте взаимодействий и изменениях регистрации не дают честной оценки распространённости.

Если знаменатель неизвестен:

```text
BASE_RATE_STATUS = UNKNOWN
COVERAGE/CONFIDENCE ↓
```

## 10. Output contract

Минимальный выход слоя:

```text
source_access_mode
source_family
original_source_known
coverage_total
coverage_topology
base_rate_status
agenda_visibility
agenda_social_prevalence
agenda_behavioral_impact
representation_reality_gap
information_amplification
coordination_evidence
attribution_confidence
access_gaps
observation_bias_flags
```

## 11. Граница

Этот слой не определяет, истинно ли утверждение о мире. Он описывает качество и форму наблюдения.

```text
OBSERVATION_QUALITY != WORLD_TRUTH
```

## 12. Следующий шаг

Связать этот слой с `SOCIAL_GROUP_FIELD_v0_1` и затем заморозить историческую схему до массового наполнения кейсов Россия–Украина и Мьянма.