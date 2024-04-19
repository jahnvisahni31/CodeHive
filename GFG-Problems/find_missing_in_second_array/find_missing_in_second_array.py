
class Solution:
    def findMissing(self,a,b,n,m):
        set_v = set(b)
        re = []
        for nu in a:
            if nu not in set_v:
                re.append(nu)
            
        return re
