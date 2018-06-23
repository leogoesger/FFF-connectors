class GaugeSuitability:

    def __init__(self, flow_bin, time_series):
        # {T5: [100, 200, 300]}
        self.flow_bin = flow_bin
        self.time_series = time_series

    def calculate_suitability(self):
        for flow_data in self.time_series:
            print(flow_data)
            next
