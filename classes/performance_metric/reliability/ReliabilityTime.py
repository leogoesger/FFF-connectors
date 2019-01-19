from inquirer import prompt, List, Text
from utils.constants import CGREEN, CVIOLET, CEND
from utils.helpers import write_arrays_to_csv, transpose_csv


class ReliabilityTime:
    """Calculate reliability time for multiple datasets

       limits: {
           func_0: {
               lower_limit: string
               upper_limit: string
           }
       }

       reliability_time = [realibility]
       realibility = {
           file_name: string
           timing_status: {
               func_0: [Boolean]
           }
       }
    """

    def __init__(self, datasets, inputs):
        self.datasets = datasets
        self.inputs = inputs
        self.limits = {}
        self.reliability_time = []

        self.get_limits()
        self.get_reliability_time()
        self.save_csv()

    def get_limits(self):
        print("")
        print(CVIOLET + "Calculating reliability times" + CEND)
        print("")
        for key in self.inputs:
            lw_choices = ['min', '10th', '25th']
            up_choices = ['75th', '90th', 'max']
            question = [
                List('lower',
                     message="Lower Limit for {}?".format(key),
                     choices=lw_choices),
                List('upper',
                     message="Upper Limit for {}?".format(key),
                     choices=up_choices),
            ]

            answers = prompt(question)
            self.limits[key] = {}
            self.limits[key]["lower_limit"] = answers['lower']
            self.limits[key]["upper_limit"] = answers['upper']

    def get_reliability_time(self):
        for dataset in self.datasets:
            self.reliability_time.append(
                {"file_name": dataset["file_name"], "timing_status": {}})
            # import pdb
            # pdb.set_trace()
            for func_key, value in dataset["scenarios"].items():
                self.reliability_time[-1]["timing_status"][func_key] = []

                scen_key = "binnings" if "binnings" in self.limits[func_key] else "magnitude"
                opt_key = "binnings" if "binnings" in self.limits[func_key] else "percentiles"

                scen_array = value[scen_key]
                opt_array = dataset["optimal"][func_key][opt_key]

                lower_key = self.limits[func_key]['lower_limit']
                upper_key = self.limits[func_key]['upper_limit']

                self.reliability_time[-1]["timing_status"][func_key] = [True if float(scen_val) >= opt_array[index][lower_key] and float(
                    scen_val) <= opt_array[index][upper_key] else False for index, scen_val in enumerate(scen_array)]

    def save_csv(self):
        folder_path = "files_output/performance_metrics/"

        for data in self.reliability_time:
            file_path = folder_path + \
                data["file_name"] + "_performance.csv"
            d = []
            for _, value in data["timing_status"].items():
                d.append(value)
            write_arrays_to_csv(d, file_path, 'a')
            transpose_csv(file_path)
