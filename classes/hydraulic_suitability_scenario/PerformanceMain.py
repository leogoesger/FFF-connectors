from classes.hydraulic_suitability_scenario.optimal_performance.OptimalMain import OptimalMain
from classes.hydraulic_suitability_scenario.senario.Senario import Senario
from utils.helpers import write_arrays_to_csv, transpose_csv
from classes.hydraulic_suitability_scenario.reliability.ReliabilityTime import ReliabilityTime


class PerformanceMain:
    def __init__(self):
        """ 
          Main entry function for performance. 
          op_datasets: [dataset]

          dataset: {
            file_name: string,
            ts: [[]],
            scenario_csv: [[]],
            scenarios: {func_0: {
                data_ary: [], 
                magnitude: [], 
                binnings?: []}
            },
            optimal: {func_0: {
              data_ary: [], 
              date_ary: [], 
              matrix: [[]], 
              percentiles: [{min, 10th, 25th, 50th, 75th, 90th, max}]}, 
              binnings?: [{min, 10th, 25th, 50th, 75th, 90th, max}]}
            }

          user_inputs: {
            fun_0: {
              type: string, 
              bioperiod_start_date: string, 
              bioperiod_end_date: string, 
              binnings?: []}
            }
        """

        _op = OptimalMain()
        self.op_datasets = _op.input_datasets
        self.user_inputs = _op.user_inputs

        self.get_senario_binnings()
        self.save_result()
        self.get_reliability_timing()

    def get_senario_binnings(self):
        for dataset in self.op_datasets:
            dataset["scenarios"] = Senario(
                dataset["scenario_csv"], self.user_inputs).scenarios

    def get_reliability_timing(self):
        ReliabilityTime(self.op_datasets, self.user_inputs)

    def save_result(self):
        folder_path = "files_output/hydraulic_suitability_scenario/"
        for dataset in self.op_datasets:
            for key, value in dataset["optimal"].items():

                # Saving optimal whole matrix
                optimal_matrix_file_path = folder_path + \
                    "{}_{}_opt_matrix.csv".format(dataset["file_name"], key)
                write_arrays_to_csv(value["matrix"], optimal_matrix_file_path)

                # Saving optimal percentile into 7 columns
                optimal_percentile_file_path = folder_path + \
                    "{}_{}_opt_percentile.csv".format(
                        dataset["file_name"], key)
                percentiles = [[perc["min"], perc["10th"], perc["25th"], perc["50th"], perc["75th"],
                                perc["90th"], perc["max"]] for perc in value["percentiles"]]
                write_arrays_to_csv(percentiles, optimal_percentile_file_path)

                # Saving optimal binnings into 7 columns
                if "binnings" in value:
                    optimal_binning_file_path = folder_path + \
                        "{}_{}_opt_binnings.csv".format(
                            dataset["file_name"], key)
                    binnings = [[bins["min"], bins["10th"], bins["25th"], bins["50th"], bins["75th"],
                                 bins["90th"], bins["max"]] for bins in value["binnings"]]
                    write_arrays_to_csv(binnings, optimal_binning_file_path)

            for key, value in dataset["scenarios"].items():
                scenario_file_path = folder_path + \
                    "{}_{}_senario.csv".format(dataset["file_name"], key)
                senario_data = [value["data_ary"], value["magnitude"]]
                if "binnings" in value:
                    senario_data.append(value["binnings"])
                write_arrays_to_csv(senario_data, scenario_file_path)
                transpose_csv(scenario_file_path)
