from calculations.performance_metrics.calculate_resilience import get_comparision_array, get_recorvery_days, get_deficit_days
from utils.helpers import write_single_dict_to_csv


class Resilience:
    """ Calculate Volunerability by comparing optimal with senario

    Step 1: Check each senario value whether it falls within limits, if it does then 0, otherwise the difference

    Step 2: Count the recorvery dates by counting the zero that is following non zero number

    Step 3: Count all the days in step 1 that is not a zero

    Step 4: Count from step two divide count from step three


    limits: {
              func_0: {
                  lower_limit: string
                  upper_limit: string
              }
          }

    user_inputs: {
            fun_0: {
              bioperiod_start_date: string, 
              bioperiod_end_date: string, 
            }

    Returns:
    resilience: [value] 
           value: {
               file_name: string
               value: {
                   func0: float
                   func1: float
               }
    """

    def __init__(self, limits, inputs, datasets):
        self.limits = limits  # limits gives the lower and upper bound for each function
        self.inputs = inputs  # inputs gives the bioperiod start and end dates
        self.datasets = datasets
        self.resilience = []

        self.calc_resilience()
        self.save_csv()

    def calc_resilience(self):
        """ Loop through all the database, and in each dataset loop through function

        """

        for dataset in self.datasets:
            value = {}
            for func in self.inputs:

                scenario_matrix = dataset['scenarios'][func]['magnitude']
                percentile_matrix = dataset['optimal'][func]['percentiles']

                # Step 1
                senario_compare_opt = get_comparision_array(
                    {'scenario': scenario_matrix, 'percentile': percentile_matrix}, self.limits[func], self.inputs[func])
                # Step 2
                recorvery_days = get_recorvery_days(senario_compare_opt)
                # Step 3
                deficit_days = get_deficit_days(senario_compare_opt)

                value.update({func: recorvery_days / deficit_days})

            self.resilience.append(
                {'file_name': dataset['file_name'], 'value': value})

    def save_csv(self):
        folder_path = "files_output/performance_metrics/"

        for data in self.resilience:
            file_path = folder_path + \
                data["file_name"] + "_performance.csv"
            write_single_dict_to_csv(data['value'], file_path, 'a')
