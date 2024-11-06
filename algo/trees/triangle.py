# min path sum as part of the

# also a DP problem as O(n^2)-, mem is O(n) n is num of rows

def minTotal(triangle: List[List[int]]) -> int:
    dp = [0] * (len(triangle) + 1)

    for row in triangle[::-1]:
        for i, n in enumerate(row):
            dp[i] = n + min(dp[i], dp[i + 1]) # min of children

    return dp[0]
