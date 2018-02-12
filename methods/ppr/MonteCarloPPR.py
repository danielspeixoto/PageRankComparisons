import random
from networkx import DiGraph
from methods.ppr.PersonalizedPageRank import PersonalizedPageRank


class MonteCarloPPR(PersonalizedPageRank):

    def __init__(self, graph: DiGraph):
        super().__init__(graph)
        self.nodes_on_walk = 0

    def get_distance(self, s,  walks=5)-> float:
        for walk in range(walks):
            self.walk(s, self.ranks)

        for i in range(len(self.ranks)):
            self.ranks[i] = self.ranks[i] / self.nodes_on_walk
        return self.ranks

    def walk(self, node: int, ranks):
        while random.random() < self.prob:
            edges = list(self.graph.edges(node))
            if len(edges) == 0:
                break
            node = random.choice(edges)[1]
            self.nodes_on_walk += 1
            ranks[node] += 1

