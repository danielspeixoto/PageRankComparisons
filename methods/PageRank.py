from typing import List

import abc
from networkx import DiGraph

from comparison import duration


class PageRank:

    time = 0
    ranks = []
    prob = 0.85

    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = self.graph.edges
        self.out_degree = self.graph.out_degree
        self.node_count = len(self.nodes)

    def setup_graph(self, graph: DiGraph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = self.graph.edges
        self.out_degree = self.graph.out_degree
        self.node_count = len(self.nodes)

    def calculate(self) -> List[int]:
        print("Calculating page rank...")

        ranks, time = duration.how_long(self.populate_ranks)
        self.time = time

        self.ranks = ranks
        total = 0
        for rank in ranks:
            total += rank

        print("Ranks ready!")
        print("total=" + str(total))
        print(ranks)
        return self.ranks

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def populate_ranks(self):
        """Method documentation"""
        return
