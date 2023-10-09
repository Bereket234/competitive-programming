# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        mem= {0: 1}
        res = 0
        def dfs(node, sum_):
            nonlocal res
            if not node:
                return 
            sum_ += node.val
            if sum_ - targetSum in mem:
                res += mem[sum_ - targetSum]
            mem[sum_] = mem.get(sum_, 0) + 1
            
            dfs(node.left, sum_)
            dfs(node.right, sum_)
            
            
            mem[sum_] -= 1
            sum_ -= node.val
        dfs(root, 0)
        return res