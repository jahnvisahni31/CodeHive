class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        l = []
        m = A[-1]
        l.append(m)
        for i in range(len(A) - 2, -1, -1):
            if A[i] >= m:
                m = A[i]
                l.insert(0, A[i])
        return l
