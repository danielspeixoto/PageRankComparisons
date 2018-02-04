from copy import deepcopy

import networkx as nx

from comparison import compare
from methods.pr import RegularPageRank
from methods.pr.MonteCarlo import MonteCarlo
from visualization import results_comparison
import data.facebookposts as fb

print("Creating graph...")
G = nx.DiGraph()
G.add_edges_from(fb.get_edges())
# G.add_edges_from([(0, 1)])

regular_pr = RegularPageRank.RegularPageRank(deepcopy(G))
regular_pr.calculate()
print("Regular=" + str(regular_pr.time) + "ms")

n_ranks = [rank * 1/regular_pr.total for rank in regular_pr.ranks]
total = 0
for rank in n_ranks:
    total += rank

print("nrank= " + str(total))

monte_carlo = MonteCarlo(deepcopy(G))
monte_carlo.calculate(100)
print("MonteCarlo=" + str(monte_carlo.time) + "ms")

print("error=" + str(compare.results(monte_carlo.ranks, n_ranks)))
results_comparison.compare(monte_carlo.ranks, n_ranks)


