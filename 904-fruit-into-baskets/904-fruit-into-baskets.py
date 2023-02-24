class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basckets= {}
        res= 0
        l=0
        for r,fruit in enumerate(fruits):
            basckets[fruit]= 1+ basckets.get(fruit, 0)
            
            while len(basckets) == 3:
                basckets[fruits[l]] -= 1
                if basckets[fruits[l]] == 0:
                    basckets.pop(fruits[l])
                l+=1
            res= max(res, r-l+1)
        return res
                    