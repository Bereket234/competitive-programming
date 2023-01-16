class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols= defaultdict(list)
        rows= defaultdict(list)
        grid= defaultdict(list)
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                val= board[i][j]
                if val in rows[i] or val in cols[j] or val in grid[(i//3, j//3)]:
                    return False
                if val != ".":
                    cols[j].append(val)
                    rows[i].append(val)
                    grid[(i//3, j//3)].append(val)
        return True