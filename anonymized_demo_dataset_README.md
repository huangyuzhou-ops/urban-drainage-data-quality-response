# Anonymized Demonstration Monitoring Dataset

This folder-level item accompanies the manuscript repository materials and provides a small public example of the monitoring-stream structure used by the workflow.

File: `anonymized_demo_liquid_level_8sensors_2months.csv`

Content:

| Field | Meaning |
|---|---|
| `sensor_id_public` | Pseudonymous demonstration sensor identifier |
| `time_index_5min` | Relative 5-min time index; absolute dates are not published |
| `relative_time_label` | Relative day-and-clock label used only for readability, formatted as `day_000 00:00` |
| `liquid_level_relative` | Sensor-level liquid value after median removal and IQR scaling |
| `observed_mask` | 1 if a value was observed on the 5-min grid, 0 otherwise |

The dataset contains 8 sensors over 59 days on a 5-min grid. It is intended for inspecting file structure, public script interfaces and example data-quality calculations. It is not used to reproduce the numerical results in the manuscript because the full raw municipal monitoring archive remains restricted. Figure-level and table-level numerical reproduction should use the derived source-data tables released with the repository. Complete regeneration from raw monitoring records requires authorised data-owner access.
