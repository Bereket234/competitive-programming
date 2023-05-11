class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap= []
        for row in matrix:
            heap.extend(row)
            
        heapq.heapify(heap)
        for i in range(k):
            val= heapq.heappop(heap)
            
        return val