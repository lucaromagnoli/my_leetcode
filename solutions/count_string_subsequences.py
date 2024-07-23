def count_subsequences(needle, haystack):
    mod = 10**8  # We need the last 8 digits
    n = len(needle)
    m = len(haystack)

    # Initialize the DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: an empty needle is a subsequence of any prefix of the haystack
    for j in range(m + 1):
        dp[0][j] = 1

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters match, add ways to form needle[:i-1] using haystack[:j-1]
            if needle[i - 1] == haystack[j - 1]:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod
            # Always add the ways to form needle[:i] using haystack[:j-1]
            dp[i][j] = (dp[i][j] + dp[i][j - 1]) % mod

    # The answer is in dp[n][m], mod it to get last 8 digits
    return dp[n][m]


print(count_subsequences("happy birthday", "hhaappyy bbiirrtthhddaayy"))
