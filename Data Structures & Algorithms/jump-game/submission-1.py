class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        dp[0] = True
        for i in range(0, len(nums)):
            if dp[i] is False:
                continue

            hops = nums[i]
            for j in range(1, hops + 1):
                if i + j >= len(nums):
                    break
                dp[i + j] = True

        return dp[-1]