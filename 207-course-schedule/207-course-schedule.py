class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cnt= [0] * numCourses
        
        graph= defaultdict(list)
        
        for p, c in prerequisites:
            graph[p].append(c)
            cnt[c] += 1
        
        deq= deque([])
        
        for i, c in enumerate(cnt):
            if not c:
                deq.append(i)
        while deq:
            node= deq.popleft()
            
            for child in graph[node]:
                cnt[child] -= 1
                if cnt[child] == 0:
                    deq.append(child)
        
        for c in cnt:
            if c:
                return False
        return True
        