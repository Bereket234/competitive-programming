# Enter your code here. Read input from STDIN. Print output to STDOUT
T= int(input())
nums=[]
ans='Yes'

def pile_up(blocks):
    stack=[max(blocks[0], blocks[-1])]
    l, r= 0, len(blocks)-1
    
    while l <= r:
        if blocks[l] < blocks[r]:
            if blocks[r] > stack[-1]:
                
                return 'No'
            stack.append(blocks[r])
            r-=1
        else:
            if blocks[l] > stack[-1]:
                return 'No'
            stack.append(blocks[l])
            l+=1
    return 'Yes'
                

for i in range(T):
    input()
    nums= list(map(int, input().split()))
    print(pile_up(nums))
    
            
