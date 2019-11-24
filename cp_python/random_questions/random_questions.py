import unittest

from data_structures.linked_list import LinkedList


def add_one_to_digit_list(digits):
    """You are given a list of digits where each entry is an integer from 0 to 9.
    If you think of the digits representing a number when one would write out the number those digits make up,
    write a function that returns a list of digits which represents a number one higher than the number represented
    by the input list.

    Proposed solution complexity:
        Time O(n)  - O(n) for list traversal and O(n) for possible insertion worst case, len and set val are O(1) ops.
        Space O(1) - No additional space required.
    """
    carry_over = 1
    idx = len(digits) - 1
    while idx >= 0:
        summed = digits[idx] + carry_over
        if summed == 10:
            carry_over = 1
        else:
            carry_over = 0
        digits[idx] = summed % 10
        idx -= 1
    if carry_over == 1:
        digits.insert(0, 1)
    return digits


def reverse_linked_list(ll: LinkedList) -> LinkedList:
    """Reverse a linked list in place. Given is a LinkedList represented by a head node.
    Returned should be a linked list in reversed order without buffering the results in-between."""
    if not ll.head or not ll.head.next:
        return ll
    curr_node = ll.head
    next_node = curr_node.next
    curr_node.next = None
    while next_node:
        over_next = next_node.next
        next_node.next = curr_node
        curr_node = next_node
        next_node = over_next
    ll.head = curr_node
    return ll


def reverse_linked_list_2(ll: LinkedList) -> LinkedList:
    """Only difference to before: Here I use prev, curr, nex pointers, while before we used
    curr, nex, over_nex pointers. Both methods work but the pointer positions are shifted by one
    where place in the linked list. This second method is arguably nicer."""
    if not ll.head or not ll.head.next:
        return ll
    prev = None
    curr = ll.head
    while curr:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    ll.head = prev
    return ll


def schnecken_dist_travelled(target_x: int, target_y: int) -> int:
    """We are on a 2D plane. Starting from (0, 0), you can do a step of 1 upwards, then 1 to the right,
    then 2 downwards, then 2 to the left, then 3 upwards, then 3 to the right, 4 downwards and so on.
    Given a target location (target_x, target_y), what is the distance you have travelled?
    You may assume that the target location given is actually on the path described."""
    current_x, current_y = 0, 0
    dist = 0
    level_step = 1
    print(f'Target: {{{target_x}, {target_y}}}')
    if target_x == 0 and target_y == 0:
        return dist
    while True:
        direction = -1 if level_step % 2 == 0 else 1
        # take vertical step
        current_y += direction * level_step
        dist += level_step
        print(f'Took step of size {level_step} {"upwards" if direction == 1 else "downwards"}')
        print(f'Total distance travelled: {dist}')
        if current_x == target_x and current_y == target_y:
            print('Target reached.')
            return dist
        # take horizontal step
        current_x += direction * level_step
        dist += level_step
        print(f'Took step of size {level_step} {"right" if direction == 1 else "left"}')
        print(f'Total distance travelled: {dist}')
        if current_x == target_x and current_y == target_y:
            print('Target reached.')
            return dist
        level_step += 1
