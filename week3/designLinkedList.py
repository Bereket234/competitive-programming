class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        i = 0
        while temp and i < index:
            temp = temp.next
            i += 1
        if not temp:
            return -1
        return temp.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.head)
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        temp = self.head

        if not self.head:
            self.head = newNode
            return

        while temp.next:
            temp = temp.next
        temp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        newNode = ListNode(val)
        temp = self.head
        i = 0
        while temp and i < index-1:
            temp = temp.next
            i += 1

        if temp == None:
            return
        newNode.next = temp.next
        temp.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return
        temp = self.head
        i = 0
        while temp and i < index-1:
            temp = temp.next
            i += 1
        if not temp:
            return
        if temp.next:
            temp2 = temp.next
            temp.next = temp.next.next
            temp2.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
