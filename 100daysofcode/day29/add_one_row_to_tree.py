# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def dfs(node, level):
            if not node:
                return
            if level == depth - 1:
                left_node = TreeNode(val)
                right_node = TreeNode(val)
                left_node.left = node.left
                right_node.right = node.right
                node.left = left_node
                node.right = right_node
            else:
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)
        
        dfs(root, 1)
        return root
        
