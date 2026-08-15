# SUCCESS ADAPTATION TRAP — BLIND PACKET 001

PACKET_SCHEMA_ID: SAT-001-V1

Статус: `READY_FOR_EXTERNAL_MULTI_MODEL_TEST / SYNTHETIC_CONTROLLED_STRESS_TEST / OUTCOME_LABELS_HIDDEN`

## 1. Цель

Проверить, способен ли кодировщик обнаруживать хрупкость, возникшую из длительно благоприятного состояния, не сводя риск к формуле `GOOD_EVENT = GOOD_OUTCOME` или `BAD_EVENT = BAD_OUTCOME`.

Пакет намеренно синтетический: это снижает исторические конфаунды и позволяет проверить сам механизм до переноса на реальные исторические кейсы.

## 2. Рабочая гипотеза

`PERSISTENT_FAVORABLE_STATE → SYSTEM_ADAPTATION → DEPENDENCY → REGIME_CONTINUATION_OR_REVERSAL → NONLINEAR_OUTCOME`

## 3. Guards

`GOOD_INDICATOR != SAFE_SYSTEM`

`GOOD_FORECAST != GOOD_SYSTEM_OUTCOME`

`PAST_SUCCESS != FUTURE_RESILIENCE`

`LARGE_RESERVE != ABSENCE_OF_RISK`

`EVENT_RISK != EVENT_VALUE`

`HIGH_ADAPTATION != CRISIS_PROVEN`

`SCENARIO_RISK != SCENARIO_CERTAINTY`

`BUFFER_EXISTS != BUFFER_IS_SUFFICIENT`

`CONTINUED_SUCCESS != AUTOMATIC_STABILITY`

## 4. Допустимые значения

`persistent_state_duration = SHORT | MEDIUM | LONG | VERY_LONG | UNKNOWN`

`adaptation_depth = LOW | MEDIUM | HIGH | VERY_HIGH | UNKNOWN`

`buffer_state = LOW | ADEQUATE | HIGH | SATURATED | UNKNOWN`

`capacity_rigidity = FLEXIBLE | MODERATE | RIGID | VERY_RIGID | UNKNOWN`

`dependency_on_persistent_state = LOW | MEDIUM | HIGH | VERY_HIGH | UNKNOWN`

`scenario_direction = CONTINUATION | NORMALIZATION | REVERSAL`

`scenario_system_fit = GOOD | MIXED | POOR | VERY_POOR | UNKNOWN`

`primary_risk_mode = NONE | OVERSUPPLY | SHORTAGE | PRICE_COLLAPSE | REVENUE_COLLAPSE | CAPACITY_OVERLOAD | STRANDED_CAPACITY | DEBT_STRESS | FISCAL_STRESS | MULTI_RISK | UNKNOWN`

`success_adaptation_trap = ABSENT | POSSIBLE | PRESENT | NOT_ASSESSABLE`

`confidence = LOW | MEDIUM | HIGH`

## 5. CASE S1 — STOCK SATURATION

### Baseline

Пять последовательных циклов дают рекордно высокий физический выпуск товара. Хранилища почти заполнены. Производители расширили посевы/мощности, взяли кредиты и заключили долгосрочные контракты, исходя из сохранения высокого выпуска и возможности продажи излишков. Экспортная инфраструктура близка к текущему пределу.

### S1-A

Следующий цикл снова даёт рекордно высокий выпуск.

### S1-B

Следующий цикл даёт нормальный средний выпуск.

### S1-C

Следующий цикл даёт резко низкий выпуск.

## 6. CASE S2 — COMMODITY REVENUE BOOM

### Baseline

В течение восьми лет экспортный товар продаётся по необычно высокой цене. Государственные расходы, зарплаты публичного сектора и крупные инфраструктурные обязательства увеличены. Значительная доля бюджета теперь зависит от доходов этого сектора. Финансовые резервы существуют, но параллельно вырос постоянный уровень расходов.

### S2-A

Высокая цена сохраняется ещё пять лет.

### S2-B

Цена возвращается к долгосрочному среднему уровню.

### S2-C

Цена быстро падает значительно ниже уровня, под который построен бюджет.

## 7. CASE S3 — CHEAP CREDIT REGIME

### Baseline

Десять лет стоимость кредита остаётся необычно низкой. Домохозяйства и компании увеличивают долг; цены активов растут; проекты с длительной окупаемостью становятся нормальными. Финансовая система остаётся платёжеспособной при текущей стоимости обслуживания долга.

### S3-A

Низкая стоимость кредита сохраняется.

### S3-B

Стоимость кредита медленно возвращается к историческому среднему.

