def levenshtein_distance(s1, s2):
    """
    # https://en.wikipedia.org/wiki/Edit_distance
    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one string
    into the other.

    dp[i][j] = min:
        - dp[i - 1][j - 1] + int(s1[i - 1] != s2[j - 1]) # substitution or no change
        - dp[i - 1][j] + 1 # deletion from s1
        - dp[i][j - 1] + 1 # insertion to s1
    """

    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(
                dp[i - 1][j],  # deletion
                dp[i][j - 1],  # insertion
                dp[i - 1][j - 1] + int(s1[i - 1] == s2[j - 1]), # substitution or no change
            )
    return dp[m][n]
