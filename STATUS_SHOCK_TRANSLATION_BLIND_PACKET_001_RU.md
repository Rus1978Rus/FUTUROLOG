# STATUS SHOCK TRANSLATION — BLIND PACKET 001

PACKET_SCHEMA_ID: SSTB-001-V1

Статус: `READY_FOR_EXTERNAL_MULTI_MODEL_TEST / COUNTRY_LABELS_HIDDEN / TEMPORAL_ORDER_VISIBLE / OUTCOMES_HIDDEN`

## 1. Цель

Определить, как похожий статусный/территориальный шок переводится в разные политические стратегии.

Не угадывать реальные страны и события. Не использовать интернет. Не использовать знания о дальнейших исходах.

## 2. Guards

`IMPERIAL_STRATEGY != IMPERIAL_NEED`

`OBJECTIVE_LOSS != PERCEIVED_LOSS`

`STATUS_FRUSTRATION != TERRITORIAL_NEED`

`RESTORATION_NARRATIVE != REVISIONIST_POLICY`

`CULTURE_OF_DEFEAT != REVISIONISM`

`EXTERNAL_CONSTRAINT != INTERNAL_VALUE_CHANGE`

`INTERNAL_RECONSTRUCTION != STATUS_SUBSTITUTION_PROVEN`

`DECLARED_REFORM != ROBUST_STRATEGY_SWITCH`

## 3. Допустимые значения

observed_loss_state = NONE | LIMITED | MAJOR | SYSTEMIC | UNKNOWN

perceived_loss_state = NONE | WEAK | SUBSTANTIAL | HIGH | UNKNOWN

status_frustration_signal = ABSENT | WEAK | SUBSTANTIAL | HIGH | UNKNOWN

switch_driver = NONE | INTERNAL_COST | EXTERNAL_CONSTRAINT | IDENTITY_CRISIS | POLITICAL_REFRAMING | MIXED | UNKNOWN

replacement_status_channel = ABSENT | INTERNAL_DEVELOPMENT | ECONOMIC_PERFORMANCE | NATIONAL_REFOUNDATION | INSTITUTIONAL_CONSOLIDATION | RELATIONSHIP_SUBSTITUTION | EXTERNAL_INTEGRATION | UNKNOWN

restoration_narrative_strength = ABSENT | WEAK | SUBSTANTIAL | DOMINANT | UNKNOWN

revisionist_policy_signal = ABSENT | PRESENT_WEAK | PRESENT_STRONG | ACTIVE | UNKNOWN

strategy_translation_state = OLD_STRATEGY_CONTINUES | SEARCHING | INWARD_RECONSTRUCTION | NATIONAL_REFOUNDATION | INSTITUTIONAL_CONSOLIDATION | RELATIONSHIP_SUBSTITUTION | REVISIONIST_TRANSLATION | MIXED | UNKNOWN

strategy_switch_evidence = NONE | EARLY | ROBUST | DIRECT | UNKNOWN

confidence = LOW | MEDIUM | HIGH

## 4. SERIES A

### A-T0
- крупное военное поражение приводит к потере значительной части территории и населения;
- прежние внешнеполитические амбиции серьёзно подорваны;
- национальный статусный шок непосредственно наблюдаем.

### A-T1
- в публичном дискурсе появляется формула, связывающая восстановление национального достоинства с тем, что нужно «выиграть внутри» то, что потеряно вовне;
- нет наблюдаемой политики немедленного территориального восстановления.

### A-T2
- усиливаются проекты внутреннего развития, образования, хозяйственной модернизации и повышения продуктивности оставшейся территории;
- национальный статус всё больше связывается с качеством внутреннего развития.

## 5. SERIES B

### B-T0
- государство теряет последние крупные заморские владения после поражения;
- поражение вызывает сильный кризис национальной идентичности и сомнения в прежнем образе страны как значительной мировой державы.

### B-T1
- возникает широкое движение «регенерации»;
- интеллектуалы, политики и общественные группы предлагают модернизацию хозяйства, образования и политической системы;
- единый новый политический канал не консолидирован.

### B-T2
- социальная и политическая фрагментация блокирует превращение модернизационного запроса в устойчивую общенациональную стратегию;
- кризис легитимности сохраняется.

## 6. SERIES C

### C-T0
- многонациональная имперская система распадается;
- остаётся небольшое государство с тяжёлым экономическим и идентификационным кризисом;
- новая государственность существует юридически, но её конечная национальная форма не воспринимается как очевидная.

### C-T1
- значимые политические силы обсуждают включение нового государства в более широкую национальную рамку;
- поиск идентичности доминирует над попыткой восстановить прежнюю империю.

### C-T2
- экономический кризис и политическая поляризация продолжаются;
- самостоятельная постимперская идентичность остаётся слабой и оспариваемой.

