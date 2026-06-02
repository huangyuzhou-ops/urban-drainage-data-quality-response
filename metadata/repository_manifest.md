# Repository Manifest

## Files to include in the public archive

| File or folder | Include? | Notes |
|---|---:|---|
| `README.md` | Yes | Repository overview and quick start |
| `DATA_AVAILABILITY.md` | Yes | Public and restricted data routes |
| `SOFTWARE_AVAILABILITY.md` | Yes | Software statement and commands |
| `REPRODUCIBILITY.md` | Yes | Public and restricted reproduction levels |
| `requirements.txt` | Yes | Python package dependencies |
| `environment.yml` | Yes | Conda environment |
| `configs/anonymization_config.yml` | Yes | Public anonymization parameters |
| `configs/rq1_experiment_config.yml` | Yes | Analysis settings with no credentials |
| `scripts/anonymize_monitoring_data.py` | Yes | Public anonymization utility |
| `data/figure_source_data/` | Yes | Source data for main and supplementary figures, including derived DQI, degradation-response, robustness, rainfall-condition and low-variation screening summaries |
| `anonymized_demo_liquid_level_8sensors_2months.csv` | Yes | Small transformed demonstration monitoring stream; not used for manuscript numerical reproduction |
| `anonymized_demo_liquid_level_8sensors_2months_provenance.json` | Yes | Transformation and use-boundary metadata for the demonstration stream |
| `data/raw/` | No | Restricted operational records |
| `_private/` | No | ID mapping and local-only provenance |
| `.zenodo.json` | Yes | Repository metadata |
| `CITATION.cff` | Yes | Citation metadata |

## Local source-to-public mapping

| Local source | Public destination |
|---|---|
| `rq1_outputs/paper_figures_v2/source_data/*.csv` | `data/figure_source_data/main_and_S1_S5/` |
| `rq1_outputs/reviewer_response_experiments/source_data/*.csv` | `data/figure_source_data/S6_S8_reviewer_response/` |
| `rq1_outputs/rainfall_static_quality/source_data/*.csv` | `data/figure_source_data/S9_S10_rainfall_low_variation/` |
| `rq1_outputs/figure_evidence_roadmap/source_data/*.csv` | `data/figure_source_data/S11_evidence_roadmap/` |
| `排水液位时序模型资料/监测点数据/` | Not public; transformed only through anonymization script |

## Public-release safeguards

- Public tables use pseudonymous sensor identifiers and exclude original coordinates, SCADA identifiers and direct asset names.
- Private ID-mapping files are excluded from the public archive.
- The Zenodo archive used for submission is version `v0.1.0` with DOI https://doi.org/10.5281/zenodo.20422917.
