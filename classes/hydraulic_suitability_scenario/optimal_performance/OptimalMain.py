import os
from utils.helpers import read_csv_to_arrays
from classes.hydraulic_suitability_scenario.optimal_performance.OptimalPerformance import OptimalPerformance
from classes.hydraulic_suitability_scenario.optimal_performance.UserInput import UserInput
from classes.hydraulic_suitability_scenario.optimal_performance.OptimalBinning import OptimalBinning


class OptimalMain:
    input_scenario_files = 'files_input/hydraulic_suitability_scenario/scenario'
    input_TS_files = 'files_input/hydraulic_suitability_scenario/time_series'

    def __init__(self):
        self.input_datasets = []
        self.number_of_funcs = None
        self.user_inputs = None  # for each func

        self.read_scenario_and_time_series()
        self.calculate_percentille()
        self.get_user_input()
        self.get_binnings()

    def read_scenario_and_time_series(self):
        """
        Read both scenario and its ts file into matrix.

        scenario file format xx_xx_x_scenario.csv
        time series file format xx_xx_x.csv
        """

        for file_name in os.listdir(self.input_TS_files):
            ts_path = os.path.join(self.input_TS_files, file_name)
            scenario_path = os.path.join(
                self.input_scenario_files, file_name.split(".")[0]+"_scenario.csv")

            ts_matrix = read_csv_to_arrays(ts_path, True)
            scenario_matrix = read_csv_to_arrays(scenario_path, True)

            self.input_datasets.append(
                {"file_name": file_name.split(".")[0], "ts": ts_matrix, "scenario_csv": scenario_matrix})

    def calculate_percentille(self):
        for dataset in self.input_datasets:
            optimalRange = OptimalPerformance(dataset["ts"])
            # each file should have the same number of funcs
            self.number_of_funcs = optimalRange.number_of_funcs
            dataset["optimal"] = optimalRange.result

    def get_user_input(self):
        self.user_inputs = UserInput(self.number_of_funcs).user_inputs

    def get_binnings(self):
        for dataset in self.input_datasets:
            optimalBins = OptimalBinning(self.user_inputs, dataset).binnings

            for func in optimalBins:
                dataset["optimal"][func]["binnings"] = optimalBins[func]
