class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges= []
        parent= [i for i in range(len(points))]
        rank= [0 for i in range(len(points))]
        
        def find(node):
            if node != parent[node]:
                parent[node]= find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            p1= find(n1)
            p2= find(n2)
            
            if rank[p2] > rank[p1]:
                p1, p2= p2, p1
            
            parent[p2]= p1
            rank[p1] += rank[p2]
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1= points[i]
                x2, y2= points[j]
                d= abs(x1 - x2) + abs(y1 - y2)
                edges.append((d, i, j))
        edges.sort()
        res= 0
        cnt= 0
        for i in range(len(edges)):
            d, n1, n2= edges[i]
            p1, p2= find(n1), find(n2)
            if cnt == len(edges):
                break
            if p1 != p2:
                union(n1, n2)
                # print(p1, p2, n1, n2, d)
                cnt+=1
                res += d
        return res
            