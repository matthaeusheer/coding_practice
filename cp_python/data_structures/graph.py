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
        print(15 * ' = ')
        for idx, node in enumerate(self.nodes):
            print(f'Node# {idx + 1:2} --- data: {node.data:2}, children: {[child.data for child in node.children]}')
        print(15 * ' = ' + '\n')


def depth_first_search(src: GraphNode, dst: GraphNode):
    """Given the graph along with a source and destination node, check if there is a path connecting the two."""
    if len(src.children) == 0:
        return False
    visited = list()
    return recursive_helper_dfs(src, dst, visited)


recursion_depth = 1


def recursive_helper_dfs(src, dst, visited):
    global recursion_depth
    indentation = recursion_depth * "-"
    if src in visited:
        return False
    if src == dst:
        recursion_depth -= 1
        return True
    visited.append(src)
    non_visited_children = [candidate for candidate in src.children if candidate not in visited]
    print(f'{indentation:10} [src: {src.data:2} - dst: {dst.data:2}]',
          f'visited: {str([node.data for node in visited]):40}'
          f'candidates: {[node.data for node in non_visited_children]}')
    for child in non_visited_children:
        recursion_depth += 1
        if recursive_helper_dfs(child, dst, visited):
            return True
    recursion_depth -= 1
    return False


def breadth_first_search(graph: Graph):
    pass