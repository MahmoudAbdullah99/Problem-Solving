class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price , max_profit = prices[0], 0
        i = 1
        
        while i < len(prices):
            if prices[i] <= min_price:
                min_price = prices[i]
            else:
                curr_profit = prices[i] - min_price
                max_profit = max(max_profit, curr_profit)
            i += 1

        return max_profit