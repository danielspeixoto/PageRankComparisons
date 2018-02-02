def results(original, other):
    count = len(original)
    error = 0
    for i in range(len(original)):
        error += abs(original[i] - other[i]) / original[i]

    return error/count

