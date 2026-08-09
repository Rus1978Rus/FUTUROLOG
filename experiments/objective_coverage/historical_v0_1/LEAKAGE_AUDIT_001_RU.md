# LEAKAGE_AUDIT 001

**Статус:** `LEAKAGE_AUDIT_COMPLETE / PASS_WITH_FINDINGS / NUMERIC_EVIDENCESTATE_BLOCKED / SCHEMA_FREEZE_PRESERVED / NOT_VALIDATED`

## 1. Цель

Проверить, не проникло ли знание известного будущего в исторические входы пилота Россия–Украина и Мьянма.

Аудит не оценивает, был ли прогноз правильным. Он проверяет только дисциплину исторического cutoff: мог ли соответствующий evidence item быть доступен системе на рассматриваемую дату и не усилен ли он формулировками, появившимися после события.

## 2. Проверяемые типы leakage

```text
PUBLICATION_TIME_LEAKAGE
RETROSPECTIVE_WORDING_LEAKAGE
OUTCOME_LABEL_LEAKAGE
SNAPSHOT_CONTAMINATION
SENSOR_VALUE_LEAKAGE
SELECTION_AFTER_OUTCOME_LEAKAGE
DERIVED_KNOWLEDGE_LEAKAGE
```

### PUBLICATION_TIME_LEAKAGE
Источник опубликован после cutoff, но используется как будто был известен раньше.

### RETROSPECTIVE_WORDING_LEAKAGE
Сам факт относится к прошлому, но формулировка/интерпретация взята из поздней реконструкции.

### OUTCOME_LABEL_LEAKAGE
Исторический сигнал получает название, которое уже предполагает известный исход: например `PRE_INVASION_PROOF`, `COUP_CAUSE`, `WAR_PRECURSOR` вместо нейтрального описания наблюдаемого состояния.

### SNAPSHOT_CONTAMINATION
Evidence из более позднего snapshot попадает в более ранний.

### SENSOR_VALUE_LEAKAGE
Существование датированного сенсора/карты ошибочно превращается в числовое значение без извлечения и проверки underlying data.

### SELECTION_AFTER_OUTCOME_LEAKAGE
После знания исхода выбираются только те источники, которые выглядят как предвестники, а counter-signals и стабилизаторы не ищутся систематически.

### DERIVED_KNOWLEDGE_LEAKAGE
Поздно вычисленный агрегат или вывод используется как будто он был доступным contemporaneous наблюдением.

## 3. Россия–Украина

### PASS

Корпус уже содержит явное разделение:

```text
CONTEMPORANEOUS
RETROSPECTIVE_ONLY
WORKING_WITH_DATE_CAUTION
QUARANTINED_FOR_BACKFILL
```

Поздние EEAS/IEA synthesis не были автоматически импортированы в ранние snapshots. Исторические ряды резервов не допущены во все cutoff только потому, что сегодня таблица содержит прошлые значения. В dry run ресурсная способность не превращена в доказательство намерения, а информационные нарративы не превращены в доказательство общественной веры.

### FINDINGS

**RU-LK-001 — reserve-series observability.** Исторические значения резервов известны, но original release timing отдельных точек ещё не восстановлен. До восстановления конкретная точка не должна участвовать в snapshot.

**RU-LK-002 — retrospective disinformation synthesis.** Поздний анализ интенсивности нарративов полезен как контроль, но не должен усиливать contemporaneous severity. Сохранять `RETROSPECTIVE_ONLY`.

**RU-LK-003 — outcome-shaped source selection risk.** Корпус сознательно собирался вокруг известного кризиса. Даже при корректных датах остаётся риск, что после знания исхода были выбраны преимущественно признаки эскалации. Это не устраняется cutoff-фильтром. Требуется отдельный `NEGATIVE_CONTROL_BACKFILL_009`.

**RU-LK-004 — neutral naming requirement.** В numeric pipeline запрещены классы и причины, содержащие скрытый результат (`inevitable invasion`, `war precursor`, `proof of attack`). Допустимы только наблюдаемые классы вроде `MILITARY_BUILDUP`, `DIPLOMATIC_COERCION_OR_WARNING`, `ECONOMIC_ENERGY_STRESS`.

## 4. Мьянма

### PASS

Year-end displacement totals не перенесены в ранние cutoff. Weekly UNHCR map products хранятся как `SENSOR_ONLY`, пока underlying numeric value не извлечён. Поздние агрегаты не используются как ранние наблюдения. Группы сопротивления не объединены задним числом в единый command structure.

