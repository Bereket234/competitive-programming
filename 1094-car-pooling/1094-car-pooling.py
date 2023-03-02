class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        max_= 0
        for trip in trips:
            n, start, end= trip
            max_ = max(end, max_)
        cnt= [0 for _ in range(max_ +1)]
        for trip in trips:
            n, start, end= trip
            cnt[start] += n
            cnt[end] -= n
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i-1]
            
        for pas in cnt:
            if pas > capacity:
                return False
        return True

        