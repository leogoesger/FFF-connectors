# Hydraulic Suitability Time Series

Generate one csv file for each river type. This calculation combines all performance functions into one file, where performance function 1 being the first column after the raw input data.

## Input

Load flow bins files inside `files_input/hydraulic_suitability_TS/flow_bins` folder. The file should have format as `riverType_`. Here is a list of valid file names:

```
T5_.csv
T6_flow_bins.csv
```

with the following format:

| Q   | Qcfs |
| --- | ---: |
| 1   |  100 |
| 2   |  800 |
| 3   | 2000 |

Load suitability table inside `files_input/hydraulic_suitability_TS/suitability_table` folder with the following format (the output file from suitability calculation is directly supported):

|      |      |      |
| ---- | :--: | ---: |
| T5_1 | 0.1  |  0.2 |
| T6-2 | 0.95 |  0.5 |
| T6-1 | 0.65 | 0.15 |

_NOTE_: `files_input/hydraulic_suitability_TS/flow_bins` and `/suitability_table` will be created once you start the program, AND chose `hydraulic_suitability_TS` option. Or you can manually create the folder structure.

## Output

Output file will be saved into `files_output/hydraulic_suitability_TS` folder. With the following format:

| Date | Flow |      |      |
| ---- | :--: | :--: | :--: |
| T5_1 | 100  | 0.2  | 0.2  |
| T6-1 | 300  | 0.15 | 0.15 |
| T6-2 | 500  | 0.5  | 0.5  |

_NOTE_: `files_output/hydraulic_suitability_TS` will be created once you start the program, AND chose `hydraulic_suitability_TS` option. Or you can manually create the folder structure.

## Validations

Validations of input files are not fully supported. Please be sure to include all river types' `flow_bins` in `flow_bins`' directory. If you have two river types, make sure you have two matching `flow_bins`.

Further, make sure velocity count for each bin matches what you have in `performance_table.csv`(suitability table). If you have `8` velocity in `T5`, then performance table should have 8 velocity defined as well.
