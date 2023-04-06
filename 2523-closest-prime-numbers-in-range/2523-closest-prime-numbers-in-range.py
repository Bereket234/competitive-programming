class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime= [1] * (right + 1)
        
        i= 2
        while i **2 <= right:
            if is_prime[i]:
                j= i * i
                while j <= right:
                    is_prime[j]= 0
                    j +=i
            i+=1
        
        res= [-1, -1]
        left= left if left != 1 else 2
        prev= None
        cnt= right - left + 1
        for i in range(left, right +1):
            if is_prime[i]:
                if prev != None and cnt > i - prev:
                    res= [prev, i]
                    cnt= i- prev
                    prev= i
                else:
                    prev= i
        
        return res
                    
                