t= int(input())
def check(arr):
      arr.sort()
      for i in range(1, len(arr)):
            if arr[i] > arr[i-1]+1:
                  return "NO"
      return "YES"

for _ in range(t):
      n= int(input())
      arr= list(map(int, input().split()))
      
      print(check(arr))