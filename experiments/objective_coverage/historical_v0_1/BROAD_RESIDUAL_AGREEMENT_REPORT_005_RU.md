# BROAD_RESIDUAL_AGREEMENT_REPORT 005

**Статус:** `BROAD_MULTI_MODEL_STRESS_TEST_COMPLETE / ABLATION_FAILURE_DETECTED / STRUCTURAL_GAP_V0_3_PATCH_REQUIRED / NUMERIC_USE_BLOCKED`

## 1. Вход

Сравнены три внешние машинные кодировки `BROAD_BLIND_RESIDUAL_PACKET_002_RU.md`: Claude, Copilot и Grok.

Пакет включал 12 обезличенных snapshots, включая два controlled observability ablations — Q11 и Q12, где часть стабилизирующей информации была намеренно удалена.

Это stress-test метода, а не доказанная outcome-blind validation.

## 2. Что выдержало тест

### 2.1 Intent guards

Все три кодировщика в целом сохранили принцип:

```text
PAST_FORCE_USE != CURRENT_INTENT
FORCE_ALREADY_USED != EXPANSION_INTENT_EVIDENCED
```

Ни одна модель не объявила `expansion_intent = DIRECTLY_EVIDENCED` там, где его не было в snapshot.

### 2.2 Strong-stabilizer cases

Q03 получил `NO_GAP` у всех трёх моделей.

Q02, Q07, Q09 также получили `NO_GAP` у всех трёх.

Это положительный сигнал: наличие высокого риска или уже случившегося инцидента само по себе не заставляет метод создавать hidden-factor hypothesis, если наблюдаемые стабилизаторы уже объясняют конфигурацию.

### 2.3 Q01 high-risk configuration

Все три модели сочли Q01 отличным от простого NO_GAP-контроля:

- Claude: `CONDITIONAL_GAP / PERSISTENT_BEHAVIORAL`
- Copilot: `OPEN_GAP / OBSERVABILITY_RESIDUAL`
- Grok: `CONDITIONAL_GAP / MISSING_LINK`

Но расхождение `OPEN` vs `CONDITIONAL` показывает, что правило observability-first всё ещё недостаточно механическое. При degraded communications OPEN_GAP пока не должен разрешаться без снятия observability explanation.

## 3. Controlled ablation result — главный тест

### Q11

Вход явно говорит, что данные о communication/intermediary/de-escalation channels **не доступны в snapshot**.

- Claude: `UNKNOWN`, hidden search `NO`
- Copilot: `OPEN_GAP`, hidden search `YES`
- Grok: `CONDITIONAL_GAP`, hidden search `YES`

### Q12

Вход явно говорит, что данные о mediation/dialogue/stabilizers **не доступны в snapshot**.

- Claude: `UNKNOWN`, hidden search `NO`
- Copilot: `OPEN_GAP`, hidden search `YES`
- Grok: `CONDITIONAL_GAP`, hidden search `YES`

Для controlled ablations intended safeguard такой:

```text
KNOWN_OBSERVATION_ABLATION != STRUCTURAL_GAP
```

Поэтому 4 из 6 model-decisions на Q11/Q12 разрешили hidden-factor search там, где пропуск был создан самим наблюдением.

**Ablation hidden-cause invention / false-trigger rate = 4/6 = 66.7%.**

Это не значит, что модели «придумали конкретную тайную причину» как факт. Они соблюдали `SEARCH_TRIGGER_ONLY`, но сам trigger был ложноположительным: missing measurement был принят за основание structural-gap search.

## 4. Over-trigger pattern

Copilot дал hidden-factor search для Q01, Q04, Q05, Q08, Q10, Q11, Q12 — 7/12.

Grok — для Q01, Q10, Q11, Q12 — 4/12.

Claude — только для Q01 — 1/12.

Это не рейтинг моделей и не majority truth. Разброс показывает, что текущая инструкция недостаточно жёстко отделяет:

```text
UNKNOWN / OBSERVATION_INCOMPLETE
от
CONDITIONAL_STRUCTURAL_GAP
```

