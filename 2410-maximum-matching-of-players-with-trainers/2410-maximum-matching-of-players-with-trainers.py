class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i, j= 0, 0
        res= 0
        players.sort()
        trainers.sort()
        while i < len(players)  and j < len(trainers):
            if players[i] <= trainers[j]:
                res+=1
                i+=1
                
            j+=1
        return res