## 7. SERIES D

### D-T0
- старая имперская структура распадается после войны;
- национальное движение ядра организует вооружённое сопротивление условиям послевоенного урегулирования;
- прежняя имперская форма не восстанавливается.

### D-T1
- новое государственное руководство добивается международного признания новой политической формы;
- отменяются внешние ограничения и привилегии, связанные со старой имперской системой;
- отношения с внешними державами перестраиваются на принцип взаимности.

### D-T2
- новая власть строит национальную политико-правовую архитектуру, отличную от прежней имперской;
- стратегия статуса переводится в создание нового национального государства, а не в восстановление старой многонациональной империи.

## 8. SERIES E

### E-T0
- военное поражение приводит к утрате важных территорий;
- потерянные территории становятся сильным символом национальной памяти.

### E-T1
- культурные и националистические организации активно поддерживают память о потерянных землях;
- при этом ведущие государственные политики не демонстрируют устойчивого курса на немедленную войну за их возвращение.

### E-T2
- государственные институты консолидируются;
- внешняя политика значительной части правящей элиты остаётся осторожной;
- культурная память о потере сохраняется, но не тождественна активной ревизионистской политике.

## 9. SERIES F

### F-T0
- метрополия после нескольких лет тяжёлого вооружённого конфликта вынужденно признаёт независимость крупной колонии;
- признание воспринимается как болезненная и травматическая потеря.

### F-T1
- попытка восстановить прямой политический контроль не становится устойчивой государственной стратегией;
- обсуждаются новые формы экономических и культурных отношений с бывшей колонией.

### F-T2
- прежняя связь постепенно переводится из прямого политического контроля в торговые, культурные и дипломатические отношения;
- имперский статус не восстанавливается.

## 10. Задание

Для каждого шага закодируй поля ниже. Затем для каждой серии укажи:
- first_status_frustration_step
- first_replacement_channel_step
- first_robust_strategy_switch_step
- dominant_translation_path

Если точки нет — NONE.

## 11. Output CSV — step rows

schema_marker,series_id,step_id,observed_loss_state,perceived_loss_state,status_frustration_signal,switch_driver,replacement_status_channel,restoration_narrative_strength,revisionist_policy_signal,strategy_translation_state,strategy_switch_evidence,confidence,reason
SSTB-001-V1,A,A-T0,,,,,,,,,,,
SSTB-001-V1,A,A-T1,,,,,,,,,,,
SSTB-001-V1,A,A-T2,,,,,,,,,,,
SSTB-001-V1,B,B-T0,,,,,,,,,,,
SSTB-001-V1,B,B-T1,,,,,,,,,,,
SSTB-001-V1,B,B-T2,,,,,,,,,,,
SSTB-001-V1,C,C-T0,,,,,,,,,,,
SSTB-001-V1,C,C-T1,,,,,,,,,,,
SSTB-001-V1,C,C-T2,,,,,,,,,,,
SSTB-001-V1,D,D-T0,,,,,,,,,,,
SSTB-001-V1,D,D-T1,,,,,,,,,,,
SSTB-001-V1,D,D-T2,,,,,,,,,,,
SSTB-001-V1,E,E-T0,,,,,,,,,,,
SSTB-001-V1,E,E-T1,,,,,,,,,,,
SSTB-001-V1,E,E-T2,,,,,,,,,,,
SSTB-001-V1,F,F-T0,,,,,,,,,,,
SSTB-001-V1,F,F-T1,,,,,,,,,,,
SSTB-001-V1,F,F-T2,,,,,,,,,,,

## 12. Output CSV — series summary

schema_marker,series_id,first_status_frustration_step,first_replacement_channel_step,first_robust_strategy_switch_step,dominant_translation_path,confidence,reason
SSTB-001-V1,A,,,,,,
SSTB-001-V1,B,,,,,,
SSTB-001-V1,C,,,,,,
SSTB-001-V1,D,,,,,,
SSTB-001-V1,E,,,,,,
SSTB-001-V1,F,,,,,,

dominant_translation_path = INWARD_RECONSTRUCTION | BLOCKED_RECONSTRUCTION | IDENTITY_REALIGNMENT | NATIONAL_REFOUNDATION | MEMORY_WITHOUT_REVISION | RELATIONSHIP_SUBSTITUTION | REVISIONISM | MIXED | UNKNOWN

## 13. Protocol gate

Отклонить результат, если:
- schema_marker != SSTB-001-V1;
- изменены series/step IDs;
- названы реальные страны или события;
- поздняя информация импортирована в более ранний шаг;
- память о потерянной территории автоматически превращена в ревизионистскую политику;
- внешнее ограничение автоматически превращено во внутреннюю ценностную смену;
- объективная потеря автоматически приравнена к субъективному статусному шоку.

Верни только два CSV, без текста до или после.