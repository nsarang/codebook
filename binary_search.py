import operator

def binary_search(L: list, x, side="left", key=None):
    """
    Finds index of first element that is >= or > x in sorted list L
    
    x: Value to search for
    side: Comparison behavior
        - "left": First element >= x
        - "right": First element > x
    key: Map L to comparable value
    """
    l, r = 0, len(L)
    # le = <=, lt = <
    cmp = operator.le if side == "left" else operator.lt
    key = key or (lambda x: x)
    while l < r:
        mid = (l + r) // 2
        if cmp(x, key(L[mid])):
            r = mid
        else:
            l = mid + 1
    return l