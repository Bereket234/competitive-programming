class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        color= [0 for i in range(len(edges))]
        
        graph= defaultdict(list)
        cycles= [-1 for i in range(len(edges))]
        curr= None
        cnts= {}
        def dfs(node, cnt):
            nonlocal curr
            if edges[node] == -1:
                return
            if color[node]== 1:
                curr= cnt - cnts[node]
                return
            cnts[node]= cnt
            if color[node] != 2:
                color[node] =1
            if color[node] != 2:
                dfs(edges[node], cnt+1)
                
            color[node] =2
        
        for i in range(len(edges)):
            if color[i] ==2:
                continue
            curr== 0
            dfs(i, 0)
            
            if curr:
                cycles[i]= curr
        print(cycles)
        return max(cycles)