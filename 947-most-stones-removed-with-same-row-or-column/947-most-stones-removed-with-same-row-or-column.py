class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        reps= {}
        
        def find(node):
            i, j= node
            
            if (i, j) not in reps:
                reps[(i, j)]= (i, j)
            if reps[(i, j)] != (i, j):
                reps[(i, j)] = find(reps[i, j])
            return reps[(i, j)]
        
        def union(n1, n2):
            p1= find(tuple(n1))
            p2= find(tuple(n2))
            
            reps[p2]= p1
            
            
        res= {}
        for i in range(len(stones)):
            for j in range(len(stones)):
                x1, y1= stones[i]
                x2, y2= stones[j]
                if x1 == x2 or y1 == y2:
                    union(stones[i], stones[j])
        for k in reps:
            v= find(k)
            if v not in res:
                res[v] = 0
            res[v] +=1
        total= 0
        for k, v in res.items():
            total += (v-1)
        return total