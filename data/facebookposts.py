import csv
from typing import Tuple, List

FACEBOOK_FILE = 'out.facebook-wosn-wall'

with open(FACEBOOK_FILE, 'r') as data:
    print("Opening file...")
    data: iter = csv.reader(data, delimiter='\t')
    print("Preprocessing...")
    first_column: List[Tuple[int, int]] = []
    amount = 0
    for start in data:
        first_column.append(start[0].split(" "))
    edges = [(int(edge[0]) - 1, int(edge[1]) - 1) for edge in first_column]
    print("Data ready!")


def get_edges(size=len(edges) - 1)-> List:
    return edges[0:size]