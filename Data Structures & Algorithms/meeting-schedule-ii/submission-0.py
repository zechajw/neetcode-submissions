"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = defaultdict(int)

        for interval in intervals:
            events[interval.start] += 1
            events[interval.end] -= 1

        sweep_line = [(time, change) for time, change in events.items()]
        sweep_line.sort(key=lambda event: event[0])

        curr_rooms, max_rooms = 0, 0
        for event, change in sweep_line:
            curr_rooms += change
            max_rooms = max(max_rooms, curr_rooms)

        return max_rooms

        