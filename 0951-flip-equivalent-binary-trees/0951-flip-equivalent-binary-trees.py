# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        graph1= defaultdict(list)
        graph2= defaultdict(list)
        def dfs(node, parent, graph):
            if not node:
                return 
            
            graph[parent].append(node.val)
            dfs(node.left, node.val, graph)
            dfs(node.right, node.val, graph)
        
        dfs(root1, -1, graph1)
        dfs(root2, -1, graph2)
        if len(graph1) != len(graph2):
            return False
        for k, v in graph1.items():
            if set(v) != set(graph2[k]):
                return False
        return True