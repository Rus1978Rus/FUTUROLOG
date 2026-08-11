# HISTORICAL_PRE_THRESHOLD_AGREEMENT_REPORT_010

**Статус:** `REAL_HISTORY_BLIND_TEST_COMPLETE / CORE_DISTINCTIONS_PARTLY_STABLE / GAP_FIELD_OVERTRIGGERS_FOUND / RUBRIC_PATCH_REQUIRED`

## 1. Вход

Сравнены три внешние кодировки `HISTORICAL_PRE_THRESHOLD_BLIND_PACKET_001`: Copilot, Claude, Grok.

Пакет содержал девять обезличенных source-backed snapshots: четыре последовательных пред-пороговых среза одного режима и пять сравнительных controls/transition cases. Названия стран и исходы были скрыты.

## 2. Что выдержало тест

### External support
FM-46: все три отличили `AVAILABLE_NOT_DEPLOYED` от фактического ввода сил.
GN-68: все три распознали `DEPLOYED`.

Следовательно guard:

```text
EXTERNAL_SUPPORT_AVAILABLE != EXTERNAL_FORCE_DEPLOYED
```

поддержан тремя кодировщиками.

### Negotiated transition
HP-75 и JQ-92: все три кодировщика не приняли наличие переговоров/переходной рамки за collapse. Во всех валидных строках hidden-factor search не разрешён.

Поддержаны guards:

```text
NEGOTIATION_EXISTS != NEGOTIATION_SUCCESS
NEGOTIATED_TRANSITION != STATE_COLLAPSE
```

### Mass protest vs collapse
EL-31: все три дали NO_GAP при высокой протестной активности и сохранённой командной структуре.

Поддержан guard:

```text
MASS_PROTEST != REGIME_COLLAPSE
```

### Capacity vs executability
DK-83: все модели разделили наличие силового ресурса и коллапс исполнимости команд. Это ключевая историческая проверка:

```text
COERCIVE_CAPACITY_EXISTS != REGIME_EXECUTABLE_CAPACITY
FORMAL_AUTHORITY != EFFECTIVE_COMMAND_EXECUTION
```

## 3. Главный дефект — structural_gap_status смешался с transition severity

Copilot начинает давать `CONDITIONAL_GAP/OPEN_GAP` уже при AX-14, BV-27, CR-52, DK-83, то есть трактует растущую кризисность и неопределённость узлов как structural gap.

Grok даёт `CONDITIONAL_GAP` на DK-83 при уже наблюдаемом collapsing executability и shifting alignment.

Claude, напротив, почти везде даёт `NO_GAP`, если наблюдаемая конфигурация уже внутренне объяснима текущими полями.

Это показывает, что поле `structural_gap_status` в данном историческом packet выполняло две несовместимые функции:

1. обнаружить неполноту модели;
2. выразить степень опасности/пороговости перехода.

Необходимо развести их.

## 4. Новый split

Ввести отдельные оси:

```text
transition_instability_state = STABLE | STRESSED | DEGRADING | THRESHOLD_NEAR | TRANSITION_UNDERWAY | UNKNOWN
structural_gap_status = NO_GAP | CONDITIONAL_GAP | OPEN_GAP | NOT_ASSESSABLE
```

Правила:

```text
HIGH_TRANSITION_RISK != STRUCTURAL_GAP
THRESHOLD_NEAR != STRUCTURAL_GAP
TRANSITION_UNDERWAY != STRUCTURAL_GAP
OBSERVED_COMMAND_COLLAPSE != STRUCTURAL_GAP
```

Structural gap разрешён только если наблюдаемая конфигурация остаётся необъяснённой после использования уже имеющихся state variables.

## 5. Observation sufficiency ambiguity

AX-14: Claude поставил `INCOMPLETE/NOT_ASSESSABLE`, потому что command executability прямо отмечена как partially observed. Copilot/Grok оставили `SUFFICIENT`.

Нужно различить:

```text
SUFFICIENT_FOR_STATE_CODING
SUFFICIENT_FOR_STRUCTURAL_GAP_ASSESSMENT
```

