from utils.helpers import write_arrays_to_csv, will_it_float
from calculations.suitability_timeseries.get_func_suitability import get_func_suitability


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
                # row is an array with date and flow value
                if row_num > 0:
                    self.suitability_TS[key].append(
                        get_func_suitability(self.interpolation, key, row, self.flow_bins))
                    self.combined[key].append(
                        [*row, *self.suitability_TS[key][-1]])
                else:
                    self.suitability_TS[key].append(row)
                    self.combined[key].append(row)

    def output_to_csv(self):
        for key in self.combined:
            write_arrays_to_csv(self.combined[key],
                                '{}/{}_{}.csv'.format(
                                    self.output_TS_folder, key, self.gauge_name))
