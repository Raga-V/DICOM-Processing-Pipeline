"""Anonymize DICOM patient-identifiable fields."""

from __future__ import annotations

from pathlib import Path

import pydicom
from pydicom.dataset import FileDataset
from pydicom.uid import generate_uid


SENSITIVE_FIELDS = {
    "PatientName": "ANONYMIZED",
    "PatientID": "ANONYMIZED",
    "PatientBirthDate": "",
    "PatientSex": "O",
    "OtherPatientIDs": "",
    "OtherPatientNames": "",
    "PatientAddress": "",
    "InstitutionName": "ANONYMIZED",
    "ReferringPhysicianName": "ANONYMIZED",
    "PerformingPhysicianName": "ANONYMIZED",
    "OperatorsName": "ANONYMIZED",
}


def anonymize_dicom(input_path: str | Path, output_path: str | Path) -> FileDataset:
    """Anonymize a DICOM file and write it to disk.

    Prints PatientName before and after anonymization to demonstrate PHI removal.
    """
    source = Path(input_path)
    target = Path(output_path)

    if not source.exists() or not source.is_file():
        raise FileNotFoundError(f"Input DICOM file not found: {source}")

    target.parent.mkdir(parents=True, exist_ok=True)

    try:
        dataset = pydicom.dcmread(source)
    except Exception as exc:  # pylint: disable=broad-except
        raise RuntimeError(f"Failed to read DICOM file {source}: {exc}") from exc

    before_name = str(getattr(dataset, "PatientName", "<not present>"))
    print(f"PatientName before anonymization: {before_name}")

    for field, replacement in SENSITIVE_FIELDS.items():
        if hasattr(dataset, field):
            setattr(dataset, field, replacement)

    # Replace identifiers commonly used for cross-system linkage.
    if hasattr(dataset, "StudyInstanceUID"):
        dataset.StudyInstanceUID = generate_uid()
    if hasattr(dataset, "SeriesInstanceUID"):
        dataset.SeriesInstanceUID = generate_uid()
    if hasattr(dataset, "SOPInstanceUID"):
        dataset.SOPInstanceUID = generate_uid()

    try:
        dataset.save_as(target)
    except Exception as exc:  # pylint: disable=broad-except
        raise RuntimeError(f"Failed to write anonymized DICOM {target}: {exc}") from exc

    anonymized = pydicom.dcmread(target)
    after_name = str(getattr(anonymized, "PatientName", "<removed>"))
    print(f"PatientName after anonymization: {after_name}")

    return anonymized
