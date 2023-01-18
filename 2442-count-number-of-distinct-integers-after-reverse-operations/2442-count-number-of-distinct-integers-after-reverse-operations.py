class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        visited= set(nums)
        cnt= 0
        print(visited)
        
        for num in nums:
            s= str(num)
            s=s[::-1].lstrip('0')
            n= int(s)
            visited.add(n)
        return len(visited)