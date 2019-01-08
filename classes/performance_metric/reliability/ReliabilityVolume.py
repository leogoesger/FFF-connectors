from utils.time_series_conversion import date_to_offset_julian


class ReliabilityVolume:
    """Calculate reliability volumne

       Sum of all daily suitable area values over water year (scenario)  / sum all _median_ daily suitable area values over water year (reference) in a given bioperiod
    """

    def __init__(self, datasets, inputs):
        self.datasets = datasets
        self.inputs = inputs
        self.limits = {}
        self.reliability_volumne = []

    def calculate_reliability_volume(self):
        for dataset in self.datasets:
            self.reliability_volumne.append(
                {"file_name": dataset.file_name, "volume": {}})
            for func, value in dataset["optimal"]:
                start = date_to_offset_julian(
                    self.inputs[func]["bioperiod_start_date"]+"/2000", "10/01")
                end = date_to_offset_julian(
                    self.inputs[func]["bioperiod_end_date"]+"/2000", "10/01")

                sum_scenario = sum(
                    dataset["scenarios"][func]["magnitude"][start:end])
                sum_optimal = sum([d["50th"]
                                   for d in value["percentiles"]][start:end])

                self.reliability_volumne[-1]["volume"] = sum_scenario / sum_optimal
