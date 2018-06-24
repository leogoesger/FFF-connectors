from utils.helpers import write_arrays_to_csv, will_it_float


class GaugeSuitability:

    def __init__(self, time_series, interpolation, flow_bins, output_TS_folder, gauge_name):
        self.time_series = time_series
        self.interpolation = interpolation
        self.flow_bins = flow_bins
        self.output_TS_folder = output_TS_folder
        self.gauge_name = gauge_name
        self.suitability_TS = {}
        self.combined = {}

        # functions
        self.calculate_suitability()
        self.output_to_csv()

    def calculate_suitability(self):
        for key in self.interpolation:
            self.suitability_TS[key] = []
            self.combined[key] = []
            for row_num, row in enumerate(self.time_series):
                if row_num > 0:
                    self.suitability_TS[key].append(
                        self.get_func_suitability(key, row))

                    self.combined[key].append(
                        [*row, *self.suitability_TS[key][-1]])
                else:
                    self.suitability_TS[key].append(row)
                    self.combined[key].append(row)

    def get_func_suitability(self, key, row):
        new_array = []
        for perc_func in self.interpolation[key]:
            ele = perc_func(float(row[1])).tolist()
            if ele < 0:  # if the value is below 0 from ip func
                new_array.append(0)
            # if value is greater than max(flow_bin)
            elif float(row[1]) > self.flow_bins[key][-1]:
                new_array.append(
                    round(perc_func(self.flow_bins[key][-1]).tolist(), 2))
            else:
                new_array.append(round(ele, 2))
        return new_array

    def output_to_csv(self):
        for key in self.combined:
            write_arrays_to_csv(self.combined[key],
                                '{}/{}_{}.csv'.format(
                                    self.output_TS_folder, key, self.gauge_name))
