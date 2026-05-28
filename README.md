# Quantifying the Effect of Liquid-Level Monitoring Data Quality on Urban Drainage Prediction Models

This repository contains the reproducibility materials for the manuscript:

**Quantifying the Effect of Liquid-Level Monitoring Data Quality on Urban Drainage Prediction Models**.

The study evaluates how liquid-level monitoring-data quality affects short-horizon prediction performance in an urban drainage network. The repository is designed to support inspection of the analysis workflow while protecting restricted municipal infrastructure monitoring data.

## Repository contents

```text
.
├── README.md
├── DATA_AVAILABILITY.md
├── SOFTWARE_AVAILABILITY.md
├── REPRODUCIBILITY.md
├── CITATION.cff
├── .zenodo.json
├── requirements.txt
├── environment.yml
├── configs/
│   ├── anonymization_config.yml
│   └── rq1_experiment_config.yml
├── data/
│   └── README.md
├── metadata/
│   ├── dataset_description.md
│   └── repository_manifest.md
└── scripts/
    └── anonymize_monitoring_data.py
```

The public release should contain:

- figure source-data tables;
- derived sensor-level Data Quality Index (DQI) tables;
- controlled-degradation metrics and statistical-test outputs;
- scripts needed to regenerate the figures from the derived outputs;
- an anonymized demonstration version of the monitoring catalogue and optional monitoring time series, produced with `scripts/anonymize_monitoring_data.py`.

The public release should not contain:

- raw municipal liquid-level time series;
- original sensor identifiers, node identifiers or SCADA identifiers;
- original coordinates or maps of the drainage network;
- unrestricted files that reveal sensitive urban-infrastructure locations.

## Analysis overview

The implemented workflow contains five steps:

1. Standardise the 113-sensor liquid-level monitoring sample.
2. Compute a five-component DQI covering completeness, continuity, stability, physical plausibility and temporal consistency.
3. Generate controlled monitoring-data degradation scenarios.
4. Evaluate prediction baselines and performance-response metrics across horizons.
5. Export figure source data, statistical tests and manuscript figures.

The original operational data are restricted. Public reproducibility therefore relies on derived tables and anonymized monitoring-data products.

## Anonymization strategy

Monitoring data are anonymized before any public release. The anonymization workflow:

- replaces original sensor, SCADA and node identifiers with stable pseudonymous IDs;
- drops original sensor coordinates by default;
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

Regenerate the analysis outputs from the restricted raw-data workspace:

```bash
python scripts/rq1_113_recovery.py
python scripts/rq1_quality_response_fast.py
python scripts/rq1_goal_stage2.py
python scripts/rq1_ablation_interpretability.py
python scripts/rq1_render_paper_figures.py
```

The full analysis commands require access to the restricted raw monitoring archive. Public users can inspect the derived outputs and rerun the figure-generation step if figure source-data tables are included.

## Citation

If you use the workflow, please cite the manuscript and the archived repository DOI. The DOI field should be updated after Zenodo or another repository issues a persistent identifier.
