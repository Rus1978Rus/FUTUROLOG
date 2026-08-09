# PRE_EVIDENCESTATE_DRY_RUN 001

**Статус:** `NON_NUMERIC_DRY_RUN_COMPLETE / NUMERIC_EVIDENCESTATE_BLOCKED / SCHEMA_FREEZE_PRESERVED / NOT_VALIDATED`

## 1. Цель

Это первый нечисловой прогон исторического пилота по двум кейсам: Россия–Украина и Мьянма.

Прогон НЕ вычисляет итоговый риск, НЕ использует известный исход как вход и НЕ запускает формулы EvidenceState. Его задача — проверить, умеет ли замороженная схема описывать состояние системы на историческом cutoff, одновременно показывая давление, стабилизаторы, пробелы и искажения наблюдаемости.

## 2. Правила прогона

Используются только evidence items, допустимые по времени публикации для соответствующего snapshot. `RETROSPECTIVE_ONLY`, `SENSOR_ONLY` без извлечённого значения и непроверенные numeric claims не повышают состояние автоматически.

Ключевые guards:

```text
OBSERVABILITY != PREVALENCE
VISIBLE_EXCEPTION != BASE_RATE
PRESSURE != OUTCOME
RESOURCE_CAPACITY != INTENT
NARRATIVE_EXISTS != POPULATION_BELIEF
SENSOR_EXISTS != NUMERIC_VALUE_VALIDATED
EVIDENCE_GAP != ZERO_PHENOMENON
SAME_SCHEMA != SAME_OBSERVABILITY
```

## 3. Россия–Украина: нечисловое состояние до 24.02.2022

### Подтверждённые pressure domains

- военное наращивание / дипломатическое напряжение и предупреждения;
- макроэкономическая и энергетическая ресурсная способность России;
- напряжённость европейского газового рынка с несколькими возможными причинами;
- длительное displacement/contact-line pressure в восточной Украине;
- институциональные ограничения и уязвимости базовых публичных услуг;
- health/COVID pressure;
- локальная уязвимость доступа к воде и повреждения критической водной инфраструктуры на линии соприкосновения;
- информационные нарративы против Украины, наблюдаемые contemporaneously;
- различия политических и институциональных ожиданий внутри Украины.

### Подтверждённые stabilizers / counter-pressures

- международная security assistance и институциональная поддержка Украины;
- программы интеграции ВПЛ;
- образовательная и health-system adaptation;
- локальные проекты восстановления водоснабжения;
- продолжающаяся работа государственных и международных институтов;
- дипломатические каналы и санкционные механизмы как ограничивающие инструменты.

### Social Group / identity state

Есть рабочий contemporaneous religious-identity sensor: KIIS 2021 показывает неоднородную религиозную структуру и различия внутри православной самоидентификации. Это допустимо как социальная структура, но НЕ как автоматический proxy политической лояльности или конфликтности.

### Observation & Coverage state

Покрытие сильнее по formal institutions, macro/energy, polling, международным организациям и публичным disinformation catalogs. Покрытие слабее по повседневному household experience, закрытым информационным каналам, локальным малым группам и части региональных basic-needs процессов.

### Нечисловой вывод

К cutoff система должна была описывать ситуацию как **многодоменное состояние повышенного давления с одновременной работой заметных стабилизаторов и высокой неопределённостью относительно перехода к полномасштабной войне**. Корпус не оправдывает формулировку `WAR_CERTAIN` и не должен превращать ресурсную способность, угрозу или дезинформацию в доказанный исход.

## 4. Мьянма: нечисловое состояние после переворота 2021

### Подтверждённые pressure domains

- военный переворот и насильственное подавление протестов;
- Civil Disobedience Movement и расширение участия профессиональных групп;
- ухудшение интернет-доступа и независимой информационной среды;
- сильный macroeconomic, banking, payment and logistics shock;
- рост цен на еду и топливо с выраженной региональной неоднородностью;
- COVID/health-system pressure;
- displacement across multiple regions;
- occupation/disruption of educational facilities;
- возникновение множества local defense groups с различной степенью связи с NUG/PDF;
- конфликтное воздействие на этнические и религиозные меньшинства в ряде регионов;
- структурная climate/disaster vulnerability, усиливающая livelihood risk в отдельных районах.

