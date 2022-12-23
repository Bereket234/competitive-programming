# Enter your code here. Read input from STDIN. Print output to STDOUT

A= set(list(map(int, input().split(' '))))
n= int(input())
sets= []
for i in range(n):
    sets.append(list(map(int, input().split(' ')))) 

def check_super_set(sets,A):
    for s in sets:
        s_= set(s)
        if len(s_) >= len(A):
            return False
        for c in s_:
            if c not in A:
                return False
        
    return True

print(check_super_set(sets, A))