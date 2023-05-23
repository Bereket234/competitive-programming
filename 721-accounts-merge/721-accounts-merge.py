class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        reps= {}
        
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                reps[accounts[i][j]]= (i, j)
            
        
        def find(node):
            i, j= node
            
            if accounts[i][j] not in reps:
                reps[accounts[i][j]]= (i, j)
            if reps[accounts[i][j]] != (i, j):
                reps[accounts[i][j]] = find(reps[accounts[i][j]])
            return reps[accounts[i][j]]
        
        def union(n1, n2):
            p1= find(tuple(n1))
            p2= find(tuple(n2))
            
            reps[accounts[p2[0]][p2[1]]]= p1
            
            
        par= defaultdict(list)
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])-1):
                union((i,j),(i, j+1))
        for k, v in reps.items():
            x, y= v
            parent= find((x, y))
            par[parent].append(k)
        res= []
        for k , v in par.items():
            x, y= k
            v.sort()
            temp= []
            temp.append(accounts[x][0])
            temp.extend(v)
            res.append(temp)
        return res
        