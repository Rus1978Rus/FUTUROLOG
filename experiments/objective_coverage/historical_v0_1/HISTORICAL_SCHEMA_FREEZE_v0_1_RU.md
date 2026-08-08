# HISTORICAL_SCHEMA_FREEZE v0.1

**Статус:** `SCHEMA_FROZEN_FOR_PILOT / BULK_COLLECTION_ALLOWED / NOT_VALIDATED`

## 1. Назначение

Этот документ замораживает структуру исторического пилота до массового наполнения кейсов Россия–Украина и Мьянма.

Цель — не позволить архитектуре бесконечно меняться после просмотра исторических исходов.

## 2. Обязательные слои пилота

Оба кейса используют одинаковую структуру:

1. `HISTORICAL_CAUSAL_DEPTH` — историческая причинная глубина H0–H5;
2. `RESOURCE_SUSTAINMENT` — деньги, сырьё, оружие, логистика, топливо, внешняя поддержка и ограничения;
3. `LATENT_PRESSURE / CROSS_DOMAIN_ACCUMULATION` — медленные междоменные процессы;
4. `SOCIAL_GROUP_FIELD` — группы любого размера и взаимодействия между ними;
5. `OBSERVATION & COVERAGE` — наблюдаемость, доступность, base rate, информационные искажения;
6. `OBJECTIVE / COVERAGE` — измеренный сигнал, покрытие, независимость, свежесть, completeness, noise, confidence.

## 3. Домены Latent Pressure

Минимальный фиксированный набор:

- социальное неравенство и распределение;
- демография;
- миграция/ВПЛ/диаспора;
- идентичность;
- религия;
- культура и коллективная память;
- образование;
- здоровье;
- информационная экология;
- теневая/криминальная экономика;
- технологическая и физическая инфраструктура;
- климат и климатические изменения;
- вода;
- продовольствие;
- топливо и энергия;
- земля и природные ресурсы;
- психологическое/ожидательное давление;
- институциональное доверие;
- стабилизаторы и противодействующие процессы.

## 4. Social Group Field

Обязательны:

- группы-носители легитимности;
- активный электорат там, где применимо;
- малые группы;
- профессиональные группы;
- региональные группы;
- религиозные и этнические группы;
- молодёжь/студенты;
- силовые/военные группы;
- диаспоры;
- связи и коалиции между группами.

Размер группы не является фильтром исключения.

## 5. Observation & Coverage

Для каждого значимого evidence item должна быть возможность определить:

```text
source_family
access_mode
original_source_status
publication_time
cutoff_admissibility
independence_group
base_rate_status
coverage_segment
information_amplification_status
possible_coordination_status
representation_reality_gap_status
```

Если поле невозможно определить, используется `UNKNOWN`, а не выдуманное значение.

## 6. Информационные операции

Информационный материал может одновременно быть:

- слабым/сомнительным свидетельством состояния общества;
- сильным свидетельством существования информационной активности;
- возможным фактором реального изменения поведения.

Эти роли не объединяются автоматически.

## 7. Запрет ретроспективной подгонки

После этого freeze запрещено тихо:

- добавлять новый домен потому, что он хорошо объясняет известный outcome;
- менять определение outcome;
- менять cutoff;
- менять Objective/Coverage формулы A/B/C;
- менять правила допуска источников;
- менять feature construction после просмотра test outcome.

Необходимое изменение оформляется как новая версия `v0_2` с объяснением причины и повторным прогоном обоих кейсов.

## 8. Exception rule

Новый архитектурный класс разрешено добавить только если обнаружено явление, которое существующая схема принципиально не умеет представить.

Условие:

```text
NEW_INTERESTING_EXAMPLE != NEW_ARCHITECTURAL_CLASS
```

## 9. Guards пилота

```text
OBSERVABILITY != PREVALENCE
EARLIER != CAUSAL
RESOURCE_LINK != MOTIVE
INEQUALITY != CONFLICT
SMALL_GROUP != IRRELEVANT
MANY_WEAK_SIGNALS != STRONG_CAUSAL_CLAIM
SYNTHETIC_PASS != REAL_WORLD_VALIDATION
HISTORICAL_FIT != FORECAST_VALIDATION
```

## 10. Разрешённый следующий этап

После этого документа разрешён `BULK_EVIDENCE_COLLECTION` для двух пилотных кейсов.

Порядок:

```text
SOURCE DISCOVERY
→ PROVENANCE
→ CUTOFF FILTER
→ DOMAIN / GROUP / RESOURCE CLASSIFICATION
→ OBSERVATION-COVERAGE ANNOTATION
→ PRESSURE / STABILIZER ANNOTATION
→ EVIDENCE STATE
→ DIAGNOSTIC RUN
```

Прогнозный слой до завершения диагностического исторического прогона не включается.

## 11. Статус

```text
SCHEMA_FROZEN_FOR_PILOT
BULK_COLLECTION_ALLOWED
OBJECTIVE_FORMULAS_FROZEN
FORECAST_LAYER_NOT_STARTED
NOT_VALIDATED
```