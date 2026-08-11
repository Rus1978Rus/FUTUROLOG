# PRE_THRESHOLD_CHRONOLOGY_SNAPSHOTS 001

**Статус:** `SOURCE_BACKED / PRE_THRESHOLD_FOCUS / FOUR_COMPARATIVE_PAIRS / READY_FOR_BLIND_PACKET_DERIVATION`

## 1. Цель

Собрать не ретроспективные объяснения исхода, а последовательные датированные срезы `t0 -> t1 -> t2` до или около порогового перехода. Будущий исход не должен использоваться как входной признак.

Ключевой guard:

```text
HISTORICAL_OUTCOME != INPUT_FEATURE
POST_EVENT_KNOWLEDGE != CUTOFF_KNOWLEDGE
```

## 2. Пара A — Россия 1917 ↔ Китай 1989

### A1. Россия — cutoff RUS-1917-T0

**Дата:** 25 февраля 1917 (старый стиль в дипломатических материалах / соответствующий мартовский период нового стиля).

Наблюдаемо по FRUS:
- Петроград помещён под военное положение из-за беспорядков.
- На этой точке императорская власть формально существует; исход не должен считаться заданным.

Источник: Office of the Historian, FRUS Russia, list of papers, запись 25 Feb 1917.

### A2. Россия — cutoff RUS-1917-T1

**Дата:** 14 марта 1917 по датировке телеграммы FRUS.

Наблюдаемо:
- Дума отказывается подчиниться приказу императора о роспуске.
- Организован Временный комитет/правительство.
- Часть полков присоединяется к революционерам.

Это уже не просто массовое недовольство, а наблюдаемая эрозия `COMMAND_EXECUTABILITY` и появление альтернативного центра.

Источник: Office of the Historian, FRUS Russia, list of papers.

### A3. Россия — threshold observation

**Дата:** 15–16 марта 1917 / 2–3 марта старого стиля.

Наблюдаемо:
- Николай II отрекается за себя и наследника.
- Михаил не принимает верховную власть до решения Учредительного собрания.
- Признаётся власть Временного правительства.

Источник: Office of the Historian, FRUS, сообщение российского посла и глава о мартовской революции.

### A4. Китай — cutoff CHN-1989-T0

**Дата:** 15 мая 1989.

Наблюдаемо по Office of the Historian:
- Протесты усиливаются на фоне визита Горбачёва.
- Начинаются голодовки.
- Международное внимание резко растёт.
- Масштаб участия расширяется за пределы студентов.

### A5. Китай — cutoff CHN-1989-T1

**Дата:** 20 мая 1989.

Наблюдаемо:
- Руководство вводит военное положение в Пекине.
- Протесты продолжаются.
- Государственный coercive capacity формально существует и переводится в режим применения, но финальный исход ещё не должен считаться известным.

### A6. Китай — threshold observation

**Дата:** ночь 3–4 июня 1989.

Наблюдаемо:
- НОАК входит в Пекин с танками и силой подавляет протесты.

Источник: U.S. Office of the Historian, `Tiananmen Square, 1989`.

### Сравниваемая переменная

```text
MASS_CRISIS
+ STATE_COERCIVE_CAPACITY
+ ALTERNATIVE_CENTER
+ COMMAND_EXECUTABILITY
+ ELITE/SECURITY_NODE_COHESION
```

Цель — проверить, почему наличие массового кризиса и формального силового ресурса само по себе не определяет, рухнет ли режим или coercive apparatus сохранит исполнение.

---

## 3. Пара B — Румыния 1989 ↔ Беларусь 2020

### B1. Румыния — structural background cutoff ROM-1989-T0

**Дата:** до декабря 1989; baseline подтверждён источниками, завершёнными до кризиса.

Library of Congress Country Study, исследование завершено в июле 1989, даёт pre-event baseline институциональной и социально-экономической системы. Отдельный UN Special Rapporteur report датирован 18 декабря 1989 и фиксирует состояние прав человека непосредственно перед финальным обвалом режима.

Дополнительный pre-event intelligence context: CIA ранее описывала тяжёлые экономические проблемы, низкий уровень жизни и персонализированное авторитарное правление Чаушеску; эти оценки являются prior/context, а не доказательством декабрьского исхода.

