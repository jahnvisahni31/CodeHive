
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        
        #code here
        v_sums = {}
        def traverse(node, hd):
            nonlocal v_sums
            if not node:
                return
            v_sums[hd] = v_sums.get(hd, 0) + node.data
            traverse(node.left, hd - 1)
            traverse(node.right, hd + 1)
        traverse(root, 0)
        return [v_sums[hd] for hd in sorted(v_sums.keys())]
        
