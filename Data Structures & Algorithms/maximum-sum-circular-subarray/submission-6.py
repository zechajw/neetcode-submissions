class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # kadane's algorithm

        # we want to get the minimum sum of the subarray, then subtract
        array_sum = sum(nums)
        min_subarray, curr_min_sum, max_subarray, curr_max_sum = nums[0], nums[0], nums[0], nums[0]

        for num in nums[1:]:
            curr_min_sum = min(num, curr_min_sum + num)
            curr_max_sum = max(num, curr_max_sum + num)
            
            # if the curr_sum ever goes above 0, we should just restart because adding the curr sum will always be larger
            min_subarray = min(curr_min_sum, min_subarray)
            max_subarray = max(curr_max_sum, max_subarray)
        

        if min_subarray == array_sum:
            return max_subarray
        else:
            return max(max_subarray, array_sum - min_subarray)