# Reproducibility Guide

This guide distinguishes public numerical checking from controlled-access reruns.

## Publicly supported checks

Public users can inspect released figure/table source data, compare numerical values against the manuscript, examine the anonymized demonstration dataset, inspect environment and configuration files, and review the anonymization utility. These materials are sufficient for figure-level and table-level numerical checking.

## Not publicly executable

The public archive does not contain the restricted raw municipal monitoring records or the full controlled-access processing workspace. It therefore does not provide a complete public rerun of DQI construction, controlled degradation, model fitting or robustness analysis from raw records. Complete regeneration requires authorised access granted by the data-owning organisation.

## Privacy checks

Public files should contain no original sensor IDs, node IDs, SCADA identifiers, coordinates, private ID mappings, raw time-series files named by real assets, credentials or absolute local paths.
