class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        locked= [1] * len(rooms)
        deq= deque([0])
        locked[0] = 0
        
        while deq:
            node= deq.popleft()
            
            for key in rooms[node]:
                if locked[key]:
                    deq.append(key)
                    locked[key] = 0
        print(locked)
        for room in locked:
            if room:
                return False
        return True
                
                    
                