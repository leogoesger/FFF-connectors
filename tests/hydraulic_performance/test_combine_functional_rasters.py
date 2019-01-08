from os import sys, path
import unittest
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from calculations.hydraulic_suitability.combine_functional_rasters import combine_functional_rasters, zip_and_compare


class TestGetFunctionalRasterMethods(unittest.TestCase):

    def test_combine_functional_rasters_general_case(self):
        spatial_boundary = ''
        raster_collection = [{'T6_5_v_': [[True, False, True], [False, True, False]],
                              'T6_6_v_': [[True, False, True], [False, True, True]]},
                             {'T6_5_d_': [[True, True, False], [False, True, False]],
                              'T6_6_d_': [[False, False, True], [True, True, False]]}]
        expected = {'T6_5_X_': [True, False, False, False, True, False],
                    'T6_6_X_': [False, False, True, False, True, False]}

        self.assertEqual(combine_functional_rasters(
            raster_collection, spatial_boundary, "All"), expected)

    def test_zip_and_compare_general_case(self):
        list_a = [True, False, True]
        list_b = [True, True, False]
        sol = [True, False, False]

        self.assertEqual(zip_and_compare(
            list_a, list_b, "All"), sol)


if __name__ == '__main__':
    unittest.main()
