import unittest
from data_structures.linked_list import LinkedList, Node


class TestLinkedListCreation(unittest.TestCase):
    def test_creation(self):
        """Calling prepend, append and insert(0, data) on empty linked list."""
        ll = LinkedList()
        self.assertEqual([], ll.to_list()), 'Linked List should be empty.'
        self.assertEqual(0, ll.size), 'Empty list should have size 0'
        # prepend
        ll.prepend(1)
        self.assertEqual([1], ll.to_list()), 'LL should have exactly one element.'
        self.assertEqual(1, ll.size), 'Should be size 1.'
        # append
        ll = LinkedList()
        ll.append(1)
        self.assertEqual([1], ll.to_list()), 'LL should have exactly one element.'
        self.assertEqual(1, ll.size), 'Should be size 1.'
        ll = LinkedList()
        # insert at zero
        ll.insert(1, 0)
        self.assertEqual([1], ll.to_list()), 'LL should have exactly one element.'
        self.assertEqual(1, ll.size), 'Should be size 1.'

    def test_from_list(self):
        input_list = [1, 2, 3, 4, 5]
        ll = LinkedList.from_list(input_list)
        self.assertEqual([1, 2, 3, 4, 5], ll.to_list())


class TestLinkedListOperations(unittest.TestCase):
    def setUp(self) -> None:
        ll = LinkedList()
        ll.prepend(5)
        ll.prepend(4)
        ll.prepend(3)
        ll.prepend(2)
        ll.prepend(1)
        self.test_list = ll

    def test_insert(self):
        self.test_list.insert(10, 1)
        self.assertEqual([1, 10, 2, 3, 4, 5], self.test_list.to_list())

    def test_append(self):
        self.test_list.append(10)
        self.assertEqual([1, 2, 3, 4, 5, 10], self.test_list.to_list())

    def test_prepend(self):
        self.test_list.prepend(10)
        self.assertEqual([10, 1, 2, 3, 4, 5], self.test_list.to_list())

    def test_remove_return(self):
        self.assertEqual(True, self.test_list.remove(3))
        self.assertEqual(False, self.test_list.remove(10))

    def test_remove_last(self):
        self.test_list.remove(5)
        self.assertEqual([1, 2, 3, 4], self.test_list.to_list())
        self.assertEqual(4, self.test_list.size)

    def test_remove_first(self):
        self.test_list.remove(1)
        self.assertEqual([2, 3, 4, 5], self.test_list.to_list())
        self.assertEqual(4, self.test_list.size)

    def test_remove(self):
        self.test_list.remove(3)
        self.assertEqual([1, 2, 4, 5], self.test_list.to_list())
        self.assertEqual(4, self.test_list.size)

    def test_search(self):
        self.assertEqual(0, self.test_list.search(1))
        self.assertEqual(-1, self.test_list.search(100))
        self.assertEqual(2, self.test_list.search(3))

    def test_search_empty(self):
        ll = LinkedList()
        self.assertEqual(-1, ll.search(1))

    def test_empty_list(self):
        ll = LinkedList(Node(data=1))
        assert ll.size == 1
