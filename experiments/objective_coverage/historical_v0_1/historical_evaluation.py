"""Leakage-safe historical evaluator for frozen Objective/Coverage candidates.

Status: EXPERIMENTAL / DATASET_NOT_SELECTED / NOT_VALIDATED

This module does not fetch data and does not tune formula parameters. It consumes
pre-built historical snapshots whose evidence timestamps are at or before cutoff.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Iterable


@dataclass(frozen=True)
class HistoricalSnapshot:
    case_id: str
    cutoff_time: str
    outcome_time: str | None
    outcome_label: int
    measured_score: float
    evidence_coverage: float
    source_independence: float
    freshness: float
    pipeline_completeness: float
    observed_noise: float
    latest_evidence_time: str

    def validate(self) -> None:
        if self.outcome_label not in (0, 1):
            raise ValueError("outcome_label must be 0 or 1")
        if self.latest_evidence_time > self.cutoff_time:
            raise ValueError("FUTURE_INFORMATION_LEAKAGE")
        for name in (
            "measured_score",
            "evidence_coverage",
            "source_independence",
            "freshness",
            "pipeline_completeness",
            "observed_noise",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be in [0,1]")


def formula_a(s: HistoricalSnapshot) -> float:
    quality = (
        0.25 * s.source_independence
        + 0.25 * s.freshness
        + 0.30 * s.pipeline_completeness
        + 0.20 * (1.0 - s.observed_noise)
    )
    return s.measured_score * s.evidence_coverage * quality


def formula_b(s: HistoricalSnapshot) -> float:
    factors = (
        s.evidence_coverage,
        s.source_independence,
        s.freshness,
        s.pipeline_completeness,
        1.0 - s.observed_noise,
    )
    support = 0.0 if any(v == 0.0 for v in factors) else prod(factors) ** 0.2
    return s.measured_score * support


def formula_c(s: HistoricalSnapshot) -> float:
    quality = (
        0.25 * s.source_independence
        + 0.25 * s.freshness
        + 0.30 * s.pipeline_completeness
        + 0.20 * (1.0 - s.observed_noise)
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


FROZEN_FORMULAS = {
    "A_LINEAR_COVERAGE": formula_a,
    "B_GEOMETRIC": formula_b,
    "C_HYBRID_MIN_CAP": formula_c,
}


def evaluate(snapshots: Iterable[HistoricalSnapshot]) -> list[dict]:
    rows: list[dict] = []
    for snapshot in snapshots:
        snapshot.validate()
        for formula_name, formula in FROZEN_FORMULAS.items():
            rows.append(
                {
                    "case_id": snapshot.case_id,
                    "cutoff_time": snapshot.cutoff_time,
                    "outcome_time": snapshot.outcome_time,
                    "outcome_label": snapshot.outcome_label,
                    "formula": formula_name,
                    "effective_confidence": formula(snapshot),
                    "evidence_coverage": snapshot.evidence_coverage,
                    "source_independence": snapshot.source_independence,
                    "pipeline_completeness": snapshot.pipeline_completeness,
                }
            )
    return rows
