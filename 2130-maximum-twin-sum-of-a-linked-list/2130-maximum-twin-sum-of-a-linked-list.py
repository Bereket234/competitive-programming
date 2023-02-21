# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow= fast= head
        
        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next
            
        temp= head
        slow= self.reverse(slow)
        res=0
        
        while slow:
            sum_= slow.val + temp.val
            res= max(sum_, res)
            slow= slow.next
            temp= temp.next
        return res
    
            
    def reverse(self, head):
        dummy= ListNode()
        temp= head
        while temp:
            curr= temp
            temp= temp.next
            curr.next= dummy.next
            dummy.next= curr
        return dummy.next