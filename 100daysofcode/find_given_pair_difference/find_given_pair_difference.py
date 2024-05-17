
from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        
        arr.sort()
        le = 0
        ri = 1
        while le < len(arr) and ri < len(arr):
            if le != ri and arr[ri] - arr[le] == x:
                return 1
            elif arr[ri] - arr[le] < x:
                ri += 1
            else:
                le += 1
        return -1
