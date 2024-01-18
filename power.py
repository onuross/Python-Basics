def recursive(base, power):
    if power == 0:
        return 1
    result = recursive(base, power - 1) * base
    return result
