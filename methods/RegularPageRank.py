from networkx import DiGraph
from typing import List

from methods.PageRank import PageRank


class RegularPageRank(PageRank):
    prob = 0.85
    time = 0
    ranks = []
    # TODO Choose error properly
    error = 0.001

    def __init__(self, graph: DiGraph):
        super().__init__(graph)

    def populate_ranks(self)-> List[float]:
        initial = 1 / len(self.nodes)
        ranks = [initial for _ in range(len(self.nodes))]

        self.ranks = ranks
        ranks = self.iterate(ranks)
        while not self.has_converged(ranks, self.error):
            self.ranks = ranks
            ranks = self.iterate(ranks)

        return ranks

    def iterate(self, ranks: List[float]) -> List[float]:
        new_ranks = [0.0] * self.node_count
        for start, end in self.edges:
            new_ranks[end] += ranks[start] / self.out_degree[start] * self.prob

        for i in range(self.node_count):
            new_ranks[i] += (1 - self.prob) / self.node_count

        return new_ranks

    def has_converged(self, ranks, error)-> bool:
        for i in range(len(ranks)):
            if abs(ranks[i] - self.ranks[i]) > error:
                return False

        return True
