class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n= len(mat), len(mat[0])
        if m*n != c*r:
            return mat
        res=[[0 for _ in range(c)] for _ in range(r)]
        print(res)
        r_ptr, c_ptr= 0, 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[r_ptr][c_ptr]= mat[i][j]
                c_ptr+=1
                if c_ptr >= c:
                    r_ptr+=1
                    c_ptr= 0
        return res