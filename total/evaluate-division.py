class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph= defaultdict(list)
        elements= set()
        for i, val in enumerate(equations):
            start,  end= val
            elements.add(start)
            elements.add(end)
            graph[start].append((end, values[i]))
            graph[end].append((start, 1 / values[i]))
        
        def dfs(node, target):
            if node == target:
                return 1
            # if node in visited:
            #     return 
            visited.add(node)
            for child, div in graph[node]:
                if child not in visited:
                    res= dfs(child, target)
                    if res:
                        return res * div
        res= []
        for node, target in queries:
            if node not in elements or target not in elements:
                res.append(float(-1))
                continue
            visited= set()
            temp= dfs(node, target)
            if temp:
                res.append(temp)
            else:
                res.append(float(-1))
        return res