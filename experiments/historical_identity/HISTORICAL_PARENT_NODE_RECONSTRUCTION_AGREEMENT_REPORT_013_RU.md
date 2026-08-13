# HISTORICAL PARENT NODE RECONSTRUCTION — AGREEMENT REPORT 013

**Статус:** `MULTI_MODEL_REVIEW / BLIND_PACKET_RESULT / NOT_NUMERICALLY_VALIDATED`

## 1. Вход

Blind packet: `HPNR-001-V1`.
Кодировщики: Copilot, Grok, Kimi, Claude.
Кейсы: PN-A4, PN-B7, PN-C2, PN-D9, PN-E5, PN-F8.

## 2. Главный результат

Механизм `PARENT_NODE_SUBSTITUTION` в целом распознаётся устойчиво, если исходная топология явно показывает ко-членство внутри общего parent-system и поздний нарратив заменяет parent node на доминирующего successor-а.

Устойчивые согласования:

- PN-C2: 4/4 — `DIRECT_SUBORDINATION`, `parent_node_substitution=NO`.
- PN-D9: 4/4 — подмена отсутствует.
- PN-F8: 4/4 — подмена отсутствует несмотря на асимметрию веса successor states.
- PN-E5: 4/4 по смыслу — continuity-identity case не должен автоматически превращаться в territorial parent substitution. Grok/Claude дали `NOT_ASSESSABLE`, Kimi дал `NO`, Copilot ошибочно тяготел к substitution.

Положительные кейсы:

- PN-A4: 2/4 дали `OBSERVED` (Grok, Claude), 2/4 — `POSSIBLE`/ошибка формального parent coding (Kimi, Copilot). Все четыре reason-поля при этом признают ключевой факт: B не был административной частью A внутри P, а поздний нарратив частично заменяет P на A.
- PN-B7: 1/4 `OBSERVED`, 3/4 `POSSIBLE`. Расхождение связано не с самой логикой, а с порогом между `POSSIBLE` и `OBSERVED`: формула «ушли от X» встречается, но packet говорит `иногда`, а не что она стала устойчиво доминирующей.

## 3. Критическая ошибка Copilot

PN-A4:

```text
formal_parent_relation = DIRECT_SUBORDINATION
```

при одновременном reason:

```text
B не был частью A
```

Это внутренняя логическая несовместимость. Для T0 топологии `P -> A + B + C + D` правильный structural relation между A и B — `SAME_PARENT_SYSTEM`, не `DIRECT_SUBORDINATION`.

Добавить mechanical consistency gate:

```text
IF T0 shows A and B as co-members of P
AND packet explicitly says B was not administratively part of A
THEN formal_parent_relation != DIRECT_SUBORDINATION
```

## 4. Главный семантический дефект рубрики

Поле `parent_node_substitution = POSSIBLE | OBSERVED` недостаточно операционализировано.

Нужна развязка:

```text
SUBSTITUTION_SIGNAL
!=
SUBSTITUTION_DOMINANCE
```

Предлагаемые поля:

```text
parent_node_substitution_signal = ABSENT | PRESENT | NOT_APPLICABLE | UNKNOWN
parent_node_substitution_prevalence = ISOLATED | CONTESTED | SUBSTANTIAL | DOMINANT | UNKNOWN | NOT_APPLICABLE
```

И производное решение:

```text
PRESENT + ISOLATED/CONTESTED
→ POSSIBLE

PRESENT + SUBSTANTIAL/DOMINANT
→ OBSERVED
```

Это снимает спор PN-B7 и часть спора PN-A4.

## 5. Второй дефект: continuity-identity case

PN-E5 показал, что `parent_node_substitution` не всегда применим.

Сейчас допустимые значения не содержат `NOT_APPLICABLE`, поэтому модели вынуждены выбирать `NO`, `POSSIBLE` или `NOT_ASSESSABLE`.

Добавить:

```text
parent_node_substitution = NO | POSSIBLE | OBSERVED | NOT_ASSESSABLE | NOT_APPLICABLE
```

И guard:

```text
NO_TERRITORIAL_PARENT_RELATION
+ CONTINUITY_IDENTITY_ONLY
→ parent_node_substitution = NOT_APPLICABLE
```

## 6. Третий дефект: successor structure

PN-A4 показал расхождение `SINGLE_CONTINUATOR` vs `SUCCESSOR_WITHOUT_EXCLUSIVE_CONTINUATOR`.

Packet говорит, что A получает наиболее сильную международную и институциональную преемственность, но не утверждает явно exclusive legal continuator status.

Нужно разделить:

```text
successor_weight = DOMINANT | COEQUAL | MIXED | UNKNOWN
exclusive_continuator_status = YES | NO | DISPUTED | UNKNOWN
```

И не заставлять одно поле `successor_structure` кодировать оба разных вопроса.

## 7. Подтверждённые guards

```text
SUCCESSOR_OF_SYSTEM != FORMER_OWNER_OF_OTHER_SYSTEM_MEMBERS
CONTINUATOR_STATUS != PARENTAL_OWNERSHIP_OF_CO_MEMBERS
SHARED_HISTORY != PRIOR_ADMINISTRATIVE_SUBORDINATION
SIZE_OR_POWER_ASYMMETRY != PARENT_RELATION
CONTINUITY_IDENTITY != TERRITORIAL_PARENT_OWNERSHIP
```

## 8. Предварительные метрики

На 24 case-coder решениях:

- clear negative-control substitution false positives: 1 заметный семантический overreach (Copilot PN-E5), остальные negative controls выдержаны;
- direct-subordination control PN-C2: 4/4 корректно `NO`;
- co-member / later-successor-parent cases PN-A4 + PN-B7: 8/8 reason-поля замечают сам механизм замены parent frame, но categorical threshold `POSSIBLE/OBSERVED` нестабилен;
- continuity-identity boundary PN-E5 выявила необходимость `NOT_APPLICABLE`.

## 9. Решение

`HPNR-001` считается успешным как conceptual discriminator, но schema требует v0.2 patch перед расширением на реальные source-backed narrative corpora.

Следующий тест не должен повторять эти же шесть кейсов без патча.
