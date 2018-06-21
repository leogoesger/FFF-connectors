import inquirer

from utils.constants import CVIOLET, CEND
from utils.helpers import write_dict_to_csv
from classes.hydraulic_performance.PerformanceFunc import PerformanceFunc


class PerformanceMain:
    def __init__(self):
        self.add_performance_function_status = True
        self.performance_count_collection = []
        self.get_overview_information()
        self.add_performance_function()
        self.write_dict_to_csv()

    def get_overview_information(self):
        print("")
        print(CVIOLET + "Calculate performance table from a set of input params."+CEND)
        print("")

    def update_add_status(self):
        print("")
        print(CVIOLET + "Performance function added!"+CEND)
        print("")

        question = [
            inquirer.List('add_performance_function_status',
                          message="Add another performance function?",
                          choices=["Yes", "No"]
                          ),
        ]

        self.add_performance_function_status = inquirer.prompt(
            question)['add_performance_function_status'] == 'Yes'

    def add_performance_function(self):
        while (self.add_performance_function_status):
            self.performance_count_collection.append(
                PerformanceFunc().performance_counts)
            self.update_add_status()

    def write_dict_to_csv(self):
        write_dict_to_csv(self.performance_count_collection,
                          'calc-result/performance_table.csv')
