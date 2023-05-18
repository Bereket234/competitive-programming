class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        reps= [i for i in range(len(edges))]
        res= []
        def find_rep(node):
            parent= node
            
            while parent != reps[parent]:
                parent= reps[parent]
            return parent
        
        for s, d in edges:
            srep= find_rep(s-1)
            drep= find_rep(d-1)
            if srep == drep:
                res= [s, d]
            
            reps[drep]= srep
        
        return res
            
            