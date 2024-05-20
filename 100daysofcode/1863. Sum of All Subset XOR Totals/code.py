 

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        t = 0
        for r in range(len(nums)+1):
            for s in combinations(nums,r):
                x = 0
                for nu in s:
                    x ^= nu
                t += x

        return t
