class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n= len(matrix), len(matrix[0])
        l, h= 0, m*n-1
        mid_= math.floor((h+l)/2)
        
        while l <= h:
            mid= math.floor((h+l)/2)
            i, j=  mid // n, mid % n
            val= matrix[i][j]
            
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l= mid +1
            else:
                h= mid -1
            
        return False