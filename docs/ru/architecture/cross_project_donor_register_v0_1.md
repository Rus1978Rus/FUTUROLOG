# CROSS_PROJECT_DONOR_REGISTER v0.1
## Реестр доноров для универсального FUTUROLOG

**Статус:** `WORKING_REGISTER / PRE-INTEGRATION / NO_CODE_IMPORTED_YET`

Цель документа — свести потенциальные донорские механизмы в одну карту до любого переноса в FUTUROLOG. Главное правило: сначала назначить хозяина функции и границы, потом импортировать или адаптировать код.

## Статусы

- `IMPORT` — можно переносить почти напрямую после локальных тестов.
- `ADAPT` — механизм полезен, но код или контракт надо адаптировать.
- `REFERENCE` — использовать как методический образец, а не runtime-зависимость.
- `LATER` — полезно, но не на текущем шаге.
- `REJECT` — не подходит текущей архитектуре.

## Донорский реестр

| Донор | Механизм | Источник | Решение | Владелец в FUTUROLOG |
|---|---|---|---|---|
| Entropy-RG v2.2 | базовый scoring/anomaly core | executable baseline v2.2 | KEEP_BASELINE | Entropy-RG Core |
| ACDM-KERNEL | нейтральные `Signal` / `Score` | `acdm_kernel/types.py` | ADAPT | Core Contracts |
| ACDM-KERNEL | append-only audit hash chain | `acdm_kernel/audit.py` | ADAPT | Runtime Audit |
| ACDM-KERNEL | observability horizon | `acdm_kernel/horizon.py` | ADAPT | Evidence Freshness |
| ACDM-KERNEL | damping + de-escalation hold | `acdm_kernel/damping.py` | ADAPT | Decision Stability |
| ACDM-KERNEL | governance tiers | `acdm_kernel/governance.py` | ADAPT | Runtime Governance |
| ACDM-KERNEL | conformance gate | `acdm_kernel/conformance.py` | IMPORT/ADAPT | Plugin Admission |
| Notarius | semantic trace | `notarius/trace.py` | ADAPT | Evidence Provenance |
| Notarius | mandatory route | `notarius/route.py` | ADAPT | Pipeline Completeness |
| Notarius | governed record | `notarius/record.py` | LATER/ADAPT | Critical Config Custody |
| Notarius | document/file analysis | `notarius/analyze.py` | ADAPT | Source Integrity |
| Motor-/SmoothGuard | hysteresis/deadband | `deadband.py` | ADAPT | Decision Stability |
| Motor-/SmoothGuard | reproducible backtest pattern | `backtest.py` | REFERENCE | Evaluation Protocol |
| QuditEngine | seeded reproducibility | engine + project discipline | REFERENCE | Evaluation Protocol |
| QuditEngine | preregistration / errata / negative-result discipline | project discipline | REFERENCE | Evaluation Protocol |
| BRUINGate | cheap gate before expensive processing | `rate_limit_gear.py`, `knock_gear.py` | ADAPT | Ingestion Gate |
| BRUINGate | de Bruijn + HMAC token | `debruijn.py`, `knock_gear.py` | REJECT_NOW | — |
| Vakhter | canonicalization pre-pass | `code/canonicalization/` | ADAPT | Text Sanitation |
| Vakhter | per-detector isolation | `code/range/product.py`, `fail_closed.py` | IMPORT/ADAPT | Detector Isolation |
| Vakhter | fail-closed behavior | `code/range/fail_closed.py` | ADAPT | Input Reliability |
| Foundation Layer | operational guards | CORE_OPERATIONAL register | REFERENCE | Governance Rules |
| E-Continuity | recoverability distinction | framework | REFERENCE/LATER | Historical Corpus Stewardship |
| E-Continuity | archive audit tool | `tools/audit_archives.py` | ADAPT | Evaluation Dataset Builder |
| CONVEYOR | staged review protocol | `CONVEYOR_PROTOCOL_CORE_SPEC_v0_1_DRAFT_RU_EN.md` | REFERENCE | Development Governance |
| MSL/MIP | independent structural axes | runtime/core axes | ADAPT | Text Structural Adapter |
| MSL/MIP | pinned data + visible degradation | `data/unicode`, `data/net` | IMPORT/ADAPT | Data Provenance |
| MSL/MIP | cheap O(n) input guard | `input_guard.py` | ADAPT | Ingestion Gate |
| Зерно и формула | карта стадий формализации | `зерно_и_формула.md`, `SPEC.md` | ADAPT/REFERENCE | Emerging Domain Assessment |
| Зерно и формула | диагностика pre-technology maturity | `seed_formula.py` / `TransformationEngine.diagnose` | ADAPT | Emerging Domain Assessment |
| Зерно и формула | численные `formality/meaning` deltas и crisis boost ×1.5 | `seed_formula.py`, `SPEC.md` | REFERENCE_ONLY / NOT_CALIBRATED | Experimental Harness |

