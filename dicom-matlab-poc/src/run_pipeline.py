"""Minimal DICOM processing pipeline entry point."""

from __future__ import annotations

import sys
from pathlib import Path

from anonymize_dicom import anonymize_dicom
from convert_to_png import convert_to_png
from extract_metadata import extract_metadata
from load_dicom import load_dicom


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "data" / "sample.dcm"
    output_dir = project_root / "output"

    anonymized_path = output_dir / "anonymized.dcm"
    metadata_path = output_dir / "metadata.csv"
    image_path = output_dir / "image.png"

    output_dir.mkdir(parents=True, exist_ok=True)

    print("Starting DICOM pipeline...")
    print(f"Input file: {data_path}")

    try:
        print("[1/4] Loading DICOM...")
        dataset, pixels = load_dicom(data_path)

        print("[2/4] Anonymizing DICOM...")
        anonymize_dicom(data_path, anonymized_path)

        print("[3/4] Extracting metadata to CSV...")
        extract_metadata(dataset, metadata_path)

        print("[4/4] Converting image to PNG...")
        convert_to_png(pixels, image_path)

        print("\nPipeline complete. Generated files:")
        print(f" - {anonymized_path}")
        print(f" - {metadata_path}")
        print(f" - {image_path}")
        return 0
    except Exception as exc:  # pylint: disable=broad-except
        print(f"\nPipeline failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
