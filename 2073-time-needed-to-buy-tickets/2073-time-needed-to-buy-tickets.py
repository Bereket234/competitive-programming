class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res= 0
        
        for i in range(len(tickets)):
            ticket = tickets[i]
            
            if i <= k:
                res+= min(ticket, tickets[k])
                
            else:
                res += min(ticket, tickets[k]-1)
        return res