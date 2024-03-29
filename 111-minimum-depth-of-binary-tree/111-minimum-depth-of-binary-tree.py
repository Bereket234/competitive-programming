# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, level):
            if  not root.left and  not root.right:
                return level
            ans=2**31
            if root.left:
                ans=min(ans, dfs(root.left, level+1))
            if root.right:
                ans=min(ans, dfs(root.right, level+1))
            return ans
        
        if not root: 
            return 0
        return dfs(root, 1)
    