class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        visited= {}
        def winner(l, r, player1):
            if (l,r,player1) in visited:
                return visited[(l,r,player1)]
            if l > r:
                return 0
            if player1:
                visited[(l,r,player1)]= max(nums[l] + winner(l + 1, r, not player1), nums[r] + winner(l, r - 1, not player1))
            else:
                visited[(l,r,player1)]= min((-nums[l] + winner(l + 1, r, not player1)), (-nums[r] + winner(l, r-1, not player1)))
            return visited[(l,r,player1)]
        return winner(0, len(nums)-1, True) >= 0