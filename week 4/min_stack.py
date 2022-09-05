class MinStack:

    def __init__(self):
        self.min_= []
        self.res= []
        
    def push(self, val: int) -> None:
        self.res.append(val)
        min_val= min(val, self.min_[-1] if self.min_ else val)
        self.min_.append(min_val)

    def pop(self) -> None:
        self.min_.pop()
        return self.res.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        return self.min_[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()