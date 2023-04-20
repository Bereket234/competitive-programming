# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res= 0
        
        def grandChildrenSum(node, i):
            if not node:
                return 0 
            if i == 2:
                return node.val
            
            left= grandChildrenSum(node.left, i + 1)
            right= grandChildrenSum(node.right, i + 1)
            
            return right + left
        def dfs(node):
            nonlocal res
            if not node:
                return
            
            if node.val % 2 == 0:
                res += grandChildrenSum(node, 0)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res