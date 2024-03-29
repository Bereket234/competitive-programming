# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        l_node= self.invertTree(root.left)
        r_node= self.invertTree(root.right)
        root.left= r_node
        root.right= l_node
        
        return root