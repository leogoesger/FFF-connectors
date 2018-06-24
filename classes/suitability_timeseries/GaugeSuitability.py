from utils.helpers import write_arrays_to_csv, will_it_float


class GaugeSuitability:

    def __init__(self, time_series, interpolation, output_TS_folder, gauge_name):
        self.time_series = time_series
        self.interpolation = interpolation
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
                    self.suitability_TS[key].append([el(float(row[1])).tolist()
                                                     for el in self.interpolation[key]])
                    self.combined[key].append(
                        [*row, *self.suitability_TS[key][-1]])
                else:
                    self.suitability_TS[key].append(row)
                    self.combined[key].append(row)

    def filter_output(self):
        for key in self.combined:
            for (index, el) in enumerate(self.combined[key]):
                if(index > 0):
                    self.combined[key][index] = [
                        round(float(d), 2) if will_it_float(d) else d for d in el]

    def output_to_csv(self):
        self.filter_output()
        for key in self.combined:
            write_arrays_to_csv(self.combined[key],
                                '{}/{}_{}.csv'.format(
                                    self.output_TS_folder, key, self.gauge_name))
