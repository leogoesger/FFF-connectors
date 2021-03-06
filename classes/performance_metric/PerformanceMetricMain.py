from classes.performance_metric.optimal_performance.OptimalMain import OptimalMain
import os
from classes.performance_metric.senario.Senario import Senario
from utils.helpers import write_arrays_to_csv, transpose_csv
from classes.performance_metric.reliability.ReliabilityTime import ReliabilityTime
from classes.performance_metric.reliability.ReliabilityVolume import ReliabilityVolume
from classes.performance_metric.vulnerability.Vulnerability import Vulnerability
from classes.performance_metric.resilience.Resilience import Resilience


class PerformanceMetricMain:
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
                binnings?: []}, 
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

          reliability_time: [time]
          time: {
              file_name: string
              timing_status: {
                func_0: [Boolean]
             }
           }

          reliability_volume: [volume]
          volume: {
              file_name: string
              value: {
                func_0: float
                func_1: float
             }
           }

           vulnerability: [value] 
           value: {
               file_name: string
               value: {
                   func0: float
                   func1: float
               }
           }

           resilience: [value] 
           value: {
               file_name: string
               value: {
                   func0: float
                   func1: float
               }
           }
        """

        _op = OptimalMain()
        self.op_datasets = _op.input_datasets
        self.user_inputs = _op.user_inputs
        self.get_senario_binnings()

        self.remove_output_files()

        self.reliabilityCalc = ReliabilityTime(
            self.op_datasets, self.user_inputs)
        self.reliability_time = self.reliabilityCalc.reliability_time

        self.reliability_volume = ReliabilityVolume(
            self.op_datasets, self.user_inputs).reliability_volumne

        self.vulnerability = Vulnerability(
            self.reliabilityCalc.limits, self.user_inputs, self.op_datasets).vulnerability

        self.resilience = Resilience(
            self.reliabilityCalc.limits, self.user_inputs, self.op_datasets).resilience

        self.save_result()

    def remove_output_files(self):
        for dataset in self.op_datasets:
            file_to_remove = 'files_output/performance_metrics/' + \
                dataset['file_name'] + '_performance.csv'
            if os.path.exists(file_to_remove):
                os.remove(file_to_remove)

    def get_senario_binnings(self):
        for dataset in self.op_datasets:
            dataset["scenarios"] = Senario(
                dataset["scenario_csv"], self.user_inputs).scenarios

    def save_result(self):
        folder_path = "files_output/performance_metrics/"
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

            for key, value in dataset["scenarios"].items():
                scenario_file_path = folder_path + \
                    "{}_{}_senario.csv".format(dataset["file_name"], key)
                senario_data = [value["data_ary"], value["magnitude"]]
                if "binnings" in value:
                    senario_data.append(value["binnings"])
                write_arrays_to_csv(senario_data, scenario_file_path)
                transpose_csv(scenario_file_path)
