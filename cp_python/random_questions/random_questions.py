import unittest


def add_one_to_digit_list(digits):
    """You are given a list of digits where each entry is an integer from 0 to 9.
    If you think of the digits representing a number when one would write out the number those digits make up,
    write a function that returns a list of digits which represents a number one higher than the number represented
    by the input list.

    Proposed solution complexity:
        Time O(n)  - O(n) for list traversal and O(n) for possible insertion worst case, len and set val are O(1) ops.
        Space O(1) - No additional space required.
    """
    carry_over = 1
    idx = len(digits) - 1
    while idx >= 0:
        summed = digits[idx] + carry_over
        if summed == 10:
            carry_over = 1
        else:
            carry_over = 0
        digits[idx] = summed % 10
        idx -= 1
    if carry_over == 1:
        digits.insert(0, 1)
    return digits


class TestQuestions(unittest.TestCase):
    def test_add_to_digit_list(self):
        test_cases = [([1, 2, 3, 4], [1, 2, 3, 5]),
                      ([4, 3, 9, 9], [4, 4, 0, 0]),
                      ([9, 9, 9],    [1, 0, 0, 0]),
                      ([1],          [2])]

        for test_idx, (digits, solution) in enumerate(test_cases):
            with self.subTest(test_idx=test_idx):
                self.assertEqual(solution, add_one_to_digit_list(digits))
