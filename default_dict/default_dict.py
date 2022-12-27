from collections import defaultdict
# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m= list(map(int,input().split()))
A, B= [], []
for i in range(n):
    A.append(input())
for i in range(m):
    B.append(input())
    
A_= defaultdict(list)
for idx, char in enumerate(A):
    A_[char].append(str(idx+1))

for char in B:
    if char in A_:
        print(' '.join(A_[char]))
    else:
        print(-1)
