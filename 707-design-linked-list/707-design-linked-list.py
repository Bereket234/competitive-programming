class Node:
    def __init__(self, val= 0, next_= None):
        self.val= val
        self.next= next_

class MyLinkedList:

    def __init__(self):
        self.dummy= Node()
        
    def get(self, index: int) -> int:
        temp= self.dummy.next
        i= 0
        while temp:
            if i == index:
                return temp.val
            i+=1
            temp= temp.next
        return -1

    def addAtHead(self, val: int) -> None:
        curr= self.dummy.next
        node= Node(val,curr)
        self.dummy.next= node

    def addAtTail(self, val: int) -> None:
        node= Node(val)
        temp= self.dummy
        while temp.next:
            temp= temp.next
        temp.next=node
    def addAtIndex(self, index: int, val: int) -> None:
        temp= self.dummy
        i= 0
        while temp:
            if i == index:
                node= Node(val, temp.next)
                temp.next= node
                break
            i+=1
            temp= temp.next
            
        
    def deleteAtIndex(self, index: int) -> None:
        temp= self.dummy
        i=0
        while temp.next:
            if i == index:
                temp.next= temp.next.next
                break
            i+=1
            temp= temp.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)