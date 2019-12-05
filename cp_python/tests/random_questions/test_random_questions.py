import unittest

from random_questions.random_questions import add_one_to_digit_list
from random_questions.random_questions import reverse_linked_list, reverse_linked_list_2
from random_questions.random_questions import schnecken_dist_travelled
from random_questions.random_questions import longest_range
from data_structures.linked_list import LinkedList
from tests.test_utils import run_sub_tests


class TestRandomQuestions(unittest.TestCase):
    def test_add_to_digit_list(self):
        test_cases = [([1, 2, 3, 4], [1, 2, 3, 5]),
                      ([4, 3, 9, 9], [4, 4, 0, 0]),
                      ([9, 9, 9],    [1, 0, 0, 0]),
                      ([1],          [2])]

        for test_idx, (digits, solution) in enumerate(test_cases):
            with self.subTest(test_idx=test_idx):
                self.assertEqual(solution, add_one_to_digit_list(digits))

    def test_reverse_linked_list(self):
        in_list = [1, 1, 2, 2, 3, 3, 4, 4]
        out_list = [4, 4, 3, 3, 2, 2, 1, 1]
        for func in [reverse_linked_list, reverse_linked_list_2]:
            ll_in = LinkedList.from_list(in_list)
            with self.subTest(reverse_func=func.__name__):
                run_sub_tests(self, func, [ll_in], [out_list], LinkedList.to_list)

    def test_schnecken_dist_travelled(self):
        target_coords = [(0, 1), (1, 1), (1, -1), (-1, -1), (-1, 2), (2, 2), (2, -2)]
        distances = [1, 2, 4, 6, 9, 12, 16]
        run_sub_tests(self, schnecken_dist_travelled, target_coords, distances,
                      sub_test_print_divide=lambda: print('---'))

    def test_longest_range(self):
        test_cases = [([0, 5, 2, 7, 3, -1, 1], [-1, 3]),
                      ([], [None, None]),
                      ([1], [1, 1]),
                      ([1, 1, 4, 3, 5, 9, 7, 6, 8], [3, 9])]
        for test_idx, (in_arr, solution) in enumerate(test_cases):
            with self.subTest(test_idx=test_idx):
                self.assertEqual(solution, longest_range(in_arr))

