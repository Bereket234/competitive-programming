class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph= defaultdict(list)
        
        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1], succProb[i]))
            graph[edges[i][1]].append((edges[i][0], succProb[i]))
        
        heap= []
        heapq.heapify(heap)
        heapq.heappush(heap, (-1, start_node))
        visited= set()
        
        
        while heap:
            s, node= heapq.heappop(heap)
            if node == end_node:
                return -s
            visited.add(node)
            
            for child in graph[node]:
                if child[0] not in visited:
                    heapq.heappush(heap, (s * child[1], child[0]))
        return 0
        