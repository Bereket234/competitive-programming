class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res= [set() for _ in range(n)]
        inbound= [0] * n
        graph = defaultdict(list)
        
        for s, e in edges:
            inbound[e]+=1
            graph[s].append(e)
        
        que= deque([])
        
        for i, c in enumerate(inbound):
            if not c:
                que.append(i)
        
        while que:
            node= que.popleft()
            
            
            for child in graph[node]:
                res[child].update(res[node])
                res[child].add(node)
                inbound[child] -= 1
                if inbound[child] == 0:
                    que.append(child)
        for i in range(n):
            res[i] = list(res[i])
            res[i].sort()
        return res