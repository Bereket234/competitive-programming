class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder= 0
        for seeker in range(len(nums)):
            if nums[seeker] != nums[holder]:
                holder+=1
                nums[holder]= nums[seeker]
        return holder+1
        