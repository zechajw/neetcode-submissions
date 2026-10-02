class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(start: int, end: int) -> int:
            skip, take = 0, nums[start]

            for i in range(start + 1, end + 1):
                skip, take = take, max(nums[i] + skip, take)

            return take

        return max(helper(0, len(nums) - 2), helper(1, len(nums) - 1))