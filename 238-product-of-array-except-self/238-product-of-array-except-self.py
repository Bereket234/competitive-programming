class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev_prod=[1]
        
        for num in nums:
            prev_prod.append(num * prev_prod[-1])
        prod= 1
        
        for i in range(len(nums)-1, -1, -1):
            num= nums[i]
            nums[i]= prod * prev_prod[i]
            prod *= num
        return nums