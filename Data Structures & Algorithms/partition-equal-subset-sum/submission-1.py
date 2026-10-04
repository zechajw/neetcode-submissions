class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        memo = {}
        def canPartition(index: int, sum1: int) -> bool:
            if index >= len(nums):
                return sum1 == total_sum // 2

            if sum1 > total_sum // 2:
                return False

            if sum1 == total_sum // 2:
                return True
            
            if (index, sum1) in memo:
                return memo[(index, sum1)]

            take_num = canPartition(index + 1, sum1 + nums[index])
            dont_take_num = canPartition(index + 1, sum1)

            result = take_num or dont_take_num
            memo[(index, sum1)] = result
            return result

        return canPartition(0, 0)