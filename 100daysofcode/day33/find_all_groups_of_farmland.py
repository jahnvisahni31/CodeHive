class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n, res = len(land), len(land[0]), []
        for i in range(m):
            j = 0
            while j < n:
                if land[i][j] < 0:
                    j = -land[i][j]
                elif land[i][j] == 1:
                    k, l = j+1, i+1
                    while k < n and land[i][k]==1: k += 1
                    k += 1
                    while l < m and land[l][j]==1:
                        land[l][j] = -k
                        l += 1
                    if l < m:
                        land[l][j] = 1-k
                    res.append([i,j,l-1,k-2])
                    j = k
                else:
                    j += 1
        return res
