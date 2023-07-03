class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        s, m= float('inf'), float('inf')
        for num in nums:
            if num < s:
                s= num
            elif num > s and num < m:
                m= num
            elif num > s and num > m:
                return True
        return False