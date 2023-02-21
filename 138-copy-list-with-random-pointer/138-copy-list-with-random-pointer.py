"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy= Node(0)
        obj_map= {}
        
        temp= head
        while temp:
            newNode= Node(temp.val)
            obj_map[temp]= newNode
            temp= temp.next
        temp = head
        curr= dummy
        while temp:
            obj= obj_map[temp]
            obj.random= obj_map.get(temp.random, None)
            curr.next= obj
            curr= curr.next
            temp= temp.next
        return dummy.next
        
            
        