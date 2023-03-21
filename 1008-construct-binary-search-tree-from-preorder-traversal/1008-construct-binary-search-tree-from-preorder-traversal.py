# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root= TreeNode(preorder[0])      
        def dfs(node, val):
            if not node:
                return TreeNode(val)
        
            if node.val < val:
                node.right= dfs(node.right, val)
            else:
                node.left= dfs(node.left, val)
            return node
        
        for i in range(1,len(preorder)):
            dfs(root, preorder[i])
            
            
        return root