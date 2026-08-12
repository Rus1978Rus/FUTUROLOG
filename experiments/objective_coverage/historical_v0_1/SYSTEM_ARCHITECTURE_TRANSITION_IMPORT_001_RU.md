# SYSTEM ARCHITECTURE TRANSITION IMPORT 001

**Статус:** `CONCEPTUAL_IMPORT / HISTORICAL_CASE_CLASS / NOT_FINAL_STANDARD / NOT_NUMERICALLY_VALIDATED`

## 1. Источник идеи

Тридцатилетняя война (1618–1648) используется не как доказательство тезиса «Вестфалия создала современные национальные государства», а как исторический кейс перестройки политической архитектуры Европы.

Современная историография предупреждает против упрощённого «Westphalian myth»: мир 1648 года не одномоментно создал систему полностью суверенных национальных государств, а стал частью более длинной трансформации. Священная Римская империя продолжила существовать после 1648 года, а внешние интервенционные права и сложная имперская правовая структура сохранялись.

## 2. Новый класс перехода

```text
SYSTEM_ARCHITECTURE_TRANSITION
```

Определение:

> Изменение правил координации между политическими узлами, при котором формальные институты могут сохраняться, но реальное распределение полномочий, автономии и внешней субъектности меняется.

## 3. Новые оси

```text
system_coordination_mode = HIERARCHICAL | HYBRID | POLYCENTRIC | SOVEREIGN_UNITS | UNKNOWN
formal_center_authority = HIGH | MEDIUM | LOW | UNKNOWN
effective_center_control = HIGH | MEDIUM | LOW | UNKNOWN
node_external_agency = LOW | PARTIAL | HIGH | UNKNOWN
intervention_regime = RESTRICTED | CONDITIONAL | GUARANTEED | OPEN | UNKNOWN
architecture_transition_state = STABLE | SHIFTING | RECONFIGURING | RECONFIGURED | UNKNOWN
```

## 4. Guards

```text
FORMAL_CENTER_SURVIVES != PREVIOUS_AUTHORITY_SURVIVES
FORMAL_SUPREMACY != EFFECTIVE_CONTROL
TREATY_EXISTS != ARCHITECTURE_INSTANTLY_RECONFIGURED
WESTPHALIA_1648 != BIRTH_OF_MODERN_NATION_STATE
NODE_AUTONOMY != FULL_SOVEREIGN_INDEPENDENCE
SYSTEM_ARCHITECTURE_TRANSITION != STATE_COLLAPSE
POLYCENTRICITY != ANARCHY
```

## 5. Historical interpretation guard

Допустимый тезис:

> Тридцатилетняя война и Вестфальский мир являются сильным кейсом изменения европейской политической архитектуры и расширения/закрепления автономии политических узлов в сложной имперской и межгосударственной системе.

Недопустимый упрощённый тезис:

> «В 1648 году были созданы современные национальные государства и абсолютный принцип невмешательства».

## 6. Значение для FUTUROLOG

До этого benchmark в основном различал:
- collapse;
- survival;
- negotiated transformation;
- center-periphery contraction;
- internal civil-war fracture.

Теперь добавляется:

```text
ARCHITECTURE_RECONFIGURATION_WITHOUT_SIMPLE_CENTER_COLLAPSE
```

Это нужно для случаев, где:
- формальный центр остаётся;
- узлы получают больше реальной автономии;
- внешняя субъектность узлов растёт;
- правила координации меняются;
- старое название системы может сохраниться, хотя функциональная архитектура уже иная.

## 7. Candidate long-run comparison family

```text
Thirty Years War / Westphalia
→ Napoleonic reordering
→ Congress of Vienna
→ WWI and imperial dissolution
→ WWII / UN order
→ Cold War bloc architecture
→ Soviet dissolution / post-Cold-War order
```

Это не одна причинная цепочка, а набор архитектурных переходов для сравнительного benchmark.

## 8. Research caution

Cambridge scholarship explicitly challenges the textbook myth that Westphalia simply replaced a hierarchical order with sovereign independent states. Oxford work also shows that post-1648 arrangements could authorize external intervention in the Empire, which is incompatible with a simplistic «absolute non-intervention» reading.

## 9. Next

```text
NEXT = SYSTEM_ARCHITECTURE_TEMPORAL_BENCHMARK_001
```

Первый benchmark должен сравнить минимум три типа:
1. architecture reconfiguration without disappearance of the formal system;
2. federation fracture with reintegration;
3. federation/system dissolution.

Proposed anchors:
- Holy Roman Empire / Westphalia;
- Switzerland 1847–1848;
- United States 1860–1865;
- USSR 1989–1991.
