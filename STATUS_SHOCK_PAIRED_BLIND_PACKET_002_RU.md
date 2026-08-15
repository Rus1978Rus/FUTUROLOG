# STATUS SHOCK PAIRED BLIND PACKET 002

PACKET_SCHEMA_ID: SSPB-002-V1

Статус: READY_FOR_EXTERNAL_MULTI_MODEL_TEST / PAIRED_CASES / COUNTRY_LABELS_HIDDEN / OUTCOMES_HIDDEN

## 1. Цель

Сравнить пары систем, переживающих сильный статусный/территориальный шок, и определить, переводится ли сходная потеря в одинаковую или различную стратегию.

Не определяй реальные страны/события. Не используй интернет. Не используй знание последующих исходов.

## 2. Guards

IMPERIAL_STRATEGY != IMPERIAL_NEED
OBJECTIVE_LOSS != PERCEIVED_LOSS
LOSS_MEMORY != RESTORATION_NARRATIVE
RESTORATION_NARRATIVE != REVISIONIST_POLICY
EXTERNAL_CONSTRAINT != INTERNAL_VALUE_CHANGE
DECLARED_REFORM != ROBUST_STRATEGY_SWITCH
CULTURAL_MEMORY != STATE_POLICY
ARMED_RESISTANCE_TO_SETTLEMENT != IMPERIAL_RESTORATION

## 3. Допустимые значения

observed_loss_state = NONE | LIMITED | MAJOR | SYSTEMIC | UNKNOWN
perceived_loss_state = NONE | WEAK | SUBSTANTIAL | HIGH | UNKNOWN
status_frustration_signal = ABSENT | WEAK | SUBSTANTIAL | HIGH | UNKNOWN
switch_pressure_source = NONE | INTERNAL_COST | EXTERNAL_CONSTRAINT | IDENTITY_CRISIS | MIXED | UNKNOWN
switch_trigger = NONE | DEFEAT | TERRITORIAL_LOSS | FAILED_RESTORATION | POLITICAL_CRISIS | NEGOTIATED_OPENING | MIXED | UNKNOWN
translation_mechanism = NONE | INWARD_REFRAMING | REGENERATIONISM | RESTORATION_NARRATIVE | NATIONAL_REFOUNDATION | RELATIONSHIP_REFRAMING | MIXED | UNKNOWN
replacement_status_channel = ABSENT | INTERNAL_DEVELOPMENT | ECONOMIC_PERFORMANCE | INSTITUTIONAL_CONSOLIDATION | NATIONAL_STATE_BUILDING | EXTERNAL_INTEGRATION | POSTCOLONIAL_RELATIONSHIP | UNKNOWN
loss_memory_strength = ABSENT | WEAK | SUBSTANTIAL | DOMINANT | UNKNOWN
restoration_narrative_strength = ABSENT | WEAK | SUBSTANTIAL | DOMINANT | UNKNOWN
revisionist_policy_signal = ABSENT | PRESENT_WEAK | PRESENT_STRONG | ACTIVE | UNKNOWN
operational_strategy_state = OLD_STRATEGY_CONTINUES | SEARCHING | INWARD_RECONSTRUCTION | BLOCKED_RECONSTRUCTION | MEMORY_WITHOUT_REVISION | REVISIONIST_TRANSLATION | IDENTITY_REALIGNMENT | NATIONAL_REFOUNDATION | DELAYED_RELATIONSHIP_SUBSTITUTION | NEGOTIATED_RELATIONSHIP_SUBSTITUTION | MIXED | UNKNOWN
robust_switch_state = NO | EARLY | ROBUST | DIRECT | UNKNOWN
confidence = LOW | MEDIUM | HIGH

## 4. PAIR A

### A1-T0
- крупное военное поражение;
- потеря значительной части территории и населения;
- национальный статусный шок непосредственно наблюдаем.

### A1-T1
- в публичном дискурсе появляется формула: восстановление достоинства должно происходить через внутреннее усиление оставшейся страны;
- устойчивой государственной политики немедленного территориального реванша не наблюдается.

