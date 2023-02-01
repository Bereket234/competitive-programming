# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy= ListNode(-201, head)
        
        prev, curr= dummy, head
        
        while curr:
            if curr.val >= x:
                break
            prev= curr
            curr= curr.next
        if not curr:
            return head
        prev2, curr2= curr, curr.next
        
        while curr2:
            if curr2.val < x:
                prev2.next= curr2.next
                curr2.next= curr
                prev.next= curr2
                prev= prev.next
                curr2= prev2.next
            else:
                prev2= prev2.next
                curr2= curr2.next
        return dummy.next