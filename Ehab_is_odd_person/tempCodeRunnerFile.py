n= int(input())
nums= list(map(int, input().split()))
min_= 0
for i in range(len(nums)):
      min_= i
      for j in range(i, len(nums)):
            if (nums[i] + nums[j]) % 2 != 0:
                  if nums[j] < nums[min_]:
                        min_ = j
            
      nums[min_], nums[i]= nums[i], nums[min_]
print(*nums)
                  