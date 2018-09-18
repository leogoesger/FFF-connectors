class MetricRow:
    def __init__(self, data, years, startY, endY, file_name):
        self.data = data
        self.year = int(years[1])
        self.startY = startY
        self.endY = endY
        self.file_name = file_name[:8]

    def get_new_row(self):
        number_of_filler = self.startY - self.year
        filler_array = [None for i in range(number_of_filler)]
        return [self.file_name, *filler_array, *self.data[1:]]
