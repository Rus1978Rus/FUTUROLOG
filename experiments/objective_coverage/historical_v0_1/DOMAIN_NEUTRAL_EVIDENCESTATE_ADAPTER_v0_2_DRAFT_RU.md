# DOMAIN_NEUTRAL_EVIDENCESTATE_ADAPTER v0.2 DRAFT

**Статус:** `DRAFT / CROSS_CASE_REPAIR_CANDIDATE / NOT_ACTIVE / NOT_CALIBRATED / NOT_VALIDATED`

## 1. Почему нужен v0.2

`EVIDENCE_STATE_ADAPTER_SPEC v0.1` остаётся неизменённым историческим артефактом. Он хорошо подходит к Russia–Ukraine pilot, но его primary classes:

```text
MILITARY_BUILDUP
DIPLOMATIC_COERCION_OR_WARNING
ECONOMIC_ENERGY_STRESS
```

не являются нейтральными для Мьянмы.

Поэтому v0.2 не заменяет v0.1 тихо, а создаётся как отдельный draft.

Guard:

```text
OLD_ADAPTER_LIMIT != PERMISSION_TO_REWRITE_HISTORY
```

## 2. Основной принцип

Вместо событийно-специфических primary classes используются domain-neutral pressure channels. Они описывают тип системного изменения, а не конкретный конфликт.

Предлагаемые каналы:

```text
P1 SECURITY_COERCION_AND_VIOLENCE
P2 INSTITUTIONAL_AND_POLITICAL_PRESSURE
P3 ECONOMIC_RESOURCE_AND_BASIC_NEEDS_STRESS
P4 SOCIAL_GROUP_MOBILIZATION_AND_FRAGMENTATION
P5 SERVICE_INFRASTRUCTURE_AND_HUMAN_SECURITY_DEGRADATION
P6 INFORMATION_ENVIRONMENT_AND_OBSERVATION_DISTORTION
```

Они не являются новой historical schema. Это только adapter layer поверх уже собранных evidence domains.

## 3. Что входит в каналы

### P1 SECURITY_COERCION_AND_VIOLENCE

Примеры:
- military buildup;
- coup-related coercion;
- conflict-event escalation;
- armed-group formation;
- direct security warnings.

Не означает intent или неизбежность исхода.

### P2 INSTITUTIONAL_AND_POLITICAL_PRESSURE

Примеры:
- diplomatic coercion;
- institutional breakdown;
- legitimacy pressure;
- repression of civic/political participation;
- constitutional/governance shock.

### P3 ECONOMIC_RESOURCE_AND_BASIC_NEEDS_STRESS

Примеры:
- macro/energy stress;
- food/fuel price shock;
- banking/payment disruption;
- affordability deterioration;
- resource-capacity signals.

Resource capacity и population hardship различаются и кодируются reason-level отдельно.

### P4 SOCIAL_GROUP_MOBILIZATION_AND_FRAGMENTATION

Примеры:
- professional-group mobilization;
- protest/CDM participation;
- local defense-group emergence;
- coalescence/fragmentation;
- legitimacy-bearing and small-group shifts.

### P5 SERVICE_INFRASTRUCTURE_AND_HUMAN_SECURITY_DEGRADATION

Примеры:
- displacement;
- health-system degradation;
- education disruption;
- water/basic-service disruption;
- humanitarian access deterioration.

### P6 INFORMATION_ENVIRONMENT_AND_OBSERVATION_DISTORTION

Примеры:
- disinformation/narrative pressure;
- media repression;
- internet shutdown;
- sensor collapse;
- agenda amplification;
- representation–reality gap.

Важно: P6 может содержать одновременно реальный social effect и observation-process degradation. Эти subclaims не должны сливаться в одно утверждение.

## 4. Severity rubric

Каждый AVAILABLE channel получает ordinal severity:

```text
0 NONE
1 WEAK
2 SUBSTANTIAL
3 SEVERE
```

Определения сохраняют дух v0.1:

- `0` — нет пригодного свидетельства изменения;
- `1` — общий/локальный сигнал без сильного структурного изменения;
- `2` — устойчивое, существенное или многократно наблюдаемое изменение;
- `3` — крупномасштабное/операционно значимое изменение с сильным пригодным evidence.

Missing channel не становится 0. Он уменьшает coverage.

## 5. Channel availability

Channel AVAILABLE только если есть минимум один item, который:

```text
publication_time <= cutoff
source_family verified
original_publication_time verified
pipeline >= QUALITY_CHECKED
not RETROSPECTIVE_ONLY
not SENSOR_ONLY without imported value if numeric claim is required
```

