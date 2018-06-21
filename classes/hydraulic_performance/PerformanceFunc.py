import inquirer

from classes.hydraulic_performance.ConditionalFunc import ConditionalFunc
from utils.constants import CVIOLET, CEND
from utils.helpers import count_truthy
from calculations.hydraulic_performance.combine_functional_rasters import combine_functional_rasters


class PerformanceFunc:
    def __init__(self):
        self.conditional_relationship = None
        self.raster_collection = []
        self.spatial_boundary = ''
        self.adding_conditional_status = True
        self.combined_rasters = {}
        self.performance_counts = {}
        self.get_user_input()
        self.add_conditional_function()
        self.combine_functional_rasters()
        self.create_performance_count_table()

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
        if(self.conditional_relationship):
            print(" * conditional_relationship: {}".format(self.conditional_relationship))
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
        self.get_conditional_function_relation()

    def get_conditional_function_relation(self):
        # Determins whether conditional functions has `any` or `all` relationship
        if(self.conditional_relationship is None and self.adding_conditional_status):
            questions = [
                inquirer.List('conditional_relationship',
                              message="Conditional functions' relationship?",
                              choices=['All', 'Any'],
                              ),
            ]
            self.conditional_relationship = inquirer.prompt(
                questions)['conditional_relationship']

    def add_conditional_function(self):
        # add more conditional functions
        while self.adding_conditional_status:
            conditional_function = ConditionalFunc(self.spatial_boundary)
            self.raster_collection.append(
                conditional_function.functional_rasters)
            self.print_added_function(
                conditional_function)  # print added function
            self.update_adding_conditional_status()

    def combine_functional_rasters(self):
        self.combined_rasters = combine_functional_rasters(
            self.raster_collection, self.spatial_boundary, self.conditional_relationship)

    def create_performance_count_table(self):
        for key in self.combined_rasters:
            self.performance_counts[key] = count_truthy(
                self.combined_rasters[key])
