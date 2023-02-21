class TimeMap:

    def __init__(self):
        self.timemap= defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr= self.timemap[key]
        n= len(arr)
        val= 0
        idx= -1
        
        low, high= 0, n-1
        while low <= high:
            mid= (low + high)//2
            
            if arr[mid][0] > val and arr[mid][0] <= timestamp:
                idx= mid
                val= arr[mid][0]
            if arr[mid][0] < timestamp:
                low= mid+1
            else:
                high= mid-1
        if idx == -1:
            return ""
        return arr[idx][1]
 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)