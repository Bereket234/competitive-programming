class TimeMap:

    def __init__(self):
        self.time_map= defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ''
        left, right= 0, len(self.time_map[key])-1
        
        while left <= right:
            mid= (left + right) // 2
            if self.time_map[key][mid][1] >  timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if right == -1:
            return ''
        return self.time_map[key][right][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)