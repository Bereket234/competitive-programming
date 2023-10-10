# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res= 0
        left= defaultdict(list)
        
        def dfs(node, dep, pos):
            nonlocal res
            if not node:
                return
            if len(left[dep]) == 0:
                left[dep].append(pos)
            res= max(res, pos - left[dep][0] +1)
            dfs(node.left, dep+1, pos*2-1)
            dfs(node.right, dep+1, pos*2)
        dfs(root,0 ,1)
        return res
            