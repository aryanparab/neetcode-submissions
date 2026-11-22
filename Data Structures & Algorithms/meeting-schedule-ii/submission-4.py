"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, interval: List[Interval]) -> int:

        intervals = []
        for i in interval:
            intervals.append([i.start,i.end])
        if intervals==[]:return 0
        
        intervals.sort()
        rooms = [intervals[0]]
        
        for i in range(1,len(intervals)):
            found = False
            for r in range(len(rooms)):
                if rooms[r][1]<=intervals[i][0]:
                    rooms[r] = intervals[i]
                    found =True
                    break
            if not found:
                rooms.append(intervals[i])
       
        return len(rooms)