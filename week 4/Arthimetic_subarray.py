class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res= []
        subArray= []
        check= True
        
        for i  in range(len(l)):
            check= True
            
            subArray= nums[l[i]: r[i]+1]
            
            subArray.sort()
            length=len(subArray)-1
            for i in range(length):
                if subArray[i+1]-subArray[i] == subArray[1]- subArray[0]:
                    pass
                else: 
                    check= False
                    break
            res.append(check)
        return res