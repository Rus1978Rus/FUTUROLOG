# Canonical Scoring Mapping v1

## 1. Сводка задачи

В проекте «Футуролог» нужно зафиксировать единое соответствие между тремя источниками истины о scoring-движке: теоретическим слоем ERG-CAD, архитектурным документом «Футуролог v1.0» и текущим кодом Entropy-RG v2.2. Главный риск состоит в том, что одни и те же идеи сейчас названы по-разному: `RG_Persistence_Score` в препринте близок к `residue` в архитектуре и коде; `Sequential_Anomaly_Score` близок к `sequential`; `Trust_Penalty` близок к `trust`, но в коде это может быть не penalty, а отдельная весовая компонента. Отдельная проблема: Objective_Risk_Score из ERG-CAD почти полностью отсутствует в текущем коде Entropy-RG v2.2, хотя именно он отвечает за проверку объективности и устойчивости сигнала. Этот документ фиксирует каноническое соответствие и задаёт основу для следующих итераций.

Основание документа: ERG-CAD Master Preprint / MVP specification, архитектурный документ `futurolog_architecture_v1.md`, а также список `DEFAULT_WEIGHTS` Entropy-RG v2.2 из задания. Сам ZIP `entropy_rg_anomaly_detector_EN_v2_2_FINAL.zip` в момент подготовки этого документа не был открыт, поэтому все выводы по коду должны быть сверены с фактическими файлами `app/scoring.py`, `app/confinement.py`, `app/sequential.py`, `app/large_deviation.py`.

## 2. Главная таблица соответствий

| ERG-CAD (препринт) | Архитектура v1 | Код Entropy-RG v2.2 | Статус | Комментарий |
|---|---|---|---|---|
| Local_Action_Risk | `gibbs` / `surprise` | `gibbs` + частично `surprise` | partial_match | Local_Action_Risk в ERG-CAD означает локальную рискованность действия. В архитектуре `gibbs` описан как отклонение от ожидаемого распределения, а `surprise` как редкость события относительно baseline. Это два возможных вычислительных аспекта локального риска. |
| Profile_Deviation | `gibbs` / `surprise` | `gibbs` + частично `surprise` | partial_match | Profile_Deviation — отклонение профиля объекта от нормы. `gibbs` ближе по смыслу к контекстному отклонению, `surprise` — к статистической редкости. Нужно решить, разделять ли local/action и profile/deviation в коде. |
| Flow_Asymmetry | None | None | missing_in_code | В ERG-CAD это отдельная компонента потока: дисбаланс входящих/исходящих действий, продаж/жалоб, активности/вывода средств и т.п. В архитектуре v1 и DEFAULT_WEIGHTS Entropy-RG отдельной компоненты flow нет. |
| Graph_Risk | `graph` | `graph` | exact_match | Все три источника имеют графовую компоненту. В препринте она богаче: centrality, PageRank, neighbor risk, community risk, cycles, hub-and-spoke, shared identifiers. В коде требуется сверить фактическую глубину реализации. |
| Trust_Penalty | None / косвенно trusted baseline | `trust` | conflict | В препринте это penalty: `trust_penalty = 1 - normalized_trust_level`. В коде ключ называется `trust`, что может означать trust score или trust penalty. Семантика знака требует решения. |
| Sequential_Anomaly_Score | `sequential` | `sequential` | rename_only | Это одна и та же идея: риск как последовательная, когерентная траектория, а не одиночный выброс. |
| RG_Persistence_Score | `residue` | `residue` | rename_only | В препринте RG persistence измеряет выживание отклонения при укрупнении масштаба. В архитектуре и коде `residue` — информационный остаток после coarse-graining. |
| Scale_Stability | `residue` / objectivity not separated | None | missing_in_code | В архитектуре v1 scale stability растворён в `residue`, но отдельного Objective_Risk layer нет. В коде отсутствует как отдельная компонента. |
| Temporal_Persistence | `sequential` / objectivity not separated | None | missing_in_code | В архитектуре temporal persistence частично покрыта `sequential`, но Objective_Risk_Score требует отдельного измерения доли временных окон, где риск сохраняется. |
| Source_Redundancy | source redundancy в confluence example | None | missing_in_code | Архитектура v1 упоминает source redundancy в confluence-логике, но не как отдельную компоненту Objective_Risk_Score. |
| Observer_Agreement | None | None | missing_in_code | В ERG-CAD это согласие независимых моделей, правил, графовой аналитики, sequence-аналитики и/или людей. В архитектуре v1 и коде отсутствует как отдельная метрика. |
| Noise_Separation | `surprise` / `robustness` частично | `robustness` частично | partial_match | Noise_Separation в ERG-CAD — отделение устойчивого сигнала от шума. В коде `robustness` применён как discount, а не как полноценная objective-компонента. |
| None | `gibbs` | `gibbs` | missing_in_preprint | В препринте нет компоненты с именем Gibbs. По смыслу это может быть вычислительная реализация Local_Action_Risk или Profile_Deviation. |
| None | `surprise` | `surprise` | missing_in_preprint | В препринте нет отдельной компоненты Surprise, но редкость/large deviation может служить реализацией Local_Action_Risk или Profile_Deviation. |
| None | `robustness` не выделен | `robustness` | missing_in_preprint | В коде есть `robustness` с весом 0.05, но в задании указано, что он применяется как discount, не как риск. В препринте отдельной universal-компоненты robustness нет. |
| None | confluence_bonus | confluence_bonus | missing_in_preprint | Confluence bonus есть в архитектуре и коде как интеграционная логика согласованности компонент, но не является отдельной компонентой ERG-CAD Universal_Risk_Score. |
| Objective_Risk_Score | objectivity_score / future layer | None | missing_in_code | Препринт явно требует отдельный слой Objective_Risk_Score. Архитектура v1 концептуально поддерживает objectivity, но код Entropy-RG v2.2 его не реализует как отдельную формулу. |

