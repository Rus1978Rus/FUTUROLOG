# TEMPORAL TRANSITION RUBRIC v0.4 — PATCH

**Статус:** `PATCH_CANDIDATE / BASED_ON_TEMPORAL_SEQUENCE_TEST_001 / NOT_NUMERICALLY_VALIDATED`

## 1. Причина патча

В slow-transition series три независимых кодировщика выбрали разные первые точки structural distinguishability, хотя согласились по моменту фактически наблюдаемого перехода. Это показывает, что одинарное поле `STRUCTURALLY_DISTINGUISHABLE` смешивает разные уровни доказательной силы.

## 2. Detection window

Заменить идею единственной точки на окно обнаружения:

```text
EARLY_DIFFERENTIATOR
ROBUST_DIFFERENTIATOR
THRESHOLD_DIFFERENTIATOR
TRANSITION_OBSERVED
```

## 3. Семантика уровней

### EARLY_DIFFERENTIATOR

Впервые наблюдается прямой системный механизм, который уже отличает траекторию от обычного pressure accumulation, но:
- механизм ещё может быть обратим;
- центр может оставаться функциональным;
- альтернативная траектория не является доминирующей;
- outcome не прогнозируется как неизбежный.

Примеры классов:
- institutionalized alternative center;
- first observed command-refusal;
- critical-node disagreement becoming operationally relevant.

### ROBUST_DIFFERENTIATOR

Ранний differentiator сохраняется, усиливается или получает подтверждение неспособности известных стабилизаторов/силовых средств восстановить прежнюю конфигурацию.

Примеры:
- coercion applied but political monopoly not restored;
- alternative center remains active across successive cutoffs;
- command erosion persists despite corrective action;
- center-periphery burden begins to affect critical-node alignment.

### THRESHOLD_DIFFERENTIATOR

Наблюдаемое сочетание прямых transition mechanisms делает system-transition interpretation намного сильнее обычного crisis explanation.

Требуется минимум одно core condition:

```text
command_executability = DEGRADING or COLLAPSING
OR critical_node_alignment = SHIFTING or OPPOSITION_ALIGNED
OR alternative_coordination = ACTIVE/DOMINANT with incumbent-center functional loss
```

и минимум один reinforcing condition:

```text
public compliance broad degradation
failed restoration attempt
formal-center/effective-center divergence
recognized alternative authority
center-periphery overstretch affecting core nodes
```

### TRANSITION_OBSERVED

Сам переход уже непосредственно наблюдается:
- old center loses effective command;
- new authority assumes executive control;
- sovereign nodes exit old system;
- negotiated institutional reconfiguration is being implemented;
- incumbent regime is actually replaced.

Это descriptive state, а не structural gap.

## 4. Новое поле

```text
trajectory_detection_stage =
NOT_YET
| EARLY_DIFFERENTIATOR
| ROBUST_DIFFERENTIATOR
| THRESHOLD_DIFFERENTIATOR
| TRANSITION_OBSERVED
| UNKNOWN
```

Старое `trajectory_distinguishability` считать superseded после нового теста.

## 5. Series-level summary

Для каждой временной серии возвращать:

```text
first_early_differentiator_step
first_robust_differentiator_step
first_threshold_differentiator_step
first_transition_observed_step
```

Если уровня нет — `NONE`.

Это позволяет различать быстрый collapse и slow-transition detection window.

## 6. Guards

```text
SLOW_TRANSITION != SINGLE_THRESHOLD_POINT
FIRST_DIFFERENTIATOR != THRESHOLD_DIFFERENTIATOR
EARLY_DIFFERENTIATOR != INEVITABLE_OUTCOME
ROBUST_DIFFERENTIATOR != CENTER_COLLAPSE
THRESHOLD_DIFFERENTIATOR != CERTAIN_FINAL_OUTCOME
TRANSITION_OBSERVED != STRUCTURAL_GAP
ALTERNATIVE_CENTER_EXISTS != TRANSITION_INEVITABLE
COERCION_FAILURE_TO_RESTORE_MONOPOLY != CENTER_COLLAPSE
FAILED_CENTER_COUP != FINAL_SYSTEM_DISSOLUTION
```

## 7. Confidence discipline

```text
confidence = LOW | MEDIUM | HIGH
```

Числовые confidence запрещены в этом rubric family.

```text
NUMERIC_CONFIDENCE => PROTOCOL_WARNING
```

Это не обязательно invalidates содержательное кодирование, но исключает автоматическое механическое сравнение confidence до нормализации.

## 8. Transition signal

Сохранить:

```text
NONE
PRESSURE_ACCUMULATION
COMMAND_EROSION
NODE_REALIGNMENT
ALTERNATIVE_COORDINATION
CENTER_PERIPHERY_OVERSTRETCH
NEGOTIATED_RECONFIGURATION
EXTERNAL_STABILIZATION
MULTI_SIGNAL
UNKNOWN
```

Но `transition_signal` описывает механизм, а `trajectory_detection_stage` — доказательную зрелость траектории.

```text
MECHANISM_CLASS != DETECTION_STAGE
```

## 9. Structural Gap separation

Structural Gap Inference не включать автоматически в temporal transition score.

```text
TRANSITION_SIGNAL_PRESENT != STRUCTURAL_GAP
DETECTION_STAGE_HIGH != MODEL_MISSPECIFICATION
```

Structural gap оценивается отдельным контуром только если наблюдаемое состояние не объясняется уже закодированными transition mechanisms.

## 10. Next test

Создать `TEMPORAL_SEQUENCE_BLIND_PACKET_002` на новых real-history series, включающих:
- survival under severe pressure;
- external-support stabilization;
- negotiated reform without collapse;
- controlled imperial contraction;
- slow federal/system fragmentation;
- rapid command collapse.

Основная проверка: различают ли внешние кодировщики EARLY / ROBUST / THRESHOLD без knowledge leakage от будущего.

## 11. Status

```text
TEMPORAL_TRANSITION_RUBRIC_V0_4_PATCH = READY
DETECTION_WINDOW = ACTIVE
SINGLE_STRUCTURAL_DISTINGUISHABILITY_POINT = SUPERSEDED
NUMERIC_USE = BLOCKED
NEXT = NEW_SERIES_BLIND_TEST_002
```
