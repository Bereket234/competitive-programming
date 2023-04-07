class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph= defaultdict(list)
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        def dfs(node,visited):
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour, visited):
                        return True
            return False
        
        return dfs(source, set())
        
                    
            