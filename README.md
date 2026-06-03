# Quantifying the Effect of Liquid-Level Monitoring Data Quality on Urban Drainage Prediction Models

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20422917.svg)](https://doi.org/10.5281/zenodo.20422917)

This repository provides public reproducibility materials for the manuscript **Quantifying the Effect of Liquid-Level Monitoring Data Quality on Urban Drainage Prediction Models**. The release is intentionally scoped for public audit of reported figures and tables while protecting restricted municipal infrastructure monitoring data.

## Public contents

- figure- and table-level source-data files for numerical checking of manuscript results;
- environment and configuration files documenting the public workflow context;
- an anonymization utility for preparing public derivatives from authorised monitoring data;
- a small anonymized demonstration liquid-level dataset with relative 5-min time indices;
- metadata, citation and availability statements for the repository and Zenodo archive.

## Boundary of public reproducibility

The public release does not include raw municipal liquid-level records, original sensor identifiers, original node or SCADA identifiers, original coordinates, or the restricted processing workspace. It supports figure-level and table-level numerical checking from released source data. It does not support a complete public rerun from raw 5-min monitoring records. Full regeneration of the study requires authorised data-owner access to the restricted records and processing environment.

## Demonstration data

The demonstration dataset is provided only to inspect public file structure and anonymization conventions. It is not the dataset used to compute the manuscript results. Absolute timestamps are replaced by relative 5-min indices and public time labels, and liquid-level values are transformed to relative public units.

## Citation

Please cite the Zenodo archive when using these materials: https://doi.org/10.5281/zenodo.20422917.
