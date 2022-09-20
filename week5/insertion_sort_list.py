# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0, head)
        
        prev, curr= head, head.next
        while curr:
            if prev.val<= curr.val:
                prev= prev.next
                curr= curr.next
                continue
            
            guard= dummy
            
            while curr.val > guard.next.val:
                guard= guard.next
            prev.next= curr.next
            curr.next= guard.next
            guard.next= curr
            curr= prev.next
        
        return dummy.next