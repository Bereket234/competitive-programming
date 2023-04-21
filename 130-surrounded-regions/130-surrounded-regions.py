class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        seen= [[1 for _ in range(len(board[0]))] for _ in range(len(board))]
        paths= [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def inbound(i, j):
            return i >= 0 and j >= 0 and i < len(board) and j < len(board[0])
        def dfs(i, j):
            seen[i][j]= 0
            
            for path in paths:
                newi= i + path[0]
                newj= j + path[1]
                
                if inbound(newi, newj) and seen[newi][newj] and board[newi][newj] == 'O':
                    dfs(newi, newj)
        for i in range(len(board)):
            if seen[i][0] and board[i][0] == "O":
                dfs(i, 0)
        for i in range(len(board)):
            if seen[i][len(board[0]) -1] and board[i][len(board[0]) -1] == "O":
                dfs(i, len(board[0]) -1)
        for i in range(len(board[0])):
            if seen[0][i] and board[0][i] == "O":
                dfs(0, i)
        for i in range(len(board[0])):
            if seen[len(board) -1][i] and board[len(board)-1][i] == "O":
                dfs(len(board) -1, i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if seen[i][j]:
                    board[i][j]= "X"
                else:
                    board[i][j]= "O"