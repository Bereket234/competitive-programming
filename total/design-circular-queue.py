class MyCircularQueue:

    def __init__(self, k: int):
        self.que= [0 for _ in range(k)]
        self.k= k
        self.front= 0
        self.rear= 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.que[self.rear%self.k] = value
            self.rear += 1
            return True
        return False
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front+=1
            return True
        return False
    def Front(self) -> int:
        if not self.isEmpty():
            return self.que[self.front %self.k]
        return -1
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.que[(self.rear-1)%self.k]
        return -1

    def isEmpty(self) -> bool:
        if self.rear ==self.front:
            return True
        return False

    def isFull(self) -> bool:
        if self.rear != self.front and self.rear - self.front >= self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()