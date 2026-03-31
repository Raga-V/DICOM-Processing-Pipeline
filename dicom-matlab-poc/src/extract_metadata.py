"""Extract DICOM metadata into CSV."""

from __future__ import annotations

import csv
from pathlib import Path

from pydicom.dataset import FileDataset


def extract_metadata(dataset: FileDataset, csv_path: str | Path) -> Path:
    """Write DICOM metadata to CSV with columns: tag, keyword, name, value."""
    if dataset is None:
        raise ValueError("Dataset is required for metadata extraction.")

    target = Path(csv_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for element in dataset.iterall():
        if element.VR == "SQ":
            value_text = "<sequence>"
        else:
            value_text = str(element.value)

        rows.append(
            {
                "tag": str(element.tag),
                "keyword": element.keyword or "",
                "name": element.name,
                "value": value_text,
            }
        )

    try:
        with target.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=["tag", "keyword", "name", "value"])
            writer.writeheader()
            writer.writerows(rows)
    except Exception as exc:  # pylint: disable=broad-except
        raise RuntimeError(f"Failed to write metadata CSV {target}: {exc}") from exc

    return target
