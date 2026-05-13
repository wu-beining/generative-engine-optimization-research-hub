#!/usr/bin/env python3
"""Validate curated CSV metadata for the GEO research hub."""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "data/papers.csv": [
        "id",
        "title",
        "year",
        "primary_url",
        "relevance_tier",
        "overlap_group",
        "novelty_score",
        "value_score",
    ],
    "data/github_repos.csv": [
        "repo",
        "category",
        "url",
        "what_it_contains",
        "value_rating",
        "maintenance_priority",
    ],
    "data/benchmarks.csv": [
        "id",
        "name",
        "year",
        "url",
        "scope",
        "metrics",
        "status",
    ],
    "data/industry_sources.csv": [
        "id",
        "title",
        "source_type",
        "url",
        "why_it_matters",
        "evidence_level",
    ],
}


def valid_url(value: str) -> bool:
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_csv(path: Path, required_fields: list[str]) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            return [f"{path}: missing header"]

        missing = [field for field in required_fields if field not in reader.fieldnames]
        if missing:
            errors.append(f"{path}: missing columns {missing}")

        seen_ids: set[str] = set()
        key_field = "id" if "id" in reader.fieldnames else "repo"

        for line_no, row in enumerate(reader, start=2):
            for field in required_fields:
                if not row.get(field, "").strip():
                    errors.append(f"{path}:{line_no}: empty required field {field}")

            key = row.get(key_field, "").strip()
            if key:
                if key in seen_ids:
                    errors.append(f"{path}:{line_no}: duplicate key {key}")
                seen_ids.add(key)

            for field, value in row.items():
                if field.endswith("_url") or field == "url":
                    if not valid_url(value.strip()):
                        errors.append(f"{path}:{line_no}: invalid URL in {field}: {value}")

            for field in ("novelty_score", "value_score", "value_rating"):
                value = row.get(field, "").strip()
                if value:
                    try:
                        score = int(value)
                    except ValueError:
                        errors.append(f"{path}:{line_no}: {field} is not an integer: {value}")
                        continue
                    if score < 1 or score > 5:
                        errors.append(f"{path}:{line_no}: {field} out of range 1-5: {value}")

    return errors


def main() -> int:
    all_errors: list[str] = []
    for relative, fields in REQUIRED.items():
        path = ROOT / relative
        if not path.exists():
            all_errors.append(f"{path}: file does not exist")
            continue
        all_errors.extend(validate_csv(path, fields))

    if all_errors:
        print("Metadata validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print("Metadata validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
