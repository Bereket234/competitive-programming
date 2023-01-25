class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def rev(end):
            l= 0
            while l < end:
                arr[end], arr[l]= arr[l], arr[end]
                l+=1
                end-=1
        res= []
        for i in range(len(arr)-1, -1, -1):
            max_= i
            for j in range(i, -1, -1):
                if arr[j] > arr[max_]:
                    max_= j
            if max_ != i:
                rev(max_)
                rev(i)
                res.append(max_+1)
                res.append(i+1)
        return res