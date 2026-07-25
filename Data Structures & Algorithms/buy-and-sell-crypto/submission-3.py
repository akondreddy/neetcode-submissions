class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Lowest price
        minPrice = prices[0]
        maxProfit = 0
        length = len(prices)

        # Keep track of the lowest buying price and
        # which would yield the highest profit
        for i in range(length):
            currentPrice = prices[i]
            # If the current buying price is less than
            # the lowest buying price so far
            if currentPrice < minPrice:
                minPrice = currentPrice
            # Otherwise, if the profit that could come
            # by selling on this day is compared to 
            # the max profit we had
            elif currentPrice - minPrice > maxProfit:
                maxProfit = currentPrice - minPrice
        return maxProfit
            