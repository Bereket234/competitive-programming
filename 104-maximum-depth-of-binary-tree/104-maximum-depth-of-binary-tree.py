# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res= 0
        
        def traverse(node, i):
            nonlocal res
            if not node:
                res= max(res, i)
                return
            
            traverse(node.left, i + 1)
            traverse(node.right, i + 1)
        traverse(root, 0)
        return res