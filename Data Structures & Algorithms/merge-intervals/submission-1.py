class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        
        prev_start, prev_end = None, None

        merged_intervals = []

        for start, end in intervals:
            if prev_start is None:
                prev_start, prev_end = start, end
                continue

            # prev interval is not None, check whether should merge or flush
            if prev_end < start:
                merged_intervals.append([prev_start, prev_end])
                prev_start, prev_end = start, end
            else:
                prev_end = max(prev_end, end)

        merged_intervals.append([prev_start, prev_end])
        return merged_intervals

            

            