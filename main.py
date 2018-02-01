from copy import copy, deepcopy

import networkx as nx

from methods import RegularPageRank
from methods.MonteCarlo import MonteCarlo
from visualization import graph, results_comparison
import data.facebookposts as fb

print("Creating graph...")
G = nx.DiGraph()
G.add_edges_from(fb.get_edges())
# G.add_edges_from([(0, 1)])

regular_pr = RegularPageRank.RegularPageRank(deepcopy(G))
regular_pr.calculate()
print("Regular=" + str(regular_pr.time) + "ms")

monte_carlo = MonteCarlo(G)
monte_carlo.calculate(100)
print("MonteCarlo=" + str(monte_carlo.time) + "ms")

results_comparison.compare(monte_carlo.ranks, regular_pr.ranks)