Предлагаемый patch:

```text
observation_status_state = SUFFICIENT | INCOMPLETE
observation_status_gap = SUFFICIENT | INCOMPLETE
```

Snapshot может быть достаточен для кодирования observable crisis state, но недостаточен для structural-gap inference.

## 6. Public compliance ambiguity

BV-27, GN-68, HP-75, JQ-92 дали расхождения по `DEGRADED_LOCAL / DEGRADED_BROAD / UNKNOWN / STABLE`.

Причина: snapshot часто не задаёт явный geographic denominator. Нельзя выводить broad degradation только из persistence/violence/negotiation.

Patch:

```text
NO_EXPLICIT_PUBLIC_SCOPE => public_compliance_signal = UNKNOWN or minimum directly supported scope
PUBLIC_COMPLIANCE_SCOPE != CRISIS_SEVERITY
```

## 7. Critical-node alignment ambiguity

FM-46 и HP-75 показали расхождение `REGIME_ALIGNED` vs `MIXED` при формулировках вроде `mostly regime-aligned with some elite uncertainty`.

Нужен explicit anchor:

```text
REGIME_ALIGNED = no observed meaningful organized defection; uncertainty alone does not make MIXED
MIXED = at least one materially relevant critical node/elite bloc is observed acting against/independently of incumbent alignment
SHIFTING = directional movement of critical nodes is directly observed
```

Guard:

```text
ELITE_UNCERTAINTY != ELITE_DEFECTION
```

## 8. Coercive-capacity scale ambiguity

BV-27, CR-52, DK-83, JQ-92 дали различия HIGH/MEDIUM. Причина: пакет не определил, оценивается ли физический запас силового ресурса, наблюдаемая активность или эффективная usable capacity.

Нужно разделить:

```text
coercive_asset_capacity = HIGH | MEDIUM | LOW | UNKNOWN
coercive_executable_capacity = HIGH | MEDIUM | LOW | UNKNOWN
```

При этом `command_executability_state` остаётся отдельной осью динамики.

## 9. Вывод по sequential threshold case

Четыре последовательных snapshots AX-14 → BV-27 → CR-52 → DK-83 показали полезную вещь: модели согласны, что кризис проходит от локальной деградации к collapsing command executability и shifting node alignment, но disagreement возникает не на самих observed state variables, а при попытке назвать это `structural gap`.

Следовательно историческая траектория требует отдельного понятия:

```text
TRANSITION_SIGNAL
```

а не использования Structural Gap Inference как общего индикатора приближения collapse.

## 10. Решение

```text
REAL_HISTORY_BLIND_TEST_001 = COMPLETE
EXTERNAL_SUPPORT_SPLIT = PASS
NEGOTIATED_TRANSITION_SPLIT = PASS
MASS_PROTEST_VS_COLLAPSE = PASS
CAPACITY_VS_EXECUTABILITY = PASS
STRUCTURAL_GAP_FIELD_IN_TRANSITION_PACKET = PARTIAL_FAIL
OBSERVATION_SUFFICIENCY_SPLIT = REQUIRED
PUBLIC_COMPLIANCE_SCOPE_PATCH = REQUIRED
CRITICAL_NODE_ALIGNMENT_ANCHORS = REQUIRED
COERCIVE_ASSET_VS_EXECUTABLE_CAPACITY_SPLIT = REQUIRED
NUMERIC_USE = BLOCKED
NEXT = HISTORICAL_TRANSITION_RUBRIC_V0_2 + BLIND_RECODE_002
```

## 11. Методологический вывод

Главный результат теста — настоящий исторический threshold не обязан создавать structural residual. Если FUTUROLOG уже наблюдает падение исполнимости команд и смещение критических узлов, это может быть хорошо объяснённый transition state, а не признак отсутствующей переменной.

```text
SYSTEM_TRANSITION != MODEL_FAILURE
OBSERVED_COLLAPSE_DYNAMICS != HIDDEN_CAUSE
```
