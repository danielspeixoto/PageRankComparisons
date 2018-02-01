import random
from networkx import DiGraph
from typing import List

from networkx.classes.reportviews import OutEdgeDataView

from methods.PageRank import PageRank


class MonteCarlo(PageRank):

    def __init__(self, graph: DiGraph):
        super().__init__(graph)
        self.ranks = [0] * self.node_count

    def populate_ranks(self, walks=1)-> List[float]:
        node_count = len(self.nodes)
        for walk in range(walks):
            for i in range(node_count):
                self.ranks[self.walk(i)] += 1

        for i in range(node_count):
            self.ranks[i] /= walks * node_count

        return self.ranks

    def walk(self, node: int):
        while random.random() < self.prob:
            edges = list(self.graph.edges(node))
            if len(edges) == 0:
                break
            node = random.choice(edges)[1]

        return node

