# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count= {}
        
        def traverse(node):
            if not node:
                return node
            traverse(node.left)
            
            count[node.val]= 1 + count.get(node.val, 0)
            traverse(node.right)
        traverse(root)
        keys = sorted(count, key= lambda x: count[x])
        keys.reverse()
        res= [keys[0]]
        for i in range(1, len(keys)):
            if count[res[-1]]== count[keys[i]]:
                res.append(keys[i])
        return res