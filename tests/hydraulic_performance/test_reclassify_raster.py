from os import sys, path
import unittest
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from calculations.hydraulic_performance.reclassify_raster import map_column_to_binning, reclassify_raster


class TestReclassifyRasterMethods(unittest.TestCase):

    def test_lower_bound(self):
        self.assertEqual(map_column_to_binning(0, [0, 1, 1.5]), 1)

    def test_lower(self):
        self.assertEqual(map_column_to_binning(-1.1, [0, 1, 1.5]), 0)

    def test_middle(self):
        self.assertEqual(map_column_to_binning(1.1, [0, 1, 1.5]), 2)

    def test_upper(self):
        self.assertEqual(map_column_to_binning(2.1, [0, 1, 1.5]), 3)

    def test_upper_bound(self):
        self.assertEqual(map_column_to_binning(1.5, [0, 1, 1.5]), 3)

    def test_classify_raster(self):
        self.assertEqual(reclassify_raster(
            [[-1, 0, 0.5], [1, 1.5, 2]], [0, 1, 2]), [[0, 1, 1], [2, 2, 3]])


if __name__ == '__main__':
    unittest.main()
