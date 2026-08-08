"""Build resource-flow visibility at each historical cutoff.

Rules:
- A flow is visible only when original_publication_time <= cutoff_time.
- RETROSPECTIVE_REFERENCE / RETROSPECTIVE_ONLY records never enter a pre-cutoff snapshot.
- Missing amount is not zero.
- Visibility is epistemic: it means the evidence record was publicly available by cutoff,
  not that the underlying resource flow began on that date.

Status: EXPERIMENTAL / AUDIT_HELPER / NOT_A_SCORER
"""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path


def parse_time(value: str) -> datetime:
    value = value.strip()
    if "T" in value:
        return datetime.fromisoformat(value)
    return datetime.fromisoformat(value + "T23:59:59")


def is_pre_cutoff_admissible(row: dict) -> bool:
    flag = row.get("cutoff_admissibility", "")
    status = row.get("status", "")
    if "RETROSPECTIVE_ONLY" in flag or status == "RETROSPECTIVE_REFERENCE":
        return False
    return True


def build(schedule_path: Path, flow_path: Path, output_path: Path) -> None:
    with schedule_path.open(encoding="utf-8", newline="") as f:
        snapshots = list(csv.DictReader(f))
    with flow_path.open(encoding="utf-8", newline="") as f:
        flows = list(csv.DictReader(f))

    rows = []
    for snapshot in snapshots:
        cutoff = parse_time(snapshot["cutoff_time"])
        visible = []
        excluded_future = []
        excluded_retro = []
        for flow in flows:
            published = parse_time(flow["original_publication_time"])
            if not is_pre_cutoff_admissible(flow):
                excluded_retro.append(flow["flow_id"])
            elif published <= cutoff:
                visible.append(flow["flow_id"])
            else:
                excluded_future.append(flow["flow_id"])
        rows.append({
            "snapshot_id": snapshot["snapshot_id"],
            "cutoff_time": snapshot["cutoff_time"],
            "visible_flow_count": len(visible),
            "visible_flow_ids": ";".join(visible),
            "excluded_future_ids": ";".join(excluded_future),
            "excluded_retrospective_ids": ";".join(excluded_retro),
        })

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
