class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        t, b=0, len(matrix)-1
        l, r= 0, len(matrix)-1
        while l<r and t<b:
            for i in range(l, r):
                temp= matrix[t][i]
                matrix[t][i] = matrix[-(i+1)][l]
                matrix[-(i+1)][l]= matrix[b][-(i+1)]
                matrix[b][-(i+1)]= matrix[i][r]
                matrix[i][r]= temp
            l+=1
            r-=1
            b-=1
            t+=1
            