from utils.time_series_conversion import TimeSeriesConversion
from calculations.hydraulic_suitability_scenario.calculate_percentile import calculate_percentile


class OptimalPerformance:

    def __init__(self, matrix):
        self.matrix = matrix
        self.number_of_funcs = len(matrix[10]) - 2
        self.result = {}

        for i in range(self.number_of_funcs):
            self.result["func_" +
                        str(i)] = {"data_ary": [], "date_ary": [], "matrix": None, "percentiles": None}

        self.create_ts_data()
        self.create_matrix()
        self.cal_percentile()

    def create_ts_data(self):
        for row in self.matrix:
            for i in range(self.number_of_funcs):
                self.result["func_" + str(i)]["date_ary"].append(row[0])
                self.result["func_" +
                            str(i)]["data_ary"].append(float(row[i + 2]))

    def create_matrix(self):
        for i in range(self.number_of_funcs):
            date_ary = self.result["func_" + str(i)]["date_ary"]
            data_ary = self.result["func_" + str(i)]["data_ary"]

            self.result["func_" + str(i)]["matrix"] = TimeSeriesConversion(
                date_ary, data_ary, "10/01").final_matrix

    def cal_percentile(self):
        for i in range(self.number_of_funcs):
            self.result["func_" + str(i)]["percentiles"] = calculate_percentile(
                self.result["func_" + str(i)]["matrix"])
