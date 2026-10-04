class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_seen = {}

        for index, num in enumerate(nums):
            difference = target - num
            
            if difference in prev_seen:
                return [prev_seen[difference], index]
            
            prev_seen[num] = index

        return [-1]