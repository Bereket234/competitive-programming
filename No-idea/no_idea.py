# Enter your code here. Read input from STDIN. Print output to STDOUT
m, n=input().split()
arr= list(map(int, input().split()))
a= set(map(int, input().split()))
b= set(map(int, input().split()))
res= 0
for i in arr:
    if i in a:
        res+=1
    if i in b:
        res-=1
print(res)


    
    
