
from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        paths = [] 
        def find_paths_recursive(node, current_path):
            if not node:
                return
            current_path.append(str(node.data))

            if not node.left and not node.right:  
                paths.append(current_path)  
            else:
                find_paths_recursive(node.left, current_path.copy())
                find_paths_recursive(node.right, current_path.copy()) 
                
        find_paths_recursive(root, [])

        return paths
            
