"""
Data Structure
--------------
    A stack is a pile of data using the LIFO (last in first out) principle. Much like a stack of pancakes, the last
    pancake added to the top of the stack is being the first one removed (popped of) when requested.

Common operations
-----------------
    pop():          O(1)    remove and return the top element of the stack
    push(item):     O(1)    push an item onto the stack
    peek():         O(1)    return the top of the stack without removing the element from the stack
    is_empty():     O(1)    check if the stack is empty

Complexity
--------------
    Operations (add / remove): all O(1). An array needs to shift elements when inserting / deleting, so O(n).
    However, no O(1) access to an element within the stack as in the case of an array.

Implementation
--------------
    We use a LinkedList. The Stack stores a reference to the top element which is the head of the underlying
    LinkedList.
"""
from data_structures.linked_list import LinkedList, Node


class Stack:
    def __init__(self):
        self.top = LinkedList().head

    def pop(self):
        if not self.top:
            raise EmptyStackException('Stack is empty. Cannot pop element from empty stack.')
        ret_val = self.top.data
        self.top = self.top.next
        return ret_val

    def push(self, item):
        self.top = Node(data=item, next_=self.top)

    def peek(self):
        if not self.top:
            raise EmptyStackException('Stack is empty. Cannot peek element from empty stack.')
        return self.top.data

    def is_empty(self):
        return self.top is None


class EmptyStackException(Exception):
    pass

