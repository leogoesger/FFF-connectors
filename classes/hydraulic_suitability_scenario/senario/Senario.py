from calculations.hydraulic_suitability_scenario.calculate_binning import get_binings_array


class Senario:
    """This determines whether 
    we use magnitude or bins
    """

    def __init__(self, dataset, user_input):
        self.dataset = dataset
        self.user_input = user_input
        self.num_of_funcs = len(self.dataset[0]) - 2
        self.binned_indexes = []  # array of index of columns that needs binning

        self.scenarios = {}
        for i in range(self.num_of_funcs):
            self.scenarios["func_" +
                           str(i)] = {"date_array": [], "magnitude": []}

        self.get_scenario_data()
        self.get_binnings()

    def get_scenario_data(self):
        for row in self.dataset:
            for i in range(self.num_of_funcs):
                self.scenarios["func_" + str(i)]["date_array"].append(row[0])
                self.scenarios["func_" +
                               str(i)]["magnitude"].append(row[i + 1])

    def get_binnings(self):
        for key, value in self.user_input.items():
            if "binnings" in value:
                self.scenarios[key]["binnings"] = get_binings_array(
                    self.scenarios[key]["magnitude"], value["binnings"])
