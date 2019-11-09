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
    Two possibilities
        LinkedList. The Stack stores a reference to the top element which is the head of the underlying LinkedList.
        Array. The Stack holds an array and the index of the top most (last) element. If the array is filled up,
        a new, larger array is being created and old content is being copied over.
"""
from abc import ABC
from data_structures.linked_list import Node


class Stack(ABC):
    pass


class LinkedListStack(Stack):
    def __init__(self):
        self.top = None

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


class ArrayStack(Stack):
    def __init__(self):
        self.curr_size = 1  # default size
        self.arr = self.curr_size * []
        self.top_idx = None

    def pop(self):
        if self.top_idx is None:
            raise EmptyStackException
        ret = self.peek()
        self.top_idx = self.top_idx - 1 if self.top_idx > 0 else None
        return ret

    def peek(self):
        if self.top_idx is None:
            raise EmptyStackException
        return self.arr[self.top_idx]

    def push(self, item):
        if self.top_idx is None:
            self.top_idx = 0
        else:
            self.top_idx += 1
        if self.top_idx == len(self.arr):
            tmp = self.arr.copy()
            self.curr_size *= 2
            self.arr = self.curr_size * [None]
            self.arr[0:len(tmp)] = tmp
        self.arr[self.top_idx] = item

    def is_empty(self):
        return self.top_idx is None


class NodeWithMin(Node):
    def __init__(self, data, min_, next_=None):
        super().__init__(data, next_)
        self.min = min_


class StackWithMin(Stack):
    """How would you design a stack which, in addition to push and pop, has a function min which returns the minimum
    element? Push, pop and min should all operate in 0(1) time!
    Idea:
            Suppose the stack has a minimum member variable and for every push, we check if the new element is smaller
            than the current minimum of the stack. If so, we update the min variable. Problems arise when popping an
            element of the stack. Which is the next smaller element now? For that we have to search the whole stack
            which is O(n).
            Solution: Every node carries a member which indicates the minimum of the current stack it is in. If the own
            value is smaller, then minimum gets set to this value, if not, the minimum value from the previous top is
            taken over. That way each node knows which is the smallest element for itself and all nodes deeper in the
            stack.
    Optimization:
            The solution above stores one integer for sure in every node. We "could" do better by having a second
            stack being responsible for the min values inside the stack. If nodes added afterwards are usually larger
            than say the first one, end up storing much less.
    """
    def __init__(self):
        self.top = None

    def push(self, item):
        if self.top is None:
            self.top = NodeWithMin(data=item, min_=item, next_=None)
        else:
            self.top = NodeWithMin(data=item, min_=item if item < self.top.min else self.top.min, next_=self.top)

    def pop(self):
        if self.top is None:
            raise EmptyStackException
        ret = self.top.data
        self.top = self.top.next
        return ret

    def peek(self):
        if self.top is None:
            raise EmptyStackException
        return self.top.data

    def is_empty(self):
        return self.top is None

    def get_min(self):
        if self.top is None:
            raise EmptyStackException
        return self.top.min


class StackWithMinOpt(LinkedListStack):
    def __init__(self):
        super().__init__()
        self.min_stack = LinkedListStack()

    def push(self, item):
        if item < self.get_min():
            self.min_stack.push(item)
        super().push(item)

    def pop(self):
        ret = super().pop()
        if ret == self.get_min():
            self.min_stack.pop()
        return ret

    def get_min(self):
        if self.top is None:
            return float('inf')
        else:
            return self.min_stack.peek()


class EmptyStackException(Exception):
    pass

