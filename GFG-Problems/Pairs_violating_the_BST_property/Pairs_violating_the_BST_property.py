from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def pairsViolatingBST(self, n : int, root : Optional['Node']) -> int:
        # code here
        s = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            s.append(node.data)
            inorder(node.right)
        inorder(root)
        
        ans = 0
        def mergesort(arr):
            nonlocal ans
            if len(arr) <= 1:
                return arr
                
            mi = len(arr)//2
            a = mergesort(arr[:mi])
            b = mergesort(arr[mi:])
            i, j, ret = 0, 0, []
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    ret.append(a[i])
                    i += 1
                else:
                    ans += len(a)-i
                    ret.append(b[j])
                    j += 1
            if i < len(a):
                ret.extend(a[i:])
            if j < len(b):
                ret.extend(b[j:])
            return ret
        mergesort(s)
        return ans
