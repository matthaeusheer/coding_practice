import unittest

from data_structures import trees
from tests.test_utils import run_sub_tests


class TestTreeTraversal(unittest.TestCase):
    def setUp(self) -> None:
        child121 = trees.BinaryTreeNode(data=6)
        child12 = trees.BinaryTreeNode(data=5, left=child121)
        child11 = trees.BinaryTreeNode(data=4)
        child1 = trees.BinaryTreeNode(data=2, left=child11, right=child12)
        child2 = trees.BinaryTreeNode(data=3)
        self.root = trees.BinaryTreeNode(data=1, left=child1, right=child2)

    @unittest.SkipTest
    def test_print_traversals(self) -> None:
        """Helper function without testing functionality to see tree traversal in action."""
        for func in [trees.bin_traverse_in_order, trees.bin_traverse_pre_order, trees.bin_traverse_post_order]:
            trees.print_bin_traversal(self.root, func)
    
    def test_bin_traversal_in_order(self):
        self.assertListEqual([4, 2, 6, 5, 1, 3], list(trees.bin_traverse_in_order(self.root)))

    def test_bin_traversal_pre_order(self):
        self.assertListEqual([1, 2, 4, 5, 6, 3], list(trees.bin_traverse_pre_order(self.root)))

    def test_bin_traversal_post_order(self):
        self.assertListEqual([4, 6, 5, 2, 3, 1], list(trees.bin_traverse_post_order(self.root)))


class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):
        root = trees.BinarySearchTreeNode(1)
        root.insert(5)
        root.insert(10)
        self.assertSetEqual({1, 5, 10}, set(trees.bin_traverse_in_order(root)))

    def test_contains(self):
        bst = trees.BinarySearchTreeNode(10)
        for value in [15, 20, 25, 30, 5, 8, 3]:
            bst.insert(value)
        self.assertTrue(bst.contains(10))
        self.assertTrue(bst.contains(15))
        self.assertTrue(bst.contains(30))
        self.assertFalse(bst.contains(1))
        self.assertFalse(bst.contains(11))
        self.assertFalse(bst.contains(24))

    def test_bst_traversal(self):
        bst = trees.BinarySearchTreeNode(10)
        in_values = [15, 20, 25, 30, 5, 8, 3]
        for value in in_values:
            bst.insert(value)
        self.assertListEqual(sorted(in_values + [10]), list(trees.bin_traverse_in_order(bst)))

    @unittest.SkipTest
    def test_print_value(self):
        bst = trees.BinarySearchTreeNode(10)
        for value in [15, 20, 25, 30, 5, 8, 3]:
            bst.insert(value)
        bst.print()