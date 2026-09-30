class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        digits = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in digits:
                return [digits[complement], i]
            else:
                digits[num] = i
        
        return [0, 0]