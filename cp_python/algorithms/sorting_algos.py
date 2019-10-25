
###################################
#                                 #
#                                 #
#       Q U I C K S O R T         #
#                                 #
#                                 #
###################################
"""
My implementation of the divide-and-conquer quicksort algorithm.
Average time complexity is O(nlogn), worst case (very rare) is O(n²).

Working principle:
    - divide step:
        divide input via pivot element in left and right parts, pivot element can go either way
    - conquer step:
        all elements < pivot go to left, all > pivot go to right,
        that means that after this step all elements in right are bigger equals elements in right

    now the sub lists can be sorted via the same procedure, this is where recursion comes into play
    TBD...
"""


def quick_sort(input_list):
    pass

