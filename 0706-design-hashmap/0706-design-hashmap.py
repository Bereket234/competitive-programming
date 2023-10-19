class Node:
    def __init__(self, key= -1, val= -1, next_= None):
        self.key= key
        self.value= val
        self.next= next_
class MyHashMap:

    def __init__(self):
        self.hash= [Node() for i in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        idx= key % 1000
        curr= self.hash[idx]
        
        while curr:
            if curr.key == key:
                curr.value= value
                break
            if not curr.next:
                temp= Node(key, value)
                curr.next= temp
        
            curr= curr.next

    def get(self, key: int) -> int:
        idx= key%1000
        curr= self.hash[idx]
        
        while curr:
            if curr.key == key:
                return curr.value
            curr= curr.next
        return -1
    def remove(self, key: int) -> None:
        prev= None
        idx= key % 1000
        curr= self.hash[idx].next
        prev= self.hash[idx]
        while curr:
            if curr.key == key:
                prev.next= curr.next
                curr.next= None
            prev= curr
            curr= curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)