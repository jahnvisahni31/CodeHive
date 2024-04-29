class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xo_al = 0
        def countb(n):
            c = 0
            while(n):
                n &= (n-1)
                c += 1
            return c
        for nu in nums:
            xo_al ^= nu
        xo = xo_al ^ k
        return countb(xo)
        
