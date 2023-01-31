class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_= max(piles)
        res= max_
        
        low, high= 1, max_
        
        mid= (low+high)//2
        
        while low <= high:
            mid= (low+high)//2
            time= 0
            
            for pile in piles:
                time += math.ceil(pile / mid)
            if time > h:
                low= mid +1
            else:
                res= min(res, mid)
                high= mid-1
        return res
                
            