# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph= defaultdict(list)
        
        visited= set()
        def dfs(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)
        deq= deque([[target.val, 0]])
        res= []
        if k == 0:
            return [target.val]
        while deq:
            node, d= deq.popleft()
            
            for n in graph[node]:
                if n not in visited and d + 1 == k and n != target.val:
                    res.append(n)
                    continue
                    
                if n not in visited:
                    deq.append([n, d + 1])
                    visited.add(n)
        return res
        