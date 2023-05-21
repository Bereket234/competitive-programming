class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        inbound= [0] * len(quiet)
        graph= defaultdict(list)
        g_cnt= [set() for i in range(len(quiet))]
        res= []
        
        for g, s in richer:
            inbound[s] += 1
            graph[g].append(s)
        
        que= deque()
        
        for i, v in enumerate(inbound):
            if not v:
                que.append(i)
        
        while que:
            node= que.popleft()
            
            for child in graph[node]:
                g_cnt[child].update(g_cnt[node])
                g_cnt[child].add(node)
                inbound[child] -=1
                if not inbound[child]:
                    que.append(child)
        
        for i in range(len(g_cnt)):
            if not g_cnt[i]:
                res.append(i)
                continue
            min_= i
            for c in g_cnt[i]:
                if quiet[min_] > quiet[c]:
                    min_= c
            res.append(min_)
        return res
        