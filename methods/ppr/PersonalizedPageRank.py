from typing import List

import abc
from networkx import DiGraph

from comparison import duration


class PersonalizedPageRank:

    time = 0
    prob = 0.5

    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = self.graph.edges
        self.out_degree = self.graph.out_degree
        self.node_count = len(self.nodes)
        self.total = 0.
        self.ranks = [0.] * self.node_count

    def setup_graph(self, graph: DiGraph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = self.graph.edges
        self.out_degree = self.graph.out_degree
        self.node_count = len(self.nodes)

    def calculate(self, *args) -> float:
        print("Calculating personalized page rank...")

        self.ranks, self.time = duration.how_long(self.get_distance, *args)

        for rank in self.ranks:
            self.total += rank

        print("Ranks ready!")
        print("total=" + str(self.total))
        return self.ranks

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_distance(self, s):
        """Method documentation"""
        return
