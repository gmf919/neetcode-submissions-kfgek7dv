"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        intervals.sort(key = lambda meeting: meeting.start)

        end_times = []

        heapq.heappush(end_times, intervals[0].end)

        for i in range(1, len(intervals)):

            if intervals[i].start >= end_times[0]:
                heapq.heappop(end_times)
        
            heapq.heappush(end_times, intervals[i].end)

        return len(end_times)