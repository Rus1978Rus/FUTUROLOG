# STRATEGIC_INTERACTION_CANDIDATE v0.1
## Кандидатный будущий слой стратегических взаимодействий

**Статус:** `ADAPT / LATER / NOT_CORE / NOT_OBJECTIVE_LAYER`

Источник идеи: агентная симуляция кооперации с памятью отношений, ресурсным дефицитом и сменой партнёров. Код-прототип не импортируется в FUTUROLOG на текущем этапе.

## Что сохраняем как структурные механизмы

```text
RELATIONSHIP_MEMORY(A, B)
PARTNER_SWITCHING
NETWORK_REDUNDANCY
RESOURCE_DEPENDENT_COOPERATION
STRATEGY_ADAPTATION
```

Особенно важное различие:

```text
UNWILLING_TO_HELP != UNABLE_TO_HELP
```

Будущая модель отношений не должна сворачивать историю в простой ярлык «хороший/плохой» или один trust-score. Кандидатный объект должен уметь хранить по крайней мере:

```text
helped_when_able
refused_when_able
unable_to_help
received_support
dependency
last_interaction
alternative_partners
```

## Потенциальное применение в GEOECON

Структурная аналогия может использоваться для анализа государств, компаний и организаций как ACTOR, связанных торговлей, помощью, санкциями, поставками, кредитом, технологиями и ресурсами.

Это не означает, что государства «ведут себя как летучие мыши», и не является доказательством геоэкономической модели.

## Границы

```text
NOT CORE
NOT OBJECTIVE SCORE
NOT GEOECON PROOF
NOT IMPLEMENTED
NOT VALIDATED
```

Текущий целевой владелец: будущий `Strategic Interaction Layer` после стабилизации универсального двигателя и Objective/Coverage.
