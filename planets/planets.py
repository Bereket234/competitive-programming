t= int(input())

def calculate_cost(n, c, planets):
      orbits= {}
      cost= 0
      for orbit in planets:
            orbits[orbit]= 1 + orbits.get(orbit, 0)
      
      for orbit, cnt in orbits.items():
            if cnt > c:
                  cost+= c
            else:
                  cost += cnt
      return cost
            

# for each testcase this block accepts an input and calls the cost calculator function to calculate the minimum cost
for i in range(t):
      n, c= tuple(map(int, input().split()))
      planets= list(map(int, input().split()))
      print(calculate_cost(n, c, planets))