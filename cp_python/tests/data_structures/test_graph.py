import unittest

from data_structures.graph import GraphNode, Graph, depth_first_search


class TestGraphSearch(unittest.TestCase):
    def test_dfs(self):
        node1 = GraphNode(data=1)
        node2 = GraphNode(data=2)
        node3 = GraphNode(data=3)
        node4 = GraphNode(data=4)
        node5 = GraphNode(data=5)
        node6 = GraphNode(data=6)
        node7 = GraphNode(data=7)
        node8 = GraphNode(data=8)
        node9 = GraphNode(data=9)
        node10 = GraphNode(data=10)
        node11 = GraphNode(data=11)
        node12 = GraphNode(data=12)
        node1.add_child(node5)
        node2.add_children([node5, node9, node10])
        node3.add_children([node2, node4])
        node4.add_children([node5, node6, node8])
        node5.add_children([node3])
        node6.add_child(node7)
        node9.add_child(node10)
        node10.add_child(node11)
        node11.add_child(node12)
        my_graph = Graph()
        my_graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8,
                            node9, node10, node11, node12])
        my_graph.print_graph()

        found = depth_first_search(node1, node6)
        print(f'Performed DFS starting from node {node1.data}, looking for node {node6.data}')
        print(f'Search was {"successful." if found else "not successful."}')
