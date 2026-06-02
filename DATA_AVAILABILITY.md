# Data Availability

## Ready-to-paste manuscript statement

The raw liquid-level monitoring records and original sensor coordinates cannot be publicly redistributed because they contain restricted municipal infrastructure information controlled by the data owner. Public release of these records could reveal the location and operating status of drainage assets. The data owner approved public release of the transformed demonstration monitoring dataset and derived tables included in the public archive. To support reproducibility without exposing restricted infrastructure data, the repository accompanying this manuscript provides derived sensor-level Data Quality Index tables, controlled-degradation metrics, paired statistical-test outputs, DQI robustness outputs, missing-handling sensitivity outputs, dilated temporal-feature ridge robustness outputs, rainfall-conditioned quality summaries, low-variation screening summaries, figure source-data tables, plotting scripts, a pseudonymised monitoring catalogue without coordinates or asset identifiers and a small anonymized demonstration monitoring dataset. Figure-level and table-level numerical reproduction is public from the derived source-data tables. Complete regeneration from the raw 5-min liquid-level records requires authorised access to the restricted municipal archive. The public GitHub repository is available at https://github.com/huangyuzhou-ops/urban-drainage-data-quality-response, and the versioned archive is available from Zenodo at https://doi.org/10.5281/zenodo.20422917. Access to the raw operational records is controlled by the data-owning organisation and is subject to its infrastructure-security and project-governance review.

## Dataset access routes

| Dataset | Access route | Public release content | Restricted content | Reason |
|---|---|---|---|---|
| Raw 5-min liquid-level time series | Controlled access only | Transformed demonstration derivative approved by the data owner | Original timestamps, sensor IDs and liquid-level records | Municipal infrastructure-security restriction |
| Sensor catalogue | Anonymized public derivative | Pseudonymous sensor IDs without coordinates or asset identifiers | Original SCADA IDs, node IDs and coordinates | Asset-location protection |
| Demonstration monitoring dataset | Public repository | 8-sensor, 59-day relative-index example with transformed liquid levels and observed masks | Absolute dates, original sensor IDs, coordinates and untransformed levels | Allows public inspection of monitoring-stream structure without exposing assets |
| Sensor-level DQI table | Public repository | DQI components, grades and non-identifying summary metrics | Original sensor IDs should be replaced before public release | Supports manuscript figures and tables |
| Controlled-degradation metrics | Public repository | Scenario-level and sensor-level aggregated metrics | Original raw monitoring records | Supports model-performance response claims |
| Statistical-test outputs | Public repository | Paired tests, confidence intervals and adjusted p-values | None expected after pseudonymisation | Supports reported uncertainty |
| Robustness outputs | Public repository | DQI perturbation summaries, missing-handling sensitivity metrics, dilated temporal-feature ridge summaries, rainfall-conditioned quality summaries and low-variation screening summaries | Original raw monitoring records | Supports reviewer-facing robustness claims |
| Figure source data | Public repository | Source CSVs for main and supplementary figures | Original asset identifiers if present | Supports figure reproducibility |
| Analysis scripts | Public repository | Python scripts and configuration files | Absolute local paths and credentials | Supports computational reproducibility |