## 3. Разбор каждой компоненты ERG-CAD

## 3.1 Local_Action_Risk (0.15)

- Что говорит препринт: локальная рискованность действия или события. В MVP specification перечислены признаки вроде abnormal price ratio, sudden price drop, complaint event intensity, unusual action time, new device event, rapid listing burst.
- Есть ли формальная запись в препринте: частично. Общая формула Universal_Risk_Score есть, но отдельной строгой формулы Local_Action_Risk нет. Есть список признаков для feature engineering.
- Соответствие в коде: вероятно `gibbs` и/или `surprise`.
- Соответствие в архитектуре v1: `gibbs` и `surprise`.
- Решение: каноническое имя для Футуролога — `local_action_risk`.
- Действие: `partial_match`; не переименовывать `gibbs` вслепую. Нужен adapter-level mapping: `gibbs` и `surprise` могут питать `local_action_risk`, но не заменять его полностью без ревью.

Комментарий: если текущий код Entropy-RG уже использует `gibbs` как общую локальную аномальность, можно на первом этапе сохранить `gibbs` как implementation key, но в канонической документации считать его подкомпонентой `local_action_risk`.

## 3.2 Profile_Deviation (0.15)

- Что говорит препринт: отклонение профиля объекта от нормы кластера, категории или глобального baseline.
- Есть ли формальная запись в препринте: частично. В спецификации перечислены признаки profile deviation: listing frequency deviation, avg price deviation from cluster, complaint rate deviation, device count deviation, ip count deviation, sales velocity deviation.
- Соответствие в коде: вероятно `gibbs` и `surprise`.
- Соответствие в архитектуре v1: `gibbs`, `surprise`.
- Решение: каноническое имя — `profile_deviation`.
- Действие: `implement_or_split`. Нужно решить, остаётся ли `gibbs` общей компонентой для Local_Action_Risk + Profile_Deviation, или мы разделяем локальный риск действия и профильное отклонение.

Комментарий: для «Футуролога» profile deviation может означать отклонение actor/source/topic от собственной истории и от peer-group: например, источник начал публиковать необычные темы, компания резко изменила паттерн найма, регион стал генерировать нетипичные сообщения.

## 3.3 Flow_Asymmetry (0.15)

- Что говорит препринт: риск, связанный с асимметрией потоков: много входящих действий и мало нормального завершения, много продаж и быстрый вывод, высокие жалобы после продаж, money flow или interaction flow.
- Есть ли формальная запись в препринте: частично. Есть список признаков, но нет единой строгой формулы.
- Соответствие в коде: None по списку DEFAULT_WEIGHTS.
- Соответствие в архитектуре v1: None.
- Решение: каноническое имя — `flow_asymmetry`.
- Действие: `implement`.

