class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        relations= defaultdict(list)
        res= 0
        visited= set()
        
        for i, node in enumerate(parent):
            if node != -1 and s[i] != s[node]:
                relations[node].append(i)
        
        def dfs(node, parent):
            nonlocal res
            curr= []
            if node not in relations:
                return 1
            
            visited.add(node)
            
            for child in relations[node]:
                if node == -1:
                    prev= "A"
                else:
                    prev= s[node]
                curr.append(dfs(child, prev))
            
            max1, i1 = 0, 0
            max2 = 0
            for i in range(len(curr)):
                if curr[i] > max1:
                    i1= i
                    max1 = curr[i]
            
            for i in range(len(curr)):
                if curr[i] > max2 and i != i1:
                    max2= curr[i]
                    
            res= max(res, max1 + max2 + 1)
            
            return 1 + max1
        for k in relations:
            if k not in visited:
                dfs(k, "A")
        
        return res if res else 1