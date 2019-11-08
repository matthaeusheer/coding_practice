import unittest
from data_structures.stack import Stack
from data_structures.stack import EmptyStackException


class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(1, stack.peek())
        self.assertEqual(1, stack.pop())
        self.assertTrue(stack.is_empty())
        self.assertRaises(EmptyStackException, stack.pop)
