class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # check whether the pivot point is on the left or the right, the opposite side would be sorted
        # we will use the side opposite to the pivot point to determine which half to prune

        # Input: nums = [3,4,5,6,1,2], target = 6
        # left = 0, right = 5, middle = 2, nums[middle] > nums[right] (which means the pivot point is on the right), so we check the left range
            # target is not within the left range, so we search to the right, left = middle + 1 = 3
        # left = 3, right = 5, middle = 4, nums[middle] < nums[right] (which means the pivot point is on the left), so we check the right range
            # target is not within the right range, so we search to the left, right = middle - 1 = 3
        # left = 3, right = 3, middle = 3 and nums[3] == 6 so we return

        # Time Complexity O(logn), Space Complexity O(1)

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle

            # pivot is on the right, check the left range
            if nums[middle] > nums[right]: 
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # pivot is on the left, check the right range
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1