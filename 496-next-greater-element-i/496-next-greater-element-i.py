class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack= []
        visited= {}
        res= []
        for i,num in enumerate(nums2):
            while stack and stack[-1] < num:
                visited[stack[-1]]= num
                stack.pop()
            stack.append(num)
        
        for num in nums1:
            res.append(visited.get(num, -1))
        return res
            
        