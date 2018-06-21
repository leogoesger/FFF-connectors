from os import sys, listdir, path
import inquirer
import rasterio

from utils.helpers import will_it_float
from calculations.reclassify_raster import reclassify_raster
from calculations.get_functional_rasters import get_functional_rasters


class ConditionalFunc:
    def __init__(self, spatial_boundary):
        self.spatial_boundary = spatial_boundary
        self.hydrologic_variable = ''
        self.binning = []
        self.functional_bin_number = None
        self.binned_rasters = {}
        self.functional_rasters = {}
        self.get_user_inputs()
        self.reclassify_rasters()
        self.get_functional_rasters()

    def get_user_inputs(self):
        # inquirer questions for hydrologic_variable, binning, and functional_bin_number
        print('')
        questions = [
            inquirer.List('hydrologic_variable',
                          message="Which hydrologic variable?",
                          choices=['d: depth', 'v: velocity',
                                   't: shear stress'],
                          ),
            inquirer.Text('binning',
                          message="Define the binning. Example: 1.2, 2.1 ",
                          validate=lambda _, d: d is not ''),

            inquirer.Text('functional_bin_number',
                          message="Input functional bin number. Example: 0 or 1",
                          validate=lambda _, d: will_it_float(d)),
        ]

        answers = inquirer.prompt(questions)
        # parse answers to desired values
        self.hydrologic_variable = answers['hydrologic_variable'][0]
        self.binning = [float(x.strip())
                        for x in answers['binning'].split(',')]
        self.functional_bin_number = int(answers['functional_bin_number'])

    def reclassify_rasters(self):
        # inspect all raw files and reclassify ones match
        for file in listdir("raw"):
            file_info = path.splitext(file)[0].split('_')

            # check to see file name has the same hydro variable and spatial bounding
            if(file_info[2] == self.hydrologic_variable and
                    file_info[3] == self.spatial_boundary):

                with rasterio.open("raw/{}".format(file)) as src:
                    # rasterio open the file and save each raster as a key/value pair
                    self.binned_rasters[path.splitext(file)[0]] = reclassify_raster(
                        src.read()[0], self.binning)

    def get_functional_rasters(self):
        # This converts reclassifiy raster from [0,1,2 ...] to [False, True, False ...] if bin number == 1
        self.functional_rasters = get_functional_rasters(
            self.binned_rasters, self.functional_bin_number)
