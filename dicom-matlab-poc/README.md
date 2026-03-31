# DICOM Python MVP

A minimal, production-style proof-of-concept (PoC) for a DICOM processing workflow in Python.

This project demonstrates a small, modular pipeline that:
1. Loads a DICOM file
2. Anonymizes patient-identifiable metadata
3. Extracts metadata into CSV
4. Converts DICOM image data into PNG

## Project Structure

```text
dicom-matlab-mvp/
|-- data/                # contains sample.dcm
|-- src/                 # Python pipeline modules
|-- output/              # generated files
`-- README.md
```

## Pipeline Modules

1. `load_dicom.py`
- Reads metadata and image pixels using `pydicom`

2. `anonymize_dicom.py`
- Removes/replaces sensitive fields
- Prints `PatientName` before and after anonymization

3. `extract_metadata.py`
- Flattens metadata elements and writes `output/metadata.csv`

4. `convert_to_png.py`
- Normalizes pixel intensity to `[0, 255]` and writes `output/image.png`

5. `run_pipeline.py`
- Runs all steps in order
- Writes outputs to `output/`
- Prints progress and error messages

## Requirements

- Python 3.10+
- Packages:
  - `pydicom`
  - `numpy`
  - `Pillow`

Install dependencies:

```bash
pip install -r requirements.txt
```

## How To Run

1. Put a valid DICOM file at `data/sample.dcm`.
2. Run the pipeline from project root:

```bash
python src/run_pipeline.py
```

## Expected Output Files

After a successful run, these files are created in `output/`:
- `anonymized.dcm`
- `metadata.csv`
- `image.png`

## Why This PoC Matters

This PoC captures core operations common in medical imaging workflows:
- Safe handling and anonymization of patient data
- Metadata extraction for indexing and downstream analytics
- Image conversion for QA and interoperability

The modules are intentionally small and extendable, so this PoC can grow into batch processing, validation, and integration work for a larger GSoC project.
