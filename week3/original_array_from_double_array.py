class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res= []
        counter= {}
        changed.sort()
        
        print(changed)
        for num in changed:
            if counter.get(num/2,0) > 0:
                res.append(num//2)
                counter[num/2]-=1
            else:
                counter[num]= 1+ counter.get(num,0)
        
        for num in counter:
            if counter[num]>0:
                return []
        return res
                
            