# COVERAGE_TOPOLOGY_MATRIX 001

**Статус:** `COVERAGE_TOPOLOGY_MATRIX_COMPLETE / CROSS_CASE_OBSERVABILITY_ASYMMETRY_EXPLICIT / NUMERIC_EVIDENCESTATE_BLOCKED`

## 1. Назначение

Этот документ фиксирует, **что именно исторический корпус FUTUROLOG способен видеть хорошо, плохо или почти не видит** в двух пилотных кейсах: Россия–Украина и Мьянма.

Это не оценка состояния стран и не оценка риска. Это карта сенсоров и слепых зон.

Ключевой принцип:

```text
OBSERVABILITY != PREVALENCE
COLLECTABILITY != PREVALENCE
SAME_SCHEMA != SAME_OBSERVABILITY
CROSS_CASE_SCORE_DIFFERENCE != TRUE_STATE_DIFFERENCE
```

## 2. Шкала покрытия

Используется качественная шкала, без числовой калибровки:

- `STRONG` — несколько пригодных source families и/или устойчивый contemporaneous sensor;
- `MODERATE` — рабочий слой есть, но ограничен по территории, группам или типам источников;
- `WEAK` — единичные/локальные источники, ограниченная независимость или выраженная sampling problem;
- `SENSOR_ONLY` — подтверждено существование сенсора, но значение/содержимое ещё не импортировано полностью;
- `RETROSPECTIVE_ONLY` — полезно для проверки после факта, но запрещено как вход раннего cutoff;
- `GAP` — пригодного покрытия пока недостаточно;
- `DEGRADED_BY_ACCESS` — наблюдаемость сама ухудшена блокировками, цензурой, shutdown, закрытыми каналами или отсутствием доступа.

`STRONG` не означает "полное" и не означает репрезентативность населения.

## 3. Россия–Украина — topology map

| Сегмент | Покрытие | Что реально видим | Главная слепая зона |
|---|---|---|---|
| Formal state institutions | STRONG | официальные решения, реформы, публичные позиции, международные программы | неформальное исполнение и локальная практика |
| Military / security signals | STRONG | публично наблюдаемое наращивание, предупреждения, дипломатическое давление | закрытые планы, намерение, разведданные вне публичного поля |
| Macro / energy / reserves | STRONG-MODERATE | ЦБ, IEA, экспортные и энергетические сигналы | точная конверсия ресурсов в конкретные решения/военные расходы |
| International assistance / sanctions | STRONG | официальные программы и меры | реальный локальный эффект по времени |
| National polling / expectations | STRONG-MODERATE | KIIS и другие формальные опросные сенсоры | lived experience вне опросных рамок, nonresponse, локальные меньшинства |
| IDP / contact-line communities | MODERATE-STRONG | UNHCR, гуманитарный доступ, социальные услуги, mobility restrictions | микролокальная бытовая жизнь и неформальные связи |
| Health / COVID | MODERATE-STRONG | WHO/observatory, финансирование, адаптация, out-of-pocket burden | повседневный доступ по регионам и домохозяйствам |
| Education | MODERATE-STRONG | COVID learning pressure + reform/adaptation | локальная фактическая доступность/качество |
| Water / critical services | MODERATE | локальные conflict-affected records + restoration programs | национальная household-level картина |
| Food / household affordability | WEAK | отдельные структурные и локальные сигналы | системная региональная household affordability |
| Fuel household access | WEAK | macro/market слой | бытовой доступ, региональная неоднородность |
| Social inequality | WEAK-MODERATE | структурные институциональные/образовательные/health различия | полная регионально-групповая матрица неравенства |
| Language / identity / collective memory | WEAK-MODERATE | отдельные polling/identity sensors | повседневные практики, малые группы, динамика интерпретаций |
| Religion / religious institutions | MODERATE | contemporaneous identity/confessional sensor | реальные межгрупповые связи, локальная институциональная роль |
| Information manipulation narratives | MODERATE-STRONG | contemporaneous EUvsDisinfo narrative cataloguing | реальная экспозиция населения, belief, behavioral effect |
| Closed social media / messengers | GAP / DEGRADED_BY_ACCESS | косвенные/вторичные следы | закрытые каналы, private groups, deleted content, inaccessible communities |
| Small informal groups | WEAK | отдельные visible nodes | большая часть low-visibility local groups |
| Lived experience / household normality | WEAK | отдельные гуманитарные/опросные элементы | огромный невидимый массив нормальных взаимодействий |
| Stabilizers / counter-signals | MODERATE | institutional adaptation, IDP, health, education, water, multi-causal alternatives | false-positive analogues и systematic normality search |

### 3.1. Основной перекос Россия–Украина

Корпус **пере-наблюдает формальные институты, макроэкономику, международные источники, опросы и публичные информационные нарративы** и недонаблюдает:

- household normality;
- закрытые мессенджеры;
- малые неформальные группы;
- локальные межгрупповые отношения;
- реальную распространённость нарратива;
- бытовую affordability еды/топлива/услуг.

Поэтому:

```text
HIGH_MEDIA_OR_INSTITUTIONAL_VISIBILITY != HIGH_SOCIAL_PREVALENCE
```

## 4. Мьянма — topology map

