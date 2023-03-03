class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr_sum= [1]
        
        for i in range(rowIndex):
            temp= [0] + curr_sum + [0]
            curr_sum= []
            for j in range(len(temp) -1):
                curr_sum.append(temp[j] + temp[j+1])
        return curr_sum