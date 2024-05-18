from typing import List

class Solution:
	def findPeakElement(self, a):
		# Code here
		l = 0
        r = len(a) - 1
        while l < r:
            mid = l + (r - l) // 2
            if a[mid] > a[mid + 1]:
                r = mid
            else:
                l = mid + 1
        
        return a[l]
