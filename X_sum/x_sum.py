t= int(input())
 
def x_sum(grid, m, n):
      
      dig_sum1= [0 for i in range(n+m-1)]
      dig_sum2= [0 for i in range(n+m-1)]
      
      for i in range(m):
            for j in range(n):
                  sum_= i + j
                  diff= j-i
                  
                  dig_sum1[sum_] += grid[i][j]
                  if diff < 0:
                        diff= n-1+abs(diff)
                  dig_sum2[diff] += grid[i][j]
      res= 0
      for i in range(m):
            for j in range(n):
                  sum_= i + j
                  diff= j-i
                  
                  if diff < 0:
                        diff= n-1+abs(diff)
                  
                  pnt= dig_sum1[sum_] + dig_sum2[diff] - grid[i][j]
                  res= max(res, pnt)
      return res
                  
 
for _ in range(t):
      grid= []
      m,n= tuple(map(int, input().split()))
      
      for _ in range(m):
            line= list(map(int, input().split()))
            grid.append(line)
      print(x_sum(grid, m, n))