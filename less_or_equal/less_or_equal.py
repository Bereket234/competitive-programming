n, k= list(map(int, input().split()))

nums= list(map(int, input().split()))

nums.sort()

if k == 0:
      if nums[0] -1 < 1:
            print(-1)
      else:
            print(nums[0] -1)
elif k < n:
      if nums[k-1] != nums[k]:
            print(nums[k-1])
      else:
            print(-1)
else:
      print(nums[k-1])