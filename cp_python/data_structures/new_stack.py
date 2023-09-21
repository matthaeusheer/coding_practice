from __future__ import annotations
from typing import Optional
from abc import ABC, abstractmethod

"""
Stack

2023 Implementation version.

Description
-----------
FIFO (first in first out) stack of pancakes. Can push elements on to the stack and remove from the top. Cannot remove
any element somewhere in the middle but only from the top (the last one added).

Operations
----------
push(item)      push a new item on to the stack
pop()           remove and return the upmost element of the stack
peek()          return the upmost element of the stack but don't actually remove it from it
is_empty()      check if there is an element in the stack


Implementations
---------------
1) LinkedListStack
2) ArrayStack

"""

"""
Implementation 1) => LinkedListStack

- idea: only a ref to the top element
- each element is a node with a pointer to the next element below it
- an empty stack has a None top element

Implementation 2) => ArrayStack
- the stack holds a list (array) internally
- initially the array is empty
- when an element is pushed to the stack is is appended on the list and removed when it is popped
"""


class Node:
    def __init__(self, value: int, next_: Node) -> None:
        self.value: int = value
        self.next_: Node = next_


class Stack(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def push(self, item: int) -> None:
        pass

    @abstractmethod
    def pop(self) -> int:
        pass

    @abstractmethod
    def peek(self) -> int:
        pass


class LinkedListStack(Stack):
    def __init__(self) -> None:
        self.top: Optional[Node] = None

    def push(self, item: int) -> None:
        """Add a new element to the stack.
        Time: O(1)
        """
        self.top = Node(value=item, next_=self.top)

    def pop(self) -> int:
        """Remove and return the top element.
        Time: O(1)
        """
        if self.is_empty():
            raise RuntimeError("Stack is empty.")
        item = self.top.value
        self.top = self.top.next_
        return item

    def peek(self) -> int:
        """Peek on the top element of the stack without removing it.
        Time: O(1)
        """
        if self.is_empty():
            raise RuntimeError("Stack is empty.")
        return self.top.value

    def is_empty(self) -> bool:
        """Checks if the stack has content or if it is actually empty.
        Time: O(1)
        """
        return self.top is None


class ArrayStack(Stack):
    def __init__(self) -> None:
        self.array: list[int] = []

    def push(self, item: int) -> None:
        """Add a new element to the stack.
        Time: O(1)
        """
        self.array.append(item)

    def pop(self) -> int:
        """Remove and return the top element.
        Time: O(1)
        """
        if self.is_empty():
            raise RuntimeError("Stack is empty.")
        value = self.array[-1]
        del self.array[-1]
        return value

    def peek(self) -> int:
        """Peek on the top element of the stack without removing it.
        Time: O(1)
        """
        if self.is_empty():
            raise RuntimeError("Stack is empty.")
        return self.array[-1]

    def is_empty(self) -> bool:
        """Checks if the stack has content or if it is actually empty.
        Time: O(1)
        """
        return len(self.array) == 0
