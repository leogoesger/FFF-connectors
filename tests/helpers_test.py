from os import sys, path
import unittest
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from utils.helpers import flatten_list, will_it_float


class TestHelperMethods(unittest.TestCase):

    def test_flatten_list(self):
        test_case_1 = [[0, 1, 2, 0], [1, 2, 3, 0]]
        solu_case_1 = [0, 1, 2, 0, 1, 2, 3, 0]

        self.assertEqual(flatten_list(
            test_case_1), solu_case_1)

    def test_will_it_float_string(self):
        test_case_1 = 'string'

        self.assertEqual(will_it_float(
            test_case_1), False)

    def test_will_it_float_int(self):
        test_case_1 = '12'

        self.assertEqual(will_it_float(
            test_case_1), True)

    def test_will_it_float_float(self):
        test_case_1 = '12.2'

        self.assertEqual(will_it_float(
            test_case_1), True)


if __name__ == '__main__':
    unittest.main()
