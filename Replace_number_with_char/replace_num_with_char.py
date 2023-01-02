t= int(input())

def map_nums(n, nums, chars):
      visited= {}
      
      for i, num in enumerate(nums):
            if num not in visited:
                  visited[num]= chars[i]
            elif num in visited and visited[num] != chars[i]:
                  return 'NO'
      return 'YES'
for i in range(t):
      n=  int(input())
      nums= list(input().split(' '))
      chars= input()
      print(map_nums(n, nums, chars))
      