class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(index: int, current_sum: int) -> int:
            if index >= len(nums):
                return 1 if current_sum == target else 0

            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            use_minus = dp(index + 1, current_sum - nums[index])
            use_plus = dp(index + 1, current_sum + nums[index])

            memo[(index, current_sum)] = use_minus + use_plus

            return use_minus + use_plus

        return dp(0, 0)