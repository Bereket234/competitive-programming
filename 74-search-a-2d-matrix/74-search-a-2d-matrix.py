class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if len(row) > 0 and row[0] <= target and row[-1] >= target:
                for num in row:
                    if num == target:
                        return True
        return False