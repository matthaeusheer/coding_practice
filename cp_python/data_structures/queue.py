"""
Data Structure
--------------
    A queue is a FIFO (first in first out) data structure like a queue of people waiting for coffee. The first person
    arriving in the line is the first person getting the coffee.

Common Operations
-----------------
    add(item):      adds an item to the end of the queue
    remove():       removes the item at the front of the queue
    peek():         checks out the item at the front of the queue
    is_empty():     check if the queue is empty

Implementation
--------------
    Using a LinkedList. Adding at last element (head), removing from first (tail).

Common Use Cases
----------------
    BFS and Caches.
"""
from data_structures.linked_list import Node


class Queue:
    def __init__(self):
        self.first = None  # Gets returned first, since it was the first one added
        self.last = None   # Gets returned last, since it was the last one added

    def add(self, item):
        new_last_node = Node(data=item, next_=None)
        if self.last is None:
            self.last = new_last_node
            self.first = self.last
        else:
            self.last.next = new_last_node
            self.last = new_last_node

    def remove(self):
        if self.first is None:
            raise EmptyQueueException('Cannot remove element from empty queue.')
        ret = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return ret

    def peek(self):
        if self.first is None:
            raise EmptyQueueException('Cannot peek from empty queue.')
        return self.first.data

    def is_empty(self):
        return self.first is None


class EmptyQueueException(Exception):
    pass
