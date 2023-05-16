class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        deq= deque([["0000", 0]])
        visited= set(deadends)
        
        def children(lock):
            res= []
            
            for i in range(4):
                digit= str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit= str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                
            return res
        
        
        while deq:
            lock, turn = deq.popleft()
            
            
            if lock == target:
                return turn
            for child in children(lock):
                
                if child not in visited:
                    visited.add(child)
                    deq.append([child, turn + 1])
        return -1