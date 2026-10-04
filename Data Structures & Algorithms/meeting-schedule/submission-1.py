"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev_interval = None

        intervals.sort(key=lambda interval: interval.end)

        for interval in intervals:
            if prev_interval is None or interval.start >= prev_interval.end:
                prev_interval = interval
                continue

            return False
            

        return True 