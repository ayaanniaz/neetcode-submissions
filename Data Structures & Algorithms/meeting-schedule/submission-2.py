"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = [[i.start, i.end] for i in intervals]
        intervals.sort(key = lambda x: x[0])
        if len(intervals) <= 1:
            return True
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            if prevEnd > start:
                return False
            prevEnd = end
        return True
