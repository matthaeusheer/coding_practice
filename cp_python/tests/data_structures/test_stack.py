import unittest
from data_structures.stack import LinkedListStack
from data_structures.stack import ArrayStack
from data_structures.stack import StackWithMin, StackWithMinOpt
from data_structures.stack import EmptyStackException


class TestStack(unittest.TestCase):
    def test_stacks(self):
        for stack_type in [LinkedListStack, ArrayStack, StackWithMin]:
            stack = stack_type()
            self.assertTrue(stack.is_empty())
            stack.push(1)
            self.assertFalse(stack.is_empty())
            self.assertEqual(1, stack.peek())
            self.assertEqual(1, stack.pop())
            self.assertTrue(stack.is_empty())
            self.assertRaises(EmptyStackException, stack.pop)

    def test_stack_wih_min(self):
        for stack_type in [StackWithMin, StackWithMinOpt]:
            stack = stack_type()
            self.assertRaises(EmptyStackException, stack.pop)
            self.assertTrue(stack.is_empty())
            stack.push(9)
            self.assertEqual(9, stack.get_min())
            stack.push(10)
            self.assertEqual(9, stack.get_min())
            stack.push(8)
            self.assertEqual(8, stack.get_min())
            self.assertFalse(stack.is_empty())
            self.assertEqual(8, stack.peek())
            self.assertEqual(8, stack.pop())
            self.assertEqual(9, stack.get_min())
            self.assertEqual(10, stack.pop())
            self.assertEqual(9, stack.pop())
            self.assertTrue(stack.is_empty())
            self.assertRaises(EmptyStackException, stack.pop)