Комментарий: в домене «Футуролога» flow_asymmetry может быть полезен, но требует адаптации. Примеры: много сигналов из одного направления без независимого обратного подтверждения; много публикаций без первичных документов; резкий приток нарратива без реального события; дисбаланс между claims и evidence.

## 3.4 Graph_Risk (0.15)

- Что говорит препринт: графовая компонента выявляет организованный риск через centrality, PageRank, neighbor risk, community risk, edge concentration, flow asymmetry, cycles, hub-and-spoke structures и shared identifiers.
- Есть ли формальная запись в препринте: частично. Есть набор графовых методов, но нет одной окончательной формулы агрегации.
- Соответствие в коде: `graph`.
- Соответствие в архитектуре v1: `graph`.
- Решение: каноническое имя — `graph_risk`.
- Действие: `rename_only` на уровне документации; в коде можно оставить `graph` как implementation key до v3.0, но публичный contract должен использовать `graph_risk`.

Комментарий: это наиболее чистое соответствие между тремя источниками. Разница только в глубине реализации.

## 3.5 Trust_Penalty (0.10)

- Что говорит препринт: `trust_penalty = 1 - normalized_trust_level`.
- Есть ли формальная запись в препринте: да, есть простая формула.
- Соответствие в коде: `trust`.
- Соответствие в архитектуре v1: косвенно через trusted baseline, source reliability, provenance trust.
- Решение: каноническое имя — `trust_penalty`, но с обязательной проверкой знака.
- Действие: `conflict`.

Комментарий: если `trust` в коде означает «чем выше, тем больше доверие», его нельзя напрямую складывать как риск. Если `trust` уже означает penalty, нужно переименовать в `trust_penalty`. Это открытый вопрос перед миграцией.

## 3.6 Sequential_Anomaly_Score (0.15)

- Что говорит препринт: стратегический риск — это не просто выброс, а когерентная траектория. Практическая форма: `Sequential_Anomaly_Score = Pattern_Risk × Sequential_Coherence × Temporal_Compression`.
- Есть ли формальная запись в препринте: да, есть операционная мультипликативная форма.
- Соответствие в коде: `sequential`.
- Соответствие в архитектуре v1: `sequential`.
- Решение: каноническое имя — `sequential_anomaly_score`.
- Действие: `rename_only`.

Комментарий: `sequential` в коде и архитектуре можно считать implementation alias. Для итогового contract лучше использовать полное имя `sequential_anomaly_score`.

## 3.7 RG_Persistence_Score (0.15)

- Что говорит препринт: RG_Persistence_Score измеряет выживание информационной асимметрии при укрупнении масштаба.
- Есть ли формальная запись в препринте: да. `RG_Persistence_Score(e) = 1 - exp(-λ * Σ_l β_l * Div(P_l(e) || P_l(N_l)))`.
- Соответствие в коде: `residue`.
- Соответствие в архитектуре v1: `residue`.
- Решение: каноническое имя — `rg_persistence_score`.
- Действие: `rename_only` или `keep_alias`.

Комментарий: `residue` — удачное короткое имя для реализации, но в документах и API лучше использовать `rg_persistence_score`, потому что оно напрямую связано с препринтом.

## 3.8 Scale_Stability (0.25 objective)

- Что говорит препринт: риск должен оставаться стабильным при наблюдении на больших масштабах. Указано: `G_R(k) = |Risk(k+1) - Risk(k)|`; риск стабилен, если `G_R(k) <= η` для `k >= k*`.
- Есть ли формальная запись в препринте: да, есть критерий стабильности через разность risk на соседних масштабах.
- Соответствие в коде: None как отдельная objective-компонента.
- Соответствие в архитектуре v1: частично `residue`.
- Решение: каноническое имя — `scale_stability`.
- Действие: `implement`.

Комментарий: важно не смешать `rg_persistence_score` и `scale_stability`. Первое — universal risk component о выживании отклонения. Второе — objective layer component о стабильности самого risk-сигнала между масштабами.

## 3.9 Temporal_Persistence (0.20 objective)

- Что говорит препринт: риск должен сохраняться через последовательность наблюдений, а не возникать как одиночный spike.
- Есть ли формальная запись в препринте: частично. В ТЗ MVP есть операционная форма: доля временных окон, где risk score превышает threshold.
- Соответствие в коде: None как отдельная objective-компонента; частично `sequential`.
- Соответствие в архитектуре v1: частично `sequential`.
- Решение: каноническое имя — `temporal_persistence`.
- Действие: `implement`.

