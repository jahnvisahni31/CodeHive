
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        low = 0
        high = n - 1
        
        while low <= high:
            mid = low + (high - low) // 2

            # Check if mid is the closest value
            if arr[mid] == k:
                return arr[mid]
            
            # Update low and high based on the comparison with k
            if arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        # Compare the elements at low and high to find the closest value
        if high < 0:
            return arr[low]
        if low >= n:
            return arr[high]
        
        if abs(arr[low] - k) == abs(arr[high] - k):
            return max(arr[low], arr[high])
        
        return arr[low] if abs(arr[low] - k) < abs(arr[high] - k) else arr[high]

        
