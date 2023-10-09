# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        temp= []
        res= []
        def dfs(node, sum_):
            if not node:
                return
            sum_ += node.val
            temp.append(node.val)
            dfs(node.left, sum_)
            
            dfs(node.right, sum_)
            if not node.right and not node.left:
                print(node.val, temp, sum_)
                if sum_ ==  targetSum and temp:
                    res.append(temp.copy())
            sum_ -= node.val
            temp.pop()
        dfs(root, 0)
        return res
            
                