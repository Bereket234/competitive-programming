# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter= 1
        
        temp= head
        
        while temp: 
            counter+=1
            temp= temp.next
        
        counter-=n
        temp=head
        for i in range(0, counter-n):
            temp= temp.next
        if temp.next:
            temp.next= temp.next.next
        else:
            temp.next= None
        return head