### B2. Румыния — cutoff ROM-1989-T1

**Дата:** 18 декабря 1989.

Наблюдаемо:
- Имеется официальный международный отчёт по нарушениям прав человека.
- Финальный переход власти ещё не является допустимым знанием на cutoff.

Важно: для blind benchmark этот срез должен использовать только факты, доступные не позднее 18 декабря.

### B3. Румыния — поздний threshold layer

**Дата:** 21–22 декабря 1989.

Этот слой будет заполняться отдельными contemporaneous источниками по Бухаресту и поведению силовых/партийных узлов. До завершения source extraction нельзя автоматически кодировать `elite defection` или `command collapse` как доказанные.

Статус: `SOURCE_EXTRACTION_PENDING`.

### B4. Беларусь — cutoff BLR-2020-T0

**Дата:** 10 августа 2020.

OSCE/ODIHR фиксирует:
- протесты после выборов 9 августа;
- непропорциональное применение силы полицией;
- многочисленные травмы и аресты;
- задержания наблюдателей и журналистов.

### B5. Беларусь — cutoff BLR-2020-T1

**Дата:** 13–19 августа 2020.

OSCE фиксирует:
- сообщения о rubber bullets, water cannons, stun grenades и массовых арестах;
- продолжающиеся массовые протесты;
- сообщения о пытках/жестоком обращении;
- необходимость диалога, но неизвестность его эффективности.

### B6. Беларусь — cutoff BLR-2020-T2

**Дата:** 17–28 августа 2020.

Наблюдаемо:
- OSCE предлагает визит и затем посредничество/фасилитацию диалога;
- протесты и поляризация продолжаются;
- наличие предложения о диалоге не равно работающему stabilizer.

### Сравниваемая переменная

```text
PUBLIC_DEFIANCE
+ COERCIVE_NODE_LOYALTY
+ COMMAND_EXECUTABILITY
+ ALTERNATIVE_POWER_CENTER
+ EXTERNAL_BACKING_EXPECTATION
```

Ключевой guard:

```text
APPARENT_COMPLIANCE != REGIME_SUPPORT
COERCIVE_CAPACITY_EXISTS != COERCIVE_CAPACITY_POLITICALLY_USABLE
```

---

## 4. Пара C — Беларусь 2020 ↔ Казахстан 2022

### C1. Беларусь — external support state

На август 2020 подтверждены внутреннее применение силы и политический кризис. Для этого benchmark нельзя автоматически кодировать ввод российских войск: такого ввода для подавления протестов не было подтверждено в используемом наборе.

Нужны отдельные поля:

```text
EXTERNAL_SUPPORT_AVAILABLE
EXTERNAL_SUPPORT_EXPECTED
EXTERNAL_FORCE_DEPLOYED
```

### C2. Казахстан — cutoff KAZ-2022-T0

**Дата:** 6 января 2022.

Официальный CSTO source фиксирует:
- решение Коллективного совета безопасности о направлении миротворческих сил;
- участие подразделений Армении, Беларуси, Кыргызстана, России и Таджикистана;
- задача: охрана важных государственных и военных объектов и помощь правоохранительным органам в стабилизации ситуации;
- российские воздушно-десантные подразделения уже перебрасываются, передовые части приступают к задачам.

Здесь `EXTERNAL_FORCE_DEPLOYED = OBSERVED`.

### C3. Казахстан — cutoff KAZ-2022-T1

**Дата:** 13 января 2022.

CSTO сообщает о завершении задач и начале завершения операции.

### C4. Казахстан — cutoff KAZ-2022-T2

**Дата:** 19 января 2022.

CSTO сообщает о полном завершении вывода контингентов.

### Сравниваемая переменная

```text
DOMESTIC_COERCIVE_CAPACITY
+ EXTERNAL_SUPPORT_AVAILABLE
+ EXTERNAL_FORCE_DEPLOYED
+ CRITICAL_INFRASTRUCTURE_PROTECTION
+ EXPECTED_BEHAVIOR_OF_SECURITY_NODES
```

Ключевой guard:

```text
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
```

---

## 5. Пара D — ЮАР 1990–1994 ↔ Родезия/Зимбабве 1979–1980

### D1. ЮАР — cutoff ZAF-1990-T0

**Дата:** февраль 1990.

