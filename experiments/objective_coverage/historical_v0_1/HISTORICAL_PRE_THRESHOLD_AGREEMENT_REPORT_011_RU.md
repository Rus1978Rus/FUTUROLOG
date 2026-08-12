# HISTORICAL PRE-THRESHOLD AGREEMENT REPORT 011

**Статус:** `REAL_HISTORY_RECODE_002_COMPLETE / TRANSITION_VS_GAP_SEPARATION_IMPROVED / HIDDEN_SEARCH_GUARD_VIOLATION_FOUND / RUBRIC_V0_3_PATCH_REQUIRED`

## 1. Вход

Сравнены три внешние кодировки `HPTB-002-V2`: Copilot, Grok, Claude.

Кейсы обезличены, страны и исходы скрыты. Оценка проводится по логике snapshot, а не по знанию исторического результата.

## 2. Главное улучшение

Все три кодировщика теперь распознали, что очень тяжёлое переходное состояние само по себе не обязано быть structural gap.

На `DK-83` все три дали:

```text
transition_instability_state = TRANSITION_UNDERWAY
structural_gap_status = NO_GAP
```

Это ключевой PASS новой схемы.

Также все три распознали `HP-75` и `JQ-92` как negotiated transition / reconfiguration, не превращая функционирующий государственный аппарат в collapse.

## 3. Критический дефект Copilot: hidden search при NO_GAP

Copilot поставил:

```text
structural_gap_status = NO_GAP
hidden_factor_search_allowed = YES_SEARCH_TRIGGER_ONLY
```

во всех девяти строках.

Это противоречит самому gate рубрики. Если gap отсутствует, hidden-factor search не разрешён.

Обязательный guard:

```text
NO_GAP => hidden_factor_search_allowed = NO
NOT_ASSESSABLE => hidden_factor_search_allowed = NO
YES_SEARCH_TRIGGER_ONLY requires structural_gap_status in {CONDITIONAL_GAP, OPEN_GAP}
```

Copilot result остаётся валидным для transition-state coding, но hidden-factor field считается систематически ошибочным и не используется как evidence agreement.

## 4. Observation sufficiency

### AX-14

Grok: state SUFFICIENT / gap INCOMPLETE.
Claude: state INCOMPLETE / gap INCOMPLETE.
Copilot: state SUFFICIENT / gap SUFFICIENT.

Snapshot прямо сообщает, что army loyalty unknown и command executability only partially observed. Для описания общего state данных достаточно, но для structural-gap inference — нет.

Рекомендуемое правило:

```text
STATE_SUFFICIENCY can be SUFFICIENT with some UNKNOWN dimensions
if transition state can still be bounded.

GAP_SUFFICIENCY requires all diagnostically necessary dimensions
for residual inference.
```

Canonical treatment для AX-14: `state=SUFFICIENT`, `gap=INCOMPLETE`.

### BV-27 / CR-52

Grok и Claude чаще кодируют gap как INCOMPLETE из-за неизвестной cohesion/alignment. Copilot кодирует SUFFICIENT.

Это показывает, что diagnostic minimum для gap inference надо задать явно.

## 5. Transition instability anchors

Согласие высокое по концам шкалы:

- AX/BV: STRESSED;
- DK: TRANSITION_UNDERWAY;
- EL/FM/GN: в основном STRESSED;
- HP/JQ: TRANSITION_UNDERWAY через negotiated reconfiguration.

Основной спор — `CR-52`:

- Copilot: DEGRADING;
- Grok: THRESHOLD_NEAR;
- Claude: DEGRADING.

Snapshot содержит broad compliance degradation + capital diffusion + stressed command, но нет observed critical-node shift. Следовательно `THRESHOLD_NEAR` пока слишком сильный вывод.

Patch:

```text
THRESHOLD_NEAR requires at least one directly observed critical transition marker:
- command executability DEGRADING/COLLAPSING, or
- critical-node alignment MIXED/SHIFTING, or
- alternative coordination with material control,
AND at least one additional reinforcing transition signal.

Mass protest + stressed command alone <= DEGRADING.
```

## 6. External support vs stabilization

FM-46:

- Copilot: transition_signal=EXTERNAL_STABILIZATION;
- Grok/Claude: PRESSURE_ACCUMULATION.

Snapshot даёт political/economic backing, но no foreign force deployment. Наличие поддержки не доказывает, что она уже стабилизирует систему.

Patch:

```text
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_STABILIZATION_EFFECT
AVAILABLE_NOT_DEPLOYED cannot alone produce EXTERNAL_STABILIZATION signal
unless observable stabilizing mechanism/effect is present.
```

GN-68:

- Copilot: TRANSITION_UNDERWAY;
- Grok/Claude: STRESSED.

Физическое развёртывание external forces само по себе не означает, что внутренний политический transition уже underway.

Patch:

```text
EXTERNAL_FORCE_DEPLOYMENT != TRANSITION_UNDERWAY
```

## 7. Critical-node alignment

FM-46: Copilot/Grok = REGIME_ALIGNED; Claude = REGIME_ALIGNED. Agreement stable after v0.2 guard.

JQ-92: Grok = MIXED, Claude = REGIME_ALIGNED, Copilot = REGIME_ALIGNED.

Long-running armed opposition is not automatically internal critical-node defection.

Patch:

```text
EXTERNAL_OR_NONSTATE_ARMED_OPPOSITION != CRITICAL_NODE_DEFECTION
MIXED requires defection/independent action by a node that is part of the incumbent system's critical execution network.
```

## 8. Coercive asset vs executable capacity

Разделение сработало. На DK-83 три модели сохраняют значительный asset capacity при низкой executable capacity / collapsing command.

Это поддерживает фундаментальный guard:

```text
ASSET_CAPACITY != EXECUTABLE_CAPACITY
```

Но численные категории HIGH/MEDIUM всё ещё зависят от того, насколько явно snapshot описывает масштаб assets. Следует запретить повышение asset capacity по контексту кризиса.

## 9. Итоговый статус

```text
TRANSITION_VS_GAP_SPLIT = PASS
ASSET_VS_EXECUTABLE_SPLIT = PASS
EXTERNAL_AVAILABLE_VS_DEPLOYED = PASS
NEGOTIATED_TRANSITION_SEPARATION = PASS
CRITICAL_NODE_RULE = IMPROVED
HIDDEN_SEARCH_GATE = FAIL_IN_COPILOT / PATCH_REQUIRED
THRESHOLD_NEAR_ANCHOR = PATCH_REQUIRED
EXTERNAL_STABILIZATION_SIGNAL = PATCH_REQUIRED
OBSERVATION_SUFFICIENCY_DIAGNOSTIC_MINIMUM = PATCH_REQUIRED
NUMERIC_FORESIGHT_USE = BLOCKED
NEXT = HISTORICAL_TRANSITION_RUBRIC_V0_3 + NEW_REAL_CASE_FAMILIES
```
