import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep minheap of top k elements, heap is always max size k

        freqs = Counter(nums)

        top_k_heap = []

        for num, freq in freqs.items():
            heapq.heappush(top_k_heap, (freq, num))

            if len(top_k_heap) > k:
                heapq.heappop(top_k_heap)

        return [num for freq, num in top_k_heap]