class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy= sell= float('inf')
        res= profit= 0
        
        for price in prices:
            if price <= sell:
                buy= price
                sell= price
                res += profit
                profit = 0
            else:
                sell = price
                profit= sell - buy
        res += profit
        return res
                
                
                