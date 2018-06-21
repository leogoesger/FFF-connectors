from os import sys, listdir, path
import inquirer
import rasterio

from utils.helpers import will_it_float
from calculations.reclassify_raster import reclassify_raster


class ConditionalFunc:
    def __init__(self, spatial_bounding):
        self.spatial_bounding = spatial_bounding
        self.hydrologic_variable = ''
        self.binning = []
        self.functional_bin = None
        self.reclassified_rasters = {}
        self.get_user_inputs()
        self.reclassify_raster()

    def get_user_inputs(self):
        # inquirer questions for hydrologic_variable, binning, and functional_bin
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

            inquirer.Text('functional_bin',
                          message="Input functional bin number. Example: 0 or 1",
                          validate=lambda _, d: will_it_float(d)),
        ]

        answers = inquirer.prompt(questions)
        # parse answers to desired values
        self.hydrologic_variable = answers['hydrologic_variable'][0]
        self.binning = [float(x.strip())
                        for x in answers['binning'].split(',')]
        self.functional_bin = int(answers['functional_bin'])

    def reclassify_raster(self):
        # inspect all raw files and reclassify ones match

        for file in listdir("raw"):
            file_info = path.splitext(file)[0].split('_')

            # check to see file name has the same hydro variable and spatial bounding
            if(file_info[2] == self.hydrologic_variable and
                    file_info[3] == self.spatial_bounding):

                with rasterio.open("raw/{}".format(file)) as src:
                    # rasterio open the file and save each raster as a key/value pair
                    self.reclassified_rasters[path.splitext(file)[0]] = reclassify_raster(
                        src.read()[0], self.binning)
