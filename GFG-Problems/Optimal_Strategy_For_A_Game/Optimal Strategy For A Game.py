#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,n, arr):
        # code here
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # Fill in the base cases for single coin selection
        for i in range(n):
            dp[i][i] = arr[i]

        # Fill in the results for subproblems with more than one coin
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                x = 0 if i + 2 > j else dp[i + 2][j]
                y = 0 if i + 1 > j - 1 else dp[i + 1][j - 1]
                z = 0 if i > j - 2 else dp[i][j - 2]
                dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))

        # The maximum possible amount of money the first player can win is stored in dp[0][n-1]
        return dp[0][n - 1]
