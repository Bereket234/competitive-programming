# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt=0
        temp= head
        dummy= ListNode(0, head)
        if not head:
            return head
        
        while temp:
            cnt+=1
            temp= temp.next
        
        k= k % cnt
        fast= head
        for i in range(k):
            fast= fast.next
            slow= head
        slow= head
        while fast.next:
            slow= slow.next
            fast= fast.next
        fast.next= dummy.next
        dummy.next= slow.next
        slow.next= None
        return dummy.next
        