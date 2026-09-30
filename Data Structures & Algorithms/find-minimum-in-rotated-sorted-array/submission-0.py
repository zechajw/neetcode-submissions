class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) //2

            # pivot point is on the right of middle
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

            
        # [3,4,5,6,1,2]
        # left= index 0, right = index 5 middle = index 2, pivot point on right so left = middle + 1 = 3
        # left = 3, right = 5, middle = 4 pivot point is on left or this element, so right = middle = 4
        # left = 3, right = 4, middle = 3, pivot point is on right so left = middle + 1 = 4

        # exit, left = 4, right = 4, answer is nums[4] = 1

        # Time Complexity O(logn), Space Complexity: O(1)

        return nums[right]