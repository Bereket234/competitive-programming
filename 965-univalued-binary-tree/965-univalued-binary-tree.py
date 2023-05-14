# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, val):
            if not node:
                return True
            
            if node.val != val:
                return False
            
            
            if not dfs(node.left, node.val):
                return False
            if not dfs(node.right, node.val):
                return False
            return True
            
        if not dfs(root, root.val):
            return False
        return True