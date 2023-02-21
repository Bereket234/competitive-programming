# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= head
        temp= head.next if head else head
        
        while temp:
            if temp.val == prev.val:
                prev.next= temp.next
                temp= temp.next
            else:
                prev= temp
                temp= temp.next
        return head
            