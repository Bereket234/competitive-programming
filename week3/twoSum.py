class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container = {}
        for i in range(len(nums)):
            if target - nums[i] in container:
                return [i, container[target-nums[i]]]
            container[nums[i]] = i
