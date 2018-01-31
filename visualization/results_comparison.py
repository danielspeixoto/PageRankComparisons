# Each result has a name for the method used
# and its rank array
from typing import Tuple, List

import matplotlib.pyplot as plt

def compare(*args: Tuple[str, List[int]]):
    print("Plotting comparison...")
    data = []
    for result in args:
        ranks = result[1]
        plt.plot(ranks)

    plt.show()
