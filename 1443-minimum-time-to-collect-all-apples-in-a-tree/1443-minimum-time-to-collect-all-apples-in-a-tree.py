class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph= defaultdict(list)
        seen= set()
        
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        def dfs(node):
            cnt= 0
            if node not in graph:
                if hasApple[node] and node != 0:
                    return 2
                return 0
            seen.add(node)
            for child in graph[node]:
                if child not in seen:
                    cnt+= dfs(child)
                
            if cnt or hasApple[node]:
                if node == 0:
                    return cnt
                return cnt + 2
            else:
                return 0
        return dfs(0)
        