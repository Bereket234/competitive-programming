class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime= [1] * (n+1)
        if len(is_prime) > 0:
            is_prime[0]= 0
            if len(is_prime) > 1:
                is_prime[1] = 0
        i=2
        while i ** 2 <= n:
            if is_prime[i]:
                j= i ** 2
                while j <= n:
                    is_prime[j] = 0
                    j += i
            i += 1
        cnt= 0
        for i in range(n):
            if is_prime[i]:
                cnt+= 1
        
        return cnt