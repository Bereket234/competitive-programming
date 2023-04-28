class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def inbound(i, j):
            return i >= 0 and j >= 0 and i < len(board) and j < len(board[0])
        directions= [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        mines_cnt= [[0 for i in range(len(board[0]))] for j in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                for r, c in directions:
                    if inbound(i + r, j + c) and board[i + r][j + c] == "M":
                        mines_cnt[i][j] += 1
        
                        
        
        def dfs(i, j):
            if board[i][j] == "M":
                board[i][j] = "X"
                return 
            if board[i][j]=="E" and mines_cnt[i][j]:
                board[i][j]= str(mines_cnt[i][j])
                return
            if board[i][j]=="E":
                board[i][j]= "B"
            
            for r, c in directions:
                newx= r + i
                newy= c + j
                if inbound(newx, newy) and board[newx][newy] == "E":
                    dfs(newx, newy)
        dfs(click[0], click[1])
        return board
                
                    
                    