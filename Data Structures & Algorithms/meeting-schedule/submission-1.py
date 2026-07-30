"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by ignoring the end of the interval
        # and sorting simply based off the start.
        # Sorts properly and makes the next step easier
        sortedList = sorted(intervals, key=lambda interval: interval.start)
        # Don't do entire sortedList length to not
        # go out of bounds
        for i in range(len(sortedList) - 1):
            # Since list is sorted, only check if the end
            # of the current one is greater than the 
            # start of the next one. If one interval is going
            # on during the time that another one starts,
            # then false.
            if sortedList[i + 1].start < sortedList[i].end:
                return False
        return True