class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph= defaultdict(list)
        cnt= [0]*n
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node, end):
            if node == end:
                cnt[node] += 1
                return True
            visited.add(node)
            curr = False
            for child in graph[node]:
                if child not in visited:
                    ans = dfs(child, end)
                    curr = curr or ans
                    if ans:
                        cnt[node] +=1 
            return curr
                        
        for trip in trips:
            visited= set()
            dfs(trip[0], trip[1])
        def dp(node):
            curr= [price[node] * cnt[node] /2, price[node] * cnt[node]]
            
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    prev= dp(child)
                    curr= [curr[0] + prev[1], curr[1] + min(prev)]
            return curr
        visited= set()
        
        return int(min(dp(0)))