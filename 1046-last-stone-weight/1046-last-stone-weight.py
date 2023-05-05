class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        
        while len(stones) > 1:
            stone1= heapq._heappop_max(stones)
            stone2= heapq._heappop_max(stones)
            res= abs(stone1 - stone2)
            if res == 0:
                continue
            heapq.heappush(stones, res)
            heapq._heapify_max(stones)
        if len(stones) < 1:
            return 0
        return stones[0]