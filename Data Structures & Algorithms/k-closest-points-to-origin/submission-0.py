import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance_from_origin = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)

            # we want the closest points, so we use a max heap instead of a min heap
            heapq.heappush(heap, (-distance_from_origin, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            distance, x, y = heapq.heappop(heap)

            result.append([x, y])

        return result