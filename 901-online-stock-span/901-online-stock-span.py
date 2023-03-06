class StockSpanner:

    def __init__(self):
        self.arr= []
        self.stack= []
        self.idx= 0

    def next(self, price: int) -> int:
        while self.stack and self.arr[self.stack[-1]] <= price:
            self.stack.pop()
        self.arr.append(price)
        self.stack.append(self.idx)
        self.idx += 1
        return self.idx if len(self.stack) == 1 else self.idx - self.stack[-2] - 1
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)