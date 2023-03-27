class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        diff_= [nums1[i] - nums2[i] for i in range(len(nums1))]
        res= 0
        def merge(arr1, arr2):
            p1, p2= 0, 0
            res= []
            
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    res.append(arr1[p1])
                    p1+=1
                else:
                    res.append(arr2[p2])
                    p2+=1
            res.extend(arr1[p1:])
            res.extend(arr2[p2:])
            return res
        
        def count(arr1, arr2):
            p1, p2= 0, 0
            nonlocal res
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] <= diff + arr2[p2]:
                    res += len(arr2) - p2
                    p1 += 1
                else:
                    p2 +=1
                    
        def divide(start, end):
            if start >= end:
                return [diff_[start]]
            
            mid= (start + end) // 2
            res1= divide(start, mid)
            res2= divide(mid + 1, end)
            
            count(res1, res2)
            return merge(res1, res2)
        
        divide(0, len(nums1) -1)
        return res