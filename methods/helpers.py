from typing import List


def ranks_to_int(ranks: List[float])-> List[float]:
    return [((ranks[i] + 0.002) * 1000) ** 3
            for i in range(len(ranks))]


def ranks_to_percent(ranks: List[float])-> List[str]:
    return [str(round(ranks[i] * 100, 5)) + "%"
            for i in range(len(ranks))]
