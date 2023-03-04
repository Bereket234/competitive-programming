class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res= [-1 for i in range(len(nums))]
        stack= []
        n= len(nums)
        for i in range((len(nums) * 2) - 1):
            while stack and nums[stack[-1]] < nums[i%n]:
                res[stack[-1]]= nums[i%n]
                stack.pop()
            stack.append(i%n)
        return res