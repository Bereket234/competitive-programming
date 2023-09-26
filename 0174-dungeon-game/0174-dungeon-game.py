class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def inbound(i, j):
            return i >= 0 and j>= 0 and i < len(dungeon) and j < len(dungeon[0])
        for i in range(len(dungeon)-1, -1, -1):
            for j in range(len(dungeon[0])-1, -1, -1):
                if inbound(i+1, j) and inbound(i, j+1):
                    sum_= max(dungeon[i+1][j], dungeon[i][j+1])
                    sum_ += dungeon[i][j]
                    if sum_ < 0:
                        dungeon[i][j] = sum_
                    else:
                        dungeon[i][j] = 0
                elif (not inbound(i+1, j)) and inbound(i, j+1):
                    sum_= dungeon[i][j+1]
                    sum_ += dungeon[i][j]
                    if sum_ < 0:
                        dungeon[i][j] = sum_
                    else:
                        dungeon[i][j] = 0
                elif inbound(i+1, j) and not inbound(i, j+1):
                    sum_= dungeon[i+1][j]
                    sum_ += dungeon[i][j]
                    if sum_ < 0:
                        dungeon[i][j] = sum_
                    else:
                        dungeon[i][j] = 0
                else:
                    sum_= dungeon[i][j]
                    if sum_ < 0:
                        dungeon[i][j] = sum_
                    else:
                        dungeon[i][j] = 0
        print(dungeon)
        return abs(dungeon[0][0]) + 1
                