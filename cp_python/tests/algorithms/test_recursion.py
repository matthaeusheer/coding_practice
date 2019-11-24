import unittest
from functools import partial

from ..test_utils import run_sub_tests
from algorithms.recursion import *


class TestRecursionAlgorithms(unittest.TestCase):

    def test_factorial(self):
        input_values = [1, 2, 3, 4, 5]
        solutions = [1, 2, 6, 24, 120]
        run_sub_tests(self, factorial, input_values, solutions)
        run_sub_tests(self, factorial_iterative, input_values, solutions)

    def test_fibonacci(self):
        input_values = [0, 1, 2, 3, 4, 5, 6, 7]
        solutions = [0, 1, 1, 2, 3, 5, 8, 13]
        run_sub_tests(self, fibonacci, input_values, solutions)
        run_sub_tests(self, fibonacci_iterative, input_values, solutions)
        run_sub_tests(self, fibonacci_dyn_progr, input_values, solutions)
        run_sub_tests(self, fibonacci_dyn_progr_2, input_values, solutions)

    def test_fibonacci_memo(self):
        input_values = [0, 1, 2, 3, 4, 5, 6, 7]
        solutions = [0, 1, 1, 2, 3, 5, 8, 13]
        # Caution: Do not initialize memo_init outside sub tests loop since the dict is mutable and altered when
        #          passed to fibonacci_memoization!
        for idx, (input_value, expected_solution) in enumerate(zip(input_values, solutions)):
            with self.subTest(test_case=idx):
                memo_init = {0: 1, 1: 1}
                self.assertEqual(expected_solution, fibonacci_memoization(input_value, memo_init),
                                 f'Sub test nr. {idx} failed. {fibonacci_memoization.__name__}({input_value}) '
                                 f'should be {expected_solution}.')

    @unittest.SkipTest
    def test_is_palindrome(self):
        in_values = [100, 2002, 1, 99, 999, 22122, 212, 122]
        solutions = [False, True, True, True, True, True, True, False]
        run_sub_tests(self, is_palindrome, in_values, solutions)

    def test_power(self):
        bases = [2, 3, 4, 5]
        exponents = [1, 2, 3, 4]
        solutions = [[2, 4,  8,   16],
                     [3, 9,  27,  81],
                     [4, 16, 64,  256],
                     [5, 25, 125, 625]]
        for func in [power_recursive, power_iterative]:
            for b_idx, base in enumerate(bases):
                for e_idx, exponent in enumerate(exponents):
                    with self.subTest(b=base, e=exponent):
                        self.assertEqual(solutions[b_idx][e_idx], func(base, exponent))