Комментарий: `sequential_anomaly_score` отвечает на вопрос «есть ли рискованная последовательная траектория». `temporal_persistence` отвечает на вопрос «долго ли сохраняется сам риск-сигнал». Это разные уровни.

## 3.10 Source_Redundancy (0.20 objective)

- Что говорит препринт: независимые источники должны поддерживать один и тот же risk type. Есть формулировка `Consensus_R = Pr[source_i and source_j agree on risk type]`.
- Есть ли формальная запись в препринте: да, в виде вероятности/консенсуса между источниками.
- Соответствие в коде: None.
- Соответствие в архитектуре v1: упоминается в confluence example, но не как отдельная компонента.
- Решение: каноническое имя — `source_redundancy`.
- Действие: `implement`.

Комментарий: для «Футуролога» это одна из важнейших компонент, потому что слабый сигнал должен подтверждаться не количеством перепечаток, а независимыми источниками.

## 3.11 Observer_Agreement (0.20 objective)

- Что говорит препринт: независимые модели, правила, графовая аналитика, sequence-аналитика и человеческие аналитики должны сходиться к одному выводу. Указано: `OI_R = Pr[Model_A conclusion = Model_B conclusion]`.
- Есть ли формальная запись в препринте: да, как вероятность совпадения выводов наблюдателей/детекторов.
- Соответствие в коде: None.
- Соответствие в архитектуре v1: None.
- Решение: каноническое имя — `observer_agreement`.
- Действие: `implement`.

Комментарий: в MVP можно считать observers как набор независимых detectors: rule-based, sequence-only, graph-only, baseline deviation, human review. Полная реализация потребует orchestration от ENRA.

## 3.12 Noise_Separation (0.15 objective)

- Что говорит препринт: случайные аномалии не должны становиться стабильным objective risk. Указано: `RiskGap(k) = StableRiskSignal(k) - NoiseSignal(k)`.
- Есть ли формальная запись в препринте: да, как разрыв между устойчивым риск-сигналом и шумовым сигналом; в MVP ТЗ также есть упрощение через average(Scale_Stability, Temporal_Persistence, Source_Redundancy) или улучшенную формулу.
- Соответствие в коде: частично `robustness`, но в коде это discount, не полноценная objective-компонента.
- Соответствие в архитектуре v1: частично `surprise`, `robustness_discount`, confluence logic.
- Решение: каноническое имя — `noise_separation`.
- Действие: `implement`.

Комментарий: `robustness` из кода не должен автоматически считаться `noise_separation`. Если он применяется как discount, его можно использовать как modifier, но не как замену objective-компоненты.

## 4. Каноническая таблица компонент Футуролога

Решение v1: каноническая модель «Футуролога» должна сохранить двухслойную структуру ERG-CAD:

```text
final_score = universal_risk × objective_risk
```

Слой `universal` отвечает за интенсивность риска/аномалии. Слой `objective` отвечает за устойчивость и проверяемость риск-сигнала.

### 4.1 Universal layer

| Канонич. имя | Слой | Вес (старт) | Реализация | Происхождение |
|---|---|---:|---|---|
| `local_action_risk` | universal | 0.15 | partial | ERG-CAD + Entropy-RG `gibbs/surprise` |
| `profile_deviation` | universal | 0.15 | partial | ERG-CAD + Entropy-RG `gibbs/surprise` |
| `flow_asymmetry` | universal | 0.15 | not_implemented | ERG-CAD |
| `graph_risk` | universal | 0.15 | ready/partial | ERG-CAD + architecture `graph` + code `graph` |
| `trust_penalty` | universal | 0.10 | partial/conflict | ERG-CAD + code `trust` |
| `sequential_anomaly_score` | universal | 0.15 | ready/partial | ERG-CAD + architecture/code `sequential` |
| `rg_persistence_score` | universal | 0.15 | ready/partial | ERG-CAD + architecture/code `residue` |

Сумма весов universal layer = 1.00.

Примечание: `gibbs`, `surprise`, `residue`, `sequential`, `graph`, `trust`, `robustness` остаются допустимыми внутренними implementation keys Entropy-RG v2.2/v3.0, но публичный scoring contract должен возвращать канонические имена или давать явный alias-map.

