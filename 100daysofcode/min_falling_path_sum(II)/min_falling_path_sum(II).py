class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [row[:] for row in grid]
        for i in range(1,n):
            for j in range(n):
                dp[i][j] = grid[i][j] + min(dp[i-1][k] for k in range(n) if k != j)
        min_su = min(dp[-1])
        return min_su
