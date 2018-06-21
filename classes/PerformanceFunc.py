import inquirer

from classes.ConditionalFunc import ConditionalFunc
from utils.constants import CVIOLET, CEND
from calculations.combine_functional_rasters import combine_functional_rasters


class PerformanceFunc:
    def __init__(self):
        self.raster_collection = []
        self.spatial_boundary = ''
        self.adding_conditional_status = True
        self.get_user_input()
        self.add_conditional_function()

    def get_user_input(self):
      # Spatial Boundary Input
        questions = [
            inquirer.List('hydrologic_variable',
                          message="What is the spatial boundary?",
                          choices=[" : entire", 'f: floodplain',
                                   'c: bankful channel'],
                          ),
        ]

        spatial_boundary = inquirer.prompt(
            questions)['hydrologic_variable'][0]
        self.spatial_boundary = (
            '' if spatial_boundary == ' ' else spatial_boundary)

    def print_added_function(self, conditional_function):
        print("")
        print(
            CVIOLET + "One conditional function added with the following parmeters:" + CEND)
        print(" * hydrologic_variable: {}".format(
            conditional_function.hydrologic_variable))
        print(" * binning: {}".format(conditional_function.binning))
        print(" * functional_bin: {}".format(
            conditional_function.functional_bin_number))
        print("")

    def update_adding_conditional_status(self):
        # Input for whether to continue adding conditional functions
        questions = [
            inquirer.List('adding_conditional_status',
                          message="Add conditional functions?",
                          choices=['Yes', 'No'],
                          ),
        ]

        self.adding_conditional_status = inquirer.prompt(
            questions)['adding_conditional_status'] == 'Yes'

    def add_conditional_function(self):
        # add more conditional functions
        while self.adding_conditional_status:
            conditional_function = ConditionalFunc(self.spatial_boundary)
            self.raster_collection.append(
                conditional_function)
            self.print_added_function(
                conditional_function)  # print added function
            self.update_adding_conditional_status()

    def combine_functional_rasters(self):
        combine_functional_rasters(self.raster_collection)