### 4.2 Objective layer

| Канонич. имя | Слой | Вес (старт) | Реализация | Происхождение |
|---|---|---:|---|---|
| `scale_stability` | objective | 0.25 | not_implemented | ERG-CAD |
| `temporal_persistence` | objective | 0.20 | not_implemented | ERG-CAD |
| `source_redundancy` | objective | 0.20 | not_implemented | ERG-CAD + architecture confluence example |
| `observer_agreement` | objective | 0.20 | not_implemented | ERG-CAD |
| `noise_separation` | objective | 0.15 | not_implemented | ERG-CAD + code `robustness` частично |

Сумма весов objective layer = 1.00.

### 4.3 Что делать с текущими DEFAULT_WEIGHTS Entropy-RG v2.2

Текущие ключи:

```text
gibbs       0.25
residue     0.22
sequential  0.18
surprise    0.18
graph       0.12
trust       0.10
robustness  0.05
```

Решение v1:

1. Не менять их немедленно в коде до завершения domain-neutral rename.
2. Зафиксировать их как `legacy_entropy_rg_weights`.
3. Добавить mapping layer, который преобразует legacy output в canonical output.
4. Не считать `robustness` самостоятельной universal-компонентой, если он реально применяется как discount.
5. Не считать `trust` эквивалентом `trust_penalty`, пока не проверен знак.

Минимальный mapping:

| Legacy key | Canonical candidate | Статус |
|---|---|---|
| `gibbs` | `local_action_risk` / `profile_deviation` | requires_review |
| `surprise` | `local_action_risk` / `profile_deviation` | requires_review |
| `residue` | `rg_persistence_score` | accepted_alias |
| `sequential` | `sequential_anomaly_score` | accepted_alias |
| `graph` | `graph_risk` | accepted_alias |
| `trust` | `trust_penalty` | conflict_sign_check |
| `robustness` | modifier for `noise_separation` or discount | requires_review |

## 5. Objective_Risk_Score: план реализации

Objective_Risk_Score полностью отсутствует в текущем коде как отдельный слой. Его нельзя подменять confluence_bonus или robustness_discount. Confluence показывает согласованность компонент внутри scoring, а Objective_Risk_Score отвечает на другой вопрос: стал ли риск-сигнал достаточно устойчивым и проверяемым, чтобы считать его операционально объективным.

## 5.1 Scale_Stability

Что нужно для расчёта:

- risk score на нескольких scale levels;
- mapping event → actor → topic → macro-topic → graph/community;
- история score по каждому масштабу;
- threshold `η`;
- минимальный уровень масштаба `k*`.

Подходящий класс алгоритмов:

- multi-scale aggregation;
- divergence measures;
- scale-to-scale gradient;
- stability thresholding.

Зависимости:

- confinement/residue module;
- graph/community aggregation;
- topic hierarchy;
- baseline context.

Сложность: high.

MVP-формула:

```text
scale_stability = number_of_scales_with_significant_deviation / total_scales
```

Более строгая форма:

```text
G_R(k) = |Risk(k+1) - Risk(k)|
stable_k = 1 if G_R(k) <= η else 0
scale_stability = mean(stable_k for k >= k*)
```

## 5.2 Temporal_Persistence

Что нужно для расчёта:

- time windows;
- risk score per window;
- persistence threshold;
- decay policy;
- history store.

Подходящий класс алгоритмов:

- rolling windows;
- exponential decay;
- sequential evidence accumulation;
- threshold survival analysis.

Зависимости:

- sequential module;
- state store;
- audit/history layer.

Сложность: medium.

MVP-формула:

```text
temporal_persistence =
    count(time_windows where risk_score >= threshold) / total_time_windows
```

Важно: это не то же самое, что `sequential_anomaly_score`. Sequential score может быть высоким из-за паттерна, а temporal persistence проверяет длительность сохранения риска.

## 5.3 Source_Redundancy

Что нужно для расчёта:

- source_id для каждого event/evidence;
- source independence graph;
- source reliability;
- duplicate/repost detection;
- claim clustering.

Подходящий класс алгоритмов:

- source clustering;
- redundancy counting;
- independence weighting;
- claim matching;
- duplicate cascade detection.

Зависимости:

- source registry;
- evidence store;
- deduplication;
- provenance model.

