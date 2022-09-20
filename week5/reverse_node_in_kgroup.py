# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head= ListNode(0, head)
        
        gprev= new_head
        kth=gprev
        
        while kth:
            kth= self.getCurr(gprev, k)
            
            
            if not kth:
                break
            
            gnext= kth.next
            
            prev, curr= kth.next, gprev.next
            
            while curr != gnext:
                temp= curr.next
                curr.next= prev
                prev= curr
                curr= temp
            temp= gprev.next
            gprev.next= kth
            gprev= temp
        
        return new_head.next
            
    def getCurr(self, curr, k):
        while curr and k>0:
            curr= curr.next
            k-=1
        
        return curr