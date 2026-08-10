# ABLATION_RETEST_REPORT 006

**Статус:** `PARTIAL_MULTI_MODEL_COMPLETE / GROK_PASS / CLAUDE_PASS / COPILOT_INVALID_PACKET_RESPONSE / ABLATION_GATE_PROVISIONALLY_PASSED_2_OF_2`

## 1. Вход

Получены три ответа, но только два относятся к `ABLATION_RETEST_001`:

- Grok: валидный ответ по `ABL-01..ABL-08` и новой schema.
- Claude: валидный ответ по `ABL-01..ABL-08` и новой schema.
- Copilot: ответ по старому broad packet `X01..X12` и старой schema. Он НЕ включается в agreement/gate metrics и требует повторного прогона правильного файла.

```text
WRONG_PACKET_RESPONSE != FAILED_METHOD
INVALID_TEST_INPUT => EXCLUDE_FROM_METRICS
```

## 2. Главный ablation gate

Целевые ablation cases:

- `ABL-02`: удалена информация о communication/intermediary/de-escalation.
- `ABL-04`: удалена информация о mediation/dialogue/stabilizers.

### Grok

Оба случая:

```text
observation_status = INCOMPLETE
structural_gap_status = NOT_ASSESSABLE
observation_recovery_search = YES
hidden_factor_search_allowed = NO
```

### Claude

Оба случая: те же четыре ключевых решения.

### Итог по двум валидным внешним кодировщикам

```text
hidden_factor_false_trigger_rate = 0 / 4 = 0%
observation_recovery_trigger_rate = 4 / 4 = 100%
```

Это устраняет главный failure mode предыдущего broad test на текущей выборке двух валидных моделей.

## 3. Остальные mechanical guards

Обе модели подтвердили:

- `ABL-05`: unknown cost tolerance НЕ создаёт structural gap;
- `ABL-06`: sequential change НЕ кодируется как sign-mismatch gap;
- `ABL-08`: naval interdiction/quarantine = military coercion; kinetic/lethal force не импортируются автоматически;
- `ABL-07`: third-party peacekeeping reinforcement не превращается в actor escalatory intent;
- все `ABL-01..08`: hidden-factor search запрещён при `NO_GAP` или `NOT_ASSESSABLE`.

## 4. Остаточные расхождения ontology

### 4.1 continuation_intent_at_observed_level

Grok:

- ABL-01/02/08: `UNKNOWN`.

Claude:

- ABL-01/02/08: `DIRECTLY_EVIDENCED`, потому что текущая coercive operation уже наблюдается.

Проблема: поле смешивает два разных вопроса:

1. действие продолжается прямо сейчас?
2. есть ли доказанное намерение продолжать его в будущем?

Patch required:

```text
CURRENT_ACTION_CONTINUATION_STATE != FUTURE_CONTINUATION_INTENT
OBSERVED_ONGOING_ACTION can evidence current continuation
OBSERVED_ONGOING_ACTION does NOT prove future continuation intent beyond observation window
```

### 4.2 military_coercion_state for communal violence

Grok ABL-03: `UNKNOWN`.
Claude ABL-03: `NOT_OBSERVED`.

Проблема: lethal communal/political violence не обязательно является military coercion. Нужна actor/instrument qualification.

```text
VIOLENCE != MILITARY_COERCION
MILITARY_COERCION requires military/security coercive instrument evidence
```

### 4.3 lethal_force_state for unspecified violent incident

Grok ABL-07: `OBSERVED`.
Claude ABL-07: `UNKNOWN`.

Snapshot говорит только `violent incident`, без явной lethal characterization. Поэтому guard должен быть механическим:

```text
VIOLENT_INCIDENT != LETHAL_FORCE
NO_EXPLICIT_LETHAL_EVIDENCE => lethal_force_state = UNKNOWN or NOT_OBSERVED_BY_SCHEMA_RULE
```

Нужно выбрать одно canonical значение. Предлагается `UNKNOWN`, если snapshot не утверждает ни наличие, ни отсутствие lethal force.

## 5. Gate decision

```text
ABLATION_GATE_VALID_CODERS = 2
ABLATION_FALSE_TRIGGER_TARGET = PASS_PROVISIONAL
OBSERVATION_RECOVERY_TARGET = PASS_PROVISIONAL
COPILOT_RETEST_REQUIRED = YES
STRUCTURAL_GAP_V0_3_CORE_GUARD = SUPPORTED
ONTOLOGY_PATCH_REQUIRED = YES
NUMERIC_USE = BLOCKED
```

`PASS_PROVISIONAL` означает: механизм выдержал тест на двух корректных независимых машинных ответах, но третий intended coder не тестировал нужный пакет.

## 6. Next

1. Повторить `ABLATION_RETEST_001` только для Copilot.
2. Применить ontology patch v0.4.
3. После Copilot rerun сделать final `ABLATION_RETEST_REPORT_007`.
4. Только затем расширять Structural Gap Inference на новые domain classes.
