# Data Availability

## Ready-to-paste manuscript statement

The raw liquid-level monitoring records and original sensor coordinates cannot be publicly redistributed because they contain restricted municipal infrastructure information controlled by the data owner. Public release of these records could reveal the location and operating status of drainage assets. To support reproducibility without exposing restricted infrastructure data, the repository accompanying this manuscript will provide derived sensor-level Data Quality Index tables, controlled-degradation metrics, paired statistical-test outputs, figure source-data tables, plotting scripts and a pseudonymised monitoring catalogue without coordinates or asset identifiers. Access to the raw operational records is controlled by the data-owning organisation and is subject to its infrastructure-security and project-governance review. Repository DOI or reviewer-access link: `[to be added before submission]`.

## Dataset access routes

| Dataset | Access route | Public release content | Restricted content | Reason |
|---|---|---|---|---|
| Raw 5-min liquid-level time series | Controlled access only | None, unless the data owner approves an anonymized derivative | Original timestamps, sensor IDs and liquid-level records | Municipal infrastructure-security restriction |
| Sensor catalogue | Anonymized public derivative | Pseudonymous sensor IDs only, unless coordinate release is explicitly approved | Original SCADA IDs, node IDs and coordinates | Asset-location protection |
| Sensor-level DQI table | Public repository | DQI components, grades and non-identifying summary metrics | Original sensor IDs should be replaced before public release | Supports manuscript figures and tables |
| Controlled-degradation metrics | Public repository | Scenario-level and sensor-level aggregated metrics | Original raw monitoring records | Supports model-performance response claims |
| Statistical-test outputs | Public repository | Paired tests, confidence intervals and adjusted p-values | None expected after pseudonymisation | Supports reported uncertainty |
| Figure source data | Public repository | Source CSVs for main and supplementary figures | Original asset identifiers if present | Supports figure reproducibility |
| Analysis scripts | Public repository | Python scripts and configuration files | Absolute local paths and credentials | Supports computational reproducibility |

## Unresolved fields before public deposition

- Replace `[to be added before submission]` with a Zenodo DOI, OSF DOI, institutional repository DOI or reviewer-access link.
- Confirm the data owner permits release of the anonymized monitoring catalogue and any anonymized time-series derivatives.
- Confirm the public data licence for derived tables, for example CC BY 4.0.
- Confirm the code licence, for example MIT or BSD-3-Clause.
- Remove private ID-mapping files before public upload.

## Repository status

Current status: `draft_with_placeholders`.

The package is suitable for internal review and repository preparation. It is not submission-ready until a persistent repository link and data-owner approval for the anonymized derivative are available.
