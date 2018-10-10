from classes.hydraulic_suitability_scenario.optimal_performance.OptimalMain import OptimalMain
from classes.hydraulic_suitability_scenario.senario.Senario import Senario
from utils.helpers import write_arrays_to_csv


class PerformanceMain:
    def __init__(self):
        """ 
          Main entry function for performance. 
          op_datasets: [dataset]

          dataset: {
            file_name: string,
            ts: [[]],
            scenario_csv: [[]],
            scenarios: {func_0: {date_ary: [], data_ary: []}},
            optimal: {func_0: {
              data_ary: [], 
              date_ary: [], 
              matrix: [[]], 
              percentiles: [{min, max, ...}]}, 
              binning: [{min, max, ...}]}
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

    def get_senario_binnings(self):
        for dataset in self.op_datasets:
            dataset["scenarios"] = Senario(
                dataset["scenario_csv"], self.user_inputs).scenarios

    def save_result(self):
        file_path = ""
