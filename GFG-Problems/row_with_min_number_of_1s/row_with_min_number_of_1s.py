class Solution:
    def minRow(self,n,m,a):
        #code here
        min_count = m + 1
        min_row = 0
        
        for i in range(n):
            ones_count = 0
            for j in range(m):
                if a[i][j] == 1:
                    ones_count += 1
            
            if ones_count < min_count:
                min_count = ones_count
                min_row = i + 1  # Adjusting to 1-based indexing
        
        return min_row
        
