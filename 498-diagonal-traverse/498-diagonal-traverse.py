class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res= []
        cnt= defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                cnt[i+j].append(mat[i][j])
        
        for i, v in cnt.items():
            if i % 2 == 0:
                for num in range(len(v)-1, -1, -1):
                    res.append(v[num])
            else:
                for num in v:
                    res.append(num)
        return res