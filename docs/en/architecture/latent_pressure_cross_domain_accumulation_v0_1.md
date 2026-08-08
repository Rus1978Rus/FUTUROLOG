# LATENT_PRESSURE / CROSS_DOMAIN_ACCUMULATION v0.1

**Status:** `DESIGN_DRAFT / CROSS_CASE / NOT_CORE_SCORE / NOT_CALIBRATED / NOT_VALIDATED`

## Purpose

This layer captures slow-moving processes that may look harmless in isolation but can alter system stability when they persist and synchronize across domains.

Core distinction:

```text
SMALL_CHANGE × MANY_DOMAINS × LONG_DURATION × SYNCHRONIZATION
!=
ONE_LOUD_EVENT
```

The layer records PRESSURE, STABILIZER, MIXED, and UNKNOWN states rather than inventing a single hidden causal score.

## Required domains

```text
DEMOGRAPHY_AND_MIGRATION
SOCIAL_FABRIC_AND_TRUST
SOCIAL_INEQUALITY_AND_DISTRIBUTION
IDENTITY_AND_GROUP_BOUNDARIES
RELIGION_AND_RELIGIOUS_INSTITUTIONS
CULTURE_AND_COLLECTIVE_MEMORY
INFORMATION_ECOLOGY
EDUCATION
HEALTH_AND_PSYCHOSOCIAL_STRESS
CRIMINAL_AND_SHADOW_ECONOMY
TECHNOLOGY_AND_INFRASTRUCTURE
CLIMATE_AND_ENVIRONMENT
FOOD_SECURITY
WATER_SECURITY
FUEL_AND_ENERGY_ACCESS
LAND_AND_RESOURCE_ACCESS
```

Food, water and fuel must distinguish physical existence from affordable and deliverable access. Climate events are not treated as automatic conflict causes; an evidence-supported transmission mechanism is required.

## Inequality and legitimacy

`SOCIAL_INEQUALITY_AND_DISTRIBUTION` is a standalone domain. It includes income, wealth, regional and group-based inequality, service-access gaps, affordability, youth unemployment, social mobility, perceived unfairness and status loss.

For every case, the system must identify evidence-supported `LEGITIMACY_BEARING_GROUP` populations rather than infer them from a regime label.

In real or nominal democracies, track:

```text
ACTIVE_ELECTORATE_INEQUALITY_PRESSURE
```

In non-democratic systems, track:

```text
LEGITIMIZING_STRATUM_INEQUALITY_PRESSURE
```

Also track:

```text
STATUS_LOSS_OF_LEGITIMACY_GROUP
EXPECTATION_REALITY_GAP
```

## Guards

```text
INEQUALITY != DISCONTENT
DISCONTENT != DELEGITIMIZATION
DELEGITIMIZATION != PROTEST
PROTEST != CONFLICT
STATUS_LOSS != RADICALIZATION
RELIGIOUS_DIFFERENCE != RELIGIOUS_CONFLICT
CULTURAL_CHANGE != POLITICAL_CAUSE
DEMOGRAPHIC_CHANGE != THREAT
```

Every transition requires its own evidence-supported link.

## Cross-domain accumulation

Do not simply add domain scores. Evaluate persistence, synchronization, domain diversity, geographic overlap, group overlap, mechanistic links, countervailing stabilizers and evidence coverage.

```text
MANY_WEAK_SIGNALS != STRONG_CAUSAL_CLAIM
LATENT_PRESSURE_LEVEL != EVIDENCE_CONFIDENCE
```

The same schema applies to the Russia–Ukraine 2021–2022 and Myanmar post-coup 2021 pilots.

**Current status:** `DESIGN_ACCEPTED_FOR_HISTORICAL_COLLECTION / NO_SINGLE_LATENT_PRESSURE_SCORE / NO_AUTOMATIC_CAUSAL_CHAIN / NOT_CALIBRATED / NOT_VALIDATED`.
