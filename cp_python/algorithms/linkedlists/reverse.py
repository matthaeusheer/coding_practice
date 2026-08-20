

class Node():
    def __init__(self, data: int, next: Node | None = None) -> None:
        self.data = data
        self.next: Node | None = next

class LinkedList():
    def __init__(self, node: Node | None = None) -> None:
        self.head = node

    def reverse(self) -> None:
        prev: Node | None = None
        curr: Node | None = self.head

        while curr is not None:
            next_: Node | None = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        self.head = prev

    def print(self) -> None:
        node: Node | None = self.head
        values = []
        while node is not None:
            values.append(str(node.data))
            node = node.next
        print(" -> ".join(values))

    def prepend(self, data: int) -> None:
        node = Node(data, None)
        node.next = self.head if self.head is not None else None
        self.head = node


if __name__ == "__main__":
    ll = LinkedList()
    ll.prepend(5)
    ll.prepend(1)
    ll.prepend(2)
    ll.print()
    ll.reverse()
    ll.print()
