# COPILOT_ABLATION_RETEST_PROTOCOL_FAILURE_007

**Статус:** `PROTOCOL_FAILURE / WRONG_SCHEMA_AND_CONTENT / NOT_A_VALID_ABLATION_RESULT / DO_NOT_SCORE_AS_MODEL_FAILURE`

## 1. Что получено

Повторный ответ, помеченный как Copilot, использует case_id `ABL-01`–`ABL-08`, но фактически сохраняет старую schema:

- `structural_gap_status`
- `primary_structural_residual_type`
- `pre_hidden_explanation_priority`
- `hidden_factor_search_allowed`
- `max_3_hypothesis_classes`
- `max_3_discriminating_evidence_targets`
- `current_force_use_state`
- `continuation_intent_at_observed_level`
- `expansion_intent`

В актуальном `ABLATION_RETEST_001` обязательна новая schema с `observation_status`, `observation_recovery_search`, `primary_missing_observation_class`, `military_coercion_state`, `kinetic_force_state`, `lethal_force_state` и др.

## 2. Признак contamination

Содержимое строк воспроизводит паттерн предыдущего broad residual ответа: ABL-01 описан как high signaling/concentration/degraded communication, ABL-02 как armed incidents + ceasefire/mediation, ABL-03 как hotline/alliance reassurance и т.д. Это не соответствует актуальным ABL-01–ABL-08 snapshots.

Следовательно простая замена case IDs произошла без выполнения нового задания либо контекст/старый шаблон доминировал над приложенным файлом.

## 3. Решение

```text
COPILOT_RETEST_2 = INVALID
FAILURE_CLASS = PROTOCOL_ADHERENCE / PACKET_CONTENT_CONTAMINATION
ABLATION_METRICS = NOT_UPDATED
GROK_VALID = YES
CLAUDE_VALID = YES
THREE_MODEL_GATE = NOT_COMPLETE
```

Нельзя считать ABL-02/ABL-04 ответом по текущему тесту, несмотря на совпадающие идентификаторы строк.

## 4. Новый guard для внешнего конвейера

```text
CASE_ID_MATCH != PACKET_COMPLIANCE
SCHEMA_MATCH REQUIRED
SNAPSHOT_SEMANTIC_MATCH REQUIRED
WRONG_SCHEMA => REJECT_BEFORE_SCORING
STALE_TEMPLATE_CONTAMINATION => REJECT_BEFORE_SCORING
```

## 5. Следующий шаг

Не повторять тот же DOCX третий раз в том же формате. Подготовить Copilot-specific minimal packet с:

- новым случайным префиксом case IDs;
- только двумя ablation pairs + ontology controls;
- обязательной первой строкой `PACKET_SCHEMA_ID`;
- checksum-like semantic challenge field, не являющимся криптографическим hash;
- запретом использовать любую schema кроме указанной;
- evaluator проверяет schema до содержательного scoring.
