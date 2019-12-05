from pprint import pprint
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
    print(f'Performing Depth-First-Search: Looking for connection {src.data} <-> {dst.data}...\n')
    print(f'{"Recursion depth":20}{"Recursive call":25}{"Visited nodes":50}{"Child candidates"}')
    print(f'{"---------------":20}{"--------------":25}{"-------------":50}{"----------------"}')
    recursion_depth = 1

    def recursive_helper_dfs(src, dst) -> bool:
        nonlocal recursion_depth
        if src == dst:
            recursion_depth -= 1
            return True
        if src in visited:
            return False
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
            if recursive_helper_dfs(child, dst):
                return True
        recursion_depth -= 1
        return False

    return recursive_helper_dfs(src, dst)


def breadth_first_search(src: GraphNode, dst: GraphNode) -> bool:
    queue = Queue()
    marked = {src}
    queue.put(src)
    print(f'{"Visiting node":15}{"Current queue"}')
    print(f'{"-------------":15}{"-------------"}')
    while not queue.empty():
        node = queue.get()
        if node == dst:
            return True
        print(f'{node.data:<15}{str([node.data for node in list(queue.queue)[::-1]])}')
        for child in node.children:
            if child not in marked:
                marked.add(child)
                queue.put(child)
    return False


def depth_first_search_var2(graph: dict) -> None:
    """While the depth_first_search function above uses the GraphNode class, I want to provide a version which
    is simpler in terms of dependencies so potentially better suitable for interview questions.

    This function does not check if two nodes are connected (see var3) but merely prints out all nodes in the
    graph using depth first exploration.

    Here, the (undirected) Graph is represented as a Hash Map (dict) consisting of vertices and edges.
    Example
    -------
        graph = {'vertices': ['a', 'b', 'c', 'd', 'e', 'f'],
                 'edges': {
                    'a': ['b'],
                    'b': ['a', 'c', 'd'],
                    'c': ['b', 'd'],
                    'd': ['b', 'c'],
                    'e': ['f'],
                    'f': ['e']
                 }
                 }
    Time complexity: O(vertices + edges)
    """
    visited = set()

    def visit(vertex: str) -> None:
        """Recursive helper function."""
        if vertex not in visited:
            visited.add(vertex)
            print(f'{vertex:>5}')
            for adjacent in [candidate for candidate in graph['edges'][vertex] if candidate not in visited]:
                visit(adjacent)

    print(f'\nDoing Depth First Search simply printing out the whole graph, even for disconnected parts')
    pprint(graph)
    for vertex in graph['vertices']:
        if vertex not in visited:
            print(f'Starting disconnected part at node {vertex}')
            visit(vertex)


def depth_first_search_var3(graph: dict, src_vertex: str, dst_vertex: str) -> bool:
    """Same approach in terms of simpler graph data structure like dfs_var2, but now we do an
    actual search where we check if there is a path from a source vertex to a destination vertex."""
    def recursive_helper(src: str, dst: str, visited: set) -> bool:
        if src == dst:
            print(f'\tFound: {dst}')
            return True
        if src in visited:
            return False
        visited.add(src)
        print(f'\tVisiting: {src}')
        for neighbour in [vert for vert in graph['edges'][src] if vert not in visited]:
            if recursive_helper(neighbour, dst, visited):
                return True
        return False

    print(f'\nDoing depth-first-search on simpler graph model. Checking if path exists from '
          f'{src_vertex} to {dst_vertex}...')
    pprint(graph)
    visited = set()
    return recursive_helper(src_vertex, dst_vertex, visited)
