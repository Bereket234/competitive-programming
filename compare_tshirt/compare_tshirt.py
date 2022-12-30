n= int(input())
#function that compare sizes and return '<', '>' or =
def compare_sizes(sizes):
      res= ''
      s= [0, 0]
      for i, size in enumerate(sizes):
            if size[-1]== 'M':
                  s[i]= 60
            if size[-1]== 'S':
                  s[i] = 50
                  for j in range(len(size)-1):
                        s[i]-=1
            if size[-1] == 'L':
                  s[i]= 70
                  for j in range(len(size)-1):
                        s[i]+=1
            
      if s[0] > s[1]:
            return '>'
      if s[0]< s[1]:
            return '<'
      if s[0]== s[1]:
            return '='

for i in range(n):
      sizes= list(input().split(' '))
      print(compare_sizes(sizes))