Особенно это видно на Q04, Q05, Q08 и Q10: часть кодировщиков создаёт gap просто из-за неизвестной эффективности стабилизаторов, неизвестного intent или смены политической фазы.

## 5. Defect: NO_GAP with residual

Grok на Q06 вернул:

```text
structural_gap_status = NO_GAP
primary_structural_residual_type = PERSISTENT_BEHAVIORAL
```

Это нарушает уже установленный invariant:

```text
NO_GAP => primary_structural_residual_type = NONE
```

Следовательно, правило должно быть не только текстовым guard, а schema-level validation rule.

## 6. Defect: force-use ontology

Q05/Q11 выявили неоднозначность `current_force_use_state`.

Naval interdiction/quarantine может быть:

- реальной coercive military operation;
- применением военной силы в широком смысле;
- но не обязательно kinetic/lethal force against opponent units.

Claude закодировал Q05/Q11 как `OBSERVED`; Copilot/Grok часто как `NOT_OBSERVED`.

Это не обычное coder disagreement — поле смешивает разные онтологические уровни.

Нужно разделить:

```text
military_coercion_state
kinetic_force_state
lethal_force_state
```

## 7. Defect: reassurance decay / temporal sequencing

Q10 дал:

- Claude: `NO_GAP / TEMPORAL_LAG`
- Copilot: `CONDITIONAL_GAP`
- Grok: `CONDITIONAL_GAP / SIGN_MISMATCH`

Проблема: старое reassurance и позднейший односторонний escalatory step не образуют logical contradiction автоматически.

Нужен guard:

```text
EARLIER_REASSURANCE + LATER_ESCALATORY_STEP != STRUCTURAL_GAP
SEQUENTIAL_STATE_CHANGE != SIGN_MISMATCH
```

Gap появляется только если текущая модель, с учётом изменения времени/контекста, всё ещё требует несовместимых выводов.

## 8. Defect: mediation uncertainty

Q04 показал аналогичную проблему. Сам факт, что settlement effectiveness неизвестна, не должен создавать structural gap.

```text
STABILIZER_EFFECT_UNKNOWN != STRUCTURAL_GAP
MEDIATION_PRESENT != STABILIZATION_PROVEN
MEDIATION_EFFECT_UNKNOWN != MISSING_MECHANISM
```

## 9. Broad agreement summary

Высокое согласие наблюдается по:

- Q02 = NO_GAP
- Q03 = NO_GAP
- Q06 = NO_GAP (но Grok residual-field violation)
- Q07 = NO_GAP
- Q09 = NO_GAP
- expansion intent generally UNKNOWN

Среднее/низкое согласие:

- Q01 gap severity/type
- Q04 whether uncertainty itself is gap
- Q05 whether extreme danger + communications creates gap
- Q08 whether unknown cost tolerance creates gap
- Q10 temporal change vs sign mismatch
- Q11/Q12 observation ablation handling

## 10. Gate decision

```text
BROAD_RESIDUAL_STRESS_TEST_005 = COMPLETE
STRONG_STABILIZER_NO_GAP_RULE = PROMISING
INTENT_GUARDS = PROMISING
OBSERVABILITY_ABLATION_GUARD = FAIL
HIDDEN_SEARCH_FALSE_TRIGGER_RATE_ON_ABLATIONS = 66.7%
FORCE_USE_ONTOLOGY = PATCH_REQUIRED
NO_GAP_SCHEMA_VALIDATION = PATCH_REQUIRED
TEMPORAL_SEQUENCING_RULE = PATCH_REQUIRED
NUMERIC_USE = BLOCKED
STRUCTURAL_GAP_RUNTIME = BLOCKED
NEXT = STRUCTURAL_GAP_INFERENCE_V0_3_PATCH + ABLATION_RETEST
```

## 11. Методологическое решение

Нельзя выбирать Claude как «правильную модель» только потому, что он оказался наиболее консервативным на ablations. Его ответы используются как evidence того, что desired behavior достижим при текущих данных, а Copilot/Grok показывают, где инструкция допускает false trigger.

Исправляется метод и схема, а не подбирается удобный кодировщик.
