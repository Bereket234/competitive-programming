class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low= max(weights)
        high= sum(weights)
        res= high
        
        while low <= high:
            mid= (low + high) // 2
            cnt= 0
            sum_= 0
            for weight in weights:
                sum_+= weight
                if sum_ > mid:
                    sum_= weight
                    cnt+= 1
                elif sum_ == mid:
                    sum_= 0
                    cnt+=1
            if sum_ != 0:
                cnt+=1
            if cnt <= days:
                res= min(res, mid)
                high= mid - 1
            else:
                low= mid + 1
        return res
                
                
            
        
        