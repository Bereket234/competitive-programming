class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res= []
        col= set()
        pos_dig= set()
        neg_dig= set()
        board= [['.' for _ in range(n)] for _ in range(n)]
        
        def backtrack(r):
            if n == r:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in pos_dig or (r - c) in neg_dig:
                    continue
                
                col.add(c)
                neg_dig.add(r - c)
                pos_dig.add(r + c)
                board[r][c]= 'Q'
                
                backtrack(r + 1)
                
                col.remove(c)
                neg_dig.remove(r - c)
                pos_dig.remove(r + c)
                board[r][c]= '.'
        backtrack(0)
        return res