## Новый донор: «Зерно и формула»

Источник — пользовательский архив `OKComputer_Философы_и_математики.zip`. В документе описана семистадийная логическая карта: вербализация вопроса → определение → идеализация → символизация → измерение → аксиоматизация → алгоритмизация. Сам источник прямо оговаривает, что это логический порядок, а не обязательный хронологический закон: реальные траектории могут возвращаться назад, менять порядок и застревать на этапах.

Для FUTUROLOG берётся не тезис о «законе развития науки», а диагностический механизм для зарождающихся областей и два защитных инварианта:

`MEASUREMENT != CONSTRUCT_VALIDITY`

`FORMALIZATION != UNDERSTANDING`

Дополнительный guard:

`FORMALIZATION_PROGRESS != REALITY_COVERAGE`

Численные параметры симулятора (`formality_delta`, `meaning_delta`, стартовые метрики и `CRISIS_BOOST = 1.5`) не считаются откалиброванными измерениями и не входят в Objective/Coverage или core scoring.

Подробная кандидатная карточка: `docs/ru/research/emerging_domain_assessment_candidate_v0_1.md`.

## Разрешение основных дублей

### ACDM audit vs Notarius trace

Notarius отвечает: `откуда пришли данные → как преобразовывались → какой элемент стал сигналом`.

ACDM Runtime Audit отвечает: `что FUTUROLOG сделал с сигналом → какое решение принял`.

`WORLD/EVIDENCE_TRACE != SYSTEM_EXECUTION_TRACE`

### Motor deadband vs ACDM damping

Motor — числовая гистерезисная зона вокруг порога. ACDM — временная устойчивость состояния и задержка деэскалации.

`NUMERIC_HYSTERESIS != STATE_HOLD`

### Vakhter vs MSL/MIP vs Notarius

- Vakhter — санитарная обработка недоверенного текста.
- MSL/MIP — структурный анализ знаков/последовательностей и pinned data.
- Notarius — происхождение и целостность элемента/документа.

### Foundation Layer vs CONVEYOR vs ACDM Governance

- Foundation Layer — принципы и guards (защитные правила).
- CONVEYOR — процесс изменения и проверки артефакта.
- ACDM Governance — runtime-права (права во время исполнения) на изменение параметров.

## Черновая архитектура

```text
RAW INPUT
   ↓
INGESTION GATE
   BRUINGate principles
   + MSL input-cost guard
   ↓
TEXT / STRUCTURE SANITATION
   Vakhter
   + optional MSL/MIP adapter
   ↓
SOURCE / ELEMENT PROVENANCE
   Notarius
   ↓
NORMALIZATION
   ↓
ENTROPY-RG CORE
   ↓
OBJECTIVE / COVERAGE / FRESHNESS
   ↓
DECISION STABILITY
   Motor deadband
   + ACDM state hold
   ↓
ENRA ORCHESTRATION
   ↓
RUNTIME GOVERNANCE / AUDIT
   ACDM mechanisms
   ↓
EXPLAINABLE OUTPUT
```

Вне runtime:

```text
Foundation Layer → защитные принципы
CONVEYOR         → как меняем и проверяем систему
Qudit discipline→ пререгистрация и воспроизводимость
E-Continuity     → сохранность и восстановимость исторического корпуса
Зерно и формула  → кандидатная диагностика зрелости зарождающейся области
```

## Текущий запрет

До отдельного решения не переносить квантовую математику QuditEngine в scoring, de Bruijn/HMAC BRUINGate в аналитическое ядро, весь MSL/MIP как обязательную зависимость, весь Notarius crypto stack, несколько конкурирующих audit chains или confidence-механизмов, а также не использовать численные deltas из «Зерна и формулы» как валидированные метрики.

## Следующий узел

`OBJECTIVE / COVERAGE v2`: measured score (измеренный результат), evidence coverage (покрытие доказательств), source independence (независимость источников), freshness (свежесть), pipeline completeness (полнота маршрута), observed noise (наблюдаемый шум), effective confidence (эффективная уверенность).

`HIGH_MEASURED_SCORE + LOW_COVERAGE != HIGH_EFFECTIVE_CONFIDENCE`

После фиксации нового донора порядок не меняется: следующий технический шаг — `OBJECTIVE_COVERAGE_FORMULA_BAKEOFF_v0_1`.
