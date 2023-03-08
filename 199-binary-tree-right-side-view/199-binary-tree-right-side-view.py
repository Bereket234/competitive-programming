# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res= defaultdict(list)
        def traverse(node, row):
            if not node:
                return
            if 0 < len(res[row]):
                res[row].pop()
            res[row].append(node.val)
            traverse(node.left, row + 1)
            traverse(node.right, row + 1)
        traverse(root, 0)
        return [v[0] for k, v in res.items()]