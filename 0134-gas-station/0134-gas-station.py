class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            gas[i]= gas[i] - cost[i]        
        if sum(gas) < 0:
            return -1
        
        res= -1
        total= 0
        for i in range(len(gas)):
            total+=gas[i]
            if res == -1:
                res = i
            if total < 0:
                res= -1
                total= 0
        
        return res