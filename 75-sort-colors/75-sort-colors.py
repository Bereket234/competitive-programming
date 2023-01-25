class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnts= [0, 0, 0]
        for num in nums:
            cnts[num] +=1
        idx= 0
        print(cnts)
        for i,cnt in enumerate(cnts):
            for j in range(cnt):
                nums[idx]= i
                idx+=1