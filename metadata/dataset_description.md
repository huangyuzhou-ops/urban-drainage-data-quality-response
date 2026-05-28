# Dataset Description

## Dataset name

Derived and anonymized data for "Quantifying the Effect of Liquid-Level Monitoring Data Quality on Urban Drainage Prediction Models".

## Study system

The original data come from an urban sewer liquid-level monitoring network. The analysed sample contains 113 monitoring points and one year of 5-min observations from 11 August 2021 00:00 to 10 August 2022 23:55.

## Public derivatives

The public repository is expected to include:

- pseudonymised sensor catalogue without asset coordinates;
- sensor-level DQI components and grades;
- clean-input prediction metrics;
- controlled-degradation scenario metrics;
- paired statistical-test outputs;
- ablation and interpretability summaries;
- figure source-data tables.

## Restricted source data

The raw monitoring records, original sensor identifiers and true coordinates are restricted because they describe municipal drainage assets. These records are controlled by the data-owning organisation and are not redistributed in the public repository.

## Anonymization method

The public monitoring catalogue is produced by:

1. replacing original identifiers with stable pseudonymous sensor IDs;
2. dropping original coordinates and asset-elevation fields by default;
3. randomly shuffling public sensor rows so that row order cannot be used as an auxiliary identifier;
4. optionally transforming liquid-level values to sensor-wise public units, if approved by the data owner.

Optional rotated and scaled coordinates can be generated for a schematic layout, but they are not included in the default public release.

## Intended use

The public derivatives are intended for:

- verifying figure-level results;
- inspecting the DQI and controlled-degradation workflow;
- reproducing public summaries and plots;
- developing comparable data-quality evaluation workflows.

They are not intended for:

- operational drainage control;
- asset-location inference;
- hydraulic calibration of the original network;
- public safety or infrastructure-security assessment.
