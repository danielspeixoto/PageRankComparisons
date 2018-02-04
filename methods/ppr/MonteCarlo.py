import random
from networkx import DiGraph
from methods.ppr.PersonalizedPageRank import PersonalizedPageRank


class MonteCarlo(PersonalizedPageRank):

    def __init__(self, graph: DiGraph):
        super().__init__(graph)
        self.nodes_on_walk = 0

    def get_distance(self, s, t, walks=5)-> float:
        for walk in range(walks):
            self.walk(s, self.ranks)

        return self.ranks[t] / self.nodes_on_walk

    def walk(self, node: int, ranks):
        while random.random() < self.prob:
            edges = list(self.graph.edges(node))
            if len(edges) == 0:
                break
            node = random.choice(edges)[1]
            if ranks[node] == 0:
                self.nodes_on_walk += 1
            ranks[node] += 1

