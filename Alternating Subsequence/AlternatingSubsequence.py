t= int(input())
    
def alternat_sum(nums):
    l= 0 
    res= 0
    max_= nums[0]
    
    for r, seeker in enumerate(nums):
        
        holder= nums[l]
        if (holder < 0 and seeker > 0) or (holder > 0 and seeker < 0):
            res+= max_
            max_= seeker
            l= r
        max_= max(seeker, max_)
    res+=max_
    return res
    
    
for _ in range(t):
    n= input()
    nums= list(map(int, input().split()))
    print(alternat_sum(nums))