n= int(input())
nums= list(map(int, input().split()))
isOdd, isEven= False, False

for num in nums:
      if num%2 == 0:
            isEven= True
      else:
            isOdd= True
if isEven and isOdd:
      nums.sort()
print(*nums)   