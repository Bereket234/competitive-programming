# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd= head
        even= head.next if head else head
        
        while even and even.next:
            temp= odd.next
            odd.next= even.next
            even.next= even.next.next
            odd.next.next= temp
            even= even.next
            odd= odd.next
        return head
            