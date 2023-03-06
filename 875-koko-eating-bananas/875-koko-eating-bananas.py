class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low= 1
        high= max(piles)
        res= high
        
        while low <= high:
            mid= (low + high) // 2
            cnt= 0
            for pile in piles:
                cnt += math.ceil(pile / mid)
            if cnt > h:
                low= mid + 1
            else:
                res= min(res, mid)
                high= mid - 1
        
        return res