### A1-T2
- усиливаются проекты хозяйственного развития, образования, кооперации и социальной консолидации;
- связь между поражением и каждым из этих процессов не считать автоматически доказанной причинностью.

### A2-T0
- крупное военное поражение;
- потеря значимой пограничной территории;
- память о потере становится сильным национальным символом.

### A2-T1
- существуют националистические и реваншистские движения;
- одновременно государственная политика не демонстрирует непрерывного курса на немедленную войну за возвращение территории.

### A2-T2
- институциональная консолидация государства продолжается;
- память о потерянной территории сохраняется;
- культурная память и политический реванш остаются различимыми слоями.

## 5. PAIR B

### B1-T0
- государство теряет последние крупные заморские владения после поражения;
- возникает сильный кризис представления страны о себе как о значимой мировой державе.

### B1-T1
- возникает широкое движение национального «возрождения/регенерации»;
- предлагаются модернизация хозяйства, образования и политической системы.

### B1-T2
- политическая, социальная и региональная фрагментация мешает превратить модернизационный запрос в устойчивую общенациональную стратегию.

### B2-T0
- государство формально относится к победителям большой войны;
- часть общества воспринимает результат как унизительно неполный и несоответствующий принесённым жертвам.

### B2-T1
- идея «неполной/урезанной победы» становится заметным националистическим нарративом;
- возникают территориальные требования.

### B2-T2
- вооружённая националистическая группа самовольно занимает спорную территорию;
- ревизионистский нарратив переходит из символического слоя в действие.

## 6. PAIR C

### C1-T0
- многонациональная имперская система распадается;
- остаётся значительно меньшее государство;
- прежний монархический/имперский центр легитимности исчезает;
- национальная идентичность нового государства не воспринимается как очевидная и завершённая.

### C1-T1
- значимые силы обсуждают присоединение к более широкой национальной общности;
- самостоятельная постимперская идентичность остаётся слабой и оспариваемой.

### C1-T2
- политическая и экономическая нестабильность сохраняется;
- robust national refoundation внутри текущего государства не наблюдается.

### C2-T0
- старая имперская структура распадается после войны;
- внешнее послевоенное урегулирование резко ограничивает ядро прежней системы;
- национальное движение организует вооружённое сопротивление условиям урегулирования.

### C2-T1
- новое руководство добивается международного признания новой политической формы;
- часть старых внешних ограничений и привилегий пересматривается;
- прежняя многонациональная имперская форма не восстанавливается.

### C2-T2
- строится новая национальная политико-правовая архитектура;
- статус переводится в строительство национального государства, а не в восстановление прежней империи.

## 7. PAIR D

### D1-T0
- после тяжёлой войны метрополия признаёт независимость крупной колонии;
- потеря воспринимается болезненно;
- прежние экономические и культурные связи остаются значимыми.

### D1-T1
- новая постколониальная конструкция отношений формально создаётся;
- сохраняются патерналистские установки и спор о ещё одной территории;
- нормализация отношений остаётся неполной.

### D1-T2
- спор об остаточной территории обостряется;
- экономические и дипломатические связи ухудшаются;
- relationship substitution задерживается и остаётся конфликтной.

### D2-T0
- длительная война за удержание крупной колониальной территории вызывает тяжёлый внутренний политический кризис;
- прежняя стратегия удержания ещё действует.

### D2-T1
- руководство постепенно переходит к признанию самоопределения как допустимого политического исхода;
- начинается переговорный канал.

### D2-T2
- подписывается соглашение о прекращении огня и переходе суверенитета;
- одновременно формулируются основы будущего сотрудничества двух государств.

## 8. Задание

Для каждого шага закодируй поля ниже. Затем по каждой подсерии A1/A2/B1/B2/C1/C2/D1/D2 укажи dominant_translation_path.

