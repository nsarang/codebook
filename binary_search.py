from typing import List
import operator

def binary_search(L: List, x, side="left", key=None):
    """
    x: The value to search for
    side: Find the leftmost or rightmost index of x in L
    key: Map L to a comparable value
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