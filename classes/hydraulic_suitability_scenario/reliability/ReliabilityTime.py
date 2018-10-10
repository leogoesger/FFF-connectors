class ReliabilityTime:
    def __init__(self, datasets, inputs, limits):
        self.count = 0
        self.datasets = datasets
        self.inputs = inputs
        self.limit_l = limits['limit_l']
        self.limit_r = limits['limit_r']
