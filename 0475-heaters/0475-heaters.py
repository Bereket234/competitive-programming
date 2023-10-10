class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if len(houses) == 1 and len(heaters) == 1:
            return abs(houses[i] - heaters[j])
        res= [float('inf')]*len(houses)
        
        houses.sort()
        heaters.sort()
        i= 0
        print(heaters)
        j = 0
        res[0]= (abs(houses[i] - heaters[j]))
        # i+=1
        while i < len(houses) and j < len(heaters):
            # print(i, j)
            if houses[i] < heaters[j]:
                res[i]= min(res[i], abs(heaters[j]- houses[i]))
                if i != 0:
                    res[i]= min(res[i], res[i-1] + (houses[i] - houses[i-1]))
                i+=1
            elif houses[i] >= heaters[j]:
                res[i] = min(res[i], abs(heaters[j] - houses[i]))
                j+=1
        print(res)
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i]= res[i-1] + (houses[i] - houses[i-1])
        return max(res)
        