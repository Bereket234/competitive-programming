class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res= [-1, -1]
        
        for i, point in enumerate(points):
            if point[0] == x or point[1]==y:
                dist= abs(x-point[0]) + abs(y-point[1])
                if res[0] == -1:
                    res= [i, dist]
                else:
                    res= [i, dist] if dist < res[1] else res
        return res[0]
                