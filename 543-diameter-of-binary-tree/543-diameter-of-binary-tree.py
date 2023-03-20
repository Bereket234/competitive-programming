# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return [0, 0]
            
            res_l= traverse(node.left)
            res_r= traverse(node.right)
            
            return[1 + max(res_l[0], res_r[0]), max(res_l[1], res_r[1], res_l[0] + res_r[0])]
        return traverse(root)[1]