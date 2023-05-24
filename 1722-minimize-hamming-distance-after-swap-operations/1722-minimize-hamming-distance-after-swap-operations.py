class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        parent= [i for i in range(len(source))]
        rank= [0 for i in range(len(source))]
        s_group= defaultdict(list)
        t_group= defaultdict(list)
        
        
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
            
        
        for n1, n2 in allowedSwaps:
            union(n1, n2)
        
        for i in range(len(parent)):
            p= find(i)
            s_group[p].append(source[i])
            t_group[p].append(target[i])
        res= 0
        
        for k in s_group:
            s_group[k].sort()
            t_group[k].sort()
   
        for k in s_group:
            n1, n2= len(s_group[k]),len(t_group[k])
            i= 0
            j= 0
            while i < n1 and j < n2:
                if s_group[k][i] == t_group[k][j]:
                    i+=1
                    j+=1
                    res +=1
                    continue
                elif s_group[k][i] < t_group[k][j]:
                    i+=1
                else:
                    j+=1
                
        return len(source) - res
            
            
            