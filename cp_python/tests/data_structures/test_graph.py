import unittest

from data_structures.graph import GraphNode, Graph
from data_structures.graph import depth_first_search, breadth_first_search, \
                                  depth_first_search_var2, depth_first_search_var3


class TestGraphSearch(unittest.TestCase):
    def setUp(self) -> None:
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
        node13 = GraphNode(data=13)
        node14 = GraphNode(data=14)
        node15 = GraphNode(data=15)
        node1.add_child(node5)
        node2.add_children([node5, node9, node10])
        node3.add_children([node2, node13, node4])
        node4.add_children([node5, node6, node8])
        node5.add_children([node3])
        node6.add_child(node7)
        node9.add_child(node10)
        node10.add_child(node11)
        node11.add_child(node12)
        node13.add_child(node14)
        node14.add_child(node15)
        my_graph = Graph()
        my_graph.add_nodes([node1, node2, node3, node4, node5, node6, node7, node8,
                            node9, node10, node11, node12, node13, node14, node15])
        self.my_graph = my_graph

    def test_dfs(self):
        source = self.my_graph.nodes[0]
        destination = self.my_graph.nodes[5]
        self.my_graph.print_graph()
        found = depth_first_search(src=source,
                                   dst=destination)
        print()
        print(f'Performed DFS starting from node {source.data}, looking for node {destination.data}.')
        print(f'Search was {"successful." if found else "not successful."}')

    def test_dfs_var2(self):
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
        depth_first_search_var2(graph)

    def test_dfs_var3(self):
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
        self.assertTrue(depth_first_search_var3(graph, 'a', 'b'))
        self.assertTrue(depth_first_search_var3(graph, 'a', 'c'))
        self.assertTrue(depth_first_search_var3(graph, 'a', 'd'))
        self.assertTrue(depth_first_search_var3(graph, 'b', 'a'))
        self.assertTrue(depth_first_search_var3(graph, 'c', 'd'))
        self.assertTrue(depth_first_search_var3(graph, 'd', 'd'))
        self.assertFalse(depth_first_search_var3(graph, 'd', 'e'))
        self.assertFalse(depth_first_search_var3(graph, 'a', 'f'))
        self.assertTrue(depth_first_search_var3(graph, 'e', 'f'))

    def test_bfs(self):
        source = self.my_graph.nodes[0]
        destination = self.my_graph.nodes[5]
        self.my_graph.print_graph()
        found = breadth_first_search(src=source, dst=destination)
        print()
        print(f'Performed BFS starting from node {source.data}, looking for node {destination.data}.')
        print(f'Search was {"successful." if found else "not successful."}')