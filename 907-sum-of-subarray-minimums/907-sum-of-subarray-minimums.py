class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod= (10**9)+7 
        stack= []
        range_map= [[-1, -1] for i in range(len(arr))]
        
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                idx= stack[-1]
                range_map[idx][1] = i - 1
                range_map[i][0]= range_map[idx][0]
                stack.pop()
            stack.append(i)
            range_map[i][0]= i if range_map[i][0] == -1 else range_map[i][0]
        
        for r in range_map:
            if r[1] == -1:
                r[1]=stack[-1]
        res= 0
        for i,r in enumerate(range_map):
            res += (i - r[0] + 1) * (r[1] - i + 1) * arr[i] 
        return res % mod