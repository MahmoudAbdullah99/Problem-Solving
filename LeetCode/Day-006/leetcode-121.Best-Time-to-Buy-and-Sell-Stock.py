"""
Problem Description:
    - You are given an array prices where prices[i] is the price of a given
    stock on the ith day.
    - You want to maximize your profit by choosing a single day to buy one
    stock and choosing a different day in the future to sell that stock.
    - Return the maximum profit you can achieve from this transaction. If you
    cannot achieve any profit, return 0.

Notes:
    - 

TODO:
    - Add notes
    - Review.
"""

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
