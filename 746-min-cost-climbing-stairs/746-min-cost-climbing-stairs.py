class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n= len(cost)
        one, two= cost[n-2], cost[n-1]
        
        for i in range(n-3, -1, -1):
            temp= two
            two= one
            one= min(cost[i] + one, cost[i] + temp)
        return min(one , two)
            