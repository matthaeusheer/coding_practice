import unittest

from data_structures.linked_list import LinkedList, ll_to_list
from cracking_coding_interview import chapter_2 as ch2
from tests.test_utils import run_sub_tests


class TestChapter2(unittest.TestCase):
    def test_exc1_remove_dups(self):
        input_lists = [[2, 3, 3, 4, 5, 6, 6],
                       [],
                       [1, 1],
                       [1],
                       [1, 1, 1]]
        expected_outputs = [[2, 3, 4, 5, 6],
                            [],
                            [1],
                            [1],
                            [1]]
        input_linked_lists = [LinkedList.from_list(list_) for list_ in input_lists]

        for func_to_test in [ch2.exc1_remove_dups, ch2.exc1_remove_dups_no_buffer, ch2.exc1_remove_dups_variant]:
            run_sub_tests(self, func_to_test, input_linked_lists, expected_outputs, apply_to_out=ll_to_list)

    def test_exc2_return_kth_to_last(self):
        inputs = [([1, 2, 3, 4], 2),
                  ([1], 1),
                  ([1, 2, 3], 3)]
        outputs = [[2, 3, 4],
                   [1],
                   [3]]
        input_linked_lists = [(LinkedList.from_list(list_), k) for list_, k in inputs]

        run_sub_tests(self, ch2.exc2_return_kth_to_last_first, input_linked_lists, outputs, apply_to_out=ll_to_list)

    def test_exc3_delete_middle_node(self):
        input_list = [1, 2, 3, 4]
        linked_list = LinkedList.from_list(input_list)
        node = linked_list.head.next.next  # Node representing 3
        expected_result = [1, 2, 4]
        ch2.exc3_delete_middle_node(node)
        self.assertEqual(expected_result, linked_list.to_list())

    def test_exc4_partition(self):
        inputs = [([1, 2, 3, 4], 2),
                  ([1], 1),
                  ([1, 2, 3], 3)]
        outputs = [[2, 3, 4],
                   [1],
                   [3]]