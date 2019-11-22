from queue import Queue
from typing import List


class GraphNode:
    def __init__(self, data, children: List['GraphNode'] = None) -> None:
        self.data = data
        self.children = children if children else []  # adjacency list of this node

    def add_child(self, child: 'GraphNode') -> None:
        self.children.append(child)

    def add_children(self, children: List['GraphNode']) -> None:
        self.children += children


class Graph:
    def __init__(self, nodes: List[GraphNode] = None) -> None:
        self.nodes = nodes if nodes else []

    def add_node(self, node: GraphNode) -> None:
        self.nodes.append(node)

    def add_nodes(self, nodes: List['GraphNodes']) -> None:
        self.nodes += nodes

    def print_graph(self) -> None:
        print()
        for idx, node in enumerate(self.nodes):
            print(f'Node# {idx + 1:2} --- data: {node.data:2}, children: {[child.data for child in node.children]}')
        print()


def depth_first_search(src: GraphNode, dst: GraphNode) -> bool:
    """Given the graph along with a source and destination node, check if there is a path connecting the two."""
    if len(src.children) == 0:
        return False
    visited = list()
    print(f'{"Recursion depth":20}{"Recursive call":25}{"Visited nodes":50}{"Child candidates"}')
    print(f'{"---------------":20}{"--------------":25}{"-------------":50}{"----------------"}')
    return recursive_helper_dfs(src, dst, visited)


recursion_depth = 1


def recursive_helper_dfs(src, dst, visited) -> bool:
    global recursion_depth
    if src in visited:
        return False
    if src == dst:
        recursion_depth -= 1
        return True
    visited.append(src)
    non_visited_children = [candidate for candidate in src.children if candidate not in visited]
    # --- printing section ----
    indentation = recursion_depth * "-"
    params = f'[src: {src.data:2} - dst: {dst.data:2}]'
    print(f'{indentation:20}'
          f'{params:25}'
          f'{str([node.data for node in visited]):50}'
          f'{[node.data for node in non_visited_children]}')
    # --- printing section ----
    for child in non_visited_children:
        recursion_depth += 1
        if recursive_helper_dfs(child, dst, visited):
            return True
    recursion_depth -= 1
    return False


def breadth_first_search(src: GraphNode, dst: GraphNode) -> bool:
    queue = Queue()
    marked = set()
    queue.put(src)
    print(f'{"Visiting node":15}{"Current queue"}')
    print(f'{"-------------":15}{"-------------"}')
    while not queue.empty():
        node = queue.get()
        if node == dst:
            return True
        print(f'{node.data:<15}{str([node.data for node in list(queue.queue)])}')
        for child in node.children:
            if child not in marked:
                marked.add(child)
                queue.put(child)
    return False
