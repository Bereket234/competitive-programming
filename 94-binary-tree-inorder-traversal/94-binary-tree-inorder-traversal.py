# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        def traverse(temp):
            if not temp:
                return
            traverse(temp.left)
            res.append(temp.val)
            traverse(temp.right)
            res.append(temp.val)
            res.pop()
        traverse(root)
        return res