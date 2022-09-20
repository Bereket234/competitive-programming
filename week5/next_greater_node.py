# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stackk= []
        stackv=[]
        res=[]
        tmp= head
        count= 1
        
        while tmp.next:
            count+=1
            tmp=tmp.next
        
        
        res= [0]*count
        i=0
        while head:
            if len(stackk) == 0:
                stackk.append(i)
                stackv.append(head.val)
                i+=1
                head= head.next
                continue
            while stackk and stackv[-1] < head.val:
                res[stackk[-1]]= head.val
                stackk.pop()
                stackv.pop()
            stackk.append(i)
            stackv.append(head.val)
            i+=1
            head= head.next
        return res
            
                
                