| Сегмент | Покрытие | Что реально видим | Главная слепая зона |
|---|---|---|---|
| Formal state institutions | MODERATE | coup-related institutional actions, public decrees, international reporting | внутреннее исполнение и закрытые command structures |
| Military violence / conflict events | MODERATE-STRONG | UN/OHCHR/humanitarian event reporting | недоучёт remote areas, inaccessible zones, reporting bias |
| Macro economy / banking / payments | STRONG-MODERATE | World Bank, banking/logistics/price disruptions | informal economy и локальная адаптация вне формальных каналов |
| Food / fuel prices | STRONG-MODERATE | WFP regional price monitoring | household-level denominator и неодинаковая доступность |
| Water access | WEAK | отдельные гуманитарные/региональные сигналы | системная water-security карта |
| Agriculture / climate / disasters | MODERATE | structural vulnerability + Rakhine agriculture/fisheries | contemporaneous direct impacts across multiple regions |
| Displacement | MODERATE + SENSOR_ONLY | event evidence + UNHCR weekly map sensors | validated numeric totals для каждого cutoff |
| Civil Disobedience Movement | STRONG-MODERATE | professional-group participation | denominator, local variation, attrition over time |
| Students / teachers / health workers | MODERATE-STRONG | OHCHR/UNICEF/UN reporting | representativeness and regional completeness |
| Ethnic / religious minorities | MODERATE | conflict exposure in selected regions | systematic nationwide group coverage |
| Local defense groups / PDFs | MODERATE | emergence, fragmentation, partial coalescence | exact size, armament, command, local survival/attrition |
| Diaspora / donations | MODERATE-WEAK | documented external donations/support nodes | total scale, allocation, military vs humanitarian use |
| Community / religious support networks | MODERATE | assistance to displaced and local resilience | national coverage and durability |
| Health / COVID | MODERATE | pre-coup pressure, later system weakness | observation degraded by reporting collapse |
| Education | MODERATE | school occupation/disruption + pre-coup adaptation | actual attendance/learning continuity nationally |
| Independent media / journalists | MODERATE | repression and media-space deterioration | what ceased to be observable after repression |
| Internet / platform access | DEGRADED_BY_ACCESS | shutdowns/restrictions themselves are visible | content and activity lost behind shutdowns |
| Information operations / rumours | WEAK | broad information-environment degradation | content-level contemporaneous catalogue + prevalence/effect |
| Household lived experience | WEAK-MODERATE | humanitarian field observations | normality denominator and inaccessible communities |
| Stabilizers / counter-signals | MODERATE | humanitarian buffers, local support, partial logistics recovery | failed escalation analogues, local ceasefire/normality pockets |

### 4.1. Основной перекос Мьянмы

Корпус **пере-наблюдает гуманитарные последствия, displacement, цены, professional mobilization и публично заметные conflict events**, но недонаблюдает:

- закрытые/удалённые районы;
- informal economy;
- content-level rumours/propaganda;
- точный scale малых вооружённых групп;
- household normality;
- события, которые не дошли до международных организаций;
- социальные процессы после internet shutdowns.

Поэтому:

```text
REPORTING_DECLINE != ACTIVITY_DECLINE
INACCESSIBLE_REGION != LOW_PRESSURE_REGION
```

## 5. Cross-case comparability

### Россия–Украина лучше наблюдается по:

```text
FORMAL_INSTITUTIONS
MACRO_ENERGY
POLLING
PUBLIC_INFORMATION_NARRATIVES
HEALTH_EDUCATION_FORMAL_SYSTEMS
```

### Мьянма лучше наблюдается по:

```text
HUMANITARIAN_FIELD_SIGNAL
LOCAL_PRICE_STRESS
DISPLACEMENT_SENSORS
PROFESSIONAL_GROUP_MOBILIZATION
INTERNET_ACCESS_DEGRADATION
```

Это означает, что будущий numeric comparison без topology annotation будет методологически опасен.

## 6. Coverage topology guard for EvidenceState

До numeric EvidenceState каждый snapshot обязан хранить минимум:

```text
coverage_strength_by_segment
known_blind_spots
access_degradation
retrospective_only_segments
sensor_only_segments
underrepresented_groups
underrepresented_regions
underrepresented_platforms
```

Нельзя сворачивать всё в один `coverage = 0.73` без сохранения структуры.

Критический guard:

```text
SAME_COVERAGE_PERCENT != SAME_COVERAGE_TOPOLOGY
```

## 7. Representation-Reality Gap integration

Для информационных и социальных сигналов topology matrix требует различать:

```text
AGENDA_VISIBILITY
AGENDA_SOCIAL_PREVALENCE
AGENDA_BEHAVIORAL_IMPACT
```

Если доступен только первый слой, остальные остаются `UNKNOWN`.

Дополнительные guards:

```text
MEDIA_VISIBILITY != POPULATION_PREVALENCE
NARRATIVE_COUNT != BELIEVER_COUNT
INCIDENT_REPORT_COUNT != BASE_RATE
ABSENCE_OF_NORMALITY_REPORTS != ABSENCE_OF_NORMALITY
```

## 8. Gate result

```text
COVERAGE_TOPOLOGY_MATRIX: PASS
BLIND_SPOTS_EXPLICIT: PASS
CROSS_CASE_ASYMMETRY_EXPLICIT: PASS
SINGLE_COVERAGE_NUMBER_SUFFICIENT: NO
READY_FOR_SECOND_CODING_CHECK: YES
READY_FOR_NUMERIC_EVIDENCESTATE: NO
```

Числовой EvidenceState остаётся заблокирован до:

```text
NEGATIVE_CONTROL_TARGETED_SOURCE_BACKFILL
SECOND_CODING_CHECK
NUMERIC_EVIDENCESTATE_GATE_REVIEW
```

## 9. Статус

```text
COVERAGE_TOPOLOGY_MATRIX_001_COMPLETE
SCHEMA_FREEZE_PRESERVED
OBSERVABILITY_ASYMMETRY_EXPLICIT
BLIND_SPOTS_EXPLICIT
SECOND_CODING_CHECK_READY
NUMERIC_EVIDENCESTATE_BLOCKED
NOT_VALIDATED
```
