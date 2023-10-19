class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff= nums[-1] - nums[0]
        if diff <= 2 * k:
            return 0
        return diff - (2 * k)
        