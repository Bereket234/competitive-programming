class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        temp= [0] + self.getRow(rowIndex-1) + [0]
        curr_sum= []
        for j in range(len(temp) -1):
            curr_sum.append(temp[j] + temp[j+1])
        return curr_sum