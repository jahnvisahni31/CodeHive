# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mo = [0]
        def dfs(node):
            if not node:
                return 0
            le = dfs(node.left)
            ri = dfs(node.right)
            mo[0] += abs(le)+abs(ri)
            return node.val + le+ri-1
        dfs(root)
        return mo[0]