После этого по каждой паре A/B/C/D ответь:
- same_shock_class = YES | NO | PARTIAL | UNKNOWN
- same_translation_path = YES | NO | PARTIAL | UNKNOWN
- primary_divergence_axis = MEMORY_TO_POLICY | RECONSTRUCTION_CAPACITY | IDENTITY_DESTINATION | RELATIONSHIP_NORMALIZATION | EXTERNAL_CONSTRAINT | UNKNOWN

## 9. Output CSV — step rows

schema_marker,subseries_id,step_id,observed_loss_state,perceived_loss_state,status_frustration_signal,switch_pressure_source,switch_trigger,translation_mechanism,replacement_status_channel,loss_memory_strength,restoration_narrative_strength,revisionist_policy_signal,operational_strategy_state,robust_switch_state,confidence,reason
SSPB-002-V1,A1,A1-T0,,,,,,,,,,,,,,
SSPB-002-V1,A1,A1-T1,,,,,,,,,,,,,,
SSPB-002-V1,A1,A1-T2,,,,,,,,,,,,,,
SSPB-002-V1,A2,A2-T0,,,,,,,,,,,,,,
SSPB-002-V1,A2,A2-T1,,,,,,,,,,,,,,
SSPB-002-V1,A2,A2-T2,,,,,,,,,,,,,,
SSPB-002-V1,B1,B1-T0,,,,,,,,,,,,,,
SSPB-002-V1,B1,B1-T1,,,,,,,,,,,,,,
SSPB-002-V1,B1,B1-T2,,,,,,,,,,,,,,
SSPB-002-V1,B2,B2-T0,,,,,,,,,,,,,,
SSPB-002-V1,B2,B2-T1,,,,,,,,,,,,,,
SSPB-002-V1,B2,B2-T2,,,,,,,,,,,,,,
SSPB-002-V1,C1,C1-T0,,,,,,,,,,,,,,
SSPB-002-V1,C1,C1-T1,,,,,,,,,,,,,,
SSPB-002-V1,C1,C1-T2,,,,,,,,,,,,,,
SSPB-002-V1,C2,C2-T0,,,,,,,,,,,,,,
SSPB-002-V1,C2,C2-T1,,,,,,,,,,,,,,
SSPB-002-V1,C2,C2-T2,,,,,,,,,,,,,,
SSPB-002-V1,D1,D1-T0,,,,,,,,,,,,,,
SSPB-002-V1,D1,D1-T1,,,,,,,,,,,,,,
SSPB-002-V1,D1,D1-T2,,,,,,,,,,,,,,
SSPB-002-V1,D2,D2-T0,,,,,,,,,,,,,,
SSPB-002-V1,D2,D2-T1,,,,,,,,,,,,,,
SSPB-002-V1,D2,D2-T2,,,,,,,,,,,,,,

## 10. Output CSV — subseries summary

schema_marker,subseries_id,dominant_translation_path,first_replacement_channel_step,first_revisionist_policy_step,first_robust_switch_step,confidence,reason
SSPB-002-V1,A1,,,,,,
SSPB-002-V1,A2,,,,,,
SSPB-002-V1,B1,,,,,,
SSPB-002-V1,B2,,,,,,
SSPB-002-V1,C1,,,,,,
SSPB-002-V1,C2,,,,,,
SSPB-002-V1,D1,,,,,,
SSPB-002-V1,D2,,,,,,

## 11. Output CSV — pair summary

schema_marker,pair_id,same_shock_class,same_translation_path,primary_divergence_axis,confidence,reason
SSPB-002-V1,A,,,,,
SSPB-002-V1,B,,,,,
SSPB-002-V1,C,,,,,
SSPB-002-V1,D,,,,,

## 12. Protocol gate

Отклонить результат, если:
- schema_marker != SSPB-002-V1;
- названы реальные страны/события;
- нарушена временная последовательность;
- LOSS_MEMORY автоматически кодируется как REVISIONIST_POLICY;
- факт поражения автоматически кодируется как желание территориального восстановления;
- внешнее ограничение автоматически объявляется внутренним изменением ценностей;
- вывод о причинности делается только из того, что событие A предшествует событию B.

Верни только три CSV, без текста до или после.
