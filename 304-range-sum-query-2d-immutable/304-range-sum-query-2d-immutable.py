class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r,c = len(matrix), len(matrix[0])
        
        self.pre_sum= [[0 for _ in range(c+1)]for _ in range(r+1)]
        
        
        for i in range(r):
            for j in range(c):
                self.pre_sum[i+1][j+1]= self.pre_sum[i+1][j] + self.pre_sum[i][j+1] - self.pre_sum[i][j] + matrix[i][j]
        
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2= row1, row2, col1, col2
        sum_= self.pre_sum
        
        return sum_[r2+1][c2+1] + sum_[r1][c1] - sum_[r2+1][c1] - sum_[r1][c2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)