### S3-C

Стоимость кредита повышается быстро и значительно.

## 8. CASE S4 — HIGH-CAPACITY EXPORT MACHINE

### Baseline

Много лет внешний спрос на продукцию страны растёт. Производственные мощности, порты, железные дороги и налоговые поступления перестроены под высокий экспорт. Внутренний спрос растёт медленнее, чем экспортная мощность. Компании оптимизировали структуру затрат под крупные серии и высокую загрузку.

### S4-A

Внешний спрос продолжает быстро расти.

### S4-B

Внешний спрос стабилизируется без падения.

### S4-C

Внешний спрос резко падает.

## 9. CASE S5 — ABUNDANT LABOR SUPPLY

### Baseline

Двадцать лет экономика получает стабильный приток молодых работников. Бизнес-модели, пенсионная система, строительство и социальная инфраструктура адаптируются к постоянному росту рабочей силы. Производительность растёт умеренно; часть отраслей компенсирует это количеством работников.

### S5-A

Приток молодых работников продолжается прежними темпами.

### S5-B

Приток постепенно замедляется до нуля.

### S5-C

Число новых работников резко сокращается, а доля пожилого населения растёт.

## 10. CASE S6 — ABUNDANT CHEAP INPUT

### Baseline

Пятнадцать лет промышленность получает важный внешний ресурс по стабильной низкой цене. Технологии, инфраструктура и цепочки поставок оптимизированы под этот ресурс; альтернативы существуют, но дороже и требуют времени для масштабирования.

### S6-A

Дешёвый ресурс остаётся доступным.

### S6-B

Цена ресурса постепенно растёт.

### S6-C

Доступ к ресурсу резко сокращается.

## 11. Задание

Для каждого baseline сначала закодируй степень адаптации и зависимости. Затем отдельно оцени A/B/C, не используя информацию из соседнего сценария как доказательство для текущего.

Не выбирай самый «плохой» сценарий автоматически. Продолжение благоприятного режима тоже может создавать риск, если система уже насыщена или чрезмерно адаптирована.

## 12. Output CSV — baseline rows

```csv
schema_marker,case_id,persistent_state_duration,adaptation_depth,buffer_state,capacity_rigidity,dependency_on_persistent_state,success_adaptation_trap,confidence,reason
SAT-001-V1,S1,,,,,,,,
SAT-001-V1,S2,,,,,,,,
SAT-001-V1,S3,,,,,,,,
SAT-001-V1,S4,,,,,,,,
SAT-001-V1,S5,,,,,,,,
SAT-001-V1,S6,,,,,,,,
```

## 13. Output CSV — scenario rows

```csv
schema_marker,case_id,scenario_id,scenario_direction,scenario_system_fit,primary_risk_mode,success_adaptation_trap,confidence,reason
SAT-001-V1,S1,S1-A,CONTINUATION,,,,,
SAT-001-V1,S1,S1-B,NORMALIZATION,,,,,
SAT-001-V1,S1,S1-C,REVERSAL,,,,,
SAT-001-V1,S2,S2-A,CONTINUATION,,,,,
SAT-001-V1,S2,S2-B,NORMALIZATION,,,,,
SAT-001-V1,S2,S2-C,REVERSAL,,,,,
SAT-001-V1,S3,S3-A,CONTINUATION,,,,,
SAT-001-V1,S3,S3-B,NORMALIZATION,,,,,
SAT-001-V1,S3,S3-C,REVERSAL,,,,,
SAT-001-V1,S4,S4-A,CONTINUATION,,,,,
SAT-001-V1,S4,S4-B,NORMALIZATION,,,,,
SAT-001-V1,S4,S4-C,REVERSAL,,,,,
SAT-001-V1,S5,S5-A,CONTINUATION,,,,,
SAT-001-V1,S5,S5-B,NORMALIZATION,,,,,
SAT-001-V1,S5,S5-C,REVERSAL,,,,,
SAT-001-V1,S6,S6-A,CONTINUATION,,,,,
SAT-001-V1,S6,S6-B,NORMALIZATION,,,,,
SAT-001-V1,S6,S6-C,REVERSAL,,,,,
```

## 14. Protocol gate

Отклонить результат до scoring, если:
- `schema_marker != SAT-001-V1`;
- case/scenario IDs изменены;
- модель автоматически считает `CONTINUATION = SAFE`;
- модель автоматически считает `REVERSAL = CRISIS`;
- `PRESENT` используется как доказательство неизбежного кризиса;
- в reason импортируются внешние страны, даты или события.

Верни только два CSV: baseline + scenarios. Без текста до или после.
