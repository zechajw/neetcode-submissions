class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        most_water = 0

        while left < right:
            left_height, right_height = heights[left], heights[right]
            width = right - left
            most_water = max(most_water, min(left_height, right_height) * width)

            if left_height > right_height:
                right -= 1
            else:
                left += 1

        return most_water