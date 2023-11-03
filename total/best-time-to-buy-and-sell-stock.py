class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy =  0
        res=0
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]: 
                buy= sell
            else:
                res= max(prices[sell] - prices[buy], res)
        return res