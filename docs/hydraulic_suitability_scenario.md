# Hydraulic Scenario (suitability table)

Generate suitability table given a set of raster files.

## Input

Load all `.tif` files inside `files_input/hydraulic_suitability` folders. The file should have format as `riverType_velocity_variable_boundary`. Here is a list of valid file names:

```
T5_1_d_.tif
T6_2_t_c.tif
```

_NOTE_: `files_input/hydraulic_suitability` will be created once you start the program, AND chose `hydraulic_suitability` option. Or you can manually create the folder structure.

## Output

Output file will be saved into `files_output/hydraulic_suitability` folder. With the following format:

| Name | func_1 | func_2 |
| ---- | :----: | -----: |
| T5_1 |  0.1   |    0.2 |
| T6-2 |  0.95  |    0.5 |
| T6-1 |  0.65  |   0.15 |

_NOTE_: `files_output/hydraulic_suitability` will be created once you start the program, AND chose `hydraulic_performance` option. Or you can manually create the folder structure.
