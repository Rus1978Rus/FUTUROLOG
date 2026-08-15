# STATUS_SHOCK_TRANSLATION_BENCHMARK_001_RU

**Статус:** `SOURCE_BACKED_DESIGN / WORKING_BENCHMARK / NOT_CAUSALLY_VALIDATED`

## 1. Цель

Проверить рабочую гипотезу:

`IMPERIAL_STRATEGY != IMPERIAL_NEED`

и более общий механизм:

`STATUS / SECURITY / DIGNITY NEED -> POLITICAL TRANSLATION -> DIFFERENT STRATEGY`

Нас интересует не сам факт потери территории или статуса, а то, **как похожий статусный шок переводится в разные политические траектории**.

## 2. Разделяемые оси

- `observed_loss_state`
- `perceived_loss_state`
- `status_frustration_signal`
- `switch_driver`
- `replacement_status_channel`
- `restoration_narrative_strength`
- `revisionist_policy_signal`
- `internal_reconstruction_channel`
- `identity_reconstruction_channel`
- `external_constraint_strength`
- `strategy_translation_state`

## 3. Ключевые guards

`OBJECTIVE_LOSS != PERCEIVED_LOSS`

`STATUS_FRUSTRATION != TERRITORIAL_NEED`

`RESTORATION_NARRATIVE != POPULATION_PRIMARY_NEED`

`DOMESTIC_RECONSTRUCTION != VALUE_CHANGE_PROVEN`

`EXTERNAL_CONSTRAINT != INTERNAL_CONSENT`

`ECONOMIC_SUCCESS != CAUSAL_PROOF_OF_STRATEGY_SWITCH`

`CULTURE_OF_DEFEAT != REVISIONISM`

`REVISIONIST_MEMORY != REVISIONIST_POLICY`

## 4. Новые сравнительные серии

### CASE A — малое государство после тяжёлой территориальной потери

После крупного поражения государство теряет около двух пятых территории и примерно треть населения. Политическая катастрофа разрушает прежние внешнеполитические амбиции. В последующие десятилетия национальный нарратив всё сильнее связывает восстановление достоинства с внутренним развитием; формула «что потеряно вовне, должно быть выиграно внутри» становится символом этого разворота.

**Назначение:** сильный `INWARD_RECONSTRUCTION` control.

Source anchors: National Museum of Denmark; Cambridge work on Denmark after 1864.

### CASE B — имперская потеря + кризис идентичности + слабая модернизационная развязка

После потери последних крупных заморских владений поражение вызывает тяжёлый кризис национальной идентичности. Возникает движение «регенерации» и множество практических предложений модернизации, но модернизационный ответ блокируется политической и социальной фрагментацией.

**Назначение:** `INTERNAL_RECONSTRUCTION_DEMAND_WITHOUT_ROBUST_SWITCH`.

Source anchors: Sebastian Balfour, Cambridge/Oxford studies on Spain after 1898; literature on Regeneracionismo.

### CASE C — распад империи + кризис самого политического субъекта

После распада многонациональной монархии остаётся маленькое государство с тяжёлым экономическим и идентификационным кризисом. Значительная часть общества не воспринимает новую государственность как естественную конечную форму и ищет включение в более широкую национальную рамку.

**Назначение:** `IDENTITY_REPLACEMENT_WITHOUT_IMPERIAL_RESTORATION`.

Source anchors: Cambridge, *A Concise History of Austria*; Austrian History Yearbook; *Red Vienna Sourcebook*.

### CASE D — имперский крах + военная победа ядра + национальная реконструкция

Старая имперская система распадается, но вооружённое национальное движение ядра добивается международного признания нового государства. Новый режим отменяет значительную часть прежней имперской политико-правовой архитектуры и строит новую национальную идентичность.

**Назначение:** `POST_IMPERIAL_NATIONAL_RECONSTRUCTION`.

Source anchors: Lausanne records and FRUS 1923; contemporary evidence on abolition of capitulations and new reciprocal treaty order.

### CASE E — территориальная потеря + культурная память без устойчивой политики реванша

После тяжёлого поражения государство теряет важные территории. Потеря становится сильным элементом национальной памяти и культуры, но позднейшие исследования показывают, что устойчивую государственную политику военного реванша легко переоценить; значительная часть элит предпочитает институциональную консолидацию и осторожную внешнюю политику.

**Назначение:** `REVANCHIST_MEMORY_WITHOUT_STRONG_REVISIONIST_POLICY`.

Source anchors: Cambridge research on France after 1871 and contemporary scholarship on revanchism.

### CASE F — колониальная потеря после войны + вынужденное признание

Метрополия после нескольких лет тяжёлого конфликта вынужденно признаёт независимость ключевой колонии. Потеря воспринимается как травматическая, но не преобразуется в длительную политику территориального восстановления; прежняя имперская связь частично перекодируется в экономические, культурные и дипломатические отношения.

**Назначение:** `POST_COLONIAL_RELATIONSHIP_SUBSTITUTION`.

Source anchors: Cambridge work on Dutch recognition of Indonesian independence and post-1949 relations.

## 5. Почему эти кейсы важнее прежних

Здесь deliberately сближён **тип исходного шока**, но разведены способы его политического перевода:

- A: `LOSS -> INWARD_RECONSTRUCTION`
- B: `LOSS -> REGENERATION_DEMAND -> BLOCKED_SWITCH`
- C: `LOSS -> IDENTITY_CRISIS -> ABSORPTION-SEEKING`
- D: `LOSS -> NATIONAL_REFOUNDATION`
- E: `LOSS -> MEMORY / CULTURAL REVANCHISM WITHOUT STRONG POLICY`
- F: `LOSS -> RELATIONSHIP_SUBSTITUTION`

Это сильнее простой пары `reconstruction vs revisionism`.

## 6. Рабочая гипотеза v0.2

Не предполагаем, что общества «хотят империю» как первичную потребность. Проверяем более слабую и проверяемую формулу:

`STATUS / SECURITY / DIGNITY / ORDER NEED`

`+ INTERPRETATION`

`+ AVAILABLE INSTITUTIONAL CHANNELS`

`+ MEMORY OF PREVIOUS STRATEGY COST`

`+ EXTERNAL CONSTRAINTS`

`-> STRATEGY TRANSLATION`

## 7. Следующий шаг

Собрать `STATUS_SHOCK_TRANSLATION_BLIND_PACKET_001` с 4–5 временными срезами на серию и вынести real-case mapping только в evaluator key.

## 8. Source notes

- Denmark 1864: National Museum of Denmark notes the defeat and the later motto «what is lost outwardly must be won inwardly»; Cambridge scholarship treats 1864 as a major culture-of-defeat turning point.
- Spain 1898: Cambridge/Oxford scholarship documents legitimacy crisis, regenerationist modernization proposals, and failure to consolidate a peaceful modernizing alternative.
- Austria 1918: Cambridge describes a profound post-imperial identity, economic and political crisis and the First Republic as a state many did not want as final national form.
- Turkey 1923: FRUS Lausanne documents show the new Turkish government negotiating reciprocity and abolition of capitulations in the new international order.
- France 1871: recent Cambridge research cautions against equating memory of Alsace-Lorraine with a sustained elite policy of military revanche.
- Netherlands/Indonesia 1949: Cambridge scholarship describes Dutch recognition as reluctant and traumatic, followed by attempts to recast ties in economic/cultural terms.
