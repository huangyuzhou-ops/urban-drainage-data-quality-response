# Software Availability

## Ready-to-paste manuscript statement

All analysis scripts used to generate the derived tables, controlled-degradation results, robustness analyses, statistical summaries and manuscript figures are available at https://github.com/huangyuzhou-ops/urban-drainage-data-quality-response. The repository includes Python source code, environment files, configuration files, figure source-data tables and command-line instructions for rerunning the workflow. The complete workflow requires access to restricted raw municipal monitoring records; however, the repository provides derived outputs and anonymized demonstration data sufficient to inspect the data-quality grading, degradation-response summaries, DQI perturbation checks, missing-handling sensitivity, dilated temporal-feature ridge outputs, rainfall-conditioned quality summaries and low-variation screening outputs. Figure-level and table-level numerical reproduction is public from the derived source-data tables. The versioned `v0.1.0` archive is available from Zenodo at https://doi.org/10.5281/zenodo.20422917.

## Software requirements

- Python 3.10 or later.
- NumPy, pandas, SciPy, scikit-learn, matplotlib and seaborn.
- openpyxl for disguised Excel files and `.xlsx` files.
- PyYAML for configuration files.

## Workflow execution

The repository provides the corresponding analysis scripts, configuration files and staged command sequence for the implemented workflow. Public users can rerun figure generation and table-level checks from the released derived outputs. Complete regeneration from raw 5-min monitoring records requires an authorised restricted-data workspace, after which the staged workflow described in the repository documentation can be executed without changing the manuscript code.
