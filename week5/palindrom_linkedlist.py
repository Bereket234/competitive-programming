# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst= []
        
        while head:
            lst.append(head.val)
            head= head.next
        lp, rp= 0,len(lst)-1
        while lp <rp:
            if lst[lp] != lst[rp]:
                return False
            lp+=1
            rp-=1
        
        return True
            