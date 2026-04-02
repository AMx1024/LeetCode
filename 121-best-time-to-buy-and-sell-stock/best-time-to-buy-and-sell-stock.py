class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = float("inf"), 0
        for price in prices:
            if price < buy:
                buy = price
            curr_profit = price - buy
            if curr_profit > profit:
                profit = curr_profit
        return profit

        