## 6. measured_pressure_score

Для AVAILABLE channels:

```text
measured_pressure_score = mean(channel_severity / 3)
```

Это pressure score, а не probability of war/coup/collapse.

Guard:

```text
PRESSURE_SCORE != OUTCOME_PROBABILITY
```

## 7. evidence_coverage

```text
evidence_coverage = available_channels / 6
```

Но scalar coverage обязательно сопровождается `coverage_topology_matrix`.

```text
SAME_COVERAGE_PERCENT != SAME_COVERAGE_TOPOLOGY
```

## 8. source_independence

Сохраняется v0.1 family-diversity heuristic, но denominator нормализуется к фактически представленным source families в snapshot, а не к фиксированным трём.

Предлагаемый draft:

```text
HHI = sum(p_i^2)
raw_diversity = 1 - HHI
max_diversity = 1 - 1/n_families
source_independence = raw_diversity / max_diversity, if n_families > 1
source_independence = 0, if n_families = 1
```

Это всё ещё diversity, а не доказанная causal independence.

## 9. freshness

Пока сохраняется прозрачная pilot-эвристика v0.1:

```text
item_freshness = max(0, 1 - age_days / 30)
```

Но v0.2 помечает её `REVIEW_REQUIRED`, потому что разные channels могут иметь разные естественные time constants.

Нельзя менять 30 дней внутри этого draft без отдельного calibration decision.

## 10. pipeline completeness

Сохраняются 7 этапов:

```text
FETCHED
SOURCE_IDENTIFIED
ORIGINAL_PUBLICATION_TIME_VERIFIED
PARSED
NORMALIZED
QUALITY_CHECKED
SCORED
```

## 11. stabilizers / counter-signals

Stabilizer не вычитается автоматически из pressure score.

Он кодируется отдельным directional ledger:

```text
+1 SUPPORTS_PRESSURE_OR_ESCALATION
0 NEUTRAL_OR_UNCLEAR
-1 COUNTERSIGNAL_OR_STABILIZER
```

и strength 1–3.

Почему отдельно: один и тот же system state может одновременно иметь высокий pressure и сильную adaptive capacity.

```text
PRESSURE - STABILIZER != AUTOMATIC_RISK_SCORE
```

## 12. observed_noise

Формула v0.1 может быть сохранена только после systematic negative-control search:

```text
signed_sum = sum(direction * strength)
absolute_sum = sum(abs(direction * strength))
coherence = abs(signed_sum) / absolute_sum
observed_noise = 1 - coherence
```

Если counter-signal search не завершён:

```text
observed_noise = BLOCKED
```

## 13. Observation & Coverage integration

Каждый snapshot обязан хранить:

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

P6 не используется как штраф к другим каналам автоматически. Observation degradation сначала отражается как uncertainty/coverage annotation, иначе система может дважды наказать один и тот же missing-data process.

## 14. Representation–Reality Gap

Для information/social claims хранятся независимо:

```text
AGENDA_VISIBILITY
AGENDA_SOCIAL_PREVALENCE
AGENDA_BEHAVIORAL_IMPACT
```

Неизвестные уровни остаются UNKNOWN.

## 15. Cross-case rule

Russia–Ukraine и Myanmar могут иметь разные populated channels, но один и тот же denominator из шести типов системного давления.

Однако сравнение чисел разрешается только вместе с topology annotation.

```text
SAME_ADAPTER != SAME_OBSERVABILITY
```

## 16. Что v0.2 намеренно НЕ делает

- не предсказывает конкретный исход;
- не выводит causal chain автоматически;
- не превращает resource capacity в intent;
- не объединяет small groups в единый actor без evidence;
- не считает media volume population prevalence;
- не импортирует retrospective evidence в cutoff;
- не калибрует вероятности.

## 17. Gate до активации

Перед переводом из DRAFT в ACTIVE_CANDIDATE нужно:

```text
1 FIRST_CODING_LEDGER_001 frozen
2 blind second-coder packet generated
3 true independent second coding completed
4 agreement report completed
5 negative-control targeted source backfill materially improved
6 leakage audit passed
7 coverage topology attached
8 at least one snapshot per case coded without outcome knowledge in the coding packet
```

## 18. Статус

```text
DOMAIN_NEUTRAL_ADAPTER_v0_2_DRAFT_CREATED
v0_1_PRESERVED
CROSS_CASE_ADAPTER_MISMATCH_ADDRESSED_CONCEPTUALLY
NOT_ACTIVE
NOT_CALIBRATED
NOT_VALIDATED
NUMERIC_EVIDENCESTATE_STILL_BLOCKED
```
