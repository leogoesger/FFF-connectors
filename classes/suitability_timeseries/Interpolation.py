import csv
from os import path, listdir
import scipy.interpolate as ip

from utils.constants import CWHITE, CREDBG, CEND
from utils.helpers import read_csv_to_arrays, flatten_list

# Interpolation class will read data from flow_bins and suitability_table and
# generate one interpolation function for each flow_bins file


class Interpolation:
    def __init__(self):
        self.flow_bins_folder = 'files_input/hydraulic_suitability_TS/flow_bins'
        self.suitability_file = 'files_input/hydraulic_suitability_TS/suitability_table/performance_table.csv'
        self.interpolations = []  # handle multiple functions
        self.flow_bins = {}
        self.suitability_tables = []  # handle multiple functions
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
        arr = []
        for _ in range(len(csv_arrays[0]) - 1):
            arr.append({})
            for key in self.flow_bins:
                arr[-1][key[:2]] = [None for i in self.flow_bins[key]]

        # Fill in the data
        for block in csv_arrays:
            for index, el in enumerate(block):
                if index > 0:
                    func_num = index-1
                    key = block[0][:2]  # 'T6_4' -> 'T6'
                    velocity = int(block[0][-1]) - 1  # 'T6_4' -> '4'
                    arr[func_num][key][velocity] = float(el)

        self.suitability_tables = arr

    def validation(self, suitability_counts):
        flow_bins_counts = len(flatten_list(list(self.flow_bins.values())))
        if suitability_counts != flow_bins_counts:
            print("")
            print(CWHITE + CREDBG +
                  'Suitability table({}) and Flow bins({}) do not match!'
                  .format(flow_bins_counts, suitability_counts) + CEND)
            print("")
            exit()

    def get_interpolation_func(self):
        for perf_func in self.suitability_tables:
            self.interpolations.append({})
            for key in perf_func:
                self.interpolations[-1][key] = (ip.UnivariateSpline(
                    self.flow_bins[key], perf_func[key], k=3, s=3))


def extract_data_from_flow_bins(csv_arrays):
    return list(map(lambda row: row[1], csv_arrays))
