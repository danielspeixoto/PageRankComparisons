from typing import List

import abc
from networkx import DiGraph

from comparison import duration


class PageRank:

    time = 0
    ranks = []

    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.nodes = self.graph.nodes
        self.edges = self.graph.edges
        self.out_degree = self.graph.out_degree

    def calculate(self) -> List[int]:
        print("Calculating regular page rank...")

        ranks, time = duration.how_long(self.populate_ranks)
        self.time = time

        print("Ranks ready! " + str(ranks))
        return ranks

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def populate_ranks(self):
        """Method documentation"""
        return
