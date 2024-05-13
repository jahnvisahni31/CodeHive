class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        for j in range(1, n):
            c = sum(grid[i][j] for i in range(m))
            if c < m/2:
                for i in range(m):
                    grid[i][j] ^= 1
        
        s = sum(int("".join(map(str,r)),2) for r in grid)
        return s
