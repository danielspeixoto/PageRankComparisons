from typing import List

import abc
from networkx import DiGraph

from comparison import duration


class PageRank:

    time = 0
    ranks = []
    prob = 0.5

    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = self.graph.edges
        self.out_degree = self.graph.out_degree
        self.node_count = len(self.nodes)
        self.total = 0

    def setup_graph(self, graph: DiGraph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = self.graph.edges
        self.out_degree = self.graph.out_degree
        self.node_count = len(self.nodes)

    def calculate(self, *args) -> List[int]:
        print("Calculating page rank...")

        ranks, time = duration.how_long(self.populate_ranks, *args)
        self.time = time

        self.ranks = ranks
        for rank in ranks:
            self.total += rank

        print("Ranks ready!")
        print("total=" + str(self.total))
        return self.ranks

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def populate_ranks(self):
        """Method documentation"""
        return
