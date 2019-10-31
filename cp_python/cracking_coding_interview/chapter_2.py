from data_structures.linked_list import LinkedList, Node


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
    Space: O(n) for the hash set lookup
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


def exc1_remove_dups_variant(ll: LinkedList) -> LinkedList:
    """Variant where we do not need a 'previous' pointer since we add the first element
    of the linked list dto the lookup and check for the next node's data for matches.
    Time: O(n)
    Space: O(n)
    """
    lookup = set()
    if not ll.head or not ll.head.next:
        return ll
    lookup.add(ll.head.data)
    node = ll.head
    while node.next:
        if node.next.data in lookup:
            node.next = node.next.next
        else:
            lookup.add(node.data)
            node = node.next
    return ll


def exc1_remove_dups_no_buffer(ll: LinkedList) -> LinkedList:
    """Same as before but now we are not allowed to use a buffer, i.e. a hash set in our case.
    Idea:
    Have two pointer, one which goes through the linked list one by one and another one which,
    for every element the first pointer points to, checks the rest of the list and removes duplicates.
    Time: O(n²)
    Space: O(1)
    """
    if not ll.head or not ll.head.next:
        return ll
    current = ll.head
    runner = current
    while current:
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            runner = runner.next
        current = current.next
        runner = current
    return ll


def exc2_return_kth_to_last_first(ll: LinkedList, k: int) -> LinkedList:
    """Implement an algorithm to find the kth to last element of a singly linked list.

    NOTE: I actually got this question wrong. What is asked is to return the kth node before
          the last node, not a linked list which represents all nodes starting from the
          k-th node to the last. This is what is implemented below.
    """
    if not ll.head or not ll.head.next:
        return ll
    node = ll.head
    for _ in range(k - 1):
        node = node.next
    ll.head = node
    return ll


def exc2_return_kth_to_last(ll: LinkedList, k: int) -> Node:
    """Implement an algorithm to find the kth to last element of a singly linked list.
    Hints:#8, #25, #41, #67, #126
    """
    raise NotImplementedError


def exc3_delete_middle_node(node: Node) -> bool:
    """Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    that node.
    Hints:
    - #72: Picture the list 1->5->9->12. Removing 9 would make it look like 1->5->12. You only
           have access to the 9 node. Can you make it look like the correct answer?

    Idea: Copy over the data from the next node to the current one we have access to and
          delete the next node such that the current node points to the next after next node.
    Time & Space: O(1)

    Node: If the node to delete is the last node of the LL, it's not possible to solve this,
          we cannot solve this. Possible solution: Marking the node as a dummy node...
    Arguments
    ---------
        node: A node of a linked list.
    Returns
    -------
        bool: True for success (could delete node), False for failure (could not delete node).
    """
    if not node or not node.next:
        return False
    node.data = node.next.data
    node.next = node.next.next
    return True


def exc4_partition(ll: LinkedList, part_val: float) -> LinkedList:
    """Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.

    Idea1:
        We could have two new linked lists, one for elements smaller to pivot (element which determines partition)
        and one for elements bigger or equal to pivot. Then, we concatenate them by setting the head of the
        second list as next of last of the first list.
        Time:  O(n), we iterate once through whole input LL and once through lower part until we can concat
        Space: O(1), since we only change the next pointers, no additional storage required
    Idea2:
        If all we need to do is have a pivot where the elements go on either side depending on their value but no
        order preservation is required, we can initialize an empty list and prepend / append elements from the
        original list.
    """
    # Implementation of Idea1 follows.
    ll_low = LinkedList()
    ll_high = LinkedList()
    node = ll.head
    # First, full up partitions
    while node:
        if node.data < part_val:
            ll_low.append(node)
        else:
            ll_high.append(node)
        node = node.next
    # Then, concat them
    node_low = ll_low.head
    while node_low:
        node_low = node_low.next
    node_low.next = ll_high.head
    return ll