Сложность: medium/high.

MVP-формула:

```text
source_redundancy =
    independent_sources_supporting_signal / total_relevant_sources
```

Уточнение: количество источников не равно независимости. Если 20 публикаций перепечатали один первоисточник, redundancy должна быть низкой.

## 5.4 Observer_Agreement

Что нужно для расчёта:

- несколько независимых detectors/observers;
- вывод каждого observer по одному signal/entity/topic;
- единая шкала conclusion;
- human review, если доступен.

Подходящий класс алгоритмов:

- ensemble agreement;
- inter-rater agreement;
- model consensus;
- voting with reliability weights.

Зависимости:

- набор detectors: rule-based, graph-only, sequence-only, baseline deviation, human review;
- ENRA audit path;
- model/version registry.

Сложность: medium.

MVP-формула:

```text
observer_agreement =
    observers_flagging_same_risk_type / total_observers
```

Более строгий вариант на будущее:

```text
observer_agreement = weighted_consensus(observer_outputs, observer_reliability)
```

## 5.5 Noise_Separation

Что нужно для расчёта:

- score для стабильных сигналов;
- score для noise baseline;
- labels или synthetic/semi-synthetic classes;
- historical separation metrics;
- robustness/discount outputs.

Подходящий класс алгоритмов:

- separation margin;
- baseline comparison;
- ablation studies;
- noise-vs-strategy classification;
- distribution distance.

Зависимости:

- calibration module;
- synthetic benchmark;
- historical outcomes;
- robustness discount;
- source/scale/time metrics.

Сложность: high.

MVP-формула из ТЗ:

```text
noise_separation =
    average(scale_stability, temporal_persistence, source_redundancy)
```

Более строгая форма из препринта:

```text
RiskGap(k) = StableRiskSignal(k) - NoiseSignal(k)
noise_separation = normalized_positive_gap(RiskGap)
```

Важно: `robustness` из кода можно использовать как modifier, но не считать полноценной заменой `noise_separation`, пока не проверено его вычисление.

## 6. Финальная формула

Каноническая формула v1:

```text
final_score = universal_risk × objective_risk
```

Где:

```text
universal_risk =
    0.15 * local_action_risk
  + 0.15 * profile_deviation
  + 0.15 * flow_asymmetry
  + 0.15 * graph_risk
  + 0.10 * trust_penalty
  + 0.15 * sequential_anomaly_score
  + 0.15 * rg_persistence_score
```

```text
objective_risk =
    0.25 * scale_stability
  + 0.20 * temporal_persistence
  + 0.20 * source_redundancy
  + 0.20 * observer_agreement
  + 0.15 * noise_separation
```

```text
final_score = universal_risk * objective_risk
```

Обоснование произведения: произведение сохраняет главный смысл ERG-CAD — риск должен быть одновременно интенсивным и объективированным. Если `universal_risk` высокий, но `objective_risk` низкий, сигнал может быть локальным шумом и final_score должен снижаться. Если `universal_risk` средний, но `objective_risk` высокий, сигнал может быть устойчивой структурой и должен сохранять значимость. Взвешенная сумма хуже разделяет эти случаи, потому что высокий local risk может компенсировать низкую objectivity.

### Softer-вариант на ревью

Для раннего MVP можно рассмотреть мягкую формулу:

```text
final_score = universal_risk × (α + (1 - α) × objective_risk)
```

Где:

```text
0 <= α <= 1
```

Интерпретация:

- `α = 0` даёт строгую ERG-CAD формулу: `universal × objective`;
- `α = 0.2` оставляет минимальный вес локального риска, даже если objective слой ещё слабый;
- `α = 1` фактически отключает objective layer.

Решение по `α` должно быть принято пользователем отдельно. До решения канонической считается строгая формула:

```text
final_score = universal_risk × objective_risk
```

## 7. Открытые вопросы

1. Что именно означает `trust` в коде Entropy-RG v2.2: доверие, которое снижает риск, или уже инвертированный penalty?  
   Решение нужно до переименования `trust -> trust_penalty`.

2. Нужно ли сохранить `gibbs` как каноническую компоненту, или перевести его в implementation detail для `local_action_risk` и `profile_deviation`?  
   Сейчас `gibbs` есть в архитектуре и коде, но отсутствует в препринте.

