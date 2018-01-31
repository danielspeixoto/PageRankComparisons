import random
from typing import Dict, List, Tuple


def nodes_count() -> int:
    return 10


def nodes() -> Dict[int, int]:
    nodes_hash = {}
    for i in range(nodes_count()):
        nodes_hash[i] = i
    return nodes_hash


def edges() -> List[Tuple[int, int]]:
    random_edges: List[Tuple[int, int]] = []
    for i in range(nodes_count()):
        edges_count = round(random.random() * min(i, 10))
        random_edges.append((i, nodes_count() - 1))
        for j in range(edges_count):
            rand = round(random.random() * nodes_count())
            random_edges.append((i, rand))

    print("edges")
    print(random_edges)
    return random_edges
