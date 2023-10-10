# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res= None
        
        def dfs(node):
            nonlocal res
            if not node:
                return False
            left= dfs(node.left)
            right= dfs(node.right)
            curr= node.val == p.val or node.val == q.val
            if ((curr and left) or (curr and right) or (left and right)) and not res:
                res=node
            return curr or right or left
        dfs(root)
        return res
        
        
        return root