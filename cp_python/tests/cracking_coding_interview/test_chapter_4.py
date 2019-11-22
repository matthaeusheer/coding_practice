import unittest

from cracking_coding_interview import chapter_4 as chap4


class TestExc2(unittest.TestCase):
    def test_print_tree(self):
        in_arr = [0, 1, 2, 5, 7, 10, 12]
        min_tree = chap4.exc2_minimal_tree(in_arr)
        min_tree.print()

    def test_depth(self):
        in_arr = [0, 1, 2, 5, 7, 10, 12]
        self.assertEqual(3, chap4.exc2_minimal_tree(in_arr).depth())
