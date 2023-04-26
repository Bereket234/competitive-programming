# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        deq= deque([root])
        res= []
        
        while deq:
            size= len(deq)
            total= 0
            for _ in range(size):
                node= deq.popleft()
                
                total += node.val
                
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            
            res.append(total / size)
        return res
            