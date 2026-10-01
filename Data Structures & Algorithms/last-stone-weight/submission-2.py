import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            heaviest, second_heaviest = -heapq.heappop(heap), -heapq.heappop(heap) 

            if heaviest == second_heaviest:
                continue
            else:
                heaviest = heaviest - second_heaviest
                heapq.heappush(heap, -heaviest)

        return -heap[0] if heap else 0