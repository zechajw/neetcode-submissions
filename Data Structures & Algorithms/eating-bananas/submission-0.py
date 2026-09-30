import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def validSpeed(speed: int) -> bool:
            total_time = 0

            for pile in piles:
                total_time += math.ceil(pile / speed)

            nonlocal h

            return total_time <= h

        min_speed, max_speed = 1, max(piles)

        while min_speed < max_speed:
            curr_speed = min_speed + (max_speed - min_speed) // 2

            if validSpeed(curr_speed):
                # prune the right search space, this speed is the maximum speed required
                max_speed = curr_speed
            else:
                min_speed = curr_speed + 1

        return min_speed + (max_speed - min_speed) // 2    