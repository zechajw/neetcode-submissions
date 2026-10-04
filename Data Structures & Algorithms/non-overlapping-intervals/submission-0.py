class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals by end time
        intervals.sort(key=lambda interval: interval[1])

        prev_start, prev_end = None, None

        removed_intervals = 0
        for start, end in intervals:
            if prev_start is None or start >= prev_end:
                prev_start, prev_end = start, end
                continue

            else:
                removed_intervals += 1

        return removed_intervals
