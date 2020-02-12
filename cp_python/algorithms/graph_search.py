import heapq
import math

from data_structures.graph import Graph, GraphNode

from typing import List, Any


class DijkstraGraphNode(GraphNode):
    def __init__(self, data: Any, children: List[GraphNode] = None, prev: GraphNode = None) -> None:
        super().__init__(data, children)
        self.prev = prev
        self.dist = math.inf

    def set_prev(self, prev: GraphNode) -> None:
        self.prev = prev

    def set_dist(self, dist: float) -> None:
        self.dist = dist


def dijkstra(graph: Graph, source: DijkstraGraphNode, target: DijkstraGraphNode) -> List[GraphNode]:
    """Dijkstra's algorithm provides us with the shortest path in a from a destination to a target
    node within a weighted graph."""
    done = {}
    prioq = []
    source.set_dist(0)
    heapq.heappush(prioq, source)
    while len(prioq) != 0:
        # heapq.heapify(prioq)
        curr_node = heapq.heappop(prioq)
        for child in curr_node.children:
            if child in done:
                continue
            else:
                child_dist = curr_node.dist + weight_of_edge_between_curr_node_and_child
                if child not in prioq:
                    child.set_prev(curr_node)
                    child.set_dist(child_dist)
                    heapq.heappush(prioq, child)
                else:
                    if child_dist < child.dist:
                        child.set_dist(child_dist)
                        child.set_prev(curr_node)
                        heapq.heapify(prioq)

