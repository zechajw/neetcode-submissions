from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # dp[i] represents minimum number of coins to make up amount == i
        dp = [0] + [math.inf] * amount 

        for amt in range(1, amount + 1):
            for c in coins:
                if c <= amt: # if the coin does not cause the amount to overshoot
                    dp[amt] = min(dp[amt], dp[amt - c] + 1)

        return dp[amount] if dp[amount] != math.inf else -1
