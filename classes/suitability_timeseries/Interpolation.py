import csv
from os import path, listdir
import scipy.interpolate as ip

from calculations.suitability_timeseries.get_suitability_table import get_suitability_table
from utils.constants import CWHITE, CREDBG, CEND
from utils.helpers import read_csv_to_arrays, flatten_list

# Interpolation class will read data from flow_bins and suitability_table and
# generate one interpolation function for each flow_bins file.
# Out interpolation dict has the following format:
# {T5: [ip1, ip2], T6: [ip1, ip2]}


class Interpolation:
    def __init__(self):
        self.flow_bins_folder = 'files_input/hydraulic_suitability_TS/flow_bins'
        self.suitability_file = 'files_input/hydraulic_suitability_TS/suitability_table/performance_table.csv'
        self.interpolations = {}  # handle multiple functions
        self.flow_bins = {}
        self.suitability_tables = []  # handle multiple functions

        # function calls
        self.read_flow_bins()
        self.read_suitability_table()
        self.get_interpolation_func()

    def read_flow_bins(self):
        for file in listdir(self.flow_bins_folder):
            # remove all files not end with csv
            split_file = path.splitext(file)
            if not (split_file[1] == '.csv'):
                continue

            csv_arrays = read_csv_to_arrays(
                '{}/{}'.format(self.flow_bins_folder, file), True)
            self.flow_bins[split_file[0][:2]] = [float(i) for i in
                                                 extract_data_from_flow_bins(csv_arrays)]

    def read_suitability_table(self):
        csv_arrays = read_csv_to_arrays(self.suitability_file, False)
        self.validation(len(csv_arrays))

        # This will create a general outline as following:
        # [{T5: [], T6: []}, {T5: [], T6: []}]
        self.suitability_tables = get_suitability_table(
            csv_arrays, self.flow_bins)

    def validation(self, suitability_counts):
        flow_bins_counts = len(flatten_list(list(self.flow_bins.values())))
        if suitability_counts != flow_bins_counts:
            print("")
            print(CWHITE + CREDBG +
                  'Suitability table({}) and Flow bins({}) do not match!'
                  .format(flow_bins_counts, suitability_counts) + CEND)
            print("Check flow bins' input files!")
            print("")
            exit()

    def get_interpolation_func(self):
        for key in self.suitability_tables[0]:
            self.interpolations[key] = []
            for perf_func in self.suitability_tables:
                self.interpolations[key].append(ip.interp1d(
                    self.flow_bins[key], perf_func[key], kind="quadratic"))


def extract_data_from_flow_bins(csv_arrays):
    return list(map(lambda row: row[1], csv_arrays))
