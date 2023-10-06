class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff= []
        a_cnt, b_cnt= 0, 0
        n= len(costs)
        
        for i in range(len(costs)):
            d= abs(costs[i][0] - costs[i][1])
            diff.append((d, i))
        diff.sort(reverse= True)
        res= 0
        for d, i in diff:
            if a_cnt < n//2 and b_cnt < n//2:
                if costs[i][0] < costs[i][1]:
                    a_cnt += 1
                    res += costs[i][0]
                else:
                    b_cnt += 1
                    res += costs[i][1]
            elif a_cnt == n//2 and b_cnt < n//2:
                b_cnt += 1
                res += costs[i][1]
            else:
                a_cnt += 1
                res += costs[i][0]
        return res