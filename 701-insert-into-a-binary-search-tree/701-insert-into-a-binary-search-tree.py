# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node):
            if node and node.val > val and (not node.left):
                node.left= TreeNode(val)
                return
            if node and node.val < val and (not node.right):
                node.right= TreeNode(val)
                return
            if not node:
                node = TreeNode(val)
            if node.val < val:
                insert(node.right)
            if node.val > val:
                insert(node.left)

        if root:        
            insert(root)
            return root
        else:
            return TreeNode(val)
            