from data_structures import graph
from data_structures import trees


def exc1_route_between_nodes(src: graph.GraphNode, dst: graph.GraphNode) -> bool:
    """Given a directed graph, design an algorithm to find out whether there is a
    route between two nodes.

    Solution
    -------
        Can be solved with either depth-first-search or breadth-first-search. Both will be able to tell if there is
        a route between two nodes in a graph.
        While DFS goes far away from a node diving deep into single recursive branches of the graph, BFS uses a queue
        to explore the closest nodes first before going deep. It does it level by level. So generally we would prefer
        breadth first search to not risk to go deep into the tree even if the destination is very close.

        Time: O(N + M) for both, DFS and BFS, N number of vertices, M number of edges (depends on denseness of graph)
        Space:
            DFS: O(D), D maximum depth of the recursive stack
            BFS: O(W), W maximum width of a level of the graph when starting at a src node
    """
    return graph.breadth_first_search(src, dst)


def exc2_minimal_tree(input_array: list) -> trees.BinarySearchTree:
    """Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a
    binary search tree with minimal height.

    Idea
    ----
        To get a well balanced BST (which is the condition to have the least amount of levels, i.e. small depth,
        it is crucial to add elements in the correct order. If we would add the elements in sorted order we would
        essentially create a linked list with maximum amount of depth in the tree.
        We consider a divide and conquer approach: First add the middle element of the input array. That makes sure
        that there are the same amount of elements on the left and on the right side of the root of the tree.
        Then enter both parts on of the list to the left and the right of this pivot element and do the same,
        that is, add the center, and so on. The base case is, when only one element in a sub list is left, then
        we simply add this element and continue back up the stack.
    Complexity
    ----------
        Time: O(length of input list), since we have to add every single element
        Space: O(maximum depth of tree), since this is the maximum "height" of a potential call stack
    """
    def recursive_helper(arr: list, tree: trees.BinarySearchTree) -> None:
        if len(arr) == 1:
            tree.insert(trees.BinarySearchTreeNode(data=arr[0]))
        else:
            mid_idx = len(arr) // 2
            tree.insert(trees.BinarySearchTreeNode(data=arr[mid_idx]))
            recursive_helper(arr[0:mid_idx], tree)
            recursive_helper(arr[mid_idx+1:len(arr)], tree)

    bin_search_tree = trees.BinarySearchTree()
    recursive_helper(input_array, bin_search_tree)
    return bin_search_tree
