# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traverse(node, p, q):
            if p.val <= node.val <= q.val:
                return node
            if node.val < p.val:
                return traverse(node.right, p, q)
            if node.val > q.val:
                return traverse(node.left, p, q)
        if p.val < q.val:
            return traverse(root, p, q)
        else:
            return traverse(root, q, p)