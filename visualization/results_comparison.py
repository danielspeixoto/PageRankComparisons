# Each result has a name for the method used
# and its rank array
from typing import Tuple, List
import matplotlib.pyplot as plt


def compare(*args: List[int]):
    print("Plotting comparison...")
    for result in args:
        plt.plot(result)

    plt.show()
