
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph= defaultdict(list)
        cnt= [0] * n
        lens= [0] * n
        
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
            cnt[e] += 1
            cnt[s] += 1
            
        deq= deque()
        visited= set()
        
        for i, c in enumerate(cnt):
            if c ==1:
                deq.append(i)
                cnt[i]-=1
        
        i= 0
        while deq:
            size = len(deq)
            for _ in range(size):
                node= deq.popleft()
                lens[node]= i
                for child in graph[node]:
                    cnt[child] -=1
                    if cnt[child] == 1:
                        deq.append(child)
            i +=1
        min_= max(lens)
        res= []
        
        for i, v in enumerate(lens):
            if v == min_:
                res.append(i)
        return res