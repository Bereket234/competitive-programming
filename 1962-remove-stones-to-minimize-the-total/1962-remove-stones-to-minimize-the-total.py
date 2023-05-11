class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles= [-i for i in piles]
        heapq.heapify(piles)
        i= 0
        for i in range(k):
            val= heapq.heappop(piles)
            if val == 0:
                break
            val = ceil((val * -1)/2)
            heapq.heappush(piles, -val)
        return sum(piles) * -1