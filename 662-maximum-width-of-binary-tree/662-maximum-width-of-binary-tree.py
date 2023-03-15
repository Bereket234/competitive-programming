# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_width= 0
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        left= defaultdict(list)
        def traverse(node, dep, pos):
            if not node:
                return
            if len(left[dep]) == 0:
                left[dep].append(pos)
            self.max_width= max(self.max_width, pos - left[dep][0] + 1)
            
            traverse(node.left, dep + 1, pos * 2)
            traverse(node.right, dep + 1, pos * 2 + 1)
            
            
        traverse(root, 0, 0)
        return self.max_width