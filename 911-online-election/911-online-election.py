class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times= times
        self.cur_max= []
        max_cnt= 0
        cnt= {}
        
        for i in range(len(persons)):
            cnt[persons[i]] = 1 + cnt.get(persons[i], 0)
            
            if cnt[persons[i]] >= max_cnt:
                max_cnt= cnt[persons[i]]
                self.cur_max.append(persons[i])
            else:
                self.cur_max.append(self.cur_max[-1])
        print(self.cur_max)

    def q(self, t: int) -> int:
        low= 0
        high= len(self.times) - 1
        
        while low <= high:
            mid= (low + high) //2
            if self.times[mid] < t:
                low= mid + 1
            elif self.times[mid] > t:
                high = mid - 1
            else:
                high= mid
                break
        return self.cur_max[high]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)