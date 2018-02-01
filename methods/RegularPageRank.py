from networkx import DiGraph
from typing import List, Tuple

from methods.PageRank import PageRank


class RegularPageRank(PageRank):

    # TODO Choose error properly
    error = 0.00001

    def __init__(self, graph: DiGraph):
        super().__init__(graph)

    def populate_ranks(self)-> List[float]:
        initial = 1 / self.node_count
        ranks = [initial] * self.node_count
        removed_edges, self.graph = RegularPageRank.remove_dangling_links(self.graph)
        self.setup_graph(self.graph)
        if self.node_count != 0:
            self.ranks = ranks
            ranks = self.iterate(ranks)
            while not self.has_converged(ranks, self.error):
                self.ranks = ranks
                ranks = self.iterate(self.ranks)

        while len(removed_edges) > 0:
            self.graph.add_edges_from(removed_edges.pop())
            self.setup_graph(self.graph)
            ranks = self.iterate(ranks)
            while not self.has_converged(ranks, self.error):
                self.ranks = ranks
                ranks = self.iterate(self.ranks)
        return ranks

    def iterate(self, ranks: List[float])-> List[float]:
        new_ranks = [0] * len(ranks)
        for node in self.nodes:
            if self.graph.has_node(node):
                edges = list(self.graph.in_edges(node))
                for edge in edges:
                    new_ranks[node] += ranks[edge[0]] / len(self.graph.out_edges(edge[0]))

                new_ranks[node] *= self.prob
                new_ranks[node] += (1 - self.prob) / self.node_count
        return new_ranks

    @staticmethod
    def remove_dangling_links(graph: DiGraph):
        has_dangling = True
        removed = []
        while has_dangling:
            to_be_removed = []
            edges = []
            has_dangling = False
            for node in graph.nodes:
                if len(graph.out_edges(node)) == 0:
                    has_dangling = True
                    edges += graph.in_edges(node)
                    to_be_removed.append(node)

            removed.append(edges)
            for node in to_be_removed:
                graph.remove_node(node)

        return removed, graph

    def has_converged(self, ranks, error)-> bool:
        for i in range(len(self.ranks)):
            if abs(ranks[i] - self.ranks[i]) > error:
                return False

        return True
