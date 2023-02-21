# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]: 
        cnt= 0
        temp= head
        
        while temp:
            cnt+=1
            temp= temp.next
        
        res= [0 for _ in range(cnt)]
        stack= [(head.val, 0)]
        
        cnt= 1
        temp= head.next
        
        while temp:
            while len(stack) > 0 and temp.val > stack[-1][0]:
                res[stack[-1][1]]= temp.val
                stack.pop()
            stack.append((temp.val, cnt))
            cnt+=1
            temp= temp.next
        return res
        
            