# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None: 
            return bool(root.val)
        left_result = self.evaluateTree(root.left)  # Added self reference
        right_result = self.evaluateTree(root.right)  # Added self reference
        if root.val == 2:  # OR operation
            return left_result or right_result
        elif root.val == 3:  # AND operation
            return left_result and right_result
        else:
            return False  # Invalid node value
