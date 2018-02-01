def results(original, other):
    count = len(original)
    error = 0
    for i in range(len(original)):
        error += pow(abs(original[i] - other[i]), 2)

    return error/count

