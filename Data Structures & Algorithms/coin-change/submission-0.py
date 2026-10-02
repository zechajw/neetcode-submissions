from functools import cache

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache    
        def helper(index: int, remaining: int) -> int:
            # you need 0 coins to make an amount of 0
            if remaining == 0:
                return 0

            # overshot the amount, this is not a valid way to make the coins
            if remaining < 0:
                return math.inf

            # no coins left to use
            if index >= len(coins):
                return math.inf

            # we either use 1 more of this coin or move onto the next coin
            use_coin = 1 + helper(index, remaining - coins[index])
            dont_use_coin = helper(index + 1, remaining)

            return min(use_coin, dont_use_coin)

        min_coins = helper(0, amount)
        if min_coins == math.inf:
            return -1
        return min_coins