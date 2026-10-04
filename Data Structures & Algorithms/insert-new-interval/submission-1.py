class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # insert intervals before
        index = 0

        result = []

        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1

        # merge intervals during
        merged_interval = newInterval
        
        while index < len(intervals) and intervals[index][0] <= merged_interval[1]:
            merged_interval = [min(merged_interval[0], intervals[index][0]), max(merged_interval[1], intervals[index][1])]
            index += 1

        result.append(merged_interval)

        # insert intervals after
        while index < len(intervals):
            result.append(intervals[index])
            index += 1

        return result