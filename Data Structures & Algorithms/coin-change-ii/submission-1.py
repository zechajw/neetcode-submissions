class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        # only 1 way to make up amount of 0
        dp[0] = 1
        for coin in coins:
            for amt in range(amount + 1):
                if coin <= amt:
                    dp[amt] += dp[amt - coin]

        return dp[amount]