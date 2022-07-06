class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum, res = 0, 0
        prevSum = {0: 1}

        for num in nums:
            currSum += num
            diff = currSum - k

            res += prevSum.get(diff, 0)
            prevSum[currSum] = 1 + prevSum.get(currSum, 0)

        return res
