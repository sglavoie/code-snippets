def is_strict_superset(superset, subset):
    len_a = len(superset)
    len_n = len(subset)
    if len_a <= len_n:
        return False
    return subset.issubset(superset)
