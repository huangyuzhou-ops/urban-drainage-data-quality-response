# Reproducibility Guide

## Purpose

This guide separates fully public reproducibility from controlled-access reproducibility.

Public users can:

- inspect the DQI construction and controlled-degradation outputs;
- regenerate the manuscript figures from figure source-data tables;
- run the anonymization script on authorised local copies of the monitoring data;
- audit model-performance response summaries and statistical-test outputs.

Only authorised data holders can:

- rerun the complete workflow from raw municipal monitoring records;
- inspect original sensor IDs, coordinates or SCADA/node identifiers;
- reproduce the exact raw-data preprocessing stage.

## Recommended public repository layout

```text
data/
├── derived/
│   ├── rq1_formal_dqi_by_sensor_public.csv
│   ├── rq1_fast_controlled_degradation_metrics_public.csv
│   ├── rq1_fast_controlled_degradation_stat_tests_public.csv
│   └── rq1_ridge_selected_metrics_public.csv
├── figure_source_data/
│   ├── fig01_formal_dqi_overview_source.csv
│   ├── fig02_formal_dqi_clean_performance_source.csv
│   ├── fig03_controlled_degradation_response_curves_source.csv
│   ├── fig04_sensitivity_landscape_source.csv
│   ├── fig05_ridge_strong_baseline_robustness_source.csv
│   └── figS01_paired_statistical_uncertainty_source.csv
└── anonymized_monitoring_demo/
    ├── sensors_anonymized.csv
    ├── timeseries_anonymized/
    └── anonymization_provenance.json
```

## Full restricted workflow

1. Place the restricted raw monitoring archive outside the public repository.
2. Update `configs/rq1_experiment_config.yml` with local restricted-data paths.
3. Run the analysis scripts in chronological order.
4. Run `scripts/anonymize_monitoring_data.py` to prepare public monitoring derivatives.
5. Inspect the public output directory for forbidden fields before upload.
6. Upload the public package to Zenodo, OSF or an institutional repository.

## Privacy checks before public upload

The public repository should contain none of the following:

- original sensor IDs such as operational SCADA names;
- original node IDs from the hydraulic or asset-management system;
- original coordinates or map layers;
- raw time-series files named by real sensor ID;
- private ID-mapping files;
- absolute local paths;
- files containing credentials, data-owner contact details or internal project notes.

## Minimum verification checklist

- `python scripts/anonymize_monitoring_data.py --config configs/anonymization_config.yml` completes successfully.
- `anonymization_provenance.json` records whether coordinates or vertical asset values were published.
- No file matching `*_id_mapping.csv` is included in the public upload.
- Figure source-data files reproduce all main figures.
- `DATA_AVAILABILITY.md` and `SOFTWARE_AVAILABILITY.md` contain a real repository DOI or reviewer-access link.
