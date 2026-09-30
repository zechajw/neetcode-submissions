class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return any(nums.count(x) > 1 for x in nums)