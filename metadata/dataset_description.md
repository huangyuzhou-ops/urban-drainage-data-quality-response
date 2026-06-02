# Dataset Description

## Dataset name

Derived and anonymized reproducibility data for "Quantifying the Effect of Liquid-Level Monitoring Data Quality on Urban Drainage Prediction Models".

## Study system

The original data come from an urban sewer liquid-level monitoring network. The analysed sample contains 113 monitoring sensors and one year of 5-min liquid-level observations. Original sensor identifiers, infrastructure coordinates and raw operational records are restricted by the data owner and are not redistributed.

## Public derivatives

The public repository contains:

- figure source-data tables for the main and supplementary figures;
- derived sensor-level Data Quality Index (DQI) components and grades;
- controlled-degradation response metrics and paired statistical-test outputs;
- DQI perturbation, missing-handling, dilated temporal-feature ridge, rainfall-conditioned quality and low-variation screening summaries;
- a small transformed demonstration monitoring stream with relative 5-min time indices;
- public configuration files and anonymization utilities.

## Restricted source data

The raw monitoring records, original sensor identifiers and true coordinates are restricted because they describe municipal drainage assets. These records are controlled by the data-owning organisation and are not redistributed in the public repository.

## Anonymization method

Public monitoring derivatives are prepared by replacing original identifiers with stable pseudonymous IDs, removing original coordinates, shuffling public sensor order where applicable and transforming liquid-level values for the demonstration stream. The demonstration monitoring file uses relative time indices and relative day-clock labels rather than absolute timestamps.

## Intended use

The public derivatives are intended for checking figure-level and table-level numerical results, inspecting the DQI and controlled-degradation workflow and developing comparable monitoring-data quality evaluation workflows. They are not intended for operational drainage control, asset-location inference, hydraulic calibration of the original network or infrastructure-security assessment.

