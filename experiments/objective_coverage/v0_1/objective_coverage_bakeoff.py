"""Comparative bakeoff for provisional Objective/Coverage aggregation families.

Status: EXPERIMENTAL / NOT_CALIBRATED / NOT_VALIDATED
None of these formulas is a calibrated forecast probability.
"""

from dataclasses import dataclass, asdict
from math import prod
import random


@dataclass(frozen=True)
class EvidenceState:
    measured_score: float
    evidence_coverage: float
    source_independence: float
    freshness: float
    pipeline_completeness: float
    observed_noise: float

    def validate(self) -> None:
        for name, value in asdict(self).items():
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be in [0, 1], got {value}")

    @property
    def low_noise(self) -> float:
        return 1.0 - self.observed_noise


def formula_a_linear_coverage(s: EvidenceState) -> float:
    s.validate()
    quality = (
        0.25 * s.source_independence
        + 0.25 * s.freshness
        + 0.30 * s.pipeline_completeness
        + 0.20 * s.low_noise
    )
    return s.measured_score * s.evidence_coverage * quality


def formula_b_geometric(s: EvidenceState) -> float:
    s.validate()
    factors = (
        s.evidence_coverage,
        s.source_independence,
        s.freshness,
        s.pipeline_completeness,
        s.low_noise,
    )
    support = 0.0 if any(v == 0.0 for v in factors) else prod(factors) ** (1.0 / 5.0)
    return s.measured_score * support


def formula_c_hybrid_cap(s: EvidenceState) -> float:
    s.validate()
    quality = (
        0.25 * s.source_independence
        + 0.25 * s.freshness
        + 0.30 * s.pipeline_completeness
        + 0.20 * s.low_noise
    )
    base = s.measured_score * quality * (
        s.evidence_coverage * s.pipeline_completeness
    ) ** 0.5
    critical_min = min(
        s.evidence_coverage,
        s.source_independence,
        s.pipeline_completeness,
    )
    provisional_cap = 0.15 + 0.85 * critical_min
    return min(base, provisional_cap)


FORMULAS = {
    "A_LINEAR_COVERAGE": formula_a_linear_coverage,
    "B_GEOMETRIC": formula_b_geometric,
    "C_HYBRID_MIN_CAP": formula_c_hybrid_cap,
}


def monotonicity_check(samples: int = 5000, seed: int = 42):
    rng = random.Random(seed)
    violations = {name: 0 for name in FORMULAS}
    positive_fields = [
        "measured_score",
        "evidence_coverage",
        "source_independence",
        "freshness",
        "pipeline_completeness",
    ]

    for _ in range(samples):
        values = {
            "measured_score": rng.random(),
            "evidence_coverage": rng.random(),
            "source_independence": rng.random(),
            "freshness": rng.random(),
            "pipeline_completeness": rng.random(),
            "observed_noise": rng.random(),
        }
        base = EvidenceState(**values)

        for formula_name, formula in FORMULAS.items():
            baseline = formula(base)

            for field in positive_fields:
                changed = dict(values)
                changed[field] = min(1.0, changed[field] + 0.05)
                if formula(EvidenceState(**changed)) + 1e-12 < baseline:
                    violations[formula_name] += 1

            changed = dict(values)
            changed["observed_noise"] = min(1.0, changed["observed_noise"] + 0.05)
            if formula(EvidenceState(**changed)) > baseline + 1e-12:
                violations[formula_name] += 1

    return violations
