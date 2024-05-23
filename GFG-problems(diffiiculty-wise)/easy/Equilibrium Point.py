# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        t = sum(A)
        l = 0
        c = 1
        for nu in A:
            t -= nu
            if t == l:
                return c
            c += 1
            l += nu
        return -1
    
