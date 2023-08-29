class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        frequency= Counter(nums)
        cnt = defaultdict(int)
        
        for num in nums:
            # print(frequency, num, cnt)
            if frequency[num] > 0:
                if cnt[num] > 0:
                    cnt[num] -=1 
                    cnt[num + 1] += 1
                    frequency[num] -= 1
                    continue
                if frequency[num + 1] > 0 and frequency[num + 2] > 0:
                    frequency[num] -= 1
                    frequency[num + 1] -= 1
                    frequency[num + 2] -= 1
                    cnt[num + 3] += 1
                else:
                    return False
        return True
                