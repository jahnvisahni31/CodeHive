class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_counts = {i: sum(grid[i][j] for j in range(cols)) for i in range(rows)}
        col_counts = {j: sum(grid[i][j] for i in range(rows)) for j in range(cols)}
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += (row_counts[i] - 1) * (col_counts[j] - 1)
    
        return count
