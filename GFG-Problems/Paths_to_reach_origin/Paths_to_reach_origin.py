class Solution:
    def ways(self, n,m):
        #write you code here
        MOD = 1000000007
        paths = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n+1):
            paths[i][0] = 1
        for j in range(m+1):
            paths[0][j] = 1
        for i in range(1, n+1):
            for j in range(1, m+1):
                paths[i][j] = (paths[i-1][j] + paths[i][j-1]) % MOD
        return paths[n][m]
