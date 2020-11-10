from typing import List


class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head
        self.size = 0 if head is None else 1

    def prepend(self, data) -> None:
        """Inserts an element at the beginning. Time: O(1)."""
        self.head = Node(data, next_=self.head)
        self.size += 1

    def append(self, data) -> None:
        """Inserts an element at the end. Time: O(n), n: size of linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        self.size += 1

    def insert(self, data, position) -> None:
        """Inserts an element at given index position. Time: O(n) worst case, n: size of linked list."""
        assert position - 1 <= self.size, f'Cannot insert at position {position} for list of size {self.size}.'
        if position == 0:
            return self.prepend(data)
        node = self.head
        for idx in range(position - 1):
            node = node.next
        new_node = Node(data, next_=node.next)
        node.next = new_node
        self.size += 1

    def remove(self, data) -> bool:
        """Remove first occurrence of an item in the list. Time: O(n)."""
        node = self.head
        if node.data == data:  # hit on head
            self.head = node.next if node.next else None
            self.size -= 1
            return True
        while node.next:
            if node.next.data == data:
                node.next = node.next.next if node.next.next else None
                self.size -= 1
                return True
            node = node.next
        return False

    def display(self):
        """Prints out the whole linked list. Time: O(n) since we need to traverse the whole thing."""
        print(self.to_list())

    def search(self, data) -> int:
        """Searches for an item and returns the index if found, else returns -1. Time: O(n)."""
        if not self.head:
            return -1  # not found
        node = self.head
        idx = 0
        while node.next:
            if node.data == data:
                return idx
            node = node.next
            idx += 1
        return -1

    def to_list(self) -> List:
        """Convert the linked list to a usual Python list. Time: O(n)."""
        node = self.head
        if self.size == 0:
            return []
        list_ = []
        while node.next is not None:
            list_.append(node.data)
            node = node.next
        list_.append(node.data)
        return list_

    @classmethod
    def from_list(cls, input_list: List) -> 'LinkedList':
        """Create a linked list from a Python list."""
        ll = LinkedList()
        for item in reversed(input_list):
            ll.prepend(item)
        return ll

    def traverse(self):
        """Generator to iterate through elements of the list."""
        node = self.head
        for _ in range(self.size + 1):
            yield node
            node = node.next


def ll_to_list(ll: LinkedList) -> List:
    """TODO: Check why typing for class methods /static methods is not possible."""
    if ll.size == 0:
        return []
    list_ = []
    node = ll.head
    while node.next:
        list_.append(node.data)
        node = node.next
    list_.append(node.data)
    return list_
