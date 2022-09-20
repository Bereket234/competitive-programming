# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head= None
        
        new_node= ListNode()
        
        while list1 or list2:
            
            if not list1:
                new_node.next= ListNode()
                new_node= new_node.next
                new_node.val= list2.val
                list2= list2.next
            elif not list2:
                new_node.next= ListNode()
                new_node= new_node.next
                new_node.val= list1.val
                list1= list1.next
            elif list1.val < list2.val:
                new_node.next= ListNode()
                new_node= new_node.next
                new_node.val= list1.val
                list1= list1.next
            else:
                new_node.next= ListNode()
                new_node= new_node.next
                new_node.val= list2.val
                list2= list2.next
            if not head:
                head= new_node
        
        return head
                