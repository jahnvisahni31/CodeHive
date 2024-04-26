class Solution:
	def FindExitPoint(self, n, m, matrix):
		# Code here
		dir = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def sol(row,col,idx):
            
            if row < 0 or col < 0 or row == n or col == m: return [row,col]
            
            
            if (matrix[row][col] == 1):
                idx = (idx+1)%4
                matrix[row][col] = 0
          
            return sol(row+dir[idx][0],col+dir[idx][1],idx)
                
        ans =  sol(0,0,0) 
        ans[0] =  max(0,min(n-1,ans[0]))
        ans[1] =  max(0,min(m-1,ans[1]))
            
        return ans
