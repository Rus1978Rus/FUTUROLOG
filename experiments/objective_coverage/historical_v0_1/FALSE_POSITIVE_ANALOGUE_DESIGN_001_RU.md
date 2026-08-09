# FALSE_POSITIVE_ANALOGUE_DESIGN 001

**Статус:** `DESIGN_COMPLETE / CANDIDATES_IDENTIFIED / SOURCE_BACKFILL_REQUIRED / NUMERIC_EVIDENCESTATE_BLOCKED`

## 1. Цель

Проверить, не является ли FUTUROLOG просто детектором тревожных сигналов. Для этого нужны historical analogues, где наблюдались сильные pressure-signals, но заданный catastrophic transition в выбранном horizon не произошёл.

Ключевой принцип:

```text
HIGH_PRESSURE_SIGNAL != CATASTROPHIC_TRANSITION
```

False-positive analogue не означает "ничего плохого не произошло". Он означает только, что конкретный target outcome, для которого проверяется система, не произошёл в заранее заданном горизонте.

## 2. Критерии отбора

Кандидат допускается, если:

1. contemporaneous evidence существовало до/во время crisis window;
2. присутствуют минимум 2 pressure channels из v0.3;
3. наблюдаются реальные stabilizers/de-escalation mechanisms;
4. target outcome задаётся заранее и операционально;
5. horizon задаётся заранее;
6. outcome не подменяется более мягким событием;
7. retrospective sources используются только для проверки исхода, не как input раннего snapshot.

## 3. Кандидат A — India–Pakistan military standoff 2001–2002

### Почему подходит

Кризис после атаки на парламент Индии сопровождался крупной военной концентрацией, жёсткой риторикой, ракетно-ядерным риском и длительным противостоянием двух ядерных государств. При этом к октябрю 2002 начался частичный отвод войск и подтверждённая деэскалация.

UN 17 October 2002 приветствовал решение Индии и Пакистана о частичном отводе войск с приграничных районов и выразил надежду на существенную деэскалацию напряжённости.

### Target outcome

```text
FULL_SCALE_INTERSTATE_WAR_WITHIN_180_DAYS
```

### Почему это сильный control

Очень высокий security-pressure без перехода к полномасштабной межгосударственной войне в выбранном crisis horizon.

### Риски

- outcome definition должна отличать border incidents / coercive mobilization от full-scale war;
- ядерный риск нельзя считать доказанным только по риторике;
- нужны contemporaneous source families с обеих сторон и внешние наблюдатели.

## 4. Кандидат B — Greece–Turkey Eastern Mediterranean crisis 2020

### Почему подходит

В 2020 наблюдались военное присутствие, риск инцидентов на море/в воздухе, взаимные обвинения и спор по морским зонам. NATO в сентябре–октябре 2020 создало bilateral military de-confliction mechanism и 24/7 hotline, прямо предназначенные для снижения риска incidents/accidents и создания пространства для дипломатии.

NATO позже в декабре 2020 сообщало, что механизм работал, каналы связи были открыты, а отдельные военные учения были отменены как confidence-building measure.

### Target outcome

```text
DIRECT_GREECE_TURKEY_INTERSTATE_WAR_WITHIN_90_DAYS
```

### Почему это сильный control

Похож на типичный security escalation sensor: military proximity + sovereignty dispute + rhetoric + operational readiness, но с явным working deconfliction/stabilizer.

### Риски

- интенсивность ниже, чем India–Pakistan;
- обе стороны находятся внутри NATO, что является очень сильным структурным stabilizer и должно быть сохранено как feature, а не скрыто.

## 5. Кандидат C — Chile social unrest 2019

### Почему подходит

В октябре 2019 протесты быстро распространились по стране, сопровождались насилием, чрезвычайными мерами и серьёзными нарушениями прав человека. OHCHR special procedures в ноябре 2019 фиксировали массовые задержания, большое число раненых и погибших в контексте протестов.

