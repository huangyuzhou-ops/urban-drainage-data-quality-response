# Repository Manifest

| Component | Public role |
|---|---|
| `README.md`, `REPRODUCIBILITY.md` | Repository scope and public reproducibility boundary |
| `DATA_AVAILABILITY.md`, `SOFTWARE_AVAILABILITY.md` | Submission-ready availability statements |
| `environment.yml`, `requirements.txt`, `configs/` | Environment and configuration metadata |
| `scripts/anonymize_monitoring_data.py` | Utility for generating public derivatives from authorised data |
| `anonymized_demo_liquid_level_8sensors_2months.csv` | Demonstration data for file-structure inspection |
| `anonymized_demo_liquid_level_8sensors_2months_provenance.json` | Provenance for the demonstration dataset |
| `data/figure_source_data/` when present | Source data for figure/table numerical checking |

The repository is not presented as a complete public rerun package. Restricted raw monitoring records and the private processing workspace are required for end-to-end regeneration.
