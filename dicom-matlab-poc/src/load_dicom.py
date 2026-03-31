"""Load DICOM metadata and pixel data."""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pydicom
from pydicom.dataset import FileDataset


def load_dicom(dicom_path: str | Path) -> Tuple[FileDataset, object]:
    """Read DICOM file and return dataset + pixel array.

    Args:
        dicom_path: Path to a .dcm file.

    Returns:
        Tuple of (dataset, pixel_array).

    Raises:
        FileNotFoundError: If file does not exist.
        ValueError: If path is empty.
        RuntimeError: If DICOM cannot be read.
    """
    path = Path(dicom_path)
    if not str(path):
        raise ValueError("A DICOM file path is required.")

    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"DICOM file not found: {path}")

    try:
        dataset = pydicom.dcmread(path)
        pixel_array = dataset.pixel_array
    except Exception as exc:  # pylint: disable=broad-except
        raise RuntimeError(f"Failed to read DICOM file {path}: {exc}") from exc

    return dataset, pixel_array
