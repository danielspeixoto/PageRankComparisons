from copy import deepcopy

import networkx as nx

from comparison import compare
from methods.ppr.ForwardPush import ForwardPush
from methods.ppr.MonteCarloPPR import MonteCarloPPR
from methods.pr import RegularPageRank
from methods.pr.MonteCarlo import MonteCarlo
from visualization import results_comparison
import data.facebookposts as fb

print("Creating graph...")
G = nx.DiGraph()
G.add_edges_from(fb.get_edges())


regular_pr = RegularPageRank.RegularPageRank(deepcopy(G))
regular_pr.calculate()
print("Regular=" + str(regular_pr.time) + "ms")

n_ranks = [rank * 1/regular_pr.total for rank in regular_pr.ranks]
total = 0
for rank in n_ranks:
    total += rank

print("nrank= " + str(total))

monte_carlo = MonteCarlo(deepcopy(G))
monte_carlo.calculate(10)
print("MonteCarlo=" + str(monte_carlo.time) + "ms")

print("error=" + str(compare.results(monte_carlo.ranks, n_ranks)))
results_comparison.compare(monte_carlo.ranks, n_ranks)

# bigger = 0
# for v in range(len(G.nodes)):
#     if G.out_degree[v] > G.out_degree[bigger]:
#         bigger = v
#
#
# # PPR
# forward_push = ForwardPush(deepcopy(G))
# forward_push.calculate(bigger)
# print("Regular=" + str(forward_push.time) + "ms")
#
# n_ranks = [rank * 1/forward_push.total for rank in forward_push.ranks]
# total = 0
# for rank in n_ranks:
#     total += rank
#
# print("nrank= " + str(total))
#
# monte_carlo_ppr = MonteCarloPPR(deepcopy(G))
# monte_carlo_ppr.calculate(bigger, 10)
# print("MonteCarlo=" + str(monte_carlo_ppr.time) + "ms")
#
# # print("error=" + str(compare.results(monte_carlo_ppr.ranks, n_ranks)))
# results_comparison.compare(monte_carlo_ppr.ranks)
# results_comparison.compare(n_ranks)
#
#
#
