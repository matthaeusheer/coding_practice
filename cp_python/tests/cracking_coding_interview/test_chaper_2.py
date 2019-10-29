import unittest

from data_structures.linked_list import LinkedList
from cracking_coding_interview import chapter_2 as ch2
from tests.test_utils import run_sub_tests


class TestChapter2(unittest.TestCase):
    def test_exc1_remove_dups(self):
        input_lists = [[2, 3, 3, 4, 5, 6, 6],
                       [],
                       [1, 1],
                       [1],
                       [1, 1, 1]]
        input_linked_lists = [LinkedList.from_list(l) for l in input_lists]
        expected_outputs = [[2, 3, 4, 5, 6],
                            [],
                            [1],
                            [1],
                            [1]]

        for func_to_test in [ch2.exc1_remove_dups, ch2.exc1_remove_dups_no_buffer, ch2.exc1_remove_dups_variant]:
            for idx, (input_list, expected_output) in enumerate(zip(input_linked_lists, expected_outputs)):
                with self.subTest(sub_test=f'Func: {func_to_test.__name__}, '
                                           f'test_idx: {idx}'):
                    self.assertEqual(expected_output, func_to_test(input_list).to_list())
