# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(temp):
            if not temp:
                return None
            if temp.val == val:
                return temp
            if temp.val < val:
                return traverse(temp.right)
            else:
                return traverse(temp.left)
        return traverse(root)
            
            