### FINDINGS

**MM-LK-001 — displacement sensor/value separation.** Наличие карты на дату подтверждает доступность сенсора, но не numeric total. Значение остаётся `UNKNOWN` до чтения и проверки underlying map/data.

**MM-LK-002 — later descriptions of resistance structure.** Поздние исследования сетей PDF/local defense groups могут помочь реконструировать taxonomy, но не имеют права автоматически определять, что было известно системе в раннем 2021. Для snapshot нужны contemporaneous records либо явная отметка `RETROSPECTIVE_STRUCTURAL_REFERENCE`.

**MM-LK-003 — diaspora/support allocation.** Позднее знание о дальнейшем использовании средств не должно переноситься назад. contemporaneous donation record подтверждает сам поток/заявленное назначение на дату, но не будущую фактическую allocation.

**MM-LK-004 — outcome-shaped source selection risk.** Как и в кейсе Россия–Украина, знание последующей гражданской войны создаёт риск переотбора конфликтных сигналов. Требуется systematic negative-control search.

## 5. Cross-case leakage risk

Главный общий риск сейчас не прямой временной leakage, а **selection leakage**.

Мы уже хорошо защищены от простой ошибки:

```text
LATE_SOURCE -> EARLY_SNAPSHOT
```

Но пока слабее защищены от более тонкой ошибки:

```text
KNOWN_OUTCOME
→ researcher notices mainly outcome-consistent signals
→ corpus looks more predictive than information environment really was
```

Поэтому:

```text
CUTOFF_CLEAN != SELECTION_UNBIASED
```

и

```text
NO_POST_DATE_SOURCE != NO_HINDSIGHT_BIAS
```

## 6. Leakage gate rules

Перед numeric EvidenceState каждый участвующий evidence item обязан иметь:

```text
original_publication_time
cutoff_admissibility
source_family
original_source_status
retrospective_flag
supporting_item_id
```

Дополнительно:

1. `RETROSPECTIVE_ONLY` механически исключается из раннего snapshot.
2. `SENSOR_ONLY` не даёт numeric value.
3. поздняя taxonomy не повышает раннюю severity без contemporaneous evidence.
4. derived aggregate не получает дату исходных наблюдений вместо даты своей публичной доступности.
5. отсутствие counter-signal search блокирует honest `observed_noise`.
6. каждая severity должна ссылаться только на cutoff-admissible item IDs.

## 7. Результат аудита

```text
PUBLICATION_TIME_DISCIPLINE: PASS_WITH_CAUTION
RETROSPECTIVE_EXCLUSION: PASS
SENSOR_VALUE_SEPARATION: PASS
OUTCOME_LABEL_DISCIPLINE: PASS_WITH_RULE_REQUIRED
SNAPSHOT_ISOLATION: PARTIAL_PASS
SELECTION_BIAS_CONTROL: FAIL_NOT_YET_IMPLEMENTED
NEGATIVE_CONTROL_SEARCH: REQUIRED
READY_FOR_NUMERIC_EVIDENCESTATE: NO
```

Critical blocker:

```text
SELECTION_AFTER_OUTCOME_LEAKAGE
```

Он закрывается не добавлением ещё большего числа подтверждающих источников, а поиском evidence, которое на тех же cutoff поддерживало стабильность, деэскалацию, нормальность, альтернативные объяснения или отсутствие ожидаемого перехода.

## 8. Следующий шаг

Разрешён следующий этап:

```text
NEGATIVE_CONTROL_BACKFILL_009
```

Его задача — для каждого ключевого pressure domain целенаправленно найти contemporaneous counter-signals / stabilizers / false-positive analogues.

После этого:

```text
COVERAGE_TOPOLOGY_MATRIX_001
→ SECOND_CODING_CHECK
→ NUMERIC_EVIDENCESTATE_GATE_REVIEW
```

## 9. Статус

```text
LEAKAGE_AUDIT_001_COMPLETE
PASS_WITH_FINDINGS
DIRECT_TIME_LEAKAGE_GUARDS_WORKING
SELECTION_LEAKAGE_NOT_YET_CLOSED
NEGATIVE_CONTROL_BACKFILL_REQUIRED
NUMERIC_EVIDENCESTATE_BLOCKED
SCHEMA_FREEZE_PRESERVED
NOT_VALIDATED
```
