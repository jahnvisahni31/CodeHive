#User function Template for python3
from collections import deque
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def noSibling(root):
    # code here
    res, q = [], deque([root])
    
    while q:
        top = q.popleft()
        
        if top.left:
            q.append(top.left)
            if top.right:
                q.append(top.right)
            else:
                res.append(top.left.data)
        elif top.right:
            res.append(top.right.data)
            q.append(top.right)
    
    return [-1] if not res else sorted(res)
