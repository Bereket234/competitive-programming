# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp= None
        res= head
        
        while head:
            if not temp:
                temp= head
                head= head.next
            elif temp.val== head.val:
                head= head.next
                temp.next= head
            else:
                temp=temp.next
                head= head.next
                
        return res