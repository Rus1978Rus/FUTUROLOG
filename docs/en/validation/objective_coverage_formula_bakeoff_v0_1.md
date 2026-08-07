# OBJECTIVE_COVERAGE_FORMULA_BAKEOFF v0.1
## Comparative Objective / Coverage formula experiment

**Status:** `EXPERIMENTAL / NOT_CALIBRATED / NOT_VALIDATED / NO_PRODUCTION_FORMULA_SELECTED`

Three provisional aggregation families were compared on eight preregistered boundary fixtures.

Pass counts:
- A_LINEAR_COVERAGE: 6/8
- B_GEOMETRIC: 5/8
- C_HYBRID_MIN_CAP: 8/8

All three had zero monotonicity violations in 5000 seeded random states.

Decision:
- A remains the baseline candidate.
- B remains a comparison candidate.
- C advances only to historical evaluation; it is not accepted as a final formula.

`SYNTHETIC_PASS != REAL_WORLD_VALIDATION`
`BEST_IN_BAKEOFF != FINAL_FORMULA`
`CONFIDENCE_IN_ANALYSIS != PROBABILITY_OF_FUTURE_EVENT`

Next gate: `OBJECTIVE_COVERAGE_HISTORICAL_EVALUATION_v0_1`.
