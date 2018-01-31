from networkx import DiGraph
from typing import List

from methods.PageRank import PageRank


class RegularPageRank(PageRank):

    # TODO Choose error properly
    error = 1

    def __init__(self, graph: DiGraph):
        super().__init__(graph)

    def populate_ranks(self)-> List[float]:
        initial = 1 / self.node_count
        ranks = [initial] * self.node_count

        self.ranks = ranks
        ranks = self.iterate(ranks)
        while not self.has_converged(ranks, self.error):
            self.ranks = ranks
            ranks = self.iterate(self.ranks)

        return ranks

    def iterate(self, ranks: List[float]) -> List[float]:
        new_ranks = [0] * self.node_count
        for node in range(self.node_count):
            edges = list(self.graph.in_edges(node))
            for edge in edges:
                new_ranks[node] += ranks[edge[0]] / self.out_degree[edge[0]]

            new_ranks[node] *= self.prob
            new_ranks[node] += (1 - self.prob) / self.node_count
        return new_ranks

    def has_converged(self, ranks, error)-> bool:
        for i in range(self.node_count):
            if abs(ranks[i] - self.ranks[i]) > error:
                return False

        return True
