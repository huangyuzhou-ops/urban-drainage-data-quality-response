# Reproducibility Guide

## Purpose

This guide separates fully public reproducibility from controlled-access reproducibility.

Public users can:

- inspect the DQI construction and controlled-degradation outputs;
- audit model-performance response summaries and statistical-test outputs;
- audit DQI perturbation, missing-handling and DTFR robustness summaries;
- audit rainfall-conditioned quality summaries and low-variation screening sensitivity outputs;
- regenerate manuscript figures from figure source-data tables when the derived tables are included;
- inspect a small anonymized demonstration monitoring dataset with relative 5-min time indices and transformed liquid-level values;
- run the anonymization script on authorised local copies of the monitoring data.

Only authorised data holders can:

- rerun the complete workflow from raw municipal monitoring records;
- inspect original sensor IDs, coordinates or SCADA/node identifiers;
- reproduce the exact raw-data preprocessing stage.

## Public repository layout

```text
data/
|-- derived/
|   |-- rq1_formal_dqi_by_sensor_public.csv
|   |-- rq1_fast_controlled_degradation_metrics_public.csv
|   |-- rq1_fast_controlled_degradation_stat_tests_public.csv
|   |-- rq1_ridge_selected_metrics_public.csv
|   |-- rq1_dqi_weight_threshold_robustness_public.csv
|   |-- rq1_missing_handling_high_severity_summary_public.csv
|   |-- rq1_dtfr_failure_ranking_public.csv
|   |-- rq1_rainfall_event_quality_summary_public.csv
|   `-- rq1_low_variation_screening_dqi_summary_public.csv
|-- figure_source_data/
|   |-- fig01_v2_quality_structure_source.csv
|   |-- fig02_v2_clean_performance_source.csv
|   |-- fig03_v2_degradation_facets_log_ci_source.csv
|   |-- fig04_v2_sensitivity_matrix_ranking_source.csv
|   |-- fig05_v2_ridge_robustness_source.csv
|   `-- reviewer_response_experiments/
`-- anonymized_monitoring_demo/
    |-- sensors_anonymized.csv
    |-- liquid_level_demo_8sensors_2months.csv
    `-- anonymization_provenance.json
```

In the submission package, the same demonstration data are supplied as `anonymized_demo_liquid_level_8sensors_2months.csv` with a separate provenance JSON. The demonstration data are useful for checking file structure and public script interfaces; exact manuscript results are reproduced from derived source-data tables or from restricted raw records under data-owner control.

## Full restricted workflow

1. Place the restricted raw monitoring archive outside the public repository.
2. Update `configs/rq1_experiment_config.yml` with local restricted-data paths.
3. Run the staged analysis workflow in the documented order to generate DQI tables, controlled-degradation outputs, robustness checks, rainfall-conditioned summaries and low-variation screening summaries.
4. Run the public-derivative preparation step to create anonymized monitoring products.
5. Regenerate manuscript figures from the exported figure source-data tables.
6. Compare the regenerated tables and figures against the archived release.
7. Inspect the public output directory for forbidden fields before upload.
8. Archive the public package in the versioned Zenodo record.

## Privacy checks before public upload

The public repository contains none of the following:

- original sensor IDs such as operational SCADA names;
- original node IDs from the hydraulic or asset-management system;
- original coordinates or map layers;
- raw time-series files named by real sensor ID;
- private ID-mapping files;
- absolute local paths;
- files containing credentials, data-owner contact details or internal project notes.

## Minimum verification checklist

- The anonymization workflow completes successfully with the repository configuration.
- The staged robustness and operating-condition workflows complete successfully when restricted raw-data paths are available.
- `anonymization_provenance.json` records whether coordinates or vertical asset values were published.
- No file matching `*_id_mapping.csv` is included in the public upload.
- Figure source-data files reproduce all main and supplementary figures.
- `DATA_AVAILABILITY.md` and `SOFTWARE_AVAILABILITY.md` contain the final repository URL and Zenodo DOI.
