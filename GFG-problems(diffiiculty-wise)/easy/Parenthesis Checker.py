User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        s = []
        b = {')': '(', ']': '[', '}': '{'}
        for c in x:
            if c in ["(",'[',"{"]:
                s.append(c)
            elif c in [")", "]", "}"]:
                if not s:
                    return False
                elif b[c] != s.pop():
                    return False
        return not s
