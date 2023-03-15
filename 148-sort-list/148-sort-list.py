# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        h1= head
        
        h2= self.getMid(head)
        temp= h2.next
        h2.next= None
        h2= temp
        
        l1= self.sortList(h1)
        l2= self.sortList(h2)
        
        return self.mergeList(l1, l2)
    
    
    def mergeList(self, l1, l2):
        dummy= ListNode()
        prev= dummy
        while l1 and l2:
            if l1.val > l2.val:
                prev.next= l2
                prev= l2
                l2= l2.next
            else:
                prev.next= l1
                prev= l1
                l1= l1.next
        if l1:
            prev.next= l1
        if l2:
            prev.next= l2
        return dummy.next
    
    
    def getMid(self, head):
        slow= head
        fast= head.next
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        return slow
    
        
        
        