from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we keep a monotonically decreasing deque
        # max of the window is always at deque[0]
        # if deque[0] goes out of the index range of the window, we remove it from the window

        # value, index
        # [(2, 1), (1, 2)]

        # when we move window to index 3,
        # [(2, 1), (1, 2), (0, 3)]

        # when we move window to index 4, value 4
        # [(4, 4)]

        decreasing_deque = deque()


        for i in range(k):
            num = nums[i]
            while decreasing_deque and decreasing_deque[-1][0] < num:
                decreasing_deque.pop()

            decreasing_deque.append((num, i))

        # for i = 0, num = 1 deque = [(1, 0)]
        # for i = 1, num = 2 deque = [(2, 1)]
        # for i = 2, num = 2 deque = [(2, 1), (1, 2)]

        sliding_max = []
        sliding_max.append(decreasing_deque[0][0]) # sliding_max = [2]

        # for i = 3, num = 0
            # top_index = 1 > i - k, still valid
            # num is not bigger than decreasing_deque[-1][0], so just append it to the deque directly
            # deque = [(2, 1), (1, 2), (3, 0)]
            # sliding_max = [2, 2]

        # for i = 4, num = 4
        # for i = 5, num = 2
        # for i = 6, num = 6
        for i in range(k, len(nums)):
            num = nums[i]

            top_value, top_index = decreasing_deque[0]
            if top_index <= i - k: # at window with i = 3, the value i - k = 0, 
                decreasing_deque.popleft()

            while decreasing_deque and decreasing_deque[-1][0] < num:
                decreasing_deque.pop()

            decreasing_deque.append((num, i))

            sliding_max.append(decreasing_deque[0][0])

        return sliding_max