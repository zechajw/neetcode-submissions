class Solution:
    def rob(self, nums: List[int]) -> int:
        no_prev, prev = 0, nums[0]

        for i in range(1, len(nums)):
            curr = max(no_prev + nums[i], prev)
            no_prev, prev = prev, curr

        return prev