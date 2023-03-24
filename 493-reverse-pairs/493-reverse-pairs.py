class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(arr1, arr2):
            p1, p2= 0, 0
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
        
        def divide(start, end):
            if start >= end:
                return [[nums[start]], 0]
            
            mid= (start + end) // 2
            
            left, left_cnt= divide(start, mid)
            right, right_cnt = divide(mid + 1, end)
            
            l, r= 0, 0
            cnt = right_cnt + left_cnt
            while l < len(left) and r < len(right):
                if left[l] > 2 * right[r]:
                    cnt += len(left) - l
                    r += 1
                else:
                    l += 1
            return [merge(left, right), cnt]
        
        return divide(0, len(nums)-1)[1]