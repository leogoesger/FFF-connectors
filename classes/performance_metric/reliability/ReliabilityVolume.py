from utils.time_series_conversion import date_to_offset_julian
from utils.helpers import write_single_dict_to_csv


class ReliabilityVolume:
    """Calculate reliability volumne

       Sum of all daily suitable area values over water year (scenario)  / sum all _median_ daily suitable area values over water year (reference) in a given bioperiod

       Returns:
       reliability_volumne: [value] 
            value: {
                file_name: string
                value: {
                    func0: float
                    func1: float
                }
    """

    def __init__(self, datasets, inputs):
        self.datasets = datasets
        self.inputs = inputs
        self.limits = {}
        self.reliability_volumne = []

        self.calculate_reliability_volume()
        self.save_csv()

    def calculate_reliability_volume(self):
        for dataset in self.datasets:
            self.reliability_volumne.append(
                {"file_name": dataset["file_name"], "value": {}})

            for func_key, value in dataset["optimal"].items():

                start = date_to_offset_julian(
                    self.inputs[func_key]["bioperiod_start_date"]+"/2000", "10/01")
                end = date_to_offset_julian(
                    self.inputs[func_key]["bioperiod_end_date"]+"/2000", "10/01")

                sum_scenario = sum(
                    [float(i) for i in dataset["scenarios"][func_key]["magnitude"]])
                sum_optimal = sum([float(d["50th"])
                                   for d in value["percentiles"]][start:end])

                self.reliability_volumne[-1]["value"][func_key] = sum_scenario / sum_optimal

    def save_csv(self):
        folder_path = "files_output/performance_metrics/"

        for data in self.reliability_volumne:
            file_path = folder_path + \
                data["file_name"] + "_performance.csv"
            write_single_dict_to_csv(data['value'], file_path, 'a')
