from data_structures.linked_list import LinkedList


def exc1_remove_dups(ll: LinkedList) -> LinkedList:
    """Write code to remove duplicates from an unsorted linked list.
    Hints:
        #9: bla
        #40: blu
    Idea:
    Move through the linked list and keep track of elements seen so far in a hash set.
    Whenever we encounter an element already in the hash set, we remove it and keep iterating.
    Since we are working with linked lists and not arrays, there is no issue with indices and
    we can do it in one pass.
    Time: O(n) since we iterate through whole linked list
    Space: O(1)
    """
    lookup = set()
    if not ll.head or not ll.head.next:
        return ll
    node = ll.head.next
    previous = ll.head
    lookup.add(previous.data)
    while node:
        if node.data in lookup:
            previous.next = node.next
        else:
            lookup.add(node.data)
            previous = node
        node = node.next
    return ll


def exc1_remove_dups_no_buffer(ll: LinkedList) -> LinkedList:
    """Same as before but now we are not allowed to use a buffer, i.e. a hash set in our case."""
    raise NotImplementedError


