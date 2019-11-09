import unittest

from data_structures.queue import Queue
from data_structures.queue import EmptyQueueException


class TestQueue(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        self.assertRaises(EmptyQueueException, q.peek)
        self.assertRaises(EmptyQueueException, q.remove)
        q.add(1)
        self.assertFalse(q.is_empty())
        q.add(2)
        q.add(3)
        self.assertEqual(1, q.peek())
        self.assertEqual(1, q.remove())
        self.assertEqual(2, q.peek())
        q.remove()
        q.remove()
        self.assertTrue(q.is_empty())
        self.assertRaises(EmptyQueueException, q.remove)