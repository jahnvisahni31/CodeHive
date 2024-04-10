class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(row, col):
            if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                grid[row][col] = 0
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
            
        for i in range(n):
            dfs(0,i)
            dfs(m-1, i)
        for i in range(1,m-1):
            dfs(i , 0)
            dfs(i , n-1)
        c = sum(row.count(1) for row in grid)
        return c
