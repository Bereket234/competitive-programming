class Solution:
    """
    function that takes 3 elements and return the winner
    """
    def check_winner(self, elts: str) -> bool:
        for i in range(1, len(elts)):
            if elts[i] != elts[i-1]:
                return False
        return True
    """
    function that returns winners as an array array 0 is if X win
    and array 1 is if O win
    """
    def verify_winner (self, board: List[str]) -> list:
        #loop to chech if there is a winner in rows
        res= [0,0]
        
        for i in range(len(board)):
            
            if self.check_winner(board[i]):
                if board[i][0] == 'X':
                    res[0]=1
                elif board[i][0] == 'O':
                    res[1] = 1
                
            if self.check_winner([board[0][i],board[1][i],board[2][i]]):
                if board[0][i] == 'X':
                    res[0]=1
                elif board[0][i] == 'O':
                    res[1] = 1
        diagonal= board[0][0] +  board[1][1] + board[2][2]
        if self.check_winner(diagonal):
                if board[0][0] == 'X':
                    res[0]=1
                elif board[0][0] == 'O':
                    res[1] = 1
        diagonal= board[0][2] +  board[1][1] + board[2][0]
        if self.check_winner(diagonal):
                if board[0][2] == 'X':
                    res[0]=1
                elif board[0][2] == 'O':
                    res[1] = 1
        return res
    def validTicTacToe(self, board: List[str]) -> bool:
        count= defaultdict(int)
        
        for row in board:
            for col in row:
                count[col]= 1 + count[col]
        if not(count['O'] + 1 == count['X'] or count['X'] == count['O']):
            return False
        winner= self.verify_winner(board)
        if winner[0] ==1 and winner[1]== 1:
            return False
        if winner[0] == 1 and count['O'] == count['X']:
            return False
        if winner[1] ==1 and count['X'] > count['O']:
            return False
        return True
        
        