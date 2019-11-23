import unittest
from functools import partial

from tests.test_utils import run_sub_tests
from algorithms.search import \
    binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        inputs = [[1, 2, 3, 4, 5],
                  [],
                  [1],
                  [1, 2]]
        test_values = [[1, 2, 5, 10],
                       [1],
                       [1, 2],
                       [1, 2, 5]]
        solutions = [[True, True, True, False],
                     [False],
                     [True, False],
                     [True, True, False]]

        for idx, (in_arr, test_items, solutions) in enumerate(zip(inputs, test_values, solutions)):
            print(f'------- test number {idx} ----------')
            print(f'input:      {in_arr}')
            print(f'test_vals:  {test_items}')
            print(f'solutions:  {solutions}')
            partial_view = partial(binary_search, in_arr)
            partial_view.__name__ = f'binary_search_{idx}'

            def divider():
                print(f'--- Sub test: {idx}')
            run_sub_tests(self, partial_view, test_items, solutions, sub_test_print_divide=divider)
