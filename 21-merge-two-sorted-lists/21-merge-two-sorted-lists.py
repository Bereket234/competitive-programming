# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node= ListNode()
        
        temp= dummy_node
        l1= list1
        l2= list2
        
        while l1 and l2:
            if l1.val < l2.val:
                newNode= ListNode(l1.val, None)
                l1= l1.next
            else:
                newNode= ListNode(l2.val, None)
                l2= l2.next
            temp.next= newNode
            temp= temp.next
        
        while l1:
            temp.next= ListNode(l1.val)
            temp= temp.next
            l1= l1.next
        while l2:
            temp.next= ListNode(l2.val)
            temp= temp.next
            l2= l2.next
        return dummy_node.next