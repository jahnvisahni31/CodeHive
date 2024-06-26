# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, path: str):
            nonlocal ans
            path = path + str(node.val)
            if not node.left and not node.right:
                ans += int(path)
            else:
                if node.left: dfs(node.left, path)
                if node.right: dfs(node.right, path)
        dfs(root, "")
        return ans
