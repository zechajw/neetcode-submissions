class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Add them to a max heap and return the top k elements

        # First, count the frequency of each
        freq = {}

        for num in nums:
            freq[num] = freq[num] + 1 if num in freq else 1

        # Then, add these elements to a list
        import heapq

        max_heap = [(count, num) for num, count in freq.items()]

        return [val for key, val in heapq.nlargest(k, max_heap)]
