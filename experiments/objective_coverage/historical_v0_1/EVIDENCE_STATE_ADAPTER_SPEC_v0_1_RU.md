# EVIDENCE_STATE_ADAPTER_SPEC v0.1
## Как исторические свидетельства превращаются в EvidenceState

**Статус:** `PILOT_ADAPTER_FROZEN / HEURISTIC / NOT_CALIBRATED / NOT_VALIDATED`

Этот adapter (адаптер / правило преобразования) предназначен только для первого historical pilot. Он не является финальной моделью FUTUROLOG.

## 1. Зачем он нужен

Нельзя после просмотра 24 февраля вручную выставить прошлому высокий `measured_score`. Поэтому заранее фиксируется механическая схема кодирования.

Выход:

```text
measured_score
evidence_coverage
source_independence
freshness
pipeline_completeness
observed_noise
```

## 2. Primary evidence classes

Три обязательных класса:

```text
MILITARY_BUILDUP
DIPLOMATIC_COERCION_OR_WARNING
ECONOMIC_ENERGY_STRESS
```

`CROSS_DOMAIN_CONVERGENCE` вычисляется позже и не используется как четвёртый независимый источник, чтобы не считать одни и те же данные дважды.

## 3. measured_score

Каждый доступный primary class кодируется по ordinal severity (порядковой силе) 0–3.

### 0 — NONE
Нет пригодного свидетельства изменения в этом классе.

### 1 — WEAK
Есть общий сигнал напряжения/стресса, но без сильного структурного изменения.

### 2 — SUBSTANTIAL
Есть явно описанное существенное и продолжающееся изменение: крупное наращивание, устойчивое давление, выраженный экономико-энергетический стресс.

### 3 — SEVERE
Есть крупномасштабное/операционно значимое изменение или прямое предупреждение о тяжёлой эскалации, подтверждённое пригодным evidence item.

Для каждого класса хранится `class_severity ∈ {0,1,2,3}` и ссылка на items, которыми значение обосновано.

`measured_score` считается только по AVAILABLE classes:

```text
measured_score = mean(class_severity / 3)
```

Если доступен один класс и он severe, measured_score может быть высоким. Это допустимо, потому что недостаток картины отдельно отражается в coverage.

Инвариант:

```text
MEASURED_SCORE != EVIDENCE_COMPLETENESS
```

## 4. evidence_coverage

Класс считается AVAILABLE только если существует минимум один evidence item, который:

- опубликован не позже cutoff;
- имеет проверенный source family;
- имеет проверяемое original publication time;
- прошёл обязательный pipeline до `QUALITY_CHECKED`.

Формула:

```text
evidence_coverage = available_primary_classes / 3
```

Допустимые значения pilot:

```text
0
0.333333
0.666667
1.0
```

Missing class не становится severity=0 для measured_score. Он уменьшает coverage.

## 5. source_independence

Единица независимости — `source_family`, а не URL.

Для всех пригодных evidence items на cutoff считаются доли items по family `p_i`.

Используется normalized diversity на основе Herfindahl concentration:

```text
raw_diversity = 1 - sum(p_i^2)
max_diversity_for_3_families = 1 - 1/3
source_independence = raw_diversity / (2/3)
```

Результат ограничивается `[0,1]`.

Если пригоден только один family:

```text
source_independence = 0
```

Это pilot-эвристика. Она измеряет разнообразие заявленных source families, а не философскую/каузальную независимость источников.

Инвариант:

```text
FAMILY_DIVERSITY != PROVEN_CAUSAL_INDEPENDENCE
```

## 6. freshness

Для каждого AVAILABLE primary class берётся самый свежий пригодный evidence item до cutoff.

Возраст:

```text
age_days = cutoff - original_publication_time
```

Pilot decay:

```text
item_freshness = max(0, 1 - age_days / 30)
```

`freshness` = mean(item_freshness) по AVAILABLE primary classes.

Почему 30: это совпадает с замороженным pilot forecast horizon и используется только как прозрачная стартовая эвристика. Это НЕ эмпирически найденный half-life.

## 7. pipeline_completeness

Обязательные шаги:

```text
1 FETCHED
2 SOURCE_IDENTIFIED
3 ORIGINAL_PUBLICATION_TIME_VERIFIED
4 PARSED
5 NORMALIZED
6 QUALITY_CHECKED
7 SCORED
```

Для каждого evidence item:

```text
item_pipeline = completed_required_steps / 7
```

Общий `pipeline_completeness` = mean(item_pipeline) по items, участвующим в snapshot.

Если item не дошёл до `QUALITY_CHECKED`, он не делает class AVAILABLE для coverage, но остаётся в audit trail как degraded/rejected input.

## 8. observed_noise

Чтобы не объявлять согласие только потому, что мы собрали лишь подтверждающие материалы, каждому пригодному claim присваивается direction:

```text
+1 SUPPORTS_ESCALATION
 0 NEUTRAL_OR_UNCLEAR
-1 COUNTERSIGNAL_OR_DEESCALATION
```

и strength:

```text
1 WEAK
2 SUBSTANTIAL
3 SEVERE
```

Для ненулевых claims:

```text
signed_sum = sum(direction * strength)
absolute_sum = sum(abs(direction * strength))
coherence = abs(signed_sum) / absolute_sum
observed_noise = 1 - coherence
```

Если `absolute_sum = 0`, noise получает статус `UNDEFINED_NO_DIRECTIONAL_EVIDENCE`, а не искусственный 0.

Критический guard:

```text
NO_COUNTERSIGNAL_SEARCH
→ NO_VALID_NOISE_ESTIMATE
```

До исторического прогона source collection обязана включать явный поиск counter-signals/de-escalation evidence. Текущий seed manifest содержит в основном escalation evidence и поэтому ещё недостаточен для расчёта honest observed_noise.

## 9. Coding discipline

Каждое ordinal значение должно хранить:

```text
coded_value
coding_reason
supporting_item_ids
coder_version
```

Запрещено использовать формулировки из post-event материалов для усиления pre-event severity.

Если формулировка двусмысленна:

`REVIEW_REQUIRED`.

## 10. Double-coding check

Перед финальным pilot run минимум подмножество snapshot должно быть независимо закодировано второй попыткой без просмотра первого результата.

Цель — измерить, насколько severity rubric зависит от интерпретатора.

`CODER_AGREEMENT != WORLD_TRUTH`, но высокий disagreement означает слабый adapter.

## 11. Freeze rule

После первого заполненного числового snapshot:

```text
ADAPTER_SPEC_FROZEN = TRUE
```

Изменение:
- severity rubric;
- coverage denominator;
- independence formula;
- freshness window;
- pipeline steps;
- noise formula

требует `v0.2`, а не тихой правки v0.1.

## 12. Что ещё блокирует запуск

Перед числовым A/B/C run нужно:

1. расширить evidence manifest counter-signals;
2. найти pre-event экономико-энергетические первичные/датированные источники вместо обратного использования post-event IEA narrative;
3. заполнить evidence items по каждому cutoff;
4. выполнить leakage audit;
5. только затем вычислить EvidenceState.

Статус сейчас:

`READY_FOR_EVIDENCE_COLLECTION / NOT_READY_FOR_NUMERIC_RUN`.