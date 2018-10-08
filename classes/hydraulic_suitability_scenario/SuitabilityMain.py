import os
from utils.helpers import read_csv_to_arrays
from classes.hydraulic_suitability_scenario.TimeSeriesPercentille import TimeSeriesPercentille


class SuitabilityScenarioMain:
    input_scenario_files = 'files_input/hydraulic_suitability_scenario/scenario'
    input_TS_files = 'files_input/hydraulic_suitability_scenario/time_series'

    def __init__(self):
        self.input_datasets = []

        self.read_scenario_and_time_series()
        self.calculate_percentille()

    def read_scenario_and_time_series(self):
        for file_name in os.listdir(self.input_TS_files):
            ts_path = os.path.join(self.input_TS_files, file_name)
            scenario_path = os.path.join(
                self.input_scenario_files, file_name.split(".")[0]+"_scenario.csv")

            ts_matrix = read_csv_to_arrays(ts_path, True)
            scenario_matrix = read_csv_to_arrays(scenario_path, True)

            self.input_datasets.append(
                {"file_name": file_name, "ts": ts_matrix, "scenario": scenario_matrix})

    def calculate_percentille(self):
        for dataset in self.input_datasets:
            dataset["percentiles"] = TimeSeriesPercentille(
                dataset).result

        import pdb
        pdb.set_trace()
        print("")
