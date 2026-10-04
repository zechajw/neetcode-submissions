class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        max_from_left = [0] * n
        max_from_right = [0] * n

        curr_max = 0
        for i in range(len(height) - 1, -1, -1):
            max_from_right[i] = curr_max
            curr_max = max(curr_max, height[i])

        curr_max = 0
        for i in range(len(height)):
            max_from_left[i] = curr_max
            curr_max = max(curr_max, height[i])

        volume = 0



        for index, elevation in enumerate(height):
            container_height = min(max_from_left[index], max_from_right[index])
            effective_volume = container_height - elevation 
            volume += effective_volume if effective_volume > 0 else 0
        return volume