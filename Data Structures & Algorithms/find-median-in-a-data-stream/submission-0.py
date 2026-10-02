import heapq

class MedianFinder:

    def __init__(self):
        self.minheap = [] # stores larger half
        self.maxheap = [] # stores lower half
        # invariant to keep len(self.minheap) - len(self.maxheap) <= 1
        # invariant no.2: all elements in self.maxheap must be smaller than or equal to the elements in self.minheap

        # how to enforce invariant no. 2

        # lets say the max heap has [1,2,3,4,5]
        # min heap has [6,7,8,9,10]

        # we want to add element 11
        # we first add it to the max heap 
        # [1,2,3,4,5,11]
        # then we add the top element to the min heap
        # [6,7,8,9,10,11]
        # if the size of max heap is bigger than min heap, then we add one element from max heap back to minheap to maintain invariant no. 1
        # [1,2,3,4,5,6], [7,8,9,10,11]
    def addNum(self, num: int) -> None:
        # to keep two invariants
        # we push the element into the max heap
        # then we push the top element from the max heap to the min heap
        # then we push the top element from the min heap to the max heap 
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap) - len(self.maxheap) > 1:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

        # ["MedianFinder", "addNum", "1", "findMedian", "addNum", "2", "findMedian", "addNum", "3", "findMedian"]
        # addNum(1) -> self.maxheap = [], self.minheap = [1]
        # findMedian -> 1
        # addNum(2) -> self.maxheap = [-1], self.minheap = [2]
        # findMedian -> (1 + 2) / 2 = 1.5
        # addNum(3) -> self.maxheap = [-1], self.minheap = [2, 3]
        # findMedian -> (2)
 

    def findMedian(self) -> float:

        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + -self.maxheap[0]) / 2
        
        else: # minheap is always >= 1 in length, so median is in minheap
            return self.minheap[0]

        
        