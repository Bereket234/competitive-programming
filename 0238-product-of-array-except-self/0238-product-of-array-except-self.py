class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        res= []
        zeros= 0
        for num in nums:
            if num == 0:
                zeros +=1
                continue
            total *= num
        
        if zeros > 1:
            return [0]* len(nums)
        for num in nums:
            if num != 0 and zeros > 0:
                res.append(0)
            elif num != 0 and zeros == 0:
                res.append(total // num)
            else:
                res.append(total)
        return res