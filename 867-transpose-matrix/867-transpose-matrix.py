class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res= [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        print(res)

        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res[j][i]= matrix[i][j]
        return res
