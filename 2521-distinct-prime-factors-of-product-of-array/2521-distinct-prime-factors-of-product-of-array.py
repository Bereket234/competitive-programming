class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        fact= set()
        
        for i in range(len(nums)):
            
            d = 2
            n= nums[i]
            while d ** 2 <= n:
                while n % d == 0:
                    fact.add(d)
                    n //= d
                d += 1
            if n > 1:
                fact.add(n)
        return len(fact)