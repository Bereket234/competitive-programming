    n, m=  list(map(int, input().split()))
     
    nums1= list(map(int, input().split()))
    nums2= list(map(int, input().split()))
     
    res= []
    p1, p2= 0, 0
    while p1 < n and p2 < m:
          if nums1[p1] < nums2[p2]:
                print(nums1[p1], end= " ")
                p1+=1
          else:
                print(nums2[p2], end= " ")
                p2+=1
    while p1 < n:
          print(nums1[p1], end= " ")
          p1+=1
    while p2 < m:
          print(nums2[p2], end= " ")
          p2+=1