from os import listdir, path

from classes.suitability_timeseries.Interpolation import Interpolation
from classes.suitability_timeseries.GaugeSuitability import GaugeSuitability
from utils.helpers import read_csv_to_arrays


class SuitabilityTSMain:
    input_TS_files = 'files_input/hydraulic_suitability_TS'
    output_TS_folder = 'files_output/hydraulic_suitability_TS'

    def __init__(self):
        self.something = None
        self.interpolations = None
        self.flow_bins = None

        # functions
        self.get_interpolation_funcs()
        self.generate_suitability_TS()

    def get_interpolation_funcs(self):
        interpolat = Interpolation()
        self.interpolations = interpolat.interpolations
        self.flow_bins = interpolat.flow_bins

    def generate_suitability_TS(self):
        print("Processing...")
        for file in listdir(self.input_TS_files):
            if(path.splitext(file)[1] == '.csv'):
                print(file)
                csv_arrays = read_csv_to_arrays('{}/{}'.format
                                                (self.input_TS_files, file))
                GaugeSuitability(csv_arrays, self.interpolations, self.flow_bins,
                                 self.output_TS_folder, path.splitext(file)[0])
        print("")
