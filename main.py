import networkx as nx

from helpers import millis
from methods import RegularPageRank
from visualization import graph, results_comparison
import data.facebookposts as fb

print("Creating graph...")
G = nx.DiGraph()
G.add_edges_from(fb.get_edges())

regular_pr = RegularPageRank.RegularPageRank(G)
regular_pr.calculate()
print(str(regular_pr.time) + "ms")

# results_comparison.compare(regular_pr, regular_pr)