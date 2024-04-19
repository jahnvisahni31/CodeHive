# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        # Your code here
        t = sum(A)
        su = 0
        for i in range(len(A)):
            if su == t - (su + A[i]):
                return i+1
            su += A[i]
        return -1
