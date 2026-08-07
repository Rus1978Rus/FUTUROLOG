# HISTORICAL_DATASET_SPEC v0.1
## Первый GEOECON pilot-корпус для исторической проверки Objective/Coverage

**Статус:** `DATASET_SPEC_FROZEN / PILOT_PIPELINE_VALIDATION / NOT_FORMULA_SELECTION / NOT_VALIDATED`

## 1. Зачем этот корпус

Первый корпус нужен не для объявления «лучшей формулы», а для проверки полного исторического пути без подглядывания в будущее.

Выбран узкий кейс:

> эскалация Россия–Украина 2021–2022 перед полномасштабным вторжением 24 февраля 2022 года.

Причина выбора: в одном эпизоде доступны военные, политические и экономико-энергетические сигналы, опубликованные до события. Это соответствует будущему GEOECON-контру, но пока остаётся только пилотным полигоном.

## 2. Target event

`TARGET_EVENT_CLASS = LARGE_SCALE_INTERSTATE_KINETIC_ESCALATION`

Для этого pilot-кейса outcome определяется строго как:

```text
Россия начинает полномасштабное вторжение в Украину 2022-02-24.
```

Это определение фиксируется до расчёта Objective/Coverage.

Не считаются отдельным target outcome:
- обычные учения;
- дипломатические угрозы;
- перемещение войск без начала полномасштабного вторжения;
- отдельные кибератаки;
- санкционные заявления;
- локальные боестолкновения до 24 февраля.

## 3. Forecast horizon

Основной горизонт pilot:

`30 DAYS`

Для каждого snapshot:

```text
outcome_label = 1
если target event наступает в интервале
(cutoff_time, cutoff_time + 30 days]
иначе 0
```

Это создаёт ранние отрицательные snapshot даже внутри одной эскалационной кампании и поздние положительные snapshot.

Важно: snapshots одного кризиса коррелированы и НЕ считаются независимыми событиями.

## 4. Snapshot schedule

Используется недельный шаг плюс финальный snapshot за день до события.

Список находится в `snapshot_schedule_v0_1.csv`.

Период:

```text
2021-12-03 .. 2022-02-23
```

Этот pilot нельзя использовать для выбора финальной формулы. Он предназначен для:
- проверки leakage guard;
- проверки построения evidence state;
- проверки поведения A/B/C во времени;
- проверки lead-time логики;
- выявления ошибок данных и provenance.

## 5. Source families

На v0.1 используются только источники с проверяемой датой публикации и явной ролью.

### MILITARY / SECURITY

`NATO_OFFICIAL`
- официальные заявления и транскрипты NATO;
- одна цепочка перепубликаций NATO считается одним source family.

`CSIS_ANALYSIS`
- независимый аналитический family;
- публикации учитываются только начиная с их фактической даты публикации.

### ECONOMY / ENERGY

`IEA_ENERGY`
- исторические данные и отчёты газового рынка;
- используются как отдельный экономико-энергетический family;
- поздние post-event выводы не разрешается переносить назад во вход.

### Добавление новых families

Reuters, Eurostat, ECB, shipping/rail data, commodity feeds и другие источники могут быть добавлены только новой версией dataset spec или отдельным extension manifest. Тихое расширение v0.1 запрещено.

## 6. Source-independence rule

```text
SOURCE_COUNT != SOURCE_INDEPENDENCE
```

Примеры:
- пять NATO-страниц, повторяющих один тезис, не дают пять независимых подтверждений;
- пересказ CSIS другого первичного источника не создаёт автоматически новую независимость;
- source family — минимальная единица для independence accounting на этом pilot.

## 7. Raw evidence classes

До Entropy-RG normalization evidence классифицируется минимум по четырём направлениям:

```text
MILITARY_BUILDUP
DIPLOMATIC_COERCION_OR_WARNING
ECONOMIC_ENERGY_STRESS
CROSS_DOMAIN_CONVERGENCE
```

`CROSS_DOMAIN_CONVERGENCE` не является отдельным первичным источником. Это derived feature и обязан хранить ссылки на исходные evidence items.

## 8. EvidenceState construction

На каждом cutoff строятся шесть полей:

