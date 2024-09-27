from typing import List

def KMP(sequence: str, pattern: str) -> List[int]:
    """
    Knuth-Morris-Pratt Algorithm

    Find all occurrences of 'pattern' in 'sequence'. Returns a list of starting indices.
    """
    joint = list(pattern) + [None] + list(sequence)
    s, p = len(joint), len(pattern)
    # T[i] stores the length of the longest prefix of the substring joint[0:i+1]
    # (i.e., from the start up to i) that is also a suffix of the same substring.
    # If T[i] == p, then the substring joint[i-p+1:i+1] == joint[0:p] == pattern.
    T = [0] * s
    for i in range(1, s):
        j = T[i - 1]
        while j and joint[i] != joint[j]:
            j = T[j - 1]
        T[i] = j + (joint[i] == joint[j])
    matches = [i - 2 * p for i in range(p + 1, s) if T[i] == p]
    return matches