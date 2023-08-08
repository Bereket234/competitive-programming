class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            p1= p2= 0
            res= []
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    res.append(arr1[p1])
                    p1 += 1
                else:
                    res.append(arr2[p2])
                    p2 += 1
            res.extend(arr1[p1:])
            res.extend(arr2[p2:])
            return res
            
            
        
        def divide(p1, p2, arr):
            if p1 == p2:
                return [arr[p1]]
            
            mid= (p1 + p2) // 2
            left= divide(p1, mid, arr)
            right= divide(mid + 1, p2, arr)
            
            return merge(left, right)
    
        return divide(0, len(nums)-1, nums)