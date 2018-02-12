from networkx import DiGraph

from methods.ppr.PersonalizedPageRank import PersonalizedPageRank


class ForwardPush(PersonalizedPageRank):

    def __init__(self, graph: DiGraph):
        super().__init__(graph)
        self.threshold = 1/self.node_count

    def there_is_edge_with_high_residual(self, residual):
        for num in range(len(residual)):
            if residual[num] > self.threshold:
                return num

        return -1

    def get_distance(self, s):
        residual = [0] * self.node_count
        probability = [0] * self.node_count
        residual[s] = 1

        vertice = self.there_is_edge_with_high_residual(residual)
        while vertice != -1:
            for v in self.graph.out_edges(vertice):
                residual[v[1]] += self.prob * residual[vertice] / self.out_degree[vertice]

            probability[vertice] += (1 - self.prob) * residual[vertice]
            residual[vertice] = 0
            vertice = self.there_is_edge_with_high_residual(residual)

        return probability
