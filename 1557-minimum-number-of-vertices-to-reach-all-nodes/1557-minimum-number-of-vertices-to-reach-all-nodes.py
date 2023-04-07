class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reached= set()
        max_= -1
        res= []
        
        for edge in edges:
            reached.add(edge[1])
        for i in range(n):
            if i not in reached:
                res.append(i)
        return res