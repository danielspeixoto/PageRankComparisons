from _ast import List

from helpers import millis


def how_long(func, *params):
    before = millis.millis()
    result = func(*params)
    total = millis.millis() - before
    return result, total



