class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent= [i for i in range(n)]
        rank= [1 for i in range(n)]
        minimum= [float('inf') for i in range(n)]
        
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2, d):
            p1= find(n1)
            p2= find(n2)
            
            if rank[p2] > rank[p1]:
                p1, p2 = p2, p1
                
            if rank[p1] == rank[p2]:
                rank[p1]+=1
                
            parent[p2] = p1
            minimum[p1]= min([minimum[p1], minimum[p2], d])
            
        for s, e, d in roads:
            union(s-1, e-1, d)
        
        return minimum[find(0)]
            