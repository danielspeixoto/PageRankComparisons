import networkx as nx

from methods import RegularPageRank
from methods.MonteCarlo import MonteCarlo
from visualization import graph, results_comparison
import data.facebookposts as fb

print("Creating graph...")
G = nx.DiGraph()
G.add_edges_from(fb.get_edges())

regular_pr = RegularPageRank.RegularPageRank(G)
regular_pr.calculate()
print("Regular=" + str(regular_pr.time) + "ms")

monte_carlo = MonteCarlo(G)
monte_carlo.calculate()
print("MonteCarlo=" + str(monte_carlo.time) + "ms")

results_comparison.compare(regular_pr.ranks, monte_carlo.ranks)