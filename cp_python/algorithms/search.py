from math import floor

from typing import Any


def binary_search(arr: list, item: Any) -> bool:
    """Check if an item is present in an array by performing binary search.
    Arguments
    ---------
        arr:    input list of items, needs to be sorted!
        item:   the item we look for in the input list
    Returns
    -------
        bool whether item has been found or not

    How Binary Search Works
    -----------------------
        - set left pointer to start and right pointer to end of array
        - continue searching while left < right, else the search terminates unsuccessful
        - set middle pivot element to be arr(middle), where middle=floor((l+r)/2)
        - if pivot < item: adjust left to be middle+1 and continue search in new partition
        - if pivot > item: adjust right to be middle-1 and continue search in lower partition
        - if pivot == item: return True
    """
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        if left_idx + right_idx == 0:
            pivot_idx = 0
        else:
            pivot_idx = (left_idx + right_idx) // 2
        print(f'left: {left_idx}, right: {right_idx}, pivot: {pivot_idx}')
        if item < arr[pivot_idx]:
            right_idx = pivot_idx - 1
        elif item > arr[pivot_idx]:
            left_idx = pivot_idx + 1
        else:  # item == pivot
            print(f'\tFound at position {left_idx}!')
            return True
    print('\tNot found.')
    return False
