# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            
            res1=traverse(p.left, q.left)
            res2=traverse(p.right, q.right)
            return res1 and res2
        return traverse(p, q)