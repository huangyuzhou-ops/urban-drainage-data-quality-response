# Software Availability

## Ready-to-paste manuscript statement

All analysis scripts used to generate the derived tables, controlled-degradation results, statistical summaries and manuscript figures will be archived in a public repository before submission or publication. The repository will include Python source code, environment files, configuration files, figure source-data tables and command-line instructions for rerunning the workflow. The complete workflow requires access to restricted raw municipal monitoring records; however, the repository will provide derived outputs and anonymized demonstration data sufficient to inspect the data-quality grading, degradation-response summaries and figure-generation procedure. Repository DOI or reviewer-access link: `[to be added before submission]`.

## Software requirements

- Python 3.10 or later.
- NumPy, pandas, SciPy, scikit-learn, matplotlib and seaborn.
- openpyxl for disguised Excel files and `.xlsx` files.
- PyYAML for configuration files.

## Core commands

```bash
python scripts/anonymize_monitoring_data.py --config configs/anonymization_config.yml
python scripts/rq1_113_recovery.py
python scripts/rq1_quality_response_fast.py
python scripts/rq1_goal_stage2.py
python scripts/rq1_ablation_interpretability.py
python scripts/rq1_render_paper_figures.py
```

The first command prepares public anonymized monitoring products. The remaining commands reproduce the paper workflow when the restricted raw-data workspace is available.

## Fields to update before submission

- Repository DOI or reviewer link.
- Exact Python version used in the final run.
- Commit hash of the archived code.
- Public licence selected for code.
- Whether raw-data dependent scripts are executable by reviewers or only by authorised data holders.

