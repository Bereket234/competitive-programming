class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        temp= 0
        res= 0
        satisfaction.sort()
        print(satisfaction)
        for i in range(len(satisfaction)):
            k= 1
            temp= 0
            for j in range(i, len(satisfaction)):
                temp += (satisfaction[j] * k)
                k+=1
            res= max(temp, res)
        return res