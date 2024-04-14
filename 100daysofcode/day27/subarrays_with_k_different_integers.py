class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(nums, k):
            result = 0
            freq = defaultdict(int)
            left = 0

            for right in range(len(nums)):
                if freq[nums[right]] == 0:
                    k -= 1
                freq[nums[right]] += 1

                while k < 0:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        k += 1
                    left += 1

                result += right - left + 1

            return result

        return atMostKDistinct(nums, k) - atMostKDistinct(nums, k - 1)
