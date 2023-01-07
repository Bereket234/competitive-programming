class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        #map the numbers to inxdex to find element in O(1) time complexity
        indices_map= {}
        for i, num in enumerate(nums):
            indices_map[num]= i
        
        #block to find element in hashmap and change the element in list
        for operation in operations:
            index= indices_map[operation[0]]
            nums[index]= operation[1]
            indices_map[operation[1]]= index
        return nums
            