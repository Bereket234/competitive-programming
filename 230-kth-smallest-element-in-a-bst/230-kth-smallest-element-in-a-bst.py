# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    k= 0
    res= None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k= k
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            self.k -= 1
            if self.k == 0:
                self.res= node.val
            traverse(node.right)
        traverse(root)   
        return self.res