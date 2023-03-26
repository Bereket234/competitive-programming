class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res= [0] * len(nums)
        def merge(arr1, arr2):
            p1, p2= 0,0
            
            res= []
            while p1 < len(arr1) and p2 < len(arr2):
                idx1= arr1[p1]
                idx2= arr2[p2]
                
                if nums[idx1] < nums[idx2]:
                    res.append(idx1)
                    p1 +=1
                else:
                    res.append(idx2)
                    p2 +=1
                    
            res.extend(arr1[p1:])
            res.extend(arr2[p2:])
            
            return res
                
        
        def count_nums(arr1, arr2):
            p1= p2= 0
            while p1 < len(arr1) and p2 < len(arr2):
                idx1= arr1[p1]
                idx2= arr2[p2]
                if nums[idx1] > nums[idx2]:
                    p2 += 1
                else:
                    res[idx1] += p2
                    p1 += 1
            while p1 < len(arr1):
                idx1= arr1[p1]
                res[idx1] += p2
                p1 += 1
        def divide(start, end):
            if start >= end:
                return [start]
            
            mid= (start + end) // 2
            
            res1= divide(start, mid)
            res2= divide(mid+1, end)
            
            count_nums(res1, res2)
            
            return merge(res1, res2)
            
        divide(0, len(nums)-1)
        return res
            