3. Нужно ли разделять `Local_Action_Risk` и `Profile_Deviation` в коде, если текущие `gibbs/surprise` фактически смешивают эти два смысла?  
   Разделение ближе к ERG-CAD, но требует изменения структуры scoring.

4. Что делать с `surprise`: считать его частью `local_action_risk`, частью `profile_deviation` или отдельной вспомогательной метрикой large deviation?  
   В препринте отдельной компоненты Surprise нет.

5. Что делать с `robustness`: оставить как discount, использовать как вход в `noise_separation`, или убрать из публичных весов canonical layer?  
   По заданию он применяется как discount, не как риск.

6. Вводить ли `flow_asymmetry` уже в Entropy-RG v3.0-domain-neutral, или оставить на v3.1 после безопасного переименования seller/listing → actor/event?  
   Компонента есть в ERG-CAD, но отсутствует в архитектуре v1 и текущем коде.

7. Какой уровень совместимости нужен для старого output Entropy-RG v2.2?  
   Варианты: возвращать оба словаря (`legacy_component_scores` и `canonical_component_scores`) или сразу перейти на canonical API.

8. Как считать `observer_agreement` в первом MVP, если пока нет нескольких независимых моделей и human review?  
   Варианты: rule-based + graph-only + sequence-only + baseline-only detectors; human review добавить позже.

9. Использовать ли строгую формулу `universal × objective` сразу или временно применить softer-вариант с `α`?  
   Строгая формула концептуально чище, но мягкая может быть удобнее на раннем этапе, пока objective layer калибруется.

10. Должны ли веса ERG-CAD из препринта заменить DEFAULT_WEIGHTS Entropy-RG v2.2 сразу после mapping, или сначала нужно провести backtest и calibration?  
    Рекомендация этого документа: не менять веса без отдельного calibration milestone.

## 8. Рекомендуемое решение для следующей итерации

Перед domain-neutral rename зафиксировать три уровня имён:

### 8.1 Legacy Entropy-RG keys

```text
gibbs
residue
sequential
surprise
graph
trust
robustness
```

Используются внутри текущего кода до стабилизации.

### 8.2 Canonical Futurolog keys

```text
local_action_risk
profile_deviation
flow_asymmetry
graph_risk
trust_penalty
sequential_anomaly_score
rg_persistence_score
scale_stability
temporal_persistence
source_redundancy
observer_agreement
noise_separation
```

Используются в архитектуре, API contract, audit records и документации.

### 8.3 Mapping layer

Добавить отдельный слой:

```python
def map_legacy_entropy_rg_to_canonical(legacy_scores: dict) -> dict:
    return {
        "rg_persistence_score": legacy_scores.get("residue"),
        "sequential_anomaly_score": legacy_scores.get("sequential"),
        "graph_risk": legacy_scores.get("graph"),
        "trust_penalty": legacy_scores.get("trust"),  # REVIEW_REQUIRED: sign
        "local_action_risk": combine_local_action(
            legacy_scores.get("gibbs"),
            legacy_scores.get("surprise"),
        ),
        "profile_deviation": combine_profile_deviation(
            legacy_scores.get("gibbs"),
            legacy_scores.get("surprise"),
        ),
        "flow_asymmetry": None,  # not implemented
    }
```

Эта функция должна быть явно помечена как transitional. Она не должна скрывать отсутствие `flow_asymmetry` и Objective_Risk_Score.

## 9. Итог

Каноническая модель «Футуролога» должна основываться не только на текущем коде и не только на препринте. Лучшее решение v1:

1. Сохранить двухслойную формулу ERG-CAD:
   `final_score = universal_risk × objective_risk`.

2. Признать текущий Entropy-RG v2.2 реализацией части universal layer, а не всей модели.

3. Считать `residue`, `sequential`, `graph` удачными implementation aliases для:
   `rg_persistence_score`, `sequential_anomaly_score`, `graph_risk`.

4. Считать `gibbs` и `surprise` полезными, но пока неоднозначными реализациями для `local_action_risk` и `profile_deviation`.

5. Считать `trust` конфликтной зоной до проверки знака.

6. Считать `robustness` modifier/discount, а не полноценной компонентой universal risk.

7. Реализовать Objective_Risk_Score отдельным слоем, а не смешивать его с confluence_bonus.

8. Все веса из препринта считать стартовыми и калибруемыми, но не менять их без отдельной задачи и backtest.
