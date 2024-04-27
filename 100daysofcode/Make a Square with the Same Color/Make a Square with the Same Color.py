class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def has2x2Square(grid):
            for i in range(2):
                for j in range(2):
                    if grid[i][j] == grid[i+1][j] == grid[i][j+1] == grid[i+1][j+1]:
                        return True
            return False
        for i in range(3):
            for j in range(3):
                temp = grid[i][j]
                grid[i][j] = 'B' if temp == 'W' else 'W'
                if has2x2Square(grid):
                    return True
                grid[i][j] = temp
        return False
