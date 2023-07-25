class Solution:
    def isHappy(self, n: int) -> bool:
        visited= set()
        sum_= n
        while sum_ != 1:
            curr= sum_
            sum_= 0
            while curr != 0:
                sum_ +=(curr % 10)**2
                curr //= 10
            if sum_ in visited:
                return False
            visited.add(sum_)
        return True