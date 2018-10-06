from os import sys, path
import unittest
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils.time_series_conversion import TimeSeriesConversion
from tests.time_series_conversion.test_data import get_year_limits_suit, get_empty_matrix_suit, get_position_index_suit


class TestGetTimeSeriesMatrix(unittest.TestCase):

    # def test_get_year_limits(self):
    #     for test in get_year_limits_suit:
    #         conv = TimeSeriesConversion(
    #             test["date_array"], test["data_array"], test["offset_date"])
    #         conv.get_year_limits()

    #         self.assertEqual(conv.start_year, test["start_year"],
    #                          test["test_name"] + " - start year")
    #         self.assertEqual(conv.end_year, test["end_year"],
    #                          test["test_name"] + " - end year")

    # def test_get_empty_matrix(self):
    #     for test in get_empty_matrix_suit:
    #         conv = TimeSeriesConversion(
    #             test["date_array"], test["data_array"], test["offset_date"])
    #         conv.get_empty_matrix()
    #         self.assertEqual(conv.final_matrix, test["sol"])

    def test_get_position_index(self):
        for test in get_position_index_suit:
            conv = TimeSeriesConversion(
                test["date_array"], test["data_array"], test["offset_date"])
            for i, case in enumerate(test["dates"]):
                r, c = conv.get_position_index(case)
                self.assertEqual(r, test["sol"][i]["r"],
                                 test["test_name"] + " - " + case)
                self.assertEqual(c, test["sol"][i]["c"],
                                 test["test_name"] + " - " + case)


if __name__ == '__main__':
    unittest.main()
