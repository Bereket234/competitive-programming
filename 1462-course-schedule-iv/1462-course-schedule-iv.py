class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph= defaultdict(list)
        cnt= [0] * numCourses
        pres= [set() for i in range(numCourses)]
        
        for p, c in prerequisites:
            graph[p].append(c)
            cnt[c] += 1
        
        deq= deque()
        
        for i, c in enumerate(cnt):
            if not c:
                deq.append(i)
        
        while deq:
            node= deq.popleft()
            
            for child in graph[node]:
                pres[child].update(pres[node])
                pres[child].add(node)
                cnt[child] -=1
                if cnt[child] == 0:
                    deq.append(child)
        res= []
        for p, c in queries:
            if p in pres[c]:
                res.append(True)
            else:
                res.append(False)
        return res
                
                