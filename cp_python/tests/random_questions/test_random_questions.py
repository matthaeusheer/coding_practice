import unittest

from random_questions.random_questions import add_one_to_digit_list
from random_questions.random_questions import reverse_linked_list, reverse_linked_list_2
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
