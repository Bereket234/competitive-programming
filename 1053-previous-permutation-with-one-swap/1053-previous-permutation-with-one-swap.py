class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > arr[i+1]:
                min_= [i+1, arr[i+1]]
                for j in range(i + 1, len(arr)):
                    if arr[j] < arr[i] and min_[1] < arr[j]:
                        min_[1]= arr[j]
                        min_[0]= j
                arr[min_[0]], arr[i]= arr[i], arr[min_[0]]
                break
        return arr