class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n+1):
            c = sum(1 for num in nums if num >= i)
            if c == i:
                return i
        return -1
