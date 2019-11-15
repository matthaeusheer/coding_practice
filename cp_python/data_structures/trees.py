from typing import List, Generator, Callable


#########################################
#                                       #
#   Generic Trees.                      #
#                                       #
#########################################

class Node:
    def __init__(self, data, children: List = None):
        self.data = data
        self.children = children


#########################################
#                                       #
#   Binary Trees.                       #
#                                       #
#########################################

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


def bin_traverse_in_order(node: BinaryTreeNode) -> Generator:
    """Traversal scheme: Traverse left, then current, then right."""
    if node.left:
        yield from bin_traverse_in_order(node.left)
    yield node.data
    if node.right:
        yield from bin_traverse_in_order(node.right)


def bin_traverse_pre_order(node: BinaryTreeNode) -> Generator:
    """Traversal scheme: Traverse current, then left, then right."""
    yield node.data
    if node.left:
        yield from bin_traverse_pre_order(node.left)
    if node.right:
        yield from bin_traverse_pre_order(node.right)


def bin_traverse_post_order(node: BinaryTreeNode) -> Generator:
    """Traversal scheme: Traverse left, then right, then current."""
    if node.left:
        yield from bin_traverse_post_order(node.left)
    if node.right:
        yield from bin_traverse_post_order(node.right)
    yield node.data


def print_bin_traversal(node: BinaryTreeNode, traverse_func: Callable) -> None:
    print(f'Traversing with {traverse_func.__name__}...')
    for idx, item in enumerate(traverse_func(node)):
        print(f'{idx:>5}: {item}')
    print()


#########################################
#                                       #
#   Binary Search Trees.                #
#                                       #
#########################################

class BinarySearchTreeNode(BinaryTreeNode):
    def __init__(self, data, left=None, right=None) -> None:
        super().__init__(data, left, right)

    def insert(self, new_data) -> None:
        if new_data <= self.data:
            if not self.left:
                self.left = BinarySearchTreeNode(new_data)
            else:
                self.left.insert(new_data)
        else:
            if not self.right:
                self.right = BinarySearchTreeNode(new_data)
            else:
                self.right.insert(new_data)

    def contains(self, lookup_data) -> bool:
        if self.data == lookup_data:
            return True
        elif lookup_data < self.data:
            if not self.left:
                return False
            else:
                return self.left.contains(lookup_data)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(lookup_data)

    def print(self):
        """In a binary search tree, by definition, in-order traverse will print the elements in order."""
        for value in bin_traverse_in_order(self):
            print(value)


#########################################
#                                       #
#   Binary Heaps.                       #
#                                       #
#########################################

class HeapNode(BinaryTreeNode):
    raise NotImplementedError