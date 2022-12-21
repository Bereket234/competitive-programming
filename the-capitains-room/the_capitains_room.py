# Enter your code here. Read input from STDIN. Print output to STDOUT
k= int(input())
nums= list(map(int, input().split()))
cnt={}
for i in nums:
    cnt[i]= 1+cnt.get(i, 0)
for i, v in cnt.items():
    if v != k:
        print(i)
