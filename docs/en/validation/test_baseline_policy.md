# Test Baseline Policy

> **English semantic mirror.** Baselines distinguish intended evolution from accidental scoring drift.

## Required baselines

### M1.4 no-objective baseline

Captures canonical behaviour after domain-neutral naming, canonical mapping, dual output, metadata, and the controlled gamma transition, but before Objective Layer activation.

When no objective components are active, every later implementation must reproduce this baseline exactly for equivalent input.

### M3.6.1 full-objective baseline

Captures behaviour after all five Objective Layer components are integrated and activation logic is enabled. It is separate from the no-objective compatibility baseline.

## Baseline contents

Baselines should cover final score, universal score, objective value and activation state, trust adjustment, confluence behaviour, legacy and canonical fields, reason codes, metadata versions, missing-input behaviour, partial status, and sealing/audit payloads where applicable.

## Update rule

A baseline may change only through an explicit versioned decision that states:

- what changed;
- why the prior behaviour is no longer correct;
- expected compatibility impact;
- affected tests and documentation;
- reviewer and validation evidence.

Passing a new test is not sufficient reason to delete or rewrite a prior baseline.
