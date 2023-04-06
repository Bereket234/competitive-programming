class Solution:
    def minSteps(self, n: int) -> int:
        facts= []
        
        i = 2
        
        while i ** 2 <= n:
            while n % i == 0:
                facts.append(i)
                n//=i
            i +=1
        
        if n > 1:
            facts.append(n)
        
        sum_= 0
        for i in range(len(facts)):
            sum_ += facts[i]
        
        return sum_