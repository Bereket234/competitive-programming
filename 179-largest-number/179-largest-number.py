class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]= str(nums[i])
        
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if float(nums[j] + nums[j+1]) < float(nums[j+1] + nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        if int(nums[0])== 0:
            return '0'
        return ''.join(nums)