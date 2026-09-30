class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        
        newIntervals = []

        currInterval = None
        for interval in intervals:
            if currInterval is None:
                currInterval = interval
                continue

            start, end = interval[0], interval[1]

            # Check if overlapping
            if start <= currInterval[1]:
                currInterval = [currInterval[0], max(currInterval[1], end)]

            else:
                newIntervals.append(currInterval)
                currInterval = interval

        newIntervals.append(currInterval)

        return newIntervals