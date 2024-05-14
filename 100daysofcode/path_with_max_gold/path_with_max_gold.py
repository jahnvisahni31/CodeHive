class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [0, 1, 0, -1, 0]
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0: return 0
            ans = 0
            orgGold = grid[r][c]
            grid[r][c] = 0
            for i in range(4):
                ans = max(ans, dfs(r + DIR[i], c + DIR[i+1]))
            grid[r][c] = orgGold
            return ans + grid[r][c]
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        return ans
