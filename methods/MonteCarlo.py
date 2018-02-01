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
        amount = 0
        for walk in range(walks):
            for i in range(node_count):
                amount += self.walk(i, self.ranks)
                # self.ranks[self.walk(i, self.ranks)] += 1

        for i in range(node_count):
            self.ranks[i] /= amount

        return self.ranks

    def walk(self, node: int, ranks):
        amount = 1
        ranks[node] += 1
        while random.random() < self.prob:
            edges = list(self.graph.edges(node))
            if len(edges) == 0:
                break
            node = random.choice(edges)[1]
            ranks[node] += 1
            amount += 1

        return amount

