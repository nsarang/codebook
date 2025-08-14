def gen_power_set(L):
    """Generate the power set of a list L."""
    power_set = []
    for i in range(2 ** len(L)):  # all possible subsets
        subset = []
        for j in range(len(L)):
            if i & (2**j):  # jth bit is on = include L[j]
                subset.append(L[j])
        power_set.append(subset)
    return power_set
