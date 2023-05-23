class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent= [i for i in range(len(stones))]
        rank= [1 for i in range(len(stones))]
        
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            p1= find(n1)
            p2= find(n2)
            
            if rank[p2] > rank[p1]:
                p1, p2 = p2, p1
                
            if rank[p1] == rank[p2]:
                rank[p1]+=1
                
            parent[p2] = p1
            
        count = 0
        for i in range(len(stones)):
            for j in range(len(stones)):
                x1, y1= stones[i]
                x2, y2= stones[j]
                if x1 == x2 or y1 == y2:
                    union(i, j)
        for node, prnt in enumerate(parent):
            if node == prnt:
                count += 1
        
        return len(parent) - count