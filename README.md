# Quantifying the Effect of Liquid-Level Monitoring Data Quality on Urban Drainage Prediction Models

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20422917.svg)](https://doi.org/10.5281/zenodo.20422917)

This repository contains the reproducibility materials for the manuscript:

**Quantifying the Effect of Liquid-Level Monitoring Data Quality on Urban Drainage Prediction Models**.

The study evaluates how liquid-level monitoring-data quality affects short-horizon prediction performance in an urban drainage network. The repository is designed to support inspection of the analysis workflow while protecting restricted municipal infrastructure monitoring data.

## Repository contents

```text
.
|-- README.md
|-- DATA_AVAILABILITY.md
|-- SOFTWARE_AVAILABILITY.md
|-- REPRODUCIBILITY.md
|-- CITATION.cff
|-- .zenodo.json
|-- requirements.txt
|-- environment.yml
|-- configs/
|   |-- anonymization_config.yml
|   |-- anonymization_config.json
|   `-- rq1_experiment_config.yml
|-- data/
|   |-- README.md
|   `-- figure_source_data/
|-- anonymized_demo_liquid_level_8sensors_2months.csv
|-- anonymized_demo_liquid_level_8sensors_2months_provenance.json
|-- anonymized_demo_dataset_README.md
|-- metadata/
|   |-- dataset_description.md
|   `-- repository_manifest.md
`-- scripts/
    `-- anonymize_monitoring_data.py
```

The public release contains:

- figure source-data tables;
- derived sensor-level Data Quality Index (DQI) tables;
- controlled-degradation metrics and statistical-test outputs;
- DQI weight-threshold robustness, missing-handling sensitivity and DTFR robustness outputs;
- rainfall-conditioned quality summaries and low-variation screening sensitivity outputs;
- scripts needed to regenerate figures from derived outputs;
- a pseudonymised monitoring catalogue without coordinates or asset identifiers;
- a small anonymized demonstration monitoring dataset with relative 5-min time indices and scaled liquid-level values.

The public release does not contain:

- raw municipal liquid-level time series;
- original sensor identifiers, node identifiers or SCADA identifiers;
- original coordinates or maps of the drainage network;
- unrestricted files that reveal sensitive urban-infrastructure locations.

## Analysis overview

The implemented workflow contains seven steps:

1. Standardise the 113-sensor liquid-level monitoring sample.
2. Compute a five-component DQI covering completeness, continuity, stability, physical plausibility and temporal consistency.
3. Generate controlled monitoring-data degradation scenarios.
4. Evaluate prediction baselines and performance-response metrics across horizons.
5. Run DQI perturbation, missing-handling and DTFR robustness checks.
6. Run rainfall-conditioned quality and low-variation screening sensitivity checks.
7. Export figure source data, statistical tests and manuscript figures.

The original operational data are restricted. Public reproducibility therefore relies on derived tables and anonymized monitoring-data products. Figure-level and table-level numerical reproduction is supported from the public derived source-data tables. Complete regeneration from raw 5-min liquid-level records requires authorised data-owner access. The demonstration monitoring dataset is included only to inspect data structure and script interfaces; it is not used to reproduce manuscript numerical results.

## Anonymization strategy

Monitoring data are anonymized before any public release. The anonymization workflow:

- replaces original sensor, SCADA and node identifiers with stable pseudonymous IDs;
- drops original sensor coordinates by default;
- shuffles the public sensor order;
- optionally rotates and scales the sensor coordinate system when an approved public schematic is needed;
- optionally converts absolute liquid-level values to sensor-wise scaled public units;
- writes a private ID mapping only when explicitly enabled in the configuration.

The default public catalogue does not contain coordinates. Rotation and scaling are retained only as an optional configuration for cases where the data owner approves release of a schematic relative layout.

## Quick start

Create the Python environment:

```bash
conda env create -f environment.yml
conda activate rq1-dqi-response
```

or:

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

Run the anonymization workflow:

```bash
python scripts/anonymize_monitoring_data.py --config configs/anonymization_config.yml
```

If PyYAML is not installed, use the equivalent JSON configuration:

```bash
python scripts/anonymize_monitoring_data.py --config configs/anonymization_config.json
```

Regenerate the analysis outputs from the restricted raw-data workspace by following the staged workflow described in `REPRODUCIBILITY.md` and the experiment configuration files. The full analysis sequence requires access to the restricted raw monitoring archive. Public users can inspect the derived outputs, inspect the anonymized demonstration monitoring dataset and rerun figure generation if figure source-data tables are included.

## Citation

If you use the workflow, please cite the manuscript and the archived repository release:

Huang, Yuzhou. (2026). Reproducibility materials for quantifying liquid-level monitoring-data quality effects on urban drainage prediction models (v0.1.0). Zenodo. https://doi.org/10.5281/zenodo.20422917

The version DOI for this release is `10.5281/zenodo.20422917`. The concept DOI for all repository versions is `10.5281/zenodo.20422916`.

