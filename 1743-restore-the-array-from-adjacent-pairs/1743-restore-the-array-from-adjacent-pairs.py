class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph= defaultdict(list)
        
        for s, e in adjacentPairs:
            graph[s].append(e)
            graph[e].append(s)
        
        visited= set()
        res= []
        for k in graph:
            if len(graph[k]) == 1:
                visited.add(k)
                res.append(k)
                break
        def dfs(node):
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    res.append(child)
                    dfs(child)
        
        
        dfs(res[0])
        return res
        