Office of the Historian фиксирует:
- F.W. de Klerk снимает запрет с ANC и других освободительных организаций;
- объявляется освобождение политических заключённых и расширение политических свобод;
- 11 февраля Nelson Mandela освобождён после 27 лет заключения.

Это наблюдаемый переход от `REPRESSION_ONLY` к `NEGOTIATED_TRANSFORMATION_AVAILABLE`.

### D2. ЮАР — transition path

Последующие наблюдаемые этапы:
- переговоры между правительством и anti-apartheid groups;
- согласие на демократические выборы;
- апрель 1994 — выборы и передача президентской власти при сохранении государства.

Для blind packet outcome 1994 скрывается в ранних cutoff.

### D3. Родезия — cutoff RHO-1979-T0

**Дата:** сентябрь 1979.

FRUS фиксирует:
- Lancaster House Conference уже созвана;
- в переговорах участвуют все стороны конфликта;
- США считают преждевременное снятие санкций риском для переговорного процесса.

### D4. Родезия — cutoff RHO-1979-T1

**Дата:** ноябрь–декабрь 1979.

FRUS фиксирует:
- переговоры всё ещё идут;
- поддерживается сохранение санкционного давления до сделки;
- обсуждаются конкретные cease-fire arrangements;
- британский губернатор должен восстановить легальную переходную authority;
- политическая схема включает переход к majority rule, interim arrangements и выборы.

### D5. Родезия — threshold implementation

**Дата:** 17 декабря 1979 и далее.

Президент США разрешает поддержку воздушной перевозки для cease-fire arrangements в координации с Великобританией.

Здесь появляется observable implementation, а не только декларация.

### Сравниваемая переменная

```text
COST_OF_HOLDING_POWER
vs
COST_OF_SURRENDERING_MONOPOLY
+ EXIT_OPTION_FOR_INCUMBENT_ELITE
+ PROPERTY/SECURITY EXPECTATIONS
+ NEGOTIATED_TRANSITION_CREDIBILITY
+ EXTERNAL_PRESSURE
```

Ключевые guards:

```text
REGIME_COLLAPSE != STATE_COLLAPSE
LOSS_OF_ELITE_POLITICAL_MONOPOLY != LOSS_OF_ALL_ELITE_RESOURCES
NEGOTIATION_EXISTS != NEGOTIATION_WILL_SUCCEED
```

---

## 6. Что уже можно делать blind

Готовы к обезличиванию и blind coding:
- Россия: RUS-1917-T0/T1;
- Китай: CHN-1989-T0/T1;
- Беларусь: BLR-2020-T0/T1;
- Казахстан: KAZ-2022-T0/T1;
- ЮАР: ZAF-1990-T0;
- Родезия: RHO-1979-T0/T1.

Румыния требует ещё одного source-extraction pass для 21–22 декабря 1989, чтобы не подменять contemporaneous evidence ретроспективной хронологией.

## 7. Следующий gate

```text
SOURCE_EXTRACT_ROMANIA_21_22_DEC_1989
THEN
BUILD_ANONYMIZED_PRE_THRESHOLD_PACKET_001
THEN
MULTI_MODEL_BLIND_CODING
THEN
OPEN_T1_AND_SCORE_TRAJECTORY_DISCRIMINATION
```

## 8. Source register

- U.S. Office of the Historian, FRUS Russia 1917/1918, March Revolution chapter and paper list.
- U.S. Office of the Historian, `Tiananmen Square, 1989`.
- OSCE/ODIHR Belarus releases dated 10, 13, 17, 19, 28 August 2020.
- CSTO releases dated 6, 13, 19 January 2022.
- U.S. Office of the Historian, `The End of Apartheid`.
- FRUS 1977–1980, Southern Africa, Rhodesia/Lancaster House documents.
- UN Special Rapporteur on Romania, report submitted 18 December 1989, E/CN.4/1990/28.
- Library of Congress Federal Research Division, `Romania: A Country Study`, research completed July 1989.

## 9. Status

```text
PRE_THRESHOLD_CHRONOLOGY_SNAPSHOTS_001 = READY_WITH_ONE_PENDING_EXTRACTION
OUTCOME_LEAKAGE_GUARD = ACTIVE
BLIND_PACKET_DERIVATION = PARTIALLY_READY
```
