from calculations.hydraulic_suitability_scenario.calculate_binning import calculate_binning


class OptimalBinning:
    def __init__(self, user_inputs, dataset):
        self.user_inputs = user_inputs
        self.dataset = dataset

        self.binnings = {}
        self.get_bins()

    def get_bins(self):
        for func_key in self.dataset["optimal"]:
            if "binnings" in self.user_inputs[func_key]:
                array_of_percentiles = self.dataset["optimal"][func_key]["percentiles"]
                bins = self.user_inputs[func_key]["binnings"]

                self.binnings[func_key] = self.get_opt_ary_binnings(
                    array_of_percentiles, bins)

    def get_opt_ary_binnings(self, opt_ary, bins):
        binned_opt_ary = []
        for dic in opt_ary:
            binned_opt_ary.append({})
            for key, value in dic.items():
                binned_opt_ary[-1][key] = calculate_binning(value, bins)
        return binned_opt_ary
