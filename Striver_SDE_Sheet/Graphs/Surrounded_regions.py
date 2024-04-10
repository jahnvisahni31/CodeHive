class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(x, y):
            board[x][y] = '#' 
            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= x2 < m and 0 <= y2 < n and board[x2][y2] == 'O':
                    dfs(x2, y2)

        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n-1] == 'O': dfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)
            if board[m-1][j] == 'O': dfs(m-1, j)
        for l in range(m):
            for o in range(n):
                if board[l][o] == 'O':
                    board[l][o] = 'X'
                elif board[l][o] == '#':
                    board[l][o] = 'O'
