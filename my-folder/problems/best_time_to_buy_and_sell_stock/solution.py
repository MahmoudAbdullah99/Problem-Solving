class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, max_price = prices[0], prices[0]
        max_profit = 0
        for price in prices:
            if price > max_price and price-min_price > max_profit:
                max_price = price
                max_profit = max_price-min_price
            elif price < min_price:
                min_price = price
                max_price = price
        
        return max_profit