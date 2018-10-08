from utils.time_series_conversion import TimeSeriesConversion
from calculations.hydraulic_suitability_scenario.calculate_percentile import calculate_percentile


class TimeSeriesPercentille:

    def __init__(self, input_dataset):
        self.input_dataset = input_dataset
        self.number_of_funcs = len(input_dataset["ts"][0]) - 2
        self.result = {}

        for i in range(self.number_of_funcs):
            self.result["func_" +
                        str(i)] = {"ts": [], "dates": [], "matrix": None, "percentiles": None}

        self.create_ts_data()
        self.create_matrix()
        self.cal_percentile()

    def create_ts_data(self):
        for row in self.input_dataset["ts"]:
            for i in range(self.number_of_funcs):
                self.result["func_" + str(i)]["dates"].append(row[0])
                self.result["func_" + str(i)]["ts"].append(float(row[i + 1]))

    def create_matrix(self):
        for i in range(self.number_of_funcs):
            date_ary = self.result["func_" + str(i)]["dates"]
            data_ary = self.result["func_" + str(i)]["ts"]

            self.result["func_" + str(i)]["matrix"] = TimeSeriesConversion(
                date_ary, data_ary, "10/01").final_matrix

    def cal_percentile(self):
        for i in range(self.number_of_funcs):
            self.result["func_" + str(i)]["percentiles"] = calculate_percentile(
                self.result["func_" + str(i)]["matrix"])