Одновременно underlying pressure включал социальное и экономическое неравенство, неравный доступ к услугам и кризис доверия. OECD позже описал 2019 protests как широкий systemic shock, но также отметил силу институциональной и макроэкономической рамки; дальнейший процесс пошёл в сторону институционализированного constitutional response, а не гражданской войны.

### Target outcome

```text
ORGANIZED_CIVIL_WAR_OR_STATE_FRAGMENTATION_WITHIN_12_MONTHS
```

### Почему это сильный control

Проверяет social-pressure, inequality, protest mobilization, violence, legitimacy strain и institutional stabilizers без перехода к organized civil war.

### Риски

- это не "мирный" кейс: были жертвы и тяжёлые нарушения;
- constitutional transition нельзя автоматически кодировать как стабилизацию;
- COVID вмешивается в horizon 2020 и должен быть отдельным exogenous shock.

## 6. Кандидат D — Kazakhstan unrest January 2022

### Почему подходит

Протесты начались на фоне роста цен на газ, быстро переросли в масштабное насилие; были погибшие, государство ввело чрезвычайные меры и запросило помощь CSTO. OSCE 5–6 January призывала к деэскалации и диалогу. Уже 24 January OSCE PA фиксировала, что кризис был быстро стабилизирован, хотя расследование продолжалось.

### Target outcome

```text
SUSTAINED_CIVIL_WAR_OR_DURABLE_STATE_FRAGMENTATION_WITHIN_90_DAYS
```

### Почему это полезный control

Высокая social/political pressure, violent escalation, внешняя силовая помощь, disruption — но без устойчивого перехода к гражданской войне.

### Риски

- стабилизация была связана в том числе с жёстким силовым подавлением; это не normative success;
- нельзя путать `ORDER_RESTORED` с legitimacy recovery;
- source topology в авторитарной среде может быть сильно искажена.

## 7. Отдельный temporal control — Russia–Ukraine spring 2021 buildup

Не использовать как полноценный false-positive analogue для 2022 outcome, потому что тяжёлая эскалация произошла позже.

Но можно использовать как horizon-specific control:

```text
TARGET = FULL_SCALE_INVASION_WITHIN_60_DAYS_FROM_SPRING_2021_PEAK
```

Весной 2021 наблюдалось серьёзное военное напряжение, после чего часть войск была отведена. Это полезно для проверки horizon discipline:

```text
NO_EVENT_WITHIN_HORIZON != EVENT_NEVER
```

## 8. Приоритет

### Tier 1

```text
A India–Pakistan 2001–2002
B Greece–Turkey 2020
C Chile 2019
```

Они покрывают три разных класса false positive: interstate military, military-deconfliction, social-systemic unrest.

### Tier 2

```text
D Kazakhstan 2022
RU-UA spring 2021 temporal control
```

## 9. Следующий сбор

Для каждого Tier-1 кейса создать отдельный folder и собрать:

```text
cutoff_definition
outcome_definition
horizon
pressure evidence
stabilizer evidence
coverage topology
negative controls
source families
retrospective outcome verification
```

Порядок:

```text
FALSE_POSITIVE_A_INDIA_PAKISTAN
→ FALSE_POSITIVE_B_GREECE_TURKEY
→ FALSE_POSITIVE_C_CHILE
→ cross-case dry run
```

## 10. Guards

```text
FALSE_POSITIVE != SAFE_CASE
NO_CATASTROPHIC_TRANSITION != NO_HARM
DEESCALATION != ROOT_CAUSE_RESOLUTION
ORDER_RESTORED != LEGITIMACY_RECOVERED
HORIZON_FALSE_POSITIVE != PERMANENT_FALSE_POSITIVE
HIGH_PRESSURE_SIGNAL != OUTCOME_CERTAINTY
```

## 11. Gate

```text
FALSE_POSITIVE_ANALOGUE_DESIGN = PASS
CANDIDATE_SET = READY
TIER_1_SOURCE_BACKFILL = REQUIRED
RUBRIC_V0_3_NUMERIC_ACTIVATION = NO
NUMERIC_EVIDENCESTATE = BLOCKED
```
