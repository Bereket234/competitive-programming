class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff= []
        for i in range(len(costs)):
            costa, costb= costs[i]
            diff.append((costa- costb, i))
        diff.sort()
        res= 0
        for i in range(len(diff) // 2):
            d, j= diff[i]
            res += costs[j][0]
        
        for i in range(len(diff) // 2, len(costs)):
            d, j= diff[i]
            res += costs[j][1]
        return res