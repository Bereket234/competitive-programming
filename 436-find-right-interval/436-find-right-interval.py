class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_= [[intervals[i][0], intervals[i][1], i] for i in range(len(intervals))]
        sorted_.sort()
        res= []
        n= len(intervals)
        for (start, end) in intervals:
            low= 0
            high= n -1
            while low <= high:
                mid= (low + high) // 2
                if sorted_[mid][0] < end:
                    low= mid + 1
                else:
                    high= mid - 1
            if low < n:
                res.append(sorted_[low][2])
            else:
                res.append(-1)
        return res