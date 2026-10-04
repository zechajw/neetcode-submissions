class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0

        profit = 0
        for sell in range(1, len(prices)):
            profit = max(profit, prices[sell] - prices[buy])

            if prices[sell] < prices[buy]:
                buy = sell

        return profit