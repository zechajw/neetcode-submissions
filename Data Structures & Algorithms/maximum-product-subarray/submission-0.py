class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far, max_so_far, best = nums[0], nums[0], nums[0]

        for num in nums[1:]:
            candidates = (min_so_far * num, max_so_far * num, num)
            min_so_far = min(candidates)
            max_so_far = max(candidates)
            best = max(best, max_so_far)

        return best