class MedianFinder:

    def __init__(self):
        self.lower= []
        self.higher= []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -1 *num)

        if self.lower and self.higher and (-1 * self.lower[0]) > self.higher[0]:
            heapq.heappush(self.higher, (-1 * heapq.heappop(self.lower)))
        
        if len(self.lower) > len(self.higher) + 1:
            heapq.heappush(self.higher,(-1 * heapq.heappop(self.lower)))
        if len(self.lower) + 1 < len(self.higher):
            heapq.heappush(self.lower,(-1 * heapq.heappop(self.higher)))
            
    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return -1 * self.lower[0]
        if len(self.lower) < len(self.higher):
            return self.higher[0]
        return ((-1 * self.lower[0]) + self.higher[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()