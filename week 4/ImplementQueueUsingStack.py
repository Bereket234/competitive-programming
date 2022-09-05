class MyQueue:

    def __init__(self):
        self.queue= []

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        self.queue.reverse()
        x= self.queue.pop()
        self.queue.reverse()
        
        return x
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return False if len(self.queue)>0 else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()