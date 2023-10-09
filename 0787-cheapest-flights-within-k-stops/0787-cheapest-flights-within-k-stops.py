class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph= defaultdict(list)
        visited= set()
        
        for f,t,p in flights:
            graph[f].append((t, p))
        
        heap= []
        heap.append((0,src,0))
        
        heapq.heapify(heap)
        
        while heap:
            p, t, c= heapq.heappop(heap)
            if t == dst:
                return p
            
            if (c, t) in visited:
                continue
            visited.add((c, t))
            if c <= k:
                for child, price in graph[t]:
                    heapq.heappush(heap, (p+price, child, c+1))
        return -1
        