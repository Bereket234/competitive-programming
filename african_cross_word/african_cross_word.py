def african_word(n, m, grid):
    row= [{} for _ in range(n)]
    col= [{} for _ in range(m)]
    res= []
    for i in range(n):
        for j in range(m):
            val= grid[i][j]
            row[i][val]=1 + row[i].get(val, 0)
            col[j][val]= 1+ col[j].get(val, 0)
    for i in range(n):
        for j in range(m):
            val= grid[i][j]
            cntr= row[i].get(val, 0)
            cntc= col[j].get(val, 0)
            if cntr == 1 and cntc ==1:
                res.append(val)
    return res
n, m= tuple(map(int, input().split()))
grid= []

for _ in range(n):
    line= input()
    grid.append(line)

print(''.join(african_word(n, m, grid)))
      