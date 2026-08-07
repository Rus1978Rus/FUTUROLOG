# HISTORICAL_DATASET_SPEC_TEMPLATE v0.1

Статус: `TEMPLATE / NO_DATASET_SELECTED / NOT_RUN`

Этот файл заполняется ДО исторического прогона.

## 1. Target event (целевое событие)

- Название класса события:
- Машиночитаемое определение outcome:
- Что НЕ считается outcome:
- Горизонт предупреждения:

## 2. Временные границы

- Начало calibration interval:
- Конец calibration interval:
- Начало test interval:
- Конец test interval:
- Правило cutoff:

## 3. Источники

Для каждого семейства источников указать:

- источник;
- тип данных;
- доступную дату публикации;
- правило определения первоначального источника;
- ограничения архива;
- возможные revision/backfill (поздние исправления).

## 4. Positive cases

Список положительных кейсов фиксируется до расчёта Objective/Coverage scores.

## 5. Negative controls

Обязательно включить:

- спокойные периоды;
- громкие ложные тревоги;
- повторяющиеся сообщения одного первоисточника;
- неполные данные;
- периоды высокого шума без outcome.

## 6. Feature construction

Для каждого из шести полей:

- `measured_score`
- `evidence_coverage`
- `source_independence`
- `freshness`
- `pipeline_completeness`
- `observed_noise`

зафиксировать алгоритм получения значения из данных, не используя информацию после cutoff.

## 7. Leakage audit

Для каждого входного элемента хранить:

```text
item_id
source_id
original_publication_time
retrieval_time
cutoff_time
included_before_cutoff: true/false
provenance_status
```

Любой `original_publication_time > cutoff_time` означает исключение элемента из snapshot.

## 8. Frozen decision

После заполнения этого документа перед первым прогоном установить:

`DATASET_SPEC_FROZEN = TRUE`

После этого изменения outcome, cutoff, feature construction или состава кейсов требуют новой версии спецификации, а не тихой правки старой.