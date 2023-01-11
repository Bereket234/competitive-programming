class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players= [i for i in range(1, n+1)]
        i= k-1
        while len(players) > 1:
            players.pop(i)
            i= (i + k-1) % len(players)
        return players[0]