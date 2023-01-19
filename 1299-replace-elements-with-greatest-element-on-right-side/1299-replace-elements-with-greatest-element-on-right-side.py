class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_= 0
        for i in range(len(arr)-1, -1, -1):
            temp= arr[i]
            if max_== 0:
                arr[i]= -1
            else:
                arr[i]= max_
            max_= max(temp, max_)
        return arr