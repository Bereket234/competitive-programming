# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map= defaultdict(list)
        def traverse(node, row, col):
            if not node:
                return
            col_map[col].append([row, node.val])
            traverse(node.left, row + 1, col - 1)
            traverse(node.right, row + 1, col + 1)
            
        traverse(root, 0, 0)
        keys= sorted(col_map)
        res= []
        for key in keys:
            res.append(col_map[key])
        for i, elt in enumerate(res):
            res[i]= sorted(elt, key= lambda x:x[1])
        for i, elt in enumerate(res):
            res[i]= sorted(elt)
        ans= [[res[j][i][1] for i in range(len(res[j]))] for j in range(len(res))]
            
        return ans