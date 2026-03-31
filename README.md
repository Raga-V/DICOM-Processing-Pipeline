# DWiM: DICOM Workflows in MATLAB

![DWiM Banner](https://github.com/Raga-V/DICOM-Processing-Pipeline/blob/main/dicom-matlab-poc/landing.png)

A complete, native MATLAB framework for DICOM image retrieval, processing, anonymization, and machine learning pipeline integration.

An open-source MATLAB counterpart to Python-first DICOM toolkits, built for medical imaging researchers who prefer MATLAB's ecosystem and reproducible workflows.

## Project Overview

DICOM is the universal standard for medical imaging, but teams often spend significant effort on retrieval, PHI-safe preprocessing, and dataset preparation before modeling can begin.

DWiM addresses this with a modular, privacy-first MATLAB framework designed to:

- Retrieve DICOM images from Orthanc or TCIA-backed sources
- Anonymize protected health information automatically
- Export metadata to MATLAB tables or CSV
- Convert imaging data to PNG or JPEG for visualization workflows
- Support DICOM-RT and 3D volume processing
- Build ML-ready datasets for downstream pipelines

Built on MATLAB Medical Imaging Toolbox and Image Processing Toolbox, with optional Python interoperability when required.

## Key Features

### Core Capabilities

- Real-time and batch retrieval from Orthanc/PACS and TCIA
- Automated anonymization using dicomanon plus configurable tag filtering
- Metadata extraction to CSV or MATLAB table formats
- DICOM to PNG/JPEG conversion while preserving processing traceability
- DICOM-RT support including ROI contour parsing
- 3D volume handling with spatial referencing
- ML-ready datastore construction for Deep Learning Toolbox workflows

### Included Sample Workflows

- Scanner usage analytics
- IVC filter detection pipeline

### User Experience

- Interactive MATLAB app built with App Designer
- Reproducible Live Scripts for end-to-end workflows
- Toolbox packaging via .mltbx for easier adoption

## Project Structure

```text
DWiM/
|-- +dicomwf/                  % Main MATLAB package
|   |-- acquisition/           % Retrieval from Orthanc/TCIA
|   |-- preprocessing/         % Anonymization and cleaning
|   |-- processing/            % Conversion, DICOM-RT, 3D
|   |-- workflows/             % Sample research workflows
|   |-- app/                   % Interactive MATLAB app
|   `-- utils/                 % Helpers and validation
|-- examples/                  % Reproducible scripts and Live Scripts
|-- data/                      % Test datasets
|-- output/                    % Generated results
|-- docs/                      % Documentation
|-- tests/                     % Unit and integration tests
|-- README.md
`-- DWiM.mltbx                 % Installable toolbox package
```

## Quick Start

### Prerequisites

- MATLAB R2025a or newer
- Medical Imaging Toolbox
- Image Processing Toolbox
- Local Orthanc server with TCIA datasets for retrieval testing

### Installation

Clone the repository:

```bash
git clone https://github.com/KathiraveluLab/DWiM.git
cd DWiM
```

Install as toolbox (recommended):

```matlab
matlab.addons.toolbox.installToolbox('DWiM.mltbx')
```

Or add source to path:

```matlab
addpath(genpath('path/to/DWiM'));
```

### Run the Pipeline

```matlab
config = dicomwf.loadConfig('examples/config.json');
data = dicomwf.retrieveFromOrthanc(config);
anonymized = dicomwf.anonymize(data);
metadata = dicomwf.extractMetadata(anonymized);
dicomwf.convertToPng(anonymized, 'output/');
```

## Architecture

The framework follows a layered architecture:

- Data layer: Orthanc, TCIA, local DICOM storage
- Processing layer: retrieval, anonymization, conversion
- Dataset layer: ML-ready datastores and metadata joins
- Integration layer: research pipelines and automation
- Visualization layer: interactive app interfaces

Modules are designed to be independently testable and extendable.

## Proof of Concept

This repository currently includes a Python PoC for the core pipeline in the src folder:

- Load DICOM
- Anonymize patient fields
- Extract metadata to CSV
- Convert image to PNG

![PoC Output](https://github.com/Raga-V/DICOM-Processing-Pipeline/blob/main/dicom-matlab-poc/output/image.png)

This PoC provides reference behavior while the full MATLAB package structure is expanded.

## Project Status

- Program: Google Summer of Code 2026 proposal track
- Organization: University of Alaska Fairbanks, Kathiravelu Lab
- Current status: Proposal stage
- Mentors: Ryan Birmingham and Pradeeban Kathiravelu

## Contributing

Contributions are welcome from the medical imaging and MATLAB communities.

1. Fork the repository
2. Create a feature branch
3. Add tests for your changes
4. Open a pull request with a clear summary

## License

Distributed under the MIT License. See LICENSE for details.

## Acknowledgments

- Mentors: Ryan Birmingham and Pradeeban Kathiravelu
- Organization: University of Alaska Fairbanks, Kathiravelu Lab
- Datasets: The Cancer Imaging Archive (TCIA)
- Infrastructure: Orthanc DICOM server

## Contact

Raga Gowtami Vinjanampati

- GitHub: @Raga-V
- Email: raga.vinjanampati@gmail.com
