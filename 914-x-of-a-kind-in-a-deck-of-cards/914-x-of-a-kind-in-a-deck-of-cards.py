class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter= Counter(deck)
        vals= list(counter.values())
        gcd= vals[0]
        
        def calc_gcd(a, b):
            a, b = min(a, b), max(a, b)
            i = a
            while a > 1 and i >= 2:
                if a % i == 0 and b % i== 0:
                    return i
                i-=1
            return 1
        
        for i in range(1, len(vals)):
            res= calc_gcd(gcd, vals[i]) 
            if res == 1:
                return False
            gcd= res
            
        return gcd != 1
            
