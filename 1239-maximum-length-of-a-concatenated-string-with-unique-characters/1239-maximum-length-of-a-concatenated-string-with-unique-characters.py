class Solution:
    def maxLength(self, arr: List[str]) -> int:
        visited= set()
        
        def overlap(curr):
            prev= visited.copy()
            for c in curr:
                if c in prev:
                    return False
                prev.add(c)
            return True
                
            
        def backtrack(i):
            if i == len(arr):
                return len(visited)
            
            res= 0
            
            if overlap(arr[i]):
                for c in arr[i]:
                    visited.add(c)
                
                res= backtrack(i+1)
                for c in arr[i]:
                    visited.remove(c)
                    
            return max(res, backtrack(i+1))
        
        return backtrack(0)