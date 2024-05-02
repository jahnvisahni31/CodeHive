class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        n = set(nums)
        m = -1
        for nu in nums:
            if -nu in n and nu > m:
                m = nu
        return m if m != -1 else -1
