class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # We only accept negative numbers within the sequence, not on the ends
        left = 0
        right = 0
        import math
        largest_sum = -math.inf

        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            largest_sum = max(curr_sum, largest_sum)
            
        return largest_sum