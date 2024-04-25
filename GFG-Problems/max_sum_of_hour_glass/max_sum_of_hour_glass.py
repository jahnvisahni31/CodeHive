class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        ma = -1
        n, m = len(mat), len(mat[0])
        for i in range(n-2):
            for j in range(m-2):
                cu = (
                    mat[i][j] + mat[i][j+1] + mat[i][j+2] + 
                    mat[i+1][j+1] + 
                    mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
                )  # Calculate sum of current hourglass
                ma = max(ma, cu)
        return ma
        
