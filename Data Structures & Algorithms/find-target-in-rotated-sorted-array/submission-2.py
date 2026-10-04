class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            
            middle = left + (right - left) // 2
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] > nums[right]: # pivot is on the right
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else: # pivot is on the left
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1