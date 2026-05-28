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
| `scripts/rq1_*.py` | Yes, after path cleanup | Analysis scripts copied from the working project |
| `data/figure_source_data/` | Yes | Source data for figures |
| `data/derived/` | Yes | Derived metrics and test outputs |
| `data/anonymized_monitoring_demo/` | Yes, if approved | Pseudonymised monitoring products; coordinates omitted by default |
| `data/raw/` | No | Restricted operational records |
| `_private/` | No | ID mapping and local-only provenance |
| `.zenodo.json` | Yes | Repository metadata |
| `CITATION.cff` | Yes | Citation metadata |

## Local source-to-public mapping

| Local source | Public destination |
|---|---|
| `rq1_outputs/paper_figures/source_data/*.csv` | `data/figure_source_data/` |
| `rq1_outputs/goal_stage2/*.csv` | `data/derived/` after ID pseudonymisation |
| `rq1_outputs/quality_response_fast/*.csv` | `data/derived/` after ID pseudonymisation |
| `rq1_outputs/ablation_interpretability/*.csv` | `data/derived/` after ID pseudonymisation |
| `scripts/rq1_*.py` | `scripts/` after replacing local absolute paths with config paths |
| `排水液位时序模型资料/监测点数据/` | Not public; transformed only through anonymization script |

## Final manual checks

- Search public archive for original sensor prefixes and road/place-name fragments.
- Search public archive for `C:/Users/` or other local absolute paths.
- Remove private mapping files.
- Confirm public source-data tables do not contain original coordinate columns.
- Confirm repository DOI and licence fields are no longer placeholders.
