class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        up= False
        dn= False
        for i in range(len(arr)-1):
            if not up:
                if arr[i] >= arr[i+1]:
                    
                    return False
                else:
                    up =True
            if up:
                if arr[i] == arr[i+1]:
                    return False
                if arr[i] > arr[i+1]:
                    dn = True
            if dn:
                if arr[i] <= arr[i+1]:
                    return False
        return dn
                
                    