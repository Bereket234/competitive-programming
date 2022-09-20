# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val= val
        self.next=next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_= 0
        res= ListNode()
        temp= res
        head= None
        
        while l1 or l2:
            if not l1:
                temp= res
                res= ListNode()
                temp.next= res
                res.val= ((sum_//10) + l2.val)%10
                sum_=(sum_//10) + l2.val
                l2=l2.next
            elif not l2:
                temp= res
                res= ListNode()
                temp.next= res
                res.val= ((sum_//10) + l1.val)%10
                sum_=(sum_//10) + l1.val
                l1=l1.next
            else:
                temp= res
                res= ListNode()
                temp.next=res
                
                res.val= ((sum_//10)+ l1.val +l2.val)%10
                sum_= (sum_//10)+ l1.val +l2.val
                l1=l1.next
                l2= l2.next
            
            if not head:
                head= res
        
        if sum_>=10:
            temp=res
            res= ListNode()
            temp.next= res
            res.val= 1
            
        return head
                