### Подтверждённые stabilizers / counter-pressures

- гуманитарная помощь WFP, UNICEF, UNHCR и локальных сетей;
- community/religious assistance to displaced people;
- pre-existing education adaptation capacity;
- частичное улучшение mobility/logistics в отдельные периоды;
- diaspora humanitarian donations и CSO/CBO networks;
- документированные внешние пожертвования в структуры NUG.

### Social Group Field state

Корпус уже различает CDM professional groups, ethnic armed organizations, NUG-aligned PDF, independent local defense groups, religious/community networks и diaspora nodes. Наличие множества акторов НЕ интерпретируется как единый command structure.

### Observation & Coverage state

Наблюдаемость деградирует из-за internet shutdowns, давления на журналистов, локальности боевых действий и неполного доступа к районам. Weekly UNHCR displacement sensors подтверждены, но numeric values из карт пока не импортированы. Поэтому снижение числа сообщений или отсутствие чисел не означает отсутствие displacement/activity.

### Нечисловой вывод

На ранних и средних cutoff 2021 система должна была описывать Мьянму как **быстро фрагментирующуюся социально-политическую систему с расширяющимся междоменным давлением, ростом локальной вооружённой самоорганизации и одновременно сохраняющимися гуманитарными/общественными stabilizers**. Корпус поддерживает `ESCALATION_AND_FRAGMENTATION_SIGNAL`, но НЕ `UNIFIED_RESISTANCE`, НЕ `TOTAL_STATE_COLLAPSE` и НЕ доказанную единую causal chain.

## 5. Cross-case diagnostic

Схема смогла представить оба кейса без добавления нового архитектурного класса. Это `PASS` для schema expressiveness, но НЕ validation прогноза.

Ключевое различие наблюдаемости:

```text
RUSSIA_UKRAINE -> stronger formal/macro/polling/media observability
MYANMAR        -> stronger humanitarian/local-displacement/group-mobilization observability
```

Поэтому сравнение будущих числовых scores требует correction/annotation for coverage topology.

## 6. Что dry run выявил

`PASS`:
- pressure и stabilizer могут существовать одновременно;
- Social Group Field не требует отбрасывать малые группы;
- information activity можно хранить отдельно от social prevalence;
- missing numeric sensor data остаются UNKNOWN;
- retrospective material можно удерживать вне cutoff;
- одна и та же frozen schema применима к обоим кейсам.

`BLOCKED / PARTIAL`:
- numeric EvidenceState;
- honest observed_noise без систематического negative-control search;
- cross-case numeric comparison;
- Myanmar numeric displacement series;
- полная coverage topology;
- независимый second coding / coder-agreement test.

## 7. Решение по gate

```text
TARGETED_BACKFILL_008: PARTIAL_PASS
PRE_EVIDENCESTATE_DRY_RUN_001: PASS_WITH_LIMITATIONS
READY_FOR_NUMERIC_EVIDENCESTATE: NO
READY_FOR_LEAKAGE_AUDIT: YES
READY_FOR_NEGATIVE_CONTROL_BACKFILL: YES
READY_FOR_SECOND_CODING_CHECK: YES
SCHEMA_CHANGE_REQUIRED: NO
```

## 8. Следующий шаг

Не открывать широкий Batch 009.

Следующий порядок:

```text
LEAKAGE_AUDIT_001
→ NEGATIVE_CONTROL_BACKFILL_009
→ COVERAGE_TOPOLOGY_MATRIX_001
→ SECOND_CODING_CHECK
→ NUMERIC_EVIDENCESTATE_GATE_REVIEW
```

Только если gate review пройден, разрешается первый numeric EvidenceState snapshot.

## 9. Статус

```text
NON_NUMERIC_DRY_RUN_COMPLETE
PASS_WITH_LIMITATIONS
NUMERIC_EVIDENCESTATE_BLOCKED
SCHEMA_FREEZE_PRESERVED
FORECAST_VALIDATION_NOT_CLAIMED
NOT_VALIDATED
```
