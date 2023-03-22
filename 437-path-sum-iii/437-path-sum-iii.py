# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        visited= {0: 1}
        res = 0
        
        def backtrack(node, sum_):
            nonlocal res
            if not node:
                return
            
            sum_ += node.val
            if sum_ - targetSum in visited:
                res += visited[sum_ - targetSum]
            visited[sum_] = 1 + visited.get(sum_, 0)
            
            backtrack(node.left, sum_)
            backtrack(node.right, sum_)
            
            visited[sum_] -= 1
            
        backtrack(root, 0)
        return res
            