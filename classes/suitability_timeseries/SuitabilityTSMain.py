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

        # functions
        self.get_interpolation_funcs()
        self.generate_suitability_TS()

    def get_interpolation_funcs(self):
        self.interpolations = Interpolation().interpolations

    def generate_suitability_TS(self):
        for file in listdir(self.input_TS_files):
            if(path.splitext(file)[1] == '.csv'):
                csv_arrays = read_csv_to_arrays('{}/{}'.format
                                                (self.input_TS_files, file))
                GaugeSuitability(
                    csv_arrays, self.interpolations, self.output_TS_folder, path.splitext(file)[0])
