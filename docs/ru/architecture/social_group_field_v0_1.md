# SOCIAL GROUP FIELD v0.1

**Статус:** `ARCHITECTURE_DRAFT / PRE-IMPLEMENTATION / NOT_VALIDATED`

## 1. Назначение

Не сводить общество к нескольким крупнейшим или политически центральным группам.

`LEGITIMACY_BEARING_GROUP` остаётся важным специальным типом группы, но не единственным.

Ключевой принцип:

```text
SMALL_GROUP != IRRELEVANT
```

## 2. Группа как объект

Для каждой группы хранить отдельно:

- размер;
- географическую концентрацию;
- экономическую роль;
- политическое влияние;
- организационную способность;
- сетевую связанность;
- контроль критической инфраструктуры;
- информационную заметность;
- доступ к ресурсам;
- степень недовольства;
- степень мобилизации;
- степень внутренней фрагментации;
- отношения с другими группами;
- роль в легитимации системы;
- статус давления/стабилизации.

## 3. Специальные типы

Система может маркировать группу как:

- `LEGITIMACY_BEARING_GROUP` — группа-носитель легитимности;
- `ACTIVE_ELECTORATE_GROUP` — политически активный электорат;
- `CRITICAL_PROFESSIONAL_GROUP` — профессия с системной функцией;
- `REGIONAL_GROUP`;
- `RELIGIOUS_GROUP`;
- `ETHNIC_GROUP`;
- `DIASPORA_GROUP`;
- `YOUTH_OR_STUDENT_GROUP`;
- `SECURITY_OR_MILITARY_GROUP`;
- `SMALL_HIGH_LEVERAGE_GROUP` — малая, но высокорычажная группа;
- `OTHER_SOCIAL_GROUP`.

Тип не означает автоматической важности.

## 4. Неравенство

Отдельный домен:

`SOCIAL_INEQUALITY_AND_DISTRIBUTION`.

Минимальные измерения:

- доходы;
- богатство;
- региональное неравенство;
- город/село;
- доступ к медицине, образованию, воде, энергии;
- безработица;
- стоимость еды и жилья относительно доходов;
- концентрация земли/ресурсов;
- социальная мобильность;
- воспринимаемая несправедливость.

Для групп-носителей легитимности дополнительно:

```text
ACTIVE_ELECTORATE_INEQUALITY_PRESSURE
LEGITIMIZING_STRATUM_INEQUALITY_PRESSURE
STATUS_LOSS_OF_LEGITIMACY_GROUP
EXPECTATION_REALITY_GAP
```

## 5. Динамика между группами

Вводятся отдельные процессы:

- `GROUP_COALESCENCE` — сближение/слияние ранее раздельных групп;
- `CROSS_GROUP_CONTAGION` — перенос настроений/нарратива между группами;
- `MINORITY_TRIGGER_WITH_BROAD_RESONANCE` — малый локальный фактор с широким резонансом;
- `CROSS_GROUP_COMMON_FRAME` — появление общей интерпретации проблемы;
- `COALITION_FORMATION` — наблюдаемое коалиционное действие;
- `COALITION_FRAGMENTATION` — распад/расхождение групп.

## 6. Давление и стабилизаторы

Для каждой группы хранить отдельно:

```text
pressure_state
stabilizer_state
mobilization_state
behavioral_change
confidence
coverage
```

Группа может быть недовольна и одновременно демобилизована.

## 7. Информационная среда

Громкость группы в сети не равна её масштабу.

```text
VISIBLE_ONLINE_ACTIVITY != REAL_SOCIAL_SCALE
MEDIA_VISIBILITY != GROUP_SIZE
BOT_ACTIVITY != GROUP_MOBILIZATION
```

Связка с Observation & Coverage Layer обязательна.

## 8. Guards

```text
SMALL_GROUP != IRRELEVANT
LARGE_GROUP != POWERFUL_GROUP
DISCONTENTED_GROUP != MOBILIZED_GROUP
SIMILAR_GRIEVANCE != COALITION
COALITION_SIGNAL != REGIME_CHANGE
INEQUALITY != DISCONTENT
DISCONTENT != DELEGITIMIZATION
DELEGITIMIZATION != PROTEST
PROTEST != CONFLICT
STATUS_LOSS != POLITICAL_BREAK
```

## 9. Пример системной роли малой группы

Малая группа может иметь:

```text
population_share = LOW
network_centrality = HIGH
critical_function = HIGH
mobilization = MEDIUM
```

и поэтому быть системно важнее большой, но слабо организованной группы.

## 10. Граница

`SOCIAL_GROUP_FIELD` не присваивает группе моральный статус и не объявляет её причиной конфликта. Это карта акторов и взаимодействий.

## 11. Следующий шаг

Применить один и тот же schema к историческим кейсам Россия–Украина и Мьянма, не добавляя case-specific поля без новой версии архитектуры.