```text
measured_score
evidence_coverage
source_independence
freshness
pipeline_completeness
observed_noise
```

### measured_score

Не задаётся вручную итоговым ярлыком «война близко».

Он должен быть получен из замороженного scoring adapter поверх evidence, доступного до cutoff. До реализации адаптера поле получает статус `NOT_COMPUTED`.

### evidence_coverage

Доля обязательных evidence classes, для которых к cutoff существует пригодный проверенный вход.

Обязательные classes для pilot:
- MILITARY_BUILDUP;
- DIPLOMATIC_COERCION_OR_WARNING;
- ECONOMIC_ENERGY_STRESS.

`CROSS_DOMAIN_CONVERGENCE` — derived, поэтому в denominator coverage не входит.

### source_independence

Считается по source families, а не по числу URL.

Точная функция перевода family diversity в [0,1] должна быть зафиксирована в scoring adapter до первого прогона.

### freshness

Каждый evidence item получает возраст относительно cutoff. Агрегация свежести не может использовать дату позднейшего пересказа вместо оригинальной даты публикации.

### pipeline_completeness

Обязательный путь:

```text
FETCHED
→ SOURCE_IDENTIFIED
→ ORIGINAL_PUBLICATION_TIME_VERIFIED
→ PARSED
→ NORMALIZED
→ QUALITY_CHECKED
→ SCORED
```

Пропуск обязательного шага уменьшает completeness и остаётся видимым.

### observed_noise

Измеряет нестабильность/противоречивость наблюдаемого входа. Отсутствие данных не должно автоматически превращаться в высокий noise.

## 9. Leakage guard

Каждый evidence item обязан иметь:

```text
item_id
source_family
source_url
original_publication_time
retrieval_time
cutoff_time
included_before_cutoff
provenance_status
```

Инвариант:

```text
original_publication_time > cutoff_time
→ EXCLUDE_FROM_SNAPSHOT
```

Если original publication time неизвестно:

`REVIEW_REQUIRED / NOT_TRUSTED_FOR_FROZEN_RUN`.

## 10. Verified seed sources

Первичный список находится в `source_manifest_v0_1.csv`.

В него включены опубликованные до события материалы NATO и CSIS, фиксировавшие военное наращивание, а также IEA для экономико-энергетического контекста.

Ключевой момент: IEA post-invasion отчёты могут использоваться для подтверждения исторических значений только если конкретное значение имело датированное существование до cutoff. Их post-event интерпретация не становится pre-event evidence.

## 11. Negative controls

Внутри pilot используются два вида отрицательного контроля:

### Temporal negatives
Snapshot, где 24 февраля ещё не попадает в 30-дневный outcome window.

### Evidence negatives
Материалы/периоды, где:
- много сообщений идёт из одного family;
- дипломатическая риторика сильная, но экономический слой слабый;
- экономический стресс присутствует, но сам по себе не является доказательством вторжения.

Нельзя интерпретировать temporal negative как «никакого риска не существовало».

## 12. Что pilot НЕ доказывает

```text
ONE_CRISIS != GENERAL_VALIDATION
WEEKLY_SNAPSHOTS != INDEPENDENT_CASES
RUSSIA_UKRAINE_2022 != ALL_GEOPOLITICS
HIGH_SCORE_BEFORE_EVENT != CAUSAL_PROOF
```

Даже идеальный результат на этом корпусе даёт только:

`PIPELINE_VALIDATED_ON_ONE_HISTORICAL_EPISODE`.

## 13. Критерий завершения pilot

Pilot завершён, когда:

1. все snapshot имеют leakage-safe evidence manifest;
2. scoring adapter построен и заморожен;
3. A/B/C получают одинаковые EvidenceState;
4. сформирован временной ряд confidence;
5. рассчитан lead time;
6. зафиксированы false/early alerts;
7. ни один параметр не менялся после просмотра outcome-части;
8. сделан audit report.

## 14. Следующий шаг

Создать и заморозить:

`EVIDENCE_STATE_ADAPTER_SPEC_v0_1_RU.md`

Только после этого разрешается начать заполнять числовые EvidenceState и запускать A/B/C.