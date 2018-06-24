from os import sys, path
import unittest
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from calculations.hydraulic_performance.get_functional_rasters import get_functional_rasters, raster_to_functional_raster


class TestGetFunctionalRasterMethods(unittest.TestCase):

    def test_get_functional_rasters_general_case(self):
        test_case_1_num = 1
        test_case_1 = {"raster_1": [[0, 1, 2, 0], [1, 2, 3, 0]],
                       "raster_2": [[1, 0, 0, 0], [1, 0, 1, 0]]}
        solu_case_1 = {"raster_1": [[False, True, False, False], [True, False, False, False]],
                       "raster_2": [[True, False, False, False], [True, False, True, False]]}

        self.assertEqual(get_functional_rasters(
            test_case_1, test_case_1_num), solu_case_1)

    def test_raster_to_functional_raster_general_case(self):
        test_case_1_num = 2
        test_case_1 = [[0, 1, 2, 0], [1, 2, 3, 0]]
        solu_case_1 = [[False, False, True, False],
                       [False, True, False, False]]

        self.assertEqual(raster_to_functional_raster(
            test_case_1, test_case_1_num), solu_case_1)


if __name__ == '__main__':
    unittest.main()
