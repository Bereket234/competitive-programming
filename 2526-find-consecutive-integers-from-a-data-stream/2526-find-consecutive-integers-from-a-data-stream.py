class DataStream:

    def __init__(self, value: int, k: int):
        self.que= deque([], maxlen= k)
        self.value= value
        self.k= k
        self.cnt= 0
        
        

    def consec(self, num: int) -> bool:
        if len(self.que) == self.k:
            if self.que[0] != self.value:
                self.cnt-=1
            self.que.popleft()
        if self.value != num:
            self.cnt+=1
        self.que.append(num)
        if self.cnt != 0 or len(self.que) < self.k:
            return False
        return True
            
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)