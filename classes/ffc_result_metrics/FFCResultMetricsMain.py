import os
import csv
from classes.ffc_result_metrics.static import metric_names
from classes.ffc_result_metrics.MetricRow import MetricRow


class FFCResultMetricsMain:
    def __init__(self):
        self.input_path = "files_input/ffc_result_metrics"
        self.output_path = "files_output/ffc_result_metrics"
        self.start_year = 1900
        self.end_year = 2018
        self.result_dict = {}
        self.generate_empty_result_dict()
        self.get_result_row()
        self.get_result_csv()

    def generate_empty_result_dict(self):
        for metric in metric_names:
            self.result_dict[metric] = []

    def get_result_row(self):
        for file_name in os.listdir(self.input_path):
            current_file_year = []
            with open(os.path.join(self.input_path, file_name), "r") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for index, row in enumerate(reader):
                    if index == 0:
                        current_file_year = row
                    else:
                        metric_row = MetricRow(
                            row, current_file_year, self.start_year, self.end_year, file_name)

                        self.result_dict[row[0]].append(
                            metric_row.get_new_row())

    def get_result_csv(self):
        for metric in metric_names:
            with open("{}/{}.csv".format(self.output_path, metric), "w") as f:
                writer = csv.writer(f)
                writer.writerows(
                    [["gauge", "class", *[self.start_year + i for i in range(self.end_year + 1 - self.start_year)]], *self.result_dict[metric]])
