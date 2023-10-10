class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph= defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        # print(graph)
        res= 0
        visited= set()
        def dfs(node):
            nonlocal res
            temp= 0
            visited.add(node)
            for i, child in enumerate(graph[node]):
                if child not in visited:
                    temp+= dfs(child)
            sum_= values[node] + temp
            # print(node, res, temp, sum_)
            if sum_ % k == 0:
                res += 1
                return 0
            return sum_
        
        dfs(0)
        return res
        
        
            