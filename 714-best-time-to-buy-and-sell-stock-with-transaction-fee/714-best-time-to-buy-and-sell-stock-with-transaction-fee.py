class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy= sell= float('inf')
        res= profit= 0
        
        for price in prices:
            if profit == 0 and price < sell:
                buy= price
                sell= price
            
            elif price < sell - fee:
                buy= price 
                sell= price
                res += profit
                profit= 0
            elif price > buy + fee and price > sell:
                sell = price 
                profit = sell - buy - fee
        res += profit
        return res
                
                