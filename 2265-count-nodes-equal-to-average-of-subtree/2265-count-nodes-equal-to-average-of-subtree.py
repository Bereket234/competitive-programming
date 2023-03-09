# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return (0, 0, 0)
            val1= traverse(node.left)
            val2= traverse(node.right)
            sum_= val1[0] + val2[0] + node.val
            avg= sum_ // (val1[1] + val2[1] + 1)
            if node.val == int(avg):
                cnt= val1[2] + val2[2] + 1
            else:
                cnt= val1[2] + val2[2]
            return (sum_, val1[1] + val2[1] + 1, cnt)
        return traverse(root)[2]
        