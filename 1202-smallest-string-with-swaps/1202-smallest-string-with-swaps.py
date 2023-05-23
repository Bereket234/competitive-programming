class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent= [i for i in range(len(s))]
        rank= [0 for i in range(len(s))]
        
        def find(node):
            if node != parent[node]:
                parent[node]= find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            parent1= find(node1)
            parent2= find(node2)
            
            if rank[parent1] < rank[parent2]:
                parent1, parent2= parent2, parent1
            
            parent[parent2]= parent1
            rank[parent1] += rank[parent2]
        
        for n1, n2 in pairs:
            union(n1, n2)
        for i in range(len(parent)):
            parent[i] = find(i)
        groups= defaultdict(list)
        for node in range(len(parent)):
            p= find(node)
            groups[p].append(s[node])
        
        for node, group in groups.items():
            groups[node]= sorted(group)
        pointer= [0 for i in range(len(s))]
        res= []
        for i, v in enumerate(parent):
            res.append(groups[v][pointer[v]])
            pointer[v] +=1
        
        return ''.join(res)
            