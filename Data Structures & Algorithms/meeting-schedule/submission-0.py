"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        e = []
        for s in intervals:
            e.append((s.start, 1))
            e.append((s.end, -1))
        e.sort()
        change = 0
        for _, c in e:
            change += c
            if change > 1:
                return False
        return True