class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res= []
        
        colors= [0] * len(graph)
        
        def dfs(node):
            if colors[node] == 1:
                return False
            if colors[node] == 2:
                return True
            colors[node]= 1
            
            for neighbour in graph[node]:
                if colors[node] == 2:
                    continue
                    
                if not dfs(neighbour):
                    return False   
            colors[node] = 2
            res.append(node)
            return True
        
        for i in range(len(graph)):
            if colors[i] != 0:
                continue
            dfs(i)
        
        return sorted(res)
                