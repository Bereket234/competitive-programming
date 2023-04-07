class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        paths= defaultdict(set)
        cnt= 0
        
        for road in roads:
            paths[road[0]].add(road[1])
            paths[road[1]].add(road[0])
        for i in range(n):
            for j in range(i+1, n):
                if j in paths[i]:
                    cnt= max(cnt, len(paths[j]) + len(paths[i]) - 1)
                else:
                    cnt= max(cnt, len(paths[j]) + len(paths[i]))
                    
        return cnt