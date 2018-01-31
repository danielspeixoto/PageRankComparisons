from networkx import DiGraph
from typing import List

from methods.PageRank import PageRank


class RegularPageRank(PageRank):
    prob = 0.85
    time = 0
    ranks = []
    # TODO Choose error properly
    error = 0.0000001

    def __init__(self, graph: DiGraph):
        super().__init__(graph)

    def populate_ranks(self):
        initial = 1 / len(self.nodes)
        ranks = [initial for _ in range(len(self.nodes))]

        self.ranks = ranks
        ranks = self.iterate(ranks)
        while not self.has_converged(ranks, self.error):
            self.ranks = ranks
            ranks = self.iterate(ranks)

    def iterate(self, ranks: List[float]) -> List[float]:
        nodes_count = len(self.nodes)
        new_ranks = [0.0] * nodes_count
        for start, end in self.edges:
            new_ranks[end] += ranks[start] / self.out_degree[start] * self.prob

        for i in range(nodes_count):
            new_ranks[i] += (1 - self.prob) / nodes_count

        return new_ranks

    def has_converged(self, ranks, error)-> bool:
        for i in range(len(ranks)):
            if abs(ranks[i] - self.ranks[i]) > error:
                return False

        return True
