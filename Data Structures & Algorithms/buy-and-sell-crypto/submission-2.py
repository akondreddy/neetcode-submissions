class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        length = len(prices)

        for i in range(length):
            currentPrice = prices[i]
            if currentPrice < minPrice:
                minPrice = currentPrice
            elif currentPrice - minPrice > maxProfit:
                maxProfit = currentPrice - minPrice
        return maxProfit
            