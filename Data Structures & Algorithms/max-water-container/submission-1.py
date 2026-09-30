class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Bar of lower height that is inside the previous cannot store more water
        # If the bar is higher, calculate the volume of both and take the one with the higher volume
        left = 0
        right = len(heights) - 1
        maxVolume = (right - left) * min(heights[left], heights[right])

        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            maxVolume = max(volume, maxVolume)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1

        return maxVolume
