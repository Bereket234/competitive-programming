# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(root):
            dummy= ListNode()
            while root:
                temp= root.next
                root.next= dummy.next
                dummy.next= root
                root= temp
            return dummy.next
        l1= reverse(l1)
        l2= reverse(l2)
        sum_ , rem= 0, 0
        head= ListNode()
        temp= head
        while l1 or l2:
            if l1 and l2:
                sum_= (l1.val + l2.val + rem)% 10
                rem=  (l1.val + l2.val + rem) // 10
                l1= l1.next
                l2= l2.next
            elif l1:
                sum_= (l1.val + rem) %10
                rem= (l1.val + rem) // 10
                l1= l1.next
            else:
                sum_= (l2.val + rem) %10
                rem= (l2.val + rem) // 10
                l2= l2.next
            curr= ListNode(sum_)
            temp.next= curr
            temp = curr
        if rem:
            curr= ListNode(rem)
            temp.next= curr
            temp = curr